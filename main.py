"""news-image-20261123 entry: copy the front-page image to /output/entry.png.

Python 3.13, standard library only. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
# Self-check: the copy must be byte-identical to the bundled image, so a
# truncated or corrupt copy fails loudly instead of entering the judge.
if _sha256(OUT_DIR / "entry.png") != _sha256(HERE / "entry.png"):
    raise SystemExit("entry.png copy failed sha256 self-check")
