"""Finder check in a real browser (Atlas davias #4 item 3).

For everyday wear, selenite must never appear in the 2-stone combination;
for special occasions it may. Run after build:
    python3 src/build.py && python3 tests/check_finder.py
Needs Python Playwright + Chromium. Exits non-zero on failure.
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

PAGE = (Path(__file__).resolve().parent.parent / "site" / "finder.html").as_uri()
fails = []


def run(page, colors, feels, wear):
    page.goto(PAGE)
    # Inputs sit under styled labels, so click the label like a shopper would.
    for box in page.query_selector_all("#finder-form input[type=checkbox]"):
        name, value = box.get_attribute("name"), box.get_attribute("value")
        if box.is_checked() != (value in (colors if name == "color" else feels)):
            page.locator(f"label:has(#f-{name}-{value})").click()
    page.locator(f"label:has(#f-wear-{wear})").click()
    return page.inner_text("#finder-result h3")


CASES = [
    # (colors, feels, wear, selenite allowed in the headline?)
    (["white"], ["clarity"], "every", False),
    (["white"], ["calm", "clarity"], "every", False),
    ([], ["calm"], "every", False),
    (["white"], ["clarity"], "gentle", True),
    (["gold"], ["confidence"], "every", False),
]
with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    for colors, feels, wear, allowed in CASES:
        head = run(page, colors, feels, wear)
        combo = "" if head.startswith("Selenite is for") else head
        ok = allowed or "Selenite" not in combo
        if wear == "gentle":
            ok = ok and "Selenite" in combo
        print(("PASS " if ok else "FAIL ") + f"{colors}+{feels}/{wear} -> {head!r}")
        if not ok:
            fails.append(head)

    # Undertone -> helix suggestions (read from each design's matching text).
    HELIX_CASES = [
        ("cool", ["Violet Vortex", "Reef Ripple", "Northern Lights", "Lapis Current", "Amethyst Strand", "Obsidian Spiral"],
         ["Earthfire Twist", "Jungle Gold", "Tiger's Eye Strand", "Blush Trinity"]),
        ("warm", ["Earthfire Twist", "Ember & Ice", "Jungle Gold", "Amber Mist", "Tiger's Eye Strand", "Obsidian Spiral"],
         ["Reef Ripple", "Amethyst Strand", "Violet Vortex", "Blush Trinity"]),
        ("neutral", ["Violet Vortex", "Northern Lights", "Lapis Current", "Obsidian Spiral"], ["Reef Ripple", "Earthfire Twist", "Blush Trinity"]),
        ("unsure", ["Obsidian Spiral", "Blush Trinity"], ["Reef Ripple", "Earthfire Twist"]),
    ]
    for tone, must, must_not in HELIX_CASES:
        page.goto(PAGE)
        page.locator(f"label:has(#f-undertone-{tone})").click()
        chips = page.inner_text("#finder-helix") if page.query_selector("#finder-helix") else ""
        bad = [n for n in must if n not in chips] + [n for n in must_not if n in chips]
        print(("PASS " if not bad else "FAIL ") + f"undertone {tone}: {chips.replace(chr(10), ', ')!r}")
        if bad:
            fails.append(f"undertone {tone}: {bad}")
    if errors:
        fails.append("page errors: " + "; ".join(errors))
        print("FAIL page errors:", errors)
    browser.close()

print(f"\n{len(fails)} failure(s)")
sys.exit(1 if fails else 0)
