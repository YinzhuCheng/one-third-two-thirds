#!/usr/bin/env python3
"""Portable, standard-library S113 replay in temporary copies.
Frozen source snapshots are never edited. Every declared output is compared;
only explicitly listed elapsed-time JSON keys may be ignored (currently none).
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


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(root, name):
    relative = Path(name)
    need(not relative.is_absolute() and '..' not in relative.parts,
         'Nonportable manifest path: ' + name)
    path = (root / relative).resolve()
    need(path.is_relative_to(root.resolve()), 'Path escaped root: ' + name)
    return path


def verify(root):
    listed = {}
    for line in (root / 'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ', 1)
        need(name not in listed, 'Duplicate checksum path: ' + name)
        path = contained(root, name)
        need(path.is_file() and not (root / name).is_symlink(), 'Missing regular file: ' + name)
        need(sha256(path) == digest, 'SHA-256 mismatch: ' + name)
        listed[name] = digest
    files = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
    need(files == set(listed) | {'SHA256SUMS'}, 'Unlisted or missing files in package')
    need(not any(p.is_symlink() for p in root.rglob('*')), 'Symlink in package')
    return listed


def normalize(value, ignored):
    if isinstance(value, dict):
        return {k: normalize(v, ignored) for k, v in value.items() if k not in ignored}
    if isinstance(value, list):
        return [normalize(v, ignored) for v in value]
    return value


def json_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    ensure_ascii=False).encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only', action='store_true')
    parser.add_argument('--receipt', type=Path, help='Receipt location outside the immutable package')
    args = parser.parse_args()
    need(__debug__ and not os.environ.get('PYTHONOPTIMIZE'),
         'Run the driver without -O and unset PYTHONOPTIMIZE; the weighted audit uses assertions.')
    if args.receipt:
        need(not args.receipt.resolve().is_relative_to(ROOT), 'Receipt must be outside package root')
    hashes = verify(ROOT)
    manifest = json.loads((ROOT / 'REPRODUCTION.json').read_text())
    ignored = manifest['ignored_json_keys']
    need(set(ignored) <= {'elapsed', 'elapsed_seconds', 'elapsed_sec'}, 'Only elapsed-time keys may be ignored')
    receipt = dict(package='S113', status='RUNNING', python=platform.python_version(),
                   checksum_files_verified=len(hashes), ignored_json_keys=ignored, steps=[],
                   original_path_access_blocked=True, remote_mutations=False)
    if args.verify_only:
        receipt.update(status='PASS', scope='Integrity only: mathematical computations were not rerun')
    else:
        with tempfile.TemporaryDirectory(prefix='poset-S113-reproduction-') as directory:
            work = Path(directory) / 'S113'
            shutil.copytree(ROOT, work)
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
            env.pop('PYTHONOPTIMIZE', None)
            env['PYTHONPATH'] = str(work / 'replay_guard')
            env['S113_REPLAY_ROOT'] = str(work)
            env['S113_FORBIDDEN_SOURCE_ROOTS'] = json.dumps(manifest['forbidden_live_source_roots'])
            for step in manifest['steps']:
                argv = [sys.executable if arg == '{python}' else arg for arg in step['argv']]
                started = time.monotonic()
                run = subprocess.run(argv, cwd=contained(work, step['cwd']), env=env,
                                     capture_output=True, text=True)
                item = dict(id=step['id'], argv=step['argv'], cwd=step['cwd'],
                            returncode=run.returncode, elapsed_seconds=round(time.monotonic()-started, 3),
                            comparisons=[])
                if args.receipt:
                    logs = args.receipt.parent / (args.receipt.stem + '-logs')
                    logs.mkdir(parents=True, exist_ok=True)
                    (logs / (step['id'] + '.stdout.log')).write_text(run.stdout)
                    (logs / (step['id'] + '.stderr.log')).write_text(run.stderr)
                need(run.returncode == 0, step['id'] + ' failed:\n' + run.stderr[-6000:] + run.stdout[-2000:])
                if step.get('stdout_file'):
                    contained(work, step['stdout_file']).write_text(run.stdout)
                for comparison in step['compare']:
                    actual_name = comparison['actual']
                    expected_name = comparison.get('expected', actual_name)
                    actual = contained(work, actual_name)
                    expected = contained(ROOT, expected_name)
                    need(actual.is_file(), 'Missing generated file: ' + actual_name)
                    a = normalize(json.loads(actual.read_text()), ignored)
                    b = normalize(json.loads(expected.read_text()), ignored)
                    need(a == b, 'JSON mismatch: ' + actual_name)
                    record = dict(actual=actual_name, expected=expected_name, status='PASS',
                                  normalized_sha256=json_hash(a))
                    if comparison.get('byte_exact'):
                        need(actual.read_bytes() == expected.read_bytes(), 'Byte mismatch: ' + actual_name)
                        record['byte_exact'] = True
                        record['sha256'] = sha256(actual)
                    item['comparisons'].append(record)
                item['status'] = 'PASS'
                receipt['steps'].append(item)
                print(step['id'] + ': PASS (' + str(item['elapsed_seconds']) + 's)', flush=True)
            need(verify(ROOT) == hashes, 'Frozen package changed during replay')
            receipt.update(status='PASS', source_files_unchanged_after_run=True)
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps(dict(status=receipt['status'], checks_rerun=len(receipt['steps']),
                         checksum_files_verified=len(hashes), receipt_written=bool(args.receipt)), indent=2))


if __name__ == '__main__':
    main()
