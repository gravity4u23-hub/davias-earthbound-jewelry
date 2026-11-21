# Davias Helix Collection

Featured authentic crystal bracelets. Exact names, stone combinations, construction, and skin-tone / eye / hair matching. Use these as the primary bracelet inventory.

All pieces are real natural crystals. Honesty engine applies: Proven mineral facts only; traditional meanings labeled as tradition.

## Designs

1. **Violet Vortex**  
   Stones: Amethyst + Clear Quartz  
   Construction: Double Helix  
   Complements: Cool & neutral skin · Blue or green eyes · Dark or silver hair.

2. **Earthfire Twist**  
   Stones: Tiger’s Eye + Onyx  
   Construction: Double Helix  
   Complements: Warm & olive skin · Brown or hazel eyes · Warm brown or black hair.

3. **Blush Trinity**  
   Stones: Rose Quartz + Pink Tourmaline  
   Construction: Triple Helix  
   Complements: Fair to medium skin · Light eyes · Blonde or light brown hair.

4. **Reef Ripple**  
   Stones: Amazonite + Aquamarine  
   Construction: Double Helix  
   Complements: Cool skin tones · Blue eyes · Ash or dark hair.

5. **Ember & Ice**  
   Stones: Carnelian + Clear Quartz  
   Construction: Double Helix  
   Complements: Warm skin tones · Amber or brown eyes · Red or warm brown hair.

6. **Northern Lights**  
   Stones: Labradorite + Moonstone  
   Construction: Double Helix  
   Complements: Cool & neutral tones · Any eye color · Dark or silver hair.

7. **Jungle Gold**  
   Stones: Citrine + Green Aventurine  
   Construction: Double Helix  
   Complements: Warm & golden skin · Brown or green eyes · Warm hair colors.

8. **Amber Mist**  
   Stones: Amber + Smoky Quartz  
   Construction: Double Helix  
   Complements: Warm, olive, and medium skin · Brown eyes and hair.

9. **Lapis Current**  
   Stones: Lapis Lazuli  
   Construction: Double Helix  
   Complements: Cool and neutral skin · Blue eyes · Dark hair.

10. **Obsidian Spiral**  
    Stones: Black Tourmaline + Obsidian  
    Construction: Triple Helix  
    Complements: All skin tones. Striking against warm complexions and light eyes.

11. **Amethyst Strand**  
    Stones: Amethyst  
    Construction: Single Strand  
    Complements: Cool skin tones · Blue or violet eyes.

12. **Tiger’s Eye Strand**  
    Stones: Tiger’s Eye  
    Construction: Single Strand  
    Complements: Warm and olive skin · Brown eyes · Warm hair.

## On the site (Nov 21, 2026)
All 12 designs have product pages, shop cards and helix filters. The last 7 (Reef Ripple, Ember & Ice, Northern Lights, Jungle Gold, Amber Mist, Lapis Current, Obsidian Spiral) landed with 12 new Proven / Traditional stone profiles in `website/src/data.py`. Amber (fossil resin) and obsidian (volcanic glass) are labelled as not minerals, and the homepage and FAQ no longer say every bead is stone. `website/tests/check_site.py` checks this file against the site so the two can't drift.

Still owner/maker questions before launch: can Octavia source each stone, and is the citrine natural or heated amethyst (the page says we will tell the buyer which)?

## Notes for implementation
- Feature these on the Home and Shop pages.
- Add filters: All / Double Helix / Triple Helix / Single Strand.
- Show the matching text on every product card and product page.
- Crystal Finder / quiz should recommend from this list based on Cool / Warm / Neutral undertone.
- Prices: leave as Ask for price until owner sets them.
- Construction: nylon-coated stainless beading wire with solid metal clasp (per existing FINISH rules).
