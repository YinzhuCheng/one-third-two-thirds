"""Recheck frozen certificates without rerunning or mutating search results.
Extract only the independent verifier functions from the archived scripts.
"""
import ast,json
from pathlib import Path
from search import *
HERE=Path(__file__).parent
def load_function(filename,name):
 tree=ast.parse((HERE/filename).read_text())
 selected=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name]
 assert len(selected)==1
 exec(compile(ast.Module(body=selected,type_ignores=[]),filename,'exec'),globals())
load_function('refine.py','verify')
load_function('singleton_and_enumerate.py','enumerate_check')
for name in ['minimal_single_gate_negative_energy','singleton_negative_energy','first_nonmonotone','induced_minimal_twelve']:
 d=json.loads((HERE/(name+'.json')).read_text())
 print(name,verify(d),enumerate_check(d))
for name in ['best_gap','best_ratio']:
 print(name,verify(json.loads((HERE/(name+'.json')).read_text())))
