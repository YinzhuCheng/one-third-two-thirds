"""Replay-only portability guard; not a security sandbox.
Refuse accidental file access to the original research workspace. All frozen
inputs are available in the temporary package. The environment propagates to
nested Python author replays. This module changes no mathematical calculation.
"""
import json
import os
from pathlib import Path
import sys

_roots = tuple(Path(p).resolve() for p in json.loads(os.environ.get('S116_FORBIDDEN_SOURCE_ROOTS', '[]')))
_replay = Path(os.environ['S116_REPLAY_ROOT']).resolve() if os.environ.get('S116_REPLAY_ROOT') else None


def _guard(event, args):
    if event != 'open' or not args:
        return
    item = args[0]
    if not isinstance(item, (str, bytes, os.PathLike)):
        return
    path = Path(os.fsdecode(item)).absolute()
    if _replay and path.is_relative_to(_replay):
        return
    if any(path.is_relative_to(root) for root in _roots):
        raise RuntimeError('S116 portability guard blocked original-workspace file access: ' + str(path))


sys.addaudithook(_guard)
