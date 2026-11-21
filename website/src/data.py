"""Site content. Edit here, then run `python3 build.py`.

Stone facts come from davias-master-plan.md (standard mineralogy). Every claim
is labeled Proven / Traditional. No prices or dates are set until the owner
decides them: price=None shows "Ask for price".
"""

SITE = {
    "name": "Davias Earthbound Jewelry",
    "domain": "https://daviasearthboundjewelry.love",
    "email": "DaviasEarthBoundJewelry@gmail.com",
    "phone": "747-528-7039",
    "instagram": "https://www.instagram.com/DaviasJewelry",
    "tiktok": "https://www.tiktok.com/@DaviasJewelry",
    "x": "https://x.com/DaviasJewelry",
    "pinterest": "https://www.pinterest.com/daviasearthboundjewelry",
    # Shown at the top of every page. Set to "" to hide.
    "notice": "Opening soon. Order any piece by message while the online checkout is being set up.",
}

STONES = {
    "quartz": {
        "name": "Yellow Quartz", "colors": ["#f2d27a", "#d9a943", "#fbe7a8"], "mohs": 7,
        "proven": "Quartz colored golden-yellow by traces of iron (often sold as citrine). Like all quartz it is piezoelectric: pressure makes a small electric charge.",
        "trad": "Warmth, joy, abundance and clarity. Shared as tradition, not fact.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "That it brings abundance or joy as a measured effect.",
    },
    "clear": {
        "name": "Clear Quartz", "colors": ["#eef3f8", "#d4dde8", "#ffffff"], "mohs": 7,
        "proven": "Nearly pure silicon dioxide, Mohs 7. Piezoelectric like all quartz: the reason quartz crystals keep time in watches and clocks.",
        "trad": "Clarity and focus; often called an \"amplifier\" stone. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "That it amplifies energy or intentions in any measured way.",
    },
    "tiger": {
        "name": "Tiger's Eye", "colors": ["#a8702a", "#d6a145", "#6b4318"], "mohs": 7,
        "proven": "Quartz, Mohs 7. The moving shimmer (chatoyancy) comes from fine fibers replaced by quartz and iron oxides.",
        "trad": "Courage, confidence and protection. Shared as tradition.",
        "care": "Tough stone. Mild soap and water is fine.",
        "no": "Protection or courage as a measured effect.",
    },
    "gjade": {
        "name": "Green Jade", "colors": ["#4f9b6e", "#79bd8f", "#2f6e4c"], "mohs": 6.5,
        "proven": "Jade is two minerals, nephrite or jadeite, Mohs 6 to 7. Famous for toughness: it resists breaking better than most stones.",
        "trad": "Harmony, balance, good luck and the heart. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "Luck or heart effects as fact.",
    },
    "pjade": {
        "name": "Purple Jade", "colors": ["#9a7cc9", "#b8a0e0", "#6f54a0"], "mohs": 7,
        "proven": "A purple jadeite, colored by traces of manganese. Same tough jade family, Mohs 6.5 to 7.",
        "trad": "Calm, intuition and spirit. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "Intuition or spiritual effects as fact.",
    },
    "selenite": {
        "name": "Selenite", "colors": ["#f3f1ea", "#dcd8cd", "#ffffff"], "mohs": 2,
        "proven": "A clear form of gypsum (calcium sulfate). Very soft, Mohs 2: it scratches with a fingernail. Shop \"selenite\" is usually satin spar, the fibrous form.",
        "trad": "Clarity, calm and cleansing a space. Shared as tradition.",
        "care": "Keep it dry. Gypsum slowly dissolves in water. Wipe clean and handle gently.",
        "no": "That it cleanses energy in any measured way, or heals anything.",
    },
    "amethyst": {
        "name": "Amethyst", "colors": ["#9b59b6", "#8e44ad", "#d2b4de"], "mohs": 7,
        "proven": "Quartz colored by iron and other trace elements. Mohs 7. Piezoelectric like all quartz.",
        "trad": "Calm, intuition, and spiritual clarity. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine. Avoid prolonged sun to preserve color.",
        "no": "Spiritual or calming effects as a measured fact.",
    },
    "onyx": {
        "name": "Onyx", "colors": ["#1a1a1a", "#333333", "#4d4d4d"], "mohs": 7,
        "proven": "Chalcedony (cryptocrystalline quartz), often banded. Mohs 6.5–7.",
        "trad": "Strength and grounding. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "Grounding as a measured effect.",
    },
    "rose": {
        "name": "Rose Quartz", "colors": ["#f4c2c2", "#e8b4b8", "#f8d7da"], "mohs": 7,
        "proven": "Quartz colored by titanium, iron, or manganese. Mohs 7. Piezoelectric.",
        "trad": "Love, compassion, and emotional balance. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "Emotional effects as a measured fact.",
    },
    "ptourmaline": {
        "name": "Pink Tourmaline", "colors": ["#e88aa8", "#d96b8f", "#f5b8c9"], "mohs": 7,
        "proven": "A boron silicate crystal, Mohs 7–7.5. Tourmaline is piezoelectric and pyroelectric: pressure or a change in temperature makes a small electric charge.",
        "trad": "Compassion and gentleness. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "Emotional effects as a measured fact.",
    },
    # Stones for the other 7 Helix designs (HELIX_COLLECTION.md 4-10). Standard mineralogy;
    # amber and obsidian are not minerals and say so.
    "amazonite": {
        "name": "Amazonite", "colors": ["#5fbfae", "#7fd3c1", "#3f9c8c"], "mohs": 6,
        "proven": "A blue-green microcline, a potassium feldspar, Mohs 6 to 6.5. Its color is linked to traces of lead in the crystal. It splits along flat planes, so a hard knock can chip it.",
        "trad": "Calm and clear communication. Shared as tradition.",
        "care": "Mild soap and water is fine. Avoid knocks and harsh cleaners.",
        "no": "Calming or communication effects as a measured fact.",
    },
    "aquamarine": {
        "name": "Aquamarine", "colors": ["#9fd4e6", "#bfe5f0", "#7cbcd4"], "mohs": 7.5,
        "proven": "Blue beryl (beryllium aluminum silicate), colored by iron. Mohs 7.5 to 8, harder than quartz. Emerald is the green form of the same mineral.",
        "trad": "Calm and courage; long called a sailors' stone. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "Calm or courage as a measured effect.",
    },
    "carnelian": {
        "name": "Carnelian", "colors": ["#d2542a", "#e57a3e", "#a8391b"], "mohs": 6.5,
        "proven": "Orange-red chalcedony, a microcrystalline quartz, colored by iron oxide. Mohs 6.5 to 7. Much \"carnelian\" sold online is dyed or heated agate; we tell you which ours is.",
        "trad": "Vitality, motivation and courage. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "Energy or motivation as a measured effect.",
    },
    "labradorite": {
        "name": "Labradorite", "colors": ["#5d6b78", "#3f8fb0", "#8aa27a"], "mohs": 6,
        "proven": "A plagioclase feldspar, Mohs 6 to 6.5. The flash of blue and green (labradorescence) is light interfering inside very thin layers in the crystal, the same physics as a soap bubble.",
        "trad": "Intuition and change. Shared as tradition.",
        "care": "Mild soap and water is fine. Avoid knocks: it can split along flat planes.",
        "no": "Intuition or protection as a measured effect.",
    },
    "moonstone": {
        "name": "Moonstone", "colors": ["#eceef2", "#cfd8e6", "#f7f3ea"], "mohs": 6,
        "proven": "A feldspar made of two minerals in very thin alternating layers. Light scattering between the layers gives the soft floating glow (adularescence). Mohs 6 to 6.5.",
        "trad": "New beginnings and intuition; a traveler's stone. Shared as tradition.",
        "care": "Mild soap and water is fine. Avoid knocks and heat.",
        "no": "Intuition or luck as a measured effect.",
    },
    "citrine": {
        "name": "Citrine", "colors": ["#f0b23a", "#f7cd6a", "#d98c1f"], "mohs": 7,
        "proven": "Yellow to orange quartz, Mohs 7, piezoelectric like all quartz. Natural citrine is rare: most citrine sold is amethyst that was heated until it turned gold. We tell you which ours is.",
        "trad": "Abundance, warmth and optimism. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine. Long hours in strong sun can fade it.",
        "no": "That it brings money or abundance as a measured effect.",
    },
    "aventurine": {
        "name": "Green Aventurine", "colors": ["#4f9a63", "#74b884", "#2e6e44"], "mohs": 6.5,
        "proven": "Quartz with tiny flat flakes of another mineral, usually green fuchsite mica. The flakes give the glitter (aventurescence). Mohs 6.5 to 7.",
        "trad": "Luck and opportunity. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "Luck as a measured effect.",
    },
    "amber": {
        "name": "Amber", "colors": ["#d98a1c", "#f0aa3c", "#a8600f"], "mohs": 2,
        "proven": "Not a mineral: fossilized tree resin, millions of years old. Very soft (Mohs 2 to 2.5) and light. Rub it and it holds a static charge; the Greek word for amber, elektron, gave us \"electricity\". Plastic and young resin (copal) fakes are common.",
        "trad": "Warmth and comfort. Shared as tradition.",
        "care": "Keep it dry and away from perfume, alcohol, hairspray and heat. Wipe with a soft cloth.",
        "no": "That it eases pain or teething. The FDA warns against teething necklaces for babies (choking and strangulation risk). Our pieces are for adults.",
    },
    "smoky": {
        "name": "Smoky Quartz", "colors": ["#6b5847", "#8f7a64", "#4a3c30"], "mohs": 7,
        "proven": "Quartz darkened by natural radiation in the rock acting on traces of aluminum. Mohs 7, piezoelectric like all quartz.",
        "trad": "Grounding and steadiness. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "Grounding or protection as a measured effect.",
    },
    "lapis": {
        "name": "Lapis Lazuli", "colors": ["#2a4ba0", "#3d63c4", "#1c3373"], "mohs": 5,
        "proven": "A rock, not a single mineral: mostly blue lazurite, with white calcite and gold flecks of pyrite. Mohs 5 to 5.5. Ground up, it was the blue paint ultramarine. It is often dyed or waxed.",
        "trad": "Wisdom and truth. Shared as tradition.",
        "care": "Keep it dry: it is softer and porous. Wipe with a soft cloth; no soaking or chemicals.",
        "no": "Wisdom or truth-telling as a measured effect.",
    },
    "btourmaline": {
        "name": "Black Tourmaline", "colors": ["#1d1d1f", "#38383b", "#0e0e10"], "mohs": 7,
        "proven": "Schorl, the iron-rich black tourmaline. A boron silicate, Mohs 7 to 7.5, piezoelectric and pyroelectric like all tourmaline.",
        "trad": "Protection. Shared as tradition.",
        "care": "Durable. Mild soap and water is fine.",
        "no": "That it blocks phone or Wi-Fi radiation (EMF) or \"negative energy\". It does not.",
    },
    "obsidian": {
        "name": "Obsidian", "colors": ["#141414", "#2b2b2e", "#3c3a40"], "mohs": 5,
        "proven": "Not a mineral: natural volcanic glass, made when lava cools too fast to form crystals. Mohs 5 to 5.5. It breaks with curved, razor-sharp edges, which is why people made blades from it for thousands of years.",
        "trad": "Protection and grounding. Shared as tradition.",
        "care": "Mild soap and water is fine. It is glass: a drop on tile can chip it.",
        "no": "Protection as a measured effect.",
    },
}

TYPES = {
    "bracelet": ("Bracelets", "Our heart. Sized to your wrist, finished like fine jewelry."),
    "earrings": ("Earrings", "Small stones with light that moves when you do."),
    "necklace": ("Necklaces", "Longer strands and single pendant stones."),
    "anklet": ("Anklets", "Summer pieces made to layer. Each page says whether its stones can take water."),
}

# Construction, from BRACELET_CORD_OPTIONS.md.
FINISH = {
    "bracelet": "Nylon-coated stainless beading wire with a solid metal clasp. No cheap stretch cord.",
    "necklace": "Nylon-coated stainless beading wire with a solid metal clasp.",
    "anklet": "Waxed cord with a sliding knot: adjustable and water-resistant. The stones decide if it goes to the beach.",
    "earrings": "Hypoallergenic hooks with metal findings.",
}

PRODUCTS = [
    # Original pieces
    {"slug": "night-quartz", "name": "Night Quartz", "type": "bracelet", "stones": ["quartz", "pjade"], "price": None,
     "story": "Golden quartz beside deep purple jade. One stone is piezoelectric; the other owes its violet to manganese.",
     "matching": "Cool & neutral skin · Blue or green eyes · Dark or silver hair."},
    {"slug": "earthbound-gold", "name": "Earthbound Gold", "type": "bracelet", "stones": ["tiger"], "price": None,
     "story": "Tiger's eye with gold-tone spacers. Turn your wrist and the shimmer travels across every bead.",
     "matching": "Warm & olive skin · Brown or hazel eyes · Warm brown or black hair."},
    {"slug": "jade-balance", "name": "Jade Balance", "type": "bracelet", "stones": ["gjade", "pjade"], "price": None,
     "story": "Green and purple jade together: the toughest stone family we string, in two colors.",
     "matching": "All skin tones. Especially striking on cool and neutral complexions."},
    {"slug": "watch-stone", "name": "Watch Stone", "type": "bracelet", "stones": ["quartz"], "price": None,
     "story": "All yellow quartz, the same mineral that keeps time inside a quartz watch.",
     "matching": "Warm skin tones · Amber or brown eyes · Warm hair colors."},
    {"slug": "sunrise-band", "name": "Sunrise Band", "type": "bracelet", "stones": ["tiger", "quartz"], "price": None,
     "story": "Tiger's eye fading into golden quartz, like the first light over the desert.",
     "matching": "Warm & golden skin · Brown or green eyes · Warm hair colors."},
    {"slug": "strength-stack", "name": "Strength Stack", "type": "bracelet", "stones": ["gjade", "tiger"], "price": None,
     "story": "Two of the most durable stones we use, made to be worn every single day.",
     "matching": "Warm and olive skin · Brown eyes · Warm hair."},
    {"slug": "earth-circle", "name": "Earth Circle", "type": "bracelet", "stones": ["quartz", "tiger", "gjade", "pjade", "selenite"], "price": None,
     "story": "All five starting stones in one circle, the bracelet from our logo.",
     "matching": "All skin tones. A versatile statement piece."},
    {"slug": "midnight-jade", "name": "Midnight Jade", "type": "necklace", "stones": ["pjade"], "price": None,
     "story": "A strand of purple jade with tiny dark spacers. Quiet, deep, elegant.",
     "matching": "Cool & neutral skin · Blue or green eyes · Dark hair."},
    {"slug": "golden-thread", "name": "Golden Thread", "type": "necklace", "stones": ["quartz"], "price": None,
     "story": "Yellow quartz with one fine gold-tone accent.",
     "matching": "Warm skin tones · Brown or amber eyes."},
    {"slug": "clear-intent", "name": "Clear Intent", "type": "earrings", "stones": ["clear", "selenite"], "price": None,
     "story": "Clear quartz and a touch of selenite. Minimal, bright, made for special days.",
     "matching": "Cool and fair skin · Light eyes."},
    {"slug": "violet-charge", "name": "Violet Charge", "type": "earrings", "stones": ["pjade", "quartz"], "price": None,
     "story": "Purple and gold, a color contrast that catches every light.",
     "matching": "Cool & neutral skin · Blue or violet eyes."},
    {"slug": "jade-garden", "name": "Jade Garden", "type": "anklet", "stones": ["gjade", "pjade"], "price": None,
     "story": "Green and purple jade alternating on waxed cord. Tough enough for the beach.",
     "matching": "All skin tones. Especially complementary to warm complexions."},
    {"slug": "soft-light", "name": "Soft Light", "type": "anklet", "stones": ["selenite", "clear"], "price": None,
     "story": "Selenite and clear quartz for evenings and occasions. Keep it out of the water.",
     "matching": "Fair to medium skin · Light eyes."},

    # Helix Collection (featured)
    {"slug": "violet-vortex", "name": "Violet Vortex", "type": "bracelet", "stones": ["amethyst", "clear"], "price": None,
     "story": "Amethyst and clear quartz in a double helix. Cool violet light that moves with the wrist.",
     "matching": "Cool & neutral skin · Blue or green eyes · Dark or silver hair.",
     "helix": "Double"},
    {"slug": "earthfire-twist", "name": "Earthfire Twist", "type": "bracelet", "stones": ["tiger", "onyx"], "price": None,
     "story": "Tiger's eye and onyx twisted together. Warm gold against deep black.",
     "matching": "Warm & olive skin · Brown or hazel eyes · Warm brown or black hair.",
     "helix": "Double"},
    {"slug": "blush-trinity", "name": "Blush Trinity", "type": "bracelet", "stones": ["rose", "ptourmaline"], "price": None,
     "story": "Rose quartz and pink tourmaline in a triple helix. Soft blush that catches light from every angle.",
     "matching": "Fair to medium skin · Light eyes · Blonde or light brown hair.",
     "helix": "Triple"},
    {"slug": "reef-ripple", "name": "Reef Ripple", "type": "bracelet", "stones": ["amazonite", "aquamarine"], "price": None,
     "story": "Amazonite and aquamarine in a double helix. Two sea-glass blues, one soft and one bright.",
     "matching": "Cool skin tones · Blue eyes · Ash or dark hair.",
     "helix": "Double"},
    {"slug": "ember-and-ice", "name": "Ember & Ice", "type": "bracelet", "stones": ["carnelian", "clear"], "price": None,
     "story": "Carnelian and clear quartz in a double helix. Glowing orange wound around clear light.",
     "matching": "Warm skin tones · Amber or brown eyes · Red or warm brown hair.",
     "helix": "Double"},
    {"slug": "northern-lights", "name": "Northern Lights", "type": "bracelet", "stones": ["labradorite", "moonstone"], "price": None,
     "story": "Labradorite and moonstone in a double helix. Two feldspars, each with its own flash of light.",
     "matching": "Cool & neutral tones · Any eye color · Dark or silver hair.",
     "helix": "Double"},
    {"slug": "jungle-gold", "name": "Jungle Gold", "type": "bracelet", "stones": ["citrine", "aventurine"], "price": None,
     "story": "Citrine and green aventurine in a double helix. Gold and green, with a fine glitter in the green.",
     "matching": "Warm & golden skin · Brown or green eyes · Warm hair colors.",
     "helix": "Double"},
    {"slug": "amber-mist", "name": "Amber Mist", "type": "bracelet", "stones": ["amber", "smoky"], "price": None,
     "story": "Amber and smoky quartz in a double helix. Honey and smoke, warm to the touch.",
     "matching": "Warm, olive, and medium skin · Brown eyes and hair.",
     "helix": "Double"},
    {"slug": "lapis-current", "name": "Lapis Current", "type": "bracelet", "stones": ["lapis"], "price": None,
     "story": "Lapis lazuli twisted into a double helix. Deep blue with flecks of gold pyrite.",
     "matching": "Cool and neutral skin · Blue eyes · Dark hair.",
     "helix": "Double"},
    {"slug": "obsidian-spiral", "name": "Obsidian Spiral", "type": "bracelet", "stones": ["btourmaline", "obsidian"], "price": None,
     "story": "Black tourmaline and obsidian in a triple helix. A crystal and a volcanic glass, both jet black.",
     "matching": "All skin tones. Striking against warm complexions and light eyes.",
     "helix": "Triple"},
    {"slug": "amethyst-strand", "name": "Amethyst Strand", "type": "bracelet", "stones": ["amethyst"], "price": None,
     "story": "Single strand of amethyst. Clean and cool, made to wear every day.",
     "matching": "Cool skin tones · Blue or violet eyes.",
     "helix": "Single"},
    {"slug": "tigers-eye-strand", "name": "Tiger's Eye Strand", "type": "bracelet", "stones": ["tiger"], "price": None,
     "story": "Single strand of tiger's eye. The classic shimmer, every day.",
     "matching": "Warm and olive skin · Brown eyes · Warm hair.",
     "helix": "Single"},
]

THEMES = ["Country & flag colors", "Team colors", "Christmas & holidays", "Faith & occasions", "Beach: shells & starfish"]

DROP = {
    "name": "Violet Vortex",
    "stones": ["amethyst", "clear"],
    "size": 100,
    "hours": 72,
    "text": "Amethyst and clear quartz in a double helix. Cool violet light that moves with the wrist.",
}

FAQ = [
    ("Do crystals have healing powers?",
     "We don't claim they do, and we never will. What's proven is the mineral itself: what it's made of, how hard it is, and, for quartz, that it's piezoelectric. Traditional meanings are shared and labeled as tradition, so you can enjoy them knowing what they are."),
    ("Are the stones real?",
     "Yes. Every bead is a natural material, and almost all are minerals. Two are not, and their pages say so: amber is fossilized tree resin and obsidian is volcanic glass. If a stone is commonly sold under another name (yellow quartz is often sold as \"citrine\"), we tell you."),
    ("What is piezoelectricity?",
     "Squeeze a quartz crystal and it makes a tiny electric charge; run electricity through it and it vibrates at a steady rate. That's how quartz watches keep time. Tiger's eye, clear quartz and yellow quartz are all quartz."),
    ("Are crystals conductive?",
     "Most gemstones are electrical insulators, not conductors like copper. You'll see \"conductive crystals\" online a lot. We'd rather tell you the real thing."),
    ("Which stone can I wear every day?",
     "Quartz, tiger's eye, jade, aquamarine and tourmaline are hard and tough (Mohs 6.5 and up). Selenite (Mohs 2) and amber (Mohs 2 to 2.5) are very soft, and lapis is porous: keep those dry and wear them with care."),
    ("How do I find my size?",
     "Wrap a soft tape measure or a strip of paper around your wrist where you'd wear it, and add about half an inch (1.3 cm) for comfort. Send us that number with your order."),
    ("How do I pay?",
     "For now we confirm every order by message first: the stones, your size, the price and shipping. We'll send payment details then. Online checkout is coming."),
]

# Crystal Finder. Every stone is reachable by color, and every tradition option
# lists only stones whose own "trad" line names one of its words (check_site #13).
FINDER = {
    "color": [
        ("gold", "Warm gold & amber", ["quartz", "tiger", "citrine", "amber", "carnelian"]),
        ("purple", "Purple", ["pjade", "amethyst"]),
        ("green", "Green", ["gjade", "aventurine", "amazonite"]),
        ("blue", "Blue", ["aquamarine", "lapis", "amazonite", "labradorite"]),
        ("pink", "Pink", ["rose", "ptourmaline"]),
        ("white", "White & clear", ["clear", "selenite", "moonstone"]),
        ("dark", "Black & smoky", ["onyx", "obsidian", "btourmaline", "smoky", "labradorite"]),
    ],
    # (value, label, stones, words the stone's trad line must contain)
    "feel": [
        ("calm", "Calm", ["pjade", "selenite", "amethyst", "amazonite", "aquamarine"], ["calm"]),
        ("confidence", "Confidence & courage", ["tiger", "carnelian", "aquamarine"], ["confidence", "courage"]),
        ("balance", "Balance", ["gjade", "rose"], ["balance"]),
        ("warmth", "Warmth & joy", ["quartz", "citrine", "amber"], ["warmth", "joy"]),
        ("clarity", "Clarity", ["clear", "selenite", "amethyst"], ["clarity"]),
        ("love", "Love & compassion", ["rose", "ptourmaline"], ["love", "compassion"]),
        ("grounding", "Grounding & protection", ["onyx", "smoky", "obsidian", "btourmaline", "tiger"], ["grounding", "protection"]),
        ("intuition", "Intuition & new beginnings", ["pjade", "amethyst", "labradorite", "moonstone"], ["intuition", "beginnings"]),
        ("luck", "Luck & abundance", ["aventurine", "citrine", "gjade", "quartz"], ["luck", "abundance"]),
        ("wisdom", "Wisdom & communication", ["lapis", "amazonite"], ["wisdom", "communication"]),
    ],
    "undertone": [
        ("unsure", "Not sure"),
        ("cool", "Cool"),
        ("warm", "Warm"),
        ("neutral", "Neutral"),
    ],
}


def undertones(matching):
    """Undertones a helix design is styled for, read from its own matching text.

    Only the skin clause (before the first "·") counts. "All skin tones" -> ["any"]
    (shown for every undertone). No undertone word (e.g. Blush Trinity's "Fair to
    medium skin") -> ["unspecified"], shown only under "Not sure", so the finder
    never invents a fit the text lacks.
    "Olive" is not mapped to an undertone of its own: every design that names
    olive also names warm, and the finder says so (check_site #14).
    """
    skin = matching.split("·")[0].lower()
    if "all skin" in skin:
        return ["any"]
    found = [u for u in ("cool", "warm", "neutral") if u in skin]
    return found or ["unspecified"]
