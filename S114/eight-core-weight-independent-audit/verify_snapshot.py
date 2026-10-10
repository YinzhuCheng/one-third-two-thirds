#!/usr/bin/env python3
"""Reproduce from a fresh temporary copy without changing frozen outputs."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    manifest=json.loads((ROOT/'MANIFEST.json').read_text())
    for rel,record in manifest['files'].items():
        p=ROOT/rel
        assert p.stat().st_size==record['bytes'] and sha(p)==record['sha256'],rel
    with tempfile.TemporaryDirectory(prefix='eight_core_weight_audit_') as temp:
        dst=Path(temp)/'audit';shutil.copytree(ROOT,dst)
        for script in ('audit.py','audit_windows.py'):
            subprocess.run([sys.executable,str(dst/script)],check=True,capture_output=True,text=True)
        old=json.loads((ROOT/'audit_results.json').read_text());new=json.loads((dst/'audit_results.json').read_text())
        old.pop('elapsed_seconds');new.pop('elapsed_seconds');assert old==new
        for name in ('window_results.json','all_pair_counts.json'):
            assert (ROOT/name).read_bytes()==(dst/name).read_bytes(),name
    print(json.dumps(dict(status='PASS',manifest_files=len(manifest['files']),
        replays=['audit.py','audit_windows.py'],exact_outputs=['all_pair_counts.json','window_results.json'],
        normalized_outputs={'audit_results.json':['elapsed_seconds']}),indent=2))

if __name__=='__main__':main()
