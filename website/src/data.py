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
}

TYPES = {
    "bracelet": ("Bracelets", "Our heart. Sized to your wrist, finished like fine jewelry."),
    "earrings": ("Earrings", "Small stones with light that moves when you do."),
    "necklace": ("Necklaces", "Longer strands and single pendant stones."),
    "anklet": ("Anklets", "Summer pieces, beach-ready, made to layer."),
}

# Construction, from BRACELET_CORD_OPTIONS.md.
FINISH = {
    "bracelet": "Nylon-coated stainless beading wire with a solid metal clasp. No cheap stretch cord.",
    "necklace": "Nylon-coated stainless beading wire with a solid metal clasp.",
    "anklet": "Waxed cord with a sliding knot: adjustable, water-resistant, beach-ready.",
    "earrings": "Hypoallergenic hooks with metal findings.",
}

PRODUCTS = [
    {"slug": "night-quartz", "name": "Night Quartz", "type": "bracelet", "stones": ["quartz", "pjade"], "price": None,
     "story": "Golden quartz beside deep purple jade. One stone is piezoelectric; the other owes its violet to manganese."},
    {"slug": "earthbound-gold", "name": "Earthbound Gold", "type": "bracelet", "stones": ["tiger"], "price": None,
     "story": "Tiger's eye with gold-tone spacers. Turn your wrist and the shimmer travels across every bead."},
    {"slug": "jade-balance", "name": "Jade Balance", "type": "bracelet", "stones": ["gjade", "pjade"], "price": None,
     "story": "Green and purple jade together: the toughest stone family we string, in two colors."},
    {"slug": "watch-stone", "name": "Watch Stone", "type": "bracelet", "stones": ["quartz"], "price": None,
     "story": "All yellow quartz, the same mineral that keeps time inside a quartz watch."},
    {"slug": "sunrise-band", "name": "Sunrise Band", "type": "bracelet", "stones": ["tiger", "quartz"], "price": None,
     "story": "Tiger's eye fading into golden quartz, like the first light over the desert."},
    {"slug": "strength-stack", "name": "Strength Stack", "type": "bracelet", "stones": ["gjade", "tiger"], "price": None,
     "story": "Two of the most durable stones we use, made to be worn every single day."},
    {"slug": "earth-circle", "name": "Earth Circle", "type": "bracelet", "stones": ["quartz", "tiger", "gjade", "pjade", "selenite"], "price": None,
     "story": "All five starting stones in one circle, the bracelet from our logo."},
    {"slug": "midnight-jade", "name": "Midnight Jade", "type": "necklace", "stones": ["pjade"], "price": None,
     "story": "A strand of purple jade with tiny dark spacers. Quiet, deep, elegant."},
    {"slug": "golden-thread", "name": "Golden Thread", "type": "necklace", "stones": ["quartz"], "price": None,
     "story": "Yellow quartz with one fine gold-tone accent. Looks far more expensive than it is."},
    {"slug": "clear-intent", "name": "Clear Intent", "type": "earrings", "stones": ["clear", "selenite"], "price": None,
     "story": "Clear quartz and a touch of selenite. Minimal, bright, made for special days."},
    {"slug": "violet-charge", "name": "Violet Charge", "type": "earrings", "stones": ["pjade", "quartz"], "price": None,
     "story": "Purple and gold, a color contrast that catches every light."},
    {"slug": "jade-garden", "name": "Jade Garden", "type": "anklet", "stones": ["gjade", "pjade"], "price": None,
     "story": "Green and purple jade alternating on waxed cord. Tough enough for the beach."},
    {"slug": "soft-light", "name": "Soft Light", "type": "anklet", "stones": ["selenite", "clear"], "price": None,
     "story": "Selenite and clear quartz for evenings and occasions. Keep it out of the water."},
]

THEMES = ["Country & flag colors", "Team colors", "Christmas & holidays", "Faith & occasions", "Beach: shells & starfish"]

DROP = {
    "name": "Night Quartz",
    "stones": ["quartz", "pjade"],
    "size": 100,
    "hours": 72,
    "text": "Golden quartz beside deep purple jade. Quartz is piezoelectric; the jade's violet comes from traces of manganese.",
}

FAQ = [
    ("Do crystals have healing powers?",
     "We don't claim they do, and we never will. What's proven is the mineral itself: what it's made of, how hard it is, and, for quartz, that it's piezoelectric. Traditional meanings are shared and labeled as tradition, so you can enjoy them knowing what they are."),
    ("Are the stones real?",
     "Yes. Every bead is natural stone. If a stone is commonly sold under another name (yellow quartz is often sold as \"citrine\"), we tell you."),
    ("What is piezoelectricity?",
     "Squeeze a quartz crystal and it makes a tiny electric charge; run electricity through it and it vibrates at a steady rate. That's how quartz watches keep time. Tiger's eye, clear quartz and yellow quartz are all quartz."),
    ("Are crystals conductive?",
     "Most gemstones are electrical insulators, not conductors like copper. You'll see \"conductive crystals\" online a lot. We'd rather tell you the real thing."),
    ("Which stone can I wear every day?",
     "Quartz, tiger's eye and jade are hard and tough (Mohs 6.5–7). Selenite is very soft (Mohs 2) and dissolves slowly in water, so wear it for special occasions."),
    ("How do I find my size?",
     "Wrap a soft tape measure or a strip of paper around your wrist where you'd wear it, and add about half an inch (1.3 cm) for comfort. Send us that number with your order."),
    ("How do I pay?",
     "For now we confirm every order by message first: the stones, your size, the price and shipping. We'll send payment details then. Online checkout is coming."),
]
