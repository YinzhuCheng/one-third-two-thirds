#!/usr/bin/env python3
"""Single entry point: regenerate and independently verify the new certificate.
Needs Python 3, g++, and installed GMP development libraries. No network access,
installation, or old-census rerun. Temporary binaries are removed on exit.
"""
from pathlib import Path
import subprocess,sys,tempfile
P=Path(__file__).resolve().parent

def run(*args):subprocess.run([str(x) for x in args],cwd=P,check=True)

def main():
    run(sys.executable,P/'enumerate_domain.py')
    with tempfile.TemporaryDirectory(prefix='seven-core-') as td:
        td=Path(td)
        for name in ('count_exact','verify_domain'):
            run('g++','-O3',P/(name+'.cpp'),'-o',td/name,'-lgmpxx','-lgmp')
        run(td/'count_exact',P/'domain_intervals.txt',P/'exact_counts.txt')
        run(td/'verify_domain',P/'independent_intervals.txt')
    run(sys.executable,P/'verify_resolution.py')
if __name__=='__main__':main()
