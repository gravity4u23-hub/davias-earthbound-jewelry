# Davias Earthbound Jewelry — Current Task

Repo live Nov 17, 2026. Identity built. Master plan awaiting full owner approval on remaining open decisions.

## Website & Storefront

**Domain:** daviasearthboundjewelry.love  
**Host:** Bluehost.com  
**Company Gmail:** Daviasearthboundjewelry@gmail.com

### Mission for the site
Upscale, beautiful, professional, **spectacular** storefront for handmade-with-love authentic crystal jewelry. Science-first honesty engine (Proven / Traditional / Open). No medical or cure claims. Premium feel, mobile-first, easy to navigate.

### PRIORITY: Integrate the Helix Collection (from Grok conversation)
The owner wants the specific double-helix, triple-helix, and single-strand authentic crystal bracelet designs we developed, with catchy names and skin-tone / eye / hair matching. These are the featured pieces.

**Exact designs to add (use these names, stone combos, and matching text):**

1. **Violet Vortex** — Amethyst + Clear Quartz — Double Helix  
   Complements: Cool & neutral skin · Blue or green eyes · Dark or silver hair.

2. **Earthfire Twist** — Tiger’s Eye + Onyx — Double Helix  
   Complements: Warm & olive skin · Brown or hazel eyes · Warm brown or black hair.

3. **Blush Trinity** — Rose Quartz + Pink Tourmaline — Triple Helix  
   Complements: Fair to medium skin · Light eyes · Blonde or light brown hair.

4. **Reef Ripple** — Amazonite + Aquamarine — Double Helix  
   Complements: Cool skin tones · Blue eyes · Ash or dark hair.

5. **Ember & Ice** — Carnelian + Clear Quartz — Double Helix  
   Complements: Warm skin tones · Amber or brown eyes · Red or warm brown hair.

6. **Northern Lights** — Labradorite + Moonstone — Double Helix  
   Complements: Cool & neutral tones · Any eye color · Dark or silver hair.

7. **Jungle Gold** — Citrine + Green Aventurine — Double Helix  
   Complements: Warm & golden skin · Brown or green eyes · Warm hair colors.

8. **Amber Mist** — Amber + Smoky Quartz — Double Helix  
   Complements: Warm, olive, and medium skin · Brown eyes and hair.

9. **Lapis Current** — Lapis Lazuli — Double Helix  
   Complements: Cool and neutral skin · Blue eyes · Dark hair.

10. **Obsidian Spiral** — Black Tourmaline + Obsidian — Triple Helix  
    Complements: All skin tones. Striking against warm complexions and light eyes.

11. **Amethyst Strand** — Amethyst — Single Strand  
    Complements: Cool skin tones · Blue or violet eyes.

12. **Tiger’s Eye Strand** — Tiger’s Eye — Single Strand  
    Complements: Warm and olive skin · Brown eyes · Warm hair.

**Requirements for the spectacular build:**
- Keep the existing multi-page structure and data-driven approach (`website/src/data.py`).
- Feature the helix collection prominently (especially on Home and Shop).
- Add skin-tone / eye / hair matching notes on every product card and product page.
- Working filters: All / Double Helix / Triple Helix / Single Strand.
- Working Crystal Finder / quiz that recommends based on Cool / Warm / Neutral undertone (and ideally eye/hair).
- Organized, beautiful inventory. Premium dark earthy-luxury aesthetic.
- Prices can stay "Ask for price" until owner sets them, or use the suggested ranges from earlier ($95–$168).
- Replace placeholder images when real photos are available; for now keep the strand visuals but make the overall presentation spectacular.
- Maintain honesty engine. No woo-woo. Real stones, real mineral facts.

### Agentic Resources
See `AGENTIC_RESOURCES.md` for the full list of free Claude Code, Agent SDK, skills, memory, hooks, and related Anthropic resources. Agents should use these when building or improving recommendation logic, the Crystal Finder, or any other agentic features for the site.

### Next actions for agents
1. **Claude:** Update `website/src/data.py` with the full helix collection above (exact names, stones, matching text). Rebuild the site so the helix pieces are the featured inventory. Add the matching system and filters. Make the visual presentation and product experience spectacular and premium. Use patterns from AGENTIC_RESOURCES.md where helpful. Push the changes.
2. **Atlas/Muse:** Review the updated site for brand voice, science accuracy, premium feel, and any drift into claims. Challenge weak copy. Suggest visual or content improvements.
3. **Grok:** Keep this task updated. Integrate owner feedback. Help refine matching logic and product presentation.

## Roles (owner confirmed)
- **Octavia:** makes the bracelets. Helps with ideas and how/where to sell them. Very important to the business.
- **David:** does most of everything else (operations, marketing, content, site, etc.).

## Open decisions — still need owner answers before full launch
1. Prices for the helix pieces.
2. Real product photos of the helix designs.
3. Payment method.
4. First monthly drop date and design.
5. Remaining items from master plan (business card confirmation, handles, packaging).

## Claude Progress
**Nov 17, 2026:** Initial multi-page site built and pushed. Owner reviewed and requested the helix collection + skin-tone matching from the Grok conversation be integrated, and the overall site made spectacular.  
**Nov 20, 2026:** Helix designs partially integrated into `data.py`. AGENTIC_RESOURCES.md added.
**Nov 21, 2026 (09:24 UTC run):** Atlas #5 items 1, 3, 5, 6 fixed on branch `claude/helix-build-5`: `build.py` now renders matching text and construction, adds All / Double Helix / Triple Helix / Single Strand filters, and the site is rebuilt (5 helix pieces now on the shop page). Blush Trinity is rose quartz + pink tourmaline everywhere (new Proven-labelled tourmaline profile). Earth Circle care no longer contradicts itself, `.pyc` untracked, two value/efficacy phrases removed. New standing check `website/tests/check_site.py` (117 checks pass). Still open: #5 item 2 (7 designs need stone profiles; the 5 are the launch set) and item 4 (drop date + payment are owner decisions).
**Nov 21, 2026 (10:25 UTC run):** Atlas #4 items 2, 3, 4 fixed on branch `claude/launch-fixes-4` (stacked on #8). Finder: for everyday wear selenite is removed from the combination and offered only as a special-occasion extra (new browser test `website/tests/check_finder.py`, 5/5 pass; the old code fails 2 of them). Drop page and home button now read "coming soon", with no date or checkout yet; "Drops sell out" and "This month's design" are gone. Anklets are no longer all called beach-ready, so the Soft Light (selenite) page no longer contradicts itself. `check_site.py` has 126 checks, all passing. Item 7 was already fixed in #8, and so was the item 6 `.pyc`. Still owner: item 1 ("Made by Octavia" timing), item 5 (beach sourcing) and the Founders numbering 1–100.
**Nov 21, 2026 (14:24 UTC run):** Atlas #5 item 2 done on branch `claude/helix-complete-5` (stacked on #9): the last 7 Helix designs (Reef Ripple, Ember & Ice, Northern Lights, Jungle Gold, Amber Mist, Lapis Current, Obsidian Spiral) are on the site with 12 new Proven / Traditional stone profiles. Amber and obsidian are labelled "not a mineral"; the homepage now says "natural materials, labeled" and the FAQ explains resin and glass; the hardness range is computed (now Mohs 2–7.5). `check_site.py` now also reads `HELIX_COLLECTION.md` and fails if any design's name, stones or construction drift from the site: 222 checks pass; on the old code the new checks fail 9 times. Still open: the Crystal Finder only recommends from the original stones; sourcing for each new stone is a maker question.
**Nov 21, 2026 (15:24 UTC run):** Crystal Finder knows all 22 stones (branch `claude/finder-all-stones`, stacked on #10). Options now live in `data.py` (`FINDER`): 7 colors, 10 traditions, plus a new undertone question (Cool / Warm / Neutral / Not sure) that suggests Helix designs read from each design's own matching text. Blush Trinity names no undertone, so it shows only under "Not sure"; Obsidian Spiral ("All skin tones") shows for every answer. A note says undertone matching is styling advice, not a rule. New standing check #13: every stone reachable by color, and each tradition option lists only stones whose own Traditional line names it. `check_site.py` 302/302, `check_finder.py` 9/9.

## Rules
- Nothing posts or publishes without the owner's tap.
- Honesty engine: every claim labeled Proven / Traditional / Open. No medical claims.
- Logo never recolored without the owner's say-so.
- Science first, tradition clearly labeled, no woo-woo.
- Company email: Daviasearthboundjewelry@gmail.com

*Live channel: Grok writes tasks here. Claude reads, builds, pushes, and logs progress. Atlas challenges and watches.*
