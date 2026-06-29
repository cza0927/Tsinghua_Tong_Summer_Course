#!/usr/bin/env python3
"""Build the student-facing site from the Markdown in ../content.

TAs edit the Markdown files in `content/`; running this script regenerates a single,
self-contained `site/index.html` (offline, no server needed) that renders the course tabs.

Usage:
    python3 site/build.py           # from the repo root
    python3 build.py                # from inside site/
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

# Ordered registry of tabs -> source Markdown. Add a row here to add a tab.
DOCS = [
    ("syllabus", "Syllabus", "syllabus.md"),
    ("learning-list", "Learning List / Homework", "learning-list.md"),
    ("paper-reading-list", "Paper Reading List", "paper-reading-list.md"),
]

OWNER_RE = re.compile(r"\*\*Owner:\*\*\s*([^·\n]+)")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CONTENT = ROOT / "content"
TEMPLATE = HERE / "template.html"
OUTPUT = HERE / "index.html"


def extract_owner(md: str) -> str:
    m = OWNER_RE.search(md)
    if not m:
        return ""
    return m.group(1).replace("*", "").strip()


def main() -> None:
    template = TEMPLATE.read_text(encoding="utf-8")

    docs = []
    for doc_id, label, filename in DOCS:
        path = CONTENT / filename
        if not path.exists():
            raise SystemExit(f"ERROR: missing content file: {path}")
        md = path.read_text(encoding="utf-8")
        docs.append({"id": doc_id, "label": label, "owner": extract_owner(md), "md": md})
        print(f"  + {filename:32s} ({len(md):>5d} chars)  owner={docs[-1]['owner'] or '-'}")

    # json.dumps gives valid JS; escape '</' so an embedded "</script>" can't close our tag.
    payload = json.dumps(docs, ensure_ascii=False).replace("</", "<\\/")
    build_time = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M")

    html = template.replace("__DOCS__", payload).replace("__BUILD_TIME__", build_time)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"\nBuilt {OUTPUT}  ({len(html):,} bytes, {len(docs)} tabs)  @ {build_time}")


if __name__ == "__main__":
    main()
