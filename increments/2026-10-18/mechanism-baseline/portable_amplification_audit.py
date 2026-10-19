#!/usr/bin/env python3
"""Optional portable entry point; original archived script remains unchanged."""
from pathlib import Path
import runpy
root=Path(__file__).resolve().parent
ns=runpy.run_path(str(root/'artifacts/audit-amplification-pilot-20261018/audit_counts.py'),run_name='archived_audit_module')
main=ns['main']
main.__globals__['PRODUCER']=root/'artifacts/amplification-mechanism-pilot-20261018'
main()
