#!/usr/bin/env python3
"""Run frozen scripts against snapshotted sources and catalogue data."""
import importlib.util,sys,runpy
from pathlib import Path
ROOT=Path(__file__).resolve().parent
for name in ('catalogue','certify'):
 spec=importlib.util.spec_from_file_location(name,ROOT/'reference_snapshot'/f'{name}.py')
 module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
sys.path.insert(0,str(ROOT))
# The original script records the original path. Redirect just that one data
# read to the frozen input, without modifying any file or proof computation.
original=Path.read_text
source=Path('/workspace/shared/prime-core-catalogue-independent-audit/orbit_and_singleton_audit.json')
def frozen_read(path,*args,**kwargs):
 return original(ROOT/'reference_snapshot'/source.name if path==source else path,*args,**kwargs)
Path.read_text=frozen_read
for name in ('research.py','completions.py','funnel_check.py','freeze_witness.py'):
 runpy.run_path(str(ROOT/name),run_name='__main__')
