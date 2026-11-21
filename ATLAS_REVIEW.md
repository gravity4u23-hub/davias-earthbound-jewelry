# Atlas Review — Helix on the Site (PR #8)

Reviewed 2026-11-21 ~13:05 MST. Branch `claude/helix-build-5` (stacked under #9/#10/#11). Reviewer: Atlas (challenger role, HIVEMIND.md).

## Verified — holds up, checked on the built site

- **Helix filters render and cover all 12 designs:** shop page carries All / Double Helix / Triple Helix / Single Strand filter buttons (`data-filter="helix-double"` etc.), and the 12 shop cards split 8 double / 2 single / 2 triple — matching the collection. Per-stone filters render for every stone.
- **Matching text renders on every card:** each product card carries its "Complements: …" line (skin / eyes / hair) from its own matching text.
- **The `.pyc` is gone.** No `__pycache__` file is tracked on this branch, on main, or at the stack head, and a `.gitignore` covers it. Atlas #4 item 6 is fixed here, as the #9 PR body states.
- **The site builds and passes its suite at the stack head** (`build.py` → 43 files; `check_site.py` 302/302), which includes this PR's helix rendering.

## Challenges

1. **The diff is mostly generated output** (tens of thousands of lines of built `site/` HTML). That's the repo's structure, not a fault — but it means review-by-diff is impractical and the test suite is the real reviewer. Keep the suite green; if the build ever drifts from `src/`, the suite is what catches it.
2. **Filter labels vs data values:** the visible buttons read "Double Helix" / "Triple Helix" / "Single Strand" while the data values are `helix-double` / `helix-triple` / `helix-single` — consistent, but the mapping lives in `site.js`. If a label is ever reworded without the value, the filter silently stops matching. The suite doesn't click the filters — one browser test clicking each filter button would close that gap (the finder test already proves the pattern works).
3. **I verified the built output at the #11 stack head, not on this branch alone.** If the stack is reordered, build + run the suite on this branch before merging it standalone.

## What is NOT verified by this review

- I did not click the filter buttons in a browser — I verified the buttons, the data attributes and the card values exist and agree. The click behavior is the one unproven link (challenge 2).
- No photos exist yet; every card still says "Photo coming soon".

## Verdict

**Mergeable. Helix is on the site, filtered and matched — add the filter-click test (challenge 2) when the suite next grows.**

---

# Atlas Review — Atlas #4 Launch Fixes (PR #9)

Reviewed 2026-11-21 ~12:30 MST. Branch `claude/launch-fixes-4`, stacked on #8. Reviewer: Atlas (challenger role, HIVEMIND.md).

## Verified — holds up, checked against the built site

- **Selenite rule is real and tested.** For everyday wear selenite is removed from the 2-stone combination and offered only as a special-occasion extra — and the browser test proves it: `check_finder.py` passes 5/5 selenite cases (re-ran the full 9-case suite at the #11 head, 9/9 pass, including all 5 selenite cases).
- **Drop page reads honestly as "coming soon".** The drop page says "Monthly limited drop: coming soon" with "The first date is not set yet" and "No date or checkout yet"; "Drops sell out" and "This month's design" are gone — verified on the built site. The home button reads "Monthly drop: coming soon". That is the fix Atlas #4 item 4 asked for: no date invented, no checkout pretended.
- **Anklets are per-stone now, not all beach-ready.** Jade Garden (jade, Mohs 6.5–7): "Tough enough for the beach." Soft Light (selenite): "Keep it out of the water." The self-contradiction is gone.
- **The suite guards the fixes:** `check_site.py` asserts the drop page says "coming soon" with no date/checkout, and the home links the drop as coming soon — so a future edit can't silently re-add a fake date.

## Challenges

1. **"Photo coming soon" is still on every product card.** That's a different "coming soon" from the one this PR fixed — it's honest (there are no photos yet), but a shop page where every card says it reads unfinished. It needs real photos (owner) or a different placeholder treatment, not a code fix. Flagging so it isn't mistaken for done.
2. **Still owner-side, per the PR body itself:** item 1 ("Made by Octavia" timing), item 5 (beach sourcing) and the Founders numbering 1–100. Nothing here blocks the merge; those are launch decisions, not code.
3. **I verified the fixes at the #11 stack head, not on this branch alone.** The suite passes there; if the stack is reordered, re-run `check_site.py` + `check_finder.py` on this branch before merging it standalone.

## What is NOT verified by this review

- The "126 checks" figure is from the PR body at this branch's time; the suite has since grown to 302 at the stack head. The count moved because later PRs added checks, not because this PR's checks broke.
- No photos exist yet; the site is a preview until the owner supplies them.

## Verdict

**Mergeable. Atlas #4 items 2, 3, 4 are fixed and test-guarded — the remaining items are owner decisions, correctly left open.**

---

# Atlas Review — Helix Complete: Last 7 Designs + 12 Stone Profiles (PR #10)

Reviewed 2026-11-21 ~12:25 MST. Branch `claude/helix-complete-5`. Reviewer: Atlas (challenger role, HIVEMIND.md).

## Verified — holds up, checked against the built site

- **All 12 designs have product pages, shop cards and helix filters** — verified on the built site at the #11 head (which stacks on this PR): 7 new designs (Reef Ripple, Ember & Ice, Northern Lights, Jungle Gold, Amber Mist, Lapis Current, Obsidian Spiral) each render a page, a shop card and a `data-helix` value.
- **Amber and obsidian are labelled as not minerals, and the site no longer claims every bead is stone.** Amber page: "Not a mineral: fossilized tree resin, millions of years old. Very soft (Mohs 2 to 2.5)"; Obsidian page: "Not a mineral: natural volcanic glass"; "every bead is stone" appears nowhere on the built site. That closes Atlas #5 item 2 for real.
- **Citrine disclosure is honest:** "Natural citrine is rare: most citrine sold is amethyst that was heated until it turned gold. We tell you which ours is." — the exact disclosure the collection note promises.
- **Proven / Traditional labels are kept apart on every profile checked** — mineral facts under Proven, lore under Traditional with "Shared as tradition." No cure/health claims in the profiles.
- **No fake commerce:** no prices are invented ("Ask for price" throughout), no cart, no checkout, no "buy now" — the ribbon reads "Opening soon. Order any piece by message while the online checkout is being set up." Honest.
- **The site check now guards the collection doc:** `check_site.py` reads `HELIX_COLLECTION.md` against the site so the two can't drift — and it passes (302 checks at the #11 head).

## Challenges

1. **Two owner/maker questions are still open before launch — and they're named in the collection note, which is good:** can Octavia source each stone, and is the citrine natural or heated amethyst. The site currently *promises* "we tell you which ours is" — that promise needs the answer before the first sale, or the page overpromises.
2. **"All 12 designs" is verified at the stack head, not on this branch alone.** If #11 changes, re-run the suite — the 302-check guard is the thing that makes that cheap.
3. **The collection note says "12 new Proven / Traditional stone profiles" — the profiles live in `data.py`, not in the collection doc.** That's fine (one source), but a future editor updating `HELIX_COLLECTION.md` won't see the profiles there. One pointer line in the doc to `website/src/data.py` as the profile source would stop a drift-by-edit.

## What is NOT verified by this review

- I did not verify each of the 12 profiles' mineral facts against an external source (Mohs values, piezoelectric claims) — the labels are internally consistent and honestly framed, but the facts themselves are Claude-sourced. Spot-check the Mohs numbers against a mineral reference before launch.
- No owner confirmation that every stone can be sourced.

## Verdict

**Mergeable. The honesty fixes are real and verified — get the citrine answer (challenge 1) before the first sale, not before the merge.**

---

# Atlas Review — Crystal Finder: All 22 Stones + Undertone (PR #11)

Reviewed 2026-11-21 ~12:20 MST. Branch `claude/finder-all-stones` (head `c185b94`), stacked on #10. Reviewer: Atlas (challenger role, HIVEMIND.md).

## Verified — holds up, run for real in a browser

- `python3 src/build.py` → **43 files built**, no errors.
- `python3 tests/check_site.py` → **302 checks, 0 failures** — including new check #13 (every stone reachable by a color; every tradition option only lists stones whose own Traditional line contains that word; each design's undertones read by hand from `HELIX_COLLECTION.md`).
- `python3 tests/check_finder.py` → **9/9 pass, 0 failures** in a real browser (5 selenite cases + 4 undertone cases: Cool shows Reef Ripple and not Earthfire Twist, as claimed).
- **`undertones()` reads only the skin clause, as documented.** It splits the matching text on "·" and takes the first clause: "All skin tones" → any; Cool/Warm/Neutral keywords → those; nothing → unspecified (shown only under "Not sure"). Blush Trinity's "Fair to medium skin" is skin *depth*, not undertone — correctly unspecified, so it appears only under "Not sure" and never as a Cool/Warm/Neutral fit. Obsidian Spiral ("All skin tones") appears for every answer. Both verified in the browser run.
- **The "styling advice, not a rule" line is on the result** — the finder doesn't overclaim.

## Challenges

1. **Amber stays in everyday combos at Mohs 2 — say why, in the code.** The PR body flags it as an owner/maker question, and the reasoning is sound (the selenite rule is about water; amber is already sold as an everyday bracelet). But nothing in `data.py` records the exemption: a future reader sees Mohs 2 + everyday and "fixes" it, or sees selenite excluded and asks why amber isn't. One comment line next to the rule closes it.
2. **Olive is unmapped — the finder decides silently.** Amber Mist says "Warm, olive, and medium" and counts as warm only; olive is not mapped to neutral. A shopper with olive undertone gets warm suggestions with no note that olive wasn't matched. Either map olive to warm+neutral explicitly or say in the finder that olive reads as warm here. As written the choice is invisible.
3. **The undertone check is circular by construction.** Check #13 verifies the site matches `HELIX_COLLECTION.md` — but the undertones were read *from* that same file by hand. If a matching line in the collection doc is wrong, site and doc agree and are both wrong. The undertone assignments need one human read (Octavia — she knows the pieces) before launch, not just a passing test.

## What is NOT verified by this review

- I verified the *logic* and the *built output*, not every generated page line-by-line — the 42 built files are covered by the 302-check suite, not by my reading each one.
- No owner/maker confirmation exists for the undertone assignments or for whether each stone can be sourced. The finder is a preview until then.

## Verdict

**Mergeable. The finder is tested, not hand-checked — add the one-line amber comment (challenge 1) and get Octavia's read on the undertone assignments (challenge 3) before launch.**
