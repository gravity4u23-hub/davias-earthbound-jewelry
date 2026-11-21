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

HELIX_NAMES = {"Double": "Double Helix", "Triple": "Triple Helix", "Single": "Single Strand"}

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

# 7. Drop reads as coming soon until a date and payment exist (Atlas #4 item 4).
drop = (SITE / "drop.html").read_text(encoding="utf-8")
home = (SITE / "index.html").read_text(encoding="utf-8")
for phrase in ("This month's design", "Drops sell out", "Then it's gone", "This month&#x27;s design"):
    check(phrase not in drop, f"drop page avoids live-drop phrase: {phrase!r}")
check("coming soon" in drop and "No date or checkout yet" in drop, "drop page says coming soon, no date or checkout yet")
check("This month's drop" not in home and "coming soon" in home, "home links the drop as coming soon")

# 8. No piece with selenite is called beach-ready (Atlas #4 item 2: Soft Light anklet).
for p in PRODUCTS:
    if "selenite" in p["stones"]:
        page = (SITE / "p" / f"{p['slug']}.html").read_text(encoding="utf-8")
        check("beach-ready" not in page and "for the beach" not in page, f"{p['name']} (selenite) not sold as beach-ready")

# 9. HELIX_COLLECTION.md and the site agree: all 12 designs, same stones, same construction (Atlas #5 item 2).
doc = (ROOT.parent / "HELIX_COLLECTION.md").read_text(encoding="utf-8").replace("\u2019", "'")
designs = re.findall(r"\*\*(.+?)\*\*\s*\n\s*Stones: (.+?)\s*\n\s*Construction: (.+?)\s*\n", doc)
check(len(designs) == 12, f"HELIX_COLLECTION.md lists 12 designs (found {len(designs)})")
by_name = {p["name"]: p for p in PRODUCTS}
name_to_key = {s["name"].lower(): k for k, s in STONES.items()}
for name, stones, construction in designs:
    p = by_name.get(name)
    check(p is not None, f"helix design {name} is a product")
    if not p:
        continue
    want = [name_to_key.get(x.strip().lower()) for x in stones.split("+")]
    check(sorted(want) == sorted(p["stones"]), f"{name} stones match the doc ({stones})")
    check(HELIX_NAMES.get(p.get("helix")) == construction.strip(), f"{name} construction is {construction.strip()}")

# 10. Not every bead is stone: amber is resin, obsidian is glass. No page may say otherwise.
for f in [SITE / "index.html", SITE / "finder.html"]:
    if f.exists():
        text = f.read_text(encoding="utf-8")
        check("natural stone beads" not in text and "Every bead is natural stone" not in text,
              f"{f.name} does not call every bead stone")
for k in ("amber", "obsidian"):
    check(k in STONES and "Not a mineral" in STONES[k]["proven"], f"{k} profile exists and says it is not a mineral")

# 11. Homepage hardness range matches the stones we actually use.
lo, hi = min(s["mohs"] for s in STONES.values()), max(s["mohs"] for s in STONES.values())
check(f"Mohs {lo:g}–{hi:g}" in home, f"home shows Mohs {lo:g}–{hi:g}")

# 12. Soft or porous stones (Mohs under 5.5 or 'Keep it dry') never get 'soap and water is fine' on their piece.
for p in PRODUCTS:
    if any("Keep it dry" in STONES[k]["care"] for k in p["stones"]):
        page = (SITE / "p" / f"{p['slug']}.html").read_text(encoding="utf-8")
        care = re.search(r'<div class="label care"><h4>Care</h4><p>(.*?)</p>', page).group(1)
        check("soap and water is fine" not in care, f"{p['name']} care keeps soft stones dry")

print(f"\n{len(fails)} failure(s)")
sys.exit(1 if fails else 0)
