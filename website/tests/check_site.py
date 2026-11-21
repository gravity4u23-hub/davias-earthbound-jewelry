"""Standing checks for the generated site (Atlas davias #5 / #4).

Run after build:  python3 src/build.py && python3 tests/check_site.py
Exits non-zero on any failure.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from data import PRODUCTS, STONES  # noqa: E402

SITE = ROOT / "site"
fails = []


def check(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        fails.append(msg)


shop = (SITE / "shop.html").read_text(encoding="utf-8")

# 1. Every product, helix ones included, is on the shop page and has its own page.
for p in PRODUCTS:
    check(f'href="p/{p["slug"]}.html"' in shop, f"shop lists {p['name']}")
    check((SITE / "p" / f"{p['slug']}.html").exists(), f"page exists for {p['name']}")

# 2. Helix filters exist and every helix piece carries its filter key.
for key in ("helix-double", "helix-triple", "helix-single"):
    check(f'data-filter="{key}"' in shop, f"shop has filter {key}")
for p in PRODUCTS:
    if p.get("helix"):
        check(f'data-helix="helix-{p["helix"].lower()}"' in shop, f"{p['name']} tagged helix-{p['helix'].lower()}")

# 3. Matching text renders on each product's own page.
for p in PRODUCTS:
    if p.get("matching"):
        page = (SITE / "p" / f"{p['slug']}.html").read_text(encoding="utf-8")
        check("<dt>Complements</dt>" in page and p["matching"].replace("&", "&amp;") in page,
              f"{p['name']} page shows its matching text")

# 4. No page tells a buyer both "soap and water is fine" and "keep it dry".
for f in sorted((SITE / "p").glob("*.html")):
    care = re.search(r'<div class="label care"><h4>Care</h4><p>(.*?)</p>', f.read_text(encoding="utf-8"))
    text = care.group(1) if care else ""
    check(not ("Mild soap and water is fine" in text and "Keep it dry" in text), f"{f.name} care is consistent")

# 5. Every product stone has a profile; no banned sales phrasing in stories.
for p in PRODUCTS:
    check(all(k in STONES for k in p["stones"]), f"{p['name']} stones all profiled")
    check(not re.search(r"quietly powerful|more expensive than it is|heal", p["story"], re.I),
          f"{p['name']} story has no efficacy/value claim")

# 6. No compiled Python tracked in git.
tracked = subprocess.run(["git", "ls-files", "*.pyc"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
check(tracked == "", "no .pyc files tracked")

print(f"\n{len(fails)} failure(s)")
sys.exit(1 if fails else 0)
