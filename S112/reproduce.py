#!/usr/bin/env python3
"""Portable S112 reproduction. Standard library only; snapshots are read-only inputs.
Run all scripts in a fresh temporary copy and compare every recorded output.
The manifest's exact elapsed-time keys are the only ignored JSON content.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(root, name):
    path = Path(name)
    require(not path.is_absolute() and '..' not in path.parts, 'Nonportable manifest path: ' + name)
    resolved = (root / path).resolve()
    require(resolved.is_relative_to(root.resolve()), 'Path escaped root: ' + name)
    return resolved


def verify_checksums(root):
    count = 0
    for line in (root / 'SHA256SUMS').read_text().splitlines():
        expected, name = line.split('  ', 1)
        path = contained(root, name)
        require(path.is_file() and not path.is_symlink(), 'Missing regular input: ' + name)
        require(digest(path) == expected, 'SHA-256 mismatch: ' + name)
        count += 1
    return count


def normalize(value, keys):
    if isinstance(value, dict):
        return {k: normalize(v, keys) for k, v in value.items() if k not in keys}
    if isinstance(value, list):
        return [normalize(v, keys) for v in value]
    return value


def comparable_hash(value):
    raw = json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only', action='store_true')
    parser.add_argument('--mode', choices=('standard', 'full'), default='standard')
    parser.add_argument('--cxx', default='g++')
    parser.add_argument('--receipt', type=Path, help='Write a machine-readable receipt outside this package')
    args = parser.parse_args()
    require(__debug__, 'Run this driver without -O: legacy identity tests intentionally use assertions.')
    require(not os.environ.get('PYTHONOPTIMIZE'), 'Unset PYTHONOPTIMIZE so legacy identity assertions remain active.')
    if args.receipt:
        require(not args.receipt.resolve().is_relative_to(ROOT), 'Receipt must be outside immutable package root.')
    checked = verify_checksums(ROOT)
    manifest = json.loads((ROOT / 'REPRODUCTION.json').read_text())
    receipt = {'package': 'S112', 'mode': args.mode, 'status': 'RUNNING',
               'python': platform.python_version(), 'checksum_files_verified': checked,
               'ignored_json_keys': manifest['ignored_json_keys'], 'steps': []}
    if args.verify_only:
        receipt.update(status='PASS', scope='SHA-256 verification only; no mathematical check was rerun')
    else:
        compiler = shutil.which(args.cxx) if args.mode == 'full' else None
        require(args.mode != 'full' or compiler, 'Full mode requires a C++17 compiler via --cxx.')
        if compiler:
            receipt['compiler'] = subprocess.run([compiler, '--version'], text=True, capture_output=True, check=True).stdout.splitlines()[0]
        with tempfile.TemporaryDirectory(prefix='poset-S112-reproduction-') as temporary:
            work = Path(temporary) / 'S112'
            shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
            env.pop('PYTHONOPTIMIZE', None)
            for step in manifest['steps']:
                if step.get('mode') == 'full' and args.mode != 'full':
                    receipt['steps'].append({'id': step['id'], 'status': 'NOT_RUN', 'reason': 'Independent C++ enumeration requires --mode full; its frozen output remains hash-bound.'})
                    continue
                argv = [(sys.executable if a == '{python}' else compiler if a == '{cxx}' else a) for a in step['argv']]
                cwd = contained(work, step.get('cwd', '.'))
                started = time.monotonic()
                run = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, text=True)
                elapsed = round(time.monotonic() - started, 3)
                item = {'id': step['id'], 'argv': step['argv'], 'cwd': step.get('cwd', '.'),
                        'returncode': run.returncode, 'elapsed_seconds': elapsed, 'comparisons': []}
                if args.receipt:
                    logs = args.receipt.parent / (args.receipt.stem + '-logs')
                    logs.mkdir(parents=True, exist_ok=True)
                    (logs / (step['id'] + '.stdout.log')).write_text(run.stdout)
                    (logs / (step['id'] + '.stderr.log')).write_text(run.stderr)
                require(run.returncode == 0, step['id'] + ' failed:\n' + run.stderr[-8000:] + run.stdout[-2000:])
                if 'stdout_file' in step:
                    contained(work, step['stdout_file']).write_text(run.stdout)
                for comparison in step.get('compare', []):
                    produced = comparison['actual']
                    expected = comparison.get('expected', produced)
                    actual_path = contained(work, produced)
                    expected_path = contained(ROOT, expected)
                    require(actual_path.is_file(), 'Missing generated output: ' + produced)
                    if comparison.get('format', 'json') == 'json':
                        actual = normalize(json.loads(actual_path.read_text()), manifest['ignored_json_keys'])
                        wanted = normalize(json.loads(expected_path.read_text()), manifest['ignored_json_keys'])
                        require(actual == wanted, 'Deterministic JSON mismatch: ' + produced)
                        item['comparisons'].append({'actual': produced, 'expected': expected, 'status': 'PASS',
                                                    'normalized_sha256': comparable_hash(actual)})
                    else:
                        require(actual_path.read_bytes() == expected_path.read_bytes(), 'Byte mismatch: ' + produced)
                        item['comparisons'].append({'actual': produced, 'expected': expected, 'status': 'PASS', 'sha256': digest(actual_path)})
                item['status'] = 'PASS'
                receipt['steps'].append(item)
                print(step['id'] + ': PASS (' + str(elapsed) + 's)', flush=True)
            require(verify_checksums(ROOT) == checked, 'Source checksum list changed during reproduction.')
            receipt['source_files_unchanged_after_run'] = True
            receipt['status'] = 'PASS'
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'status': receipt['status'], 'mode': args.mode,
                      'checksum_files_verified': checked,
                      'checks_rerun': sum(s['status'] == 'PASS' for s in receipt['steps']),
                      'not_run': [s['id'] for s in receipt['steps'] if s['status'] == 'NOT_RUN'],
                      'receipt_written': bool(args.receipt)}, indent=2))


if __name__ == '__main__':
    main()
