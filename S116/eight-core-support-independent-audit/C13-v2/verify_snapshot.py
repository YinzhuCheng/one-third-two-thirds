#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile
R=Path(__file__).resolve().parent
m=json.loads((R/'MANIFEST.json').read_text())['files']
for rel,meta in m.items():
 data=(R/rel).read_bytes()
 if len(data)!=meta['bytes'] or hashlib.sha256(data).hexdigest()!=meta['sha256']:raise RuntimeError('Manifest mismatch '+rel)
for flags in [[],['-O']]:
 with tempfile.TemporaryDirectory() as d:
  t=Path(d)/'audit';shutil.copytree(R,t)
  p=subprocess.run([sys.executable,*flags,str(t/'audit.py')],capture_output=True,text=True)
  if p.returncode:raise RuntimeError(p.stdout+p.stderr)
  if (t/'audit_results.json').read_bytes()!=(R/'audit_results.json').read_bytes():raise RuntimeError('Output mismatch')
  # A corrupt certificate must fail with and without optimization.
  c=t/'inputs/author/certificate.json';x=json.loads(c.read_text());x['cases'][0]['numerator']+=1;c.write_text(json.dumps(x))
  p=subprocess.run([sys.executable,*flags,str(t/'audit.py')],capture_output=True,text=True)
  if p.returncode==0:raise RuntimeError('Tampered certificate accepted')
print('PASS: hashes, normal/-O isolated reproduction, and normal/-O tamper rejection.')
