"""Copy the entry image to the output directory.

The entry is a pre-rendered newspaper front page (entry.png) that sums up
the world news of Tuesday, 24 November 2026. This program copies it to the
location the grader reads (/output/entry.png, or $MAKEFUN_OUTPUT_DIR).
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY_NAME = "entry.png"
SRC = os.path.join(HERE, ENTRY_NAME)
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, ENTRY_NAME)

os.makedirs(OUT_DIR, exist_ok=True)
if not os.path.isfile(SRC):
    raise SystemExit("entry.png missing next to main.py")
shutil.copyfile(SRC, DST)
