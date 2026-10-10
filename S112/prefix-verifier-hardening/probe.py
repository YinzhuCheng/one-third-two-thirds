import importlib.util,json,sys
from pathlib import Path
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('probe_certify',sys.argv[1]);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
p=json.loads(Path('/workspace/shared/poset-prefix-width3-search/exact_templates.json').read_text())[0]
c=dict(p['certificates'][0],optimum='999')
try:
 m.verify(p['F'],[p['A'][i] for i in p['selected_indices']],c)
except Exception as e:
 print(json.dumps({'optimized':not __debug__,'result':'REJECTED','exception':type(e).__name__,'message':str(e)}))
else:
 print(json.dumps({'optimized':not __debug__,'result':'ACCEPTED'}))
