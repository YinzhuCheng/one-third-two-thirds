#!/usr/bin/env python3
"""One-time archive transport. This never executes or verifies mathematical code."""
from __future__ import annotations
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from zipfile import ZipFile


def unpack(archive: Path, destination: Path, conflict_root: Path) -> dict:
    counts = {"source_files": 0, "written": 0, "already_present": 0, "preserved_conflicts": 0}
    with ZipFile(archive) as z:
        entries = [i for i in z.infolist() if not i.is_dir()]
        roots = {PurePosixPath(i.filename).parts[0] for i in entries}
        if len(roots) != 1:
            raise ValueError(f"Expected one enclosing directory: {archive.name}")
        for info in entries:
            full = PurePosixPath(info.filename)
            if full.is_absolute() or ".." in full.parts or "\\" in info.filename:
                raise ValueError(f"Unsafe archive path: {info.filename}")
            relative = Path(*full.parts[1:])
            if len(full.parts) < 2 or any(p in {".git", ".github"} for p in relative.parts):
                raise ValueError(f"Not an allowed research path: {info.filename}")
            if ((info.external_attr >> 16) & 0o170000) == 0o120000:
                raise ValueError(f"Unexpected symbolic link: {info.filename}")
            target = destination / relative
            if target.is_symlink() or any(p.is_symlink() for p in target.parents):
                raise ValueError(f"Refusing to write through a symbolic link: {target}")
            data = z.read(info)
            counts["source_files"] += 1
            if target.exists():
                if target.read_bytes() == data:
                    counts["already_present"] += 1
                    continue
                # Do not overwrite a current guide or another agent's research.
                target = conflict_root / relative
                if target.exists() and target.read_bytes() != data:
                    raise ValueError(f"An earlier source copy differs: {target}")
                counts["preserved_conflicts"] += 1
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            counts["written"] += 1
    return counts


def one(directory: Path, pattern: str) -> Path:
    matches = list(directory.glob(pattern))
    if len(matches) != 1:
        raise ValueError(f"Expected one {pattern}; found {len(matches)}. Attach both original ZIPs.")
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archives", type=Path, required=True, help="Directory containing the two original ZIPs")
    parser.add_argument("--destination", type=Path, default=Path("."))
    args = parser.parse_args()
    destination = args.destination.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    full = one(args.archives, "*COMPLETE_RESEARCH_HANDOFF*.zip")
    reading = one(args.archives, "*NEW_SESSION_READING_KIT*.zip")
    counts = {}
    counts["complete_S68"] = unpack(full, destination, destination / "archive/source_S68")
    counts["reading_kit"] = unpack(reading, destination / "archive/reading_kit_S68", destination / "archive/source_reading_kit")
    # Use the nested original from the supplied full archive, not an unrelated local ZIP.
    with ZipFile(full) as z:
        names = [n for n in z.namelist() if n.endswith("/archive/S67_original.zip")]
        if len(names) != 1:
            raise ValueError("The complete handoff must contain its original S67 archive")
        import tempfile
        with tempfile.TemporaryDirectory() as temporary:
            nested = Path(temporary) / "S67_original.zip"
            nested.write_bytes(z.read(names[0]))
            counts["history_S67"] = unpack(nested, destination / "history/S67", destination / "archive/source_history_S67")
    result = {
        "status": "source_archives_imported",
        "imported_at": datetime.now(timezone.utc).isoformat(),
        "source_archives": [full.name, reading.name],
        "counts": counts,
        "scope": "File import only. No mathematics program, proof verification, or hash gate was run.",
        "conflicts": "Current files retained; differing original bytes saved under archive/source_*.",
    }
    output = destination / "archive/IMPORT_COMPLETE.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    (destination / "archive/IMPORT_COMPLETE.md").write_text(
        "# 原始研究包已导入\n\n两个原始 ZIP 的内容和 S67 历史文件已展开。"
        "文件数量与迁入时间见 [IMPORT_COMPLETE.json](IMPORT_COMPLETE.json)。\n\n"
        "此记录仅确认文件搬运，不认证数学结论。原有研究文件若与导入副本不同，"
        "保持现行文件不变，原字节保存在 `archive/source_*`。不运行历史验证器。\n"
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
