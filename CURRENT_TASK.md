# Davias Earthbound Jewelry — Current Task

Repo live Nov 17, 2026. Identity built. Master plan awaiting full owner approval on remaining open decisions.

## Website & Storefront

**Domain:** daviasearthboundjewelry.love  
**Host:** Bluehost.com  
**Company Gmail:** Daviasearthboundjewelry@gmail.com

### Mission for the site
- Upscale, beautiful, professional storefront for handmade-with-love crystal beaded jewelry:
  - Bracelets
  - Earrings
  - Necklaces
  - Anklets
- Easy to navigate and understand. Generous space, high-quality photos, clear language.
- Room to expand product lines as money comes in.
- Sell and market on TikTok, Facebook, and every other platform that allows selling.
- Create amazing content that also educates people on the real properties and applications of the crystals.
- Incorporate all available science on crystal properties.
- Remove the woo-woo. Stick to the honesty engine already in the master plan: Proven / Traditional / Open. No medical or cure claims.

### New features requested (Nov 17)
See `PRODUCT_AND_CONTENT_IDEAS.md`, `MONTHLY_DROP_IDEAS.md`, and `MARKETING_PLAYBOOK.md` for full detail:
- Cartoon-style fun educational videos about crystals, wearing them, and how to use them
- Jewelry design ideas (color/crystal combos that mesh, unique high-end look at low price, charms)
- Packaging and display ideas (premium feel, cheap to produce)
- Site section where users input desired crystal combinations or properties → suggestions
- Q&A / recommendation area that points people in the right direction (science-first)
- **Monthly limited drop:** once a month. Start with ~100 pieces while building following; scale toward 1,000 only after proven demand. Sell at a premium for 24–72 hours. Create scarcity so buyers feel special and smart. Still science-first.
- 20 ready drop concepts in `MONTHLY_DROP_IDEAS.md`.
- Full marketing & selling playbook in `MARKETING_PLAYBOOK.md` (content mix, scarcity, platforms, process videos).
- Expand into every market: country/flag color bracelets, sports team bracelets, Christmas/holidays, religious occasions, **beach-themed pieces with shells/starfish**. Science-first labeling always.

### Next actions for agents
1. Claude: draft a clean, mobile-first, **upscale and professional** storefront structure. Support product categories (core stones, country/flag, sports teams, holidays, beach). Include customizer/recommendation section and monthly drop feature. Use company Gmail. Start from WEBSITE_BRIEF.md + other idea files. Make it feel premium and trustworthy.
2. Muse/Atlas: expand creative ideas for videos, unique jewelry looks, packaging, charms, monthly drops, and new markets (flags, teams, holidays, beach shells/starfish). Challenge anything that drifts into woo-woo. Review for brand voice, science accuracy, and premium feel.
3. Grok: keep CURRENT_TASK and HIVEMIND updated. Continue refining marketing tactics from real results.

## Roles (owner confirmed)
- **Octavia:** makes the bracelets. Helps with ideas and how/where to sell them. Very important to the business.
- **David:** does most of everything else (operations, marketing, content, site, etc.).

## Business cards
Final PDF and source files are in `business-card/`. Owner has ordered them. Confirm they open correctly on phone if needed.

## Open decisions — still need owner answers before full launch

1. Does the fixed business-card PDF open right on his phone?
2. How people order and pay at first (DM to order proposed; payment method TBD).
3. Card back wording — list the five starting stones, or say any and all crystal beads?
4. Purple mesh bags — 200-pack, 3x4", $11.99 at Walmart — are those the jewelry bags? If yes, ship to Calabasas or Arizona?
5. Handles — claim in the order in the plan, or pick a favorite first.

## Claude Progress

**Nov 17, 2026: Website built. Grok, please review.** Not live yet; Bluehost upload waits for the owner.

- **Preview link:** https://claude.ai/artifact/H8FE1Z3LnVsEPNL1jehbfP
  (It opens for people the owner shares it with on claude.ai. If it won't open for you, read the files below.)
- **Code:** PR #3, https://github.com/gravity4u23-hub/davias-earthbound-jewelry/pull/3 (branch `claude/website-draft`)
  - `website/site/`: the finished site (upload this to Bluehost `public_html`)
  - `website/src/data.py`: all content: products, stones, contact, prices (None = "Ask for price")
  - `website/README.md`: build and Bluehost upload steps
- **Pages:** Home, Shop (filters), 13 product pages, Stone Guide (6 stones), Monthly Drop, Crystal Finder + FAQ, Our Story, Order bag.
- **Grok:** please check the copy against the honesty engine, the product names and stories, and the FAQ answers. Suggest changes as PR comments or edits to `data.py`.
- **Owner still needs to give:** product photos, prices, payment method, first drop date.

## Rules

- Nothing posts or publishes without the owner's tap.
- Honesty engine: every claim labeled Proven / Traditional / Open. No medical claims.
- Logo never recolored without the owner's say-so.
- Science first, tradition clearly labeled, no woo-woo.
- Company email: Daviasearthboundjewelry@gmail.com

*Live channel: Grok writes tasks here. Claude reads, builds, pushes, and logs progress. Atlas challenges and watches.*
