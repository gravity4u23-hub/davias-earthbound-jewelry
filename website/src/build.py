"""Builds the static site into ../site/ from data.py.

    cd website/src && python3 build.py

The output folder is plain HTML/CSS/JS: upload its contents to Bluehost's
public_html (see website/README.md).
"""
import html
import json
import shutil
from datetime import date
from pathlib import Path

from PIL import Image

from data import DROP, FAQ, PRODUCTS, SITE, STONES, THEMES, TYPES, FINISH

SRC = Path(__file__).parent
OUT = SRC.parent / "site"
e = html.escape

NAV = [
    ("index.html", "Home"),
    ("shop.html", "Shop"),
    ("drop.html", "Monthly Drop"),
    ("stones.html", "Stone Guide"),
    ("finder.html", "Crystal Finder"),
    ("about.html", "Our Story"),
]


def page(path, title, body, *, desc, current=None, root=""):
    nav = "".join(
        f'<a href="{root}{href}"{" aria-current=page" if href == current else ""}>{label}</a>'
        for href, label in NAV
    )
    notice = f'<div class="ribbon">{e(SITE["notice"])}</div>' if SITE["notice"] else ""
    canonical = SITE["domain"] + "/" + ("" if path == "index.html" else path)
    full_title = SITE["name"] if path == "index.html" else f"{title} · {SITE['name']}"
    org = {
        "@context": "https://schema.org", "@type": "Organization", "name": SITE["name"],
        "url": SITE["domain"], "email": SITE["email"], "telephone": SITE["phone"],
        "logo": SITE["domain"] + "/davias-logo.webp",
        "sameAs": [SITE["instagram"], SITE["tiktok"], SITE["x"], SITE["pinterest"]],
    }
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE['domain']}/og-image.jpg">
<meta property="og:url" content="{canonical}">
<meta name="theme-color" content="#12141c">
<link rel="icon" href="{root}favicon.png">
<link rel="apple-touch-icon" href="{root}favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500&family=Pinyon+Script&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}site.css">
<script type="application/ld+json">{json.dumps(org)}</script>
</head>
<body>
{notice}
<nav class="top" aria-label="Main">
  <div class="wrap">
    <a href="{root}index.html" class="wordmark name">Davias</a>
    <div class="links" id="menu">{nav}</div>
    <div class="nav-right">
      <a class="bag-link" href="{root}order.html">Order bag <b data-bag-count>0</b></a>
      <button class="menu-btn" aria-controls="menu" aria-expanded="false">Menu</button>
    </div>
  </div>
</nav>
<main>
{body}
</main>
<footer>
  <div class="wrap">
    <span class="wordmark name" style="font-size:28px">{e(SITE["name"])}</span>
    <p>Handmade with love by David &amp; Octavia ·
      <a href="{SITE['instagram']}">Instagram</a> · <a href="{SITE['tiktok']}">TikTok</a> ·
      <a href="{SITE['pinterest']}">Pinterest</a> · <a href="{SITE['x']}">X</a></p>
    <p>{e(SITE["email"])} · {e(SITE["phone"])}</p>
    <p>Crystals are jewelry, not medicine. Traditional meanings are shared as tradition and belief.
      Nothing here diagnoses, treats or cures any condition.</p>
    <p>© {date.today().year} {e(SITE["name"])}</p>
  </div>
</footer>
<script src="{root}data.js"></script>
<script src="{root}site.js"></script>
</body>
</html>
"""
    out = OUT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")


def stone_names(keys):
    return " + ".join(STONES[k]["name"] for k in keys)


HELIX = {"Double": "Double Helix", "Triple": "Triple Helix", "Single": "Single Strand"}


def helix_key(p):
    return f"helix-{p['helix'].lower()}" if p.get("helix") else ""


def care_text(keys):
    """One care line per piece. A stone that must stay dry (selenite) overrides
    'soap and water is fine' for the whole piece, so the page never says both."""
    cares = list(dict.fromkeys(STONES[k]["care"] for k in keys))
    dry = [c for c in cares if "Keep it dry" in c]
    if dry:
        names = " and ".join(STONES[k]["name"] for k in keys if "Keep it dry" in STONES[k]["care"])
        return f"Contains {names}, so the whole piece follows its care: " + " ".join(dry)
    return " ".join(cares)


def piece_card(p, root=""):
    label = TYPES[p["type"]][0][:-1] if p["type"] != "earrings" else "Earrings"
    price = f"${p['price']}" if p["price"] else "Ask for price"
    return (
        f'<a class="card piece" href="{root}p/{p["slug"]}.html" data-type="{p["type"]}" data-helix="{helix_key(p)}" data-stones="{",".join(p["stones"])}">'
        f'<div class="photo"><div class="strand" data-strand="{",".join(p["stones"])}" data-n="9" style="width:84%;height:90px"></div>'
        f'<small>Photo coming soon</small></div>'
        f'<span class="tag">{label} · {e(stone_names(p["stones"]))}</span>'
        f'<div class="meta"><h3>{e(p["name"])}</h3><span>{price}</span></div>'
        f'<p>{e(p["story"])}</p>'
        + (f'<p class="match"><small>Complements: {e(p["matching"])}</small></p>' if p.get("matching") else "")
        + '</a>'
    )


def head(eyebrow, title, lede):
    return (f'<section class="page-head"><div class="wrap"><span class="eyebrow">{eyebrow}</span>'
            f'<h1>{title}</h1><p class="lede">{lede}</p></div></section>')


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copy(SRC / "site.css", OUT / "site.css")
    shutil.copy(SRC / "site.js", OUT / "site.js")

    # Images: web logo, favicon, social preview.
    logo = Image.open(SRC.parent.parent / "assets" / "davias-logo.webp").convert("RGB")
    web = logo.copy(); web.thumbnail((1200, 1200)); web.save(OUT / "davias-logo.webp", quality=84)
    side = min(logo.size)
    sq = logo.crop(((logo.width - side) // 2, (logo.height - side) // 2,
                    (logo.width + side) // 2, (logo.height + side) // 2))
    sq.resize((192, 192)).save(OUT / "favicon.png")
    og = logo.copy(); og.thumbnail((1200, 630)); canvas = Image.new("RGB", (1200, 630), (18, 20, 28))
    canvas.paste(og, ((1200 - og.width) // 2, (630 - og.height) // 2)); canvas.save(OUT / "og-image.jpg", quality=86)

    data = {"site": SITE, "stones": STONES, "types": TYPES, "products": PRODUCTS}
    (OUT / "data.js").write_text("window.DAVIAS = " + json.dumps(data) + ";\n", encoding="utf-8")

    # ---------- Home ----------
    featured = [p for p in PRODUCTS if p["slug"] in
                ("earthbound-gold", "watch-stone", "jade-balance", "midnight-jade", "clear-intent", "jade-garden")]
    collections = "".join(
        f'<a class="card piece" href="shop.html#{t}"><div class="strand" data-strand="{s}" style="height:64px"></div>'
        f'<h3>{e(TYPES[t][0])}</h3><p>{e(TYPES[t][1])}</p></a>'
        for t, s in [("bracelet", "tiger,quartz"), ("earrings", "pjade,selenite"),
                     ("necklace", "gjade,quartz"), ("anklet", "selenite,gjade")]
    )
    page("index.html", "Home", f"""
<header class="hero" id="top">
  <div class="wrap">
    <div class="copy">
      <span class="eyebrow">Davias Earthbound Jewelry</span>
      <h1>Real stones, real science, <em>made by hand</em> with love.</h1>
      <p class="lede">Natural crystal bracelets, earrings, necklaces and anklets. Every piece comes with the honest story of its stone: what science shows, what tradition says, and which is which.</p>
      <div class="ctas">
        <a class="btn solid" href="shop.html">Shop the collection</a>
        <a class="btn ghost" href="drop.html">Monthly drop: coming soon</a>
      </div>
      <div class="facts">
        <div><b>100%</b>natural stone beads</div>
        <div><b>Mohs 2–7</b>every hardness, explained</div>
        <div><b>0</b>medical claims, ever</div>
      </div>
    </div>
    <div class="orbit" aria-hidden="true">
      <canvas id="orbit"></canvas>
      <div class="logo"><img src="davias-logo.webp" alt=""></div>
    </div>
  </div>
</header>
<section>
  <div class="wrap">
    <div class="head"><span class="eyebrow">The collection</span><h2>Wear the <span class="name">Earth</span>, every day.</h2>
      <p class="lede">Four ways to wear it, with new lines added as the family of stones grows.</p></div>
    <div class="grid">{collections}</div>
    <div class="themes"><span class="eyebrow">Themed lines · coming soon</span>
      <div class="chips">{"".join(f'<span class="chip">{e(t)}</span>' for t in THEMES)}</div></div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="head"><span class="eyebrow">Signature pieces</span><h2>Made in small batches.</h2></div>
    <div class="grid">{"".join(piece_card(p) for p in featured)}</div>
    <p style="margin-top:28px"><a class="btn ghost" href="shop.html">See every piece</a></p>
  </div>
</section>
<section class="science">
  <div class="wrap">
    <div><h3>The real "energy" fact</h3><p>Quartz is piezoelectric: squeeze it and it makes a tiny electric charge. That is why quartz keeps time in watches. Tiger's eye, clear and yellow quartz are all quartz.</p></div>
    <div><h3>An honest word on "conductive"</h3><p>Most gemstones are electrical insulators, not conductors like copper wire. We'd rather tell you the true thing, which is more interesting anyway.</p></div>
    <div><h3>Hardness you can feel</h3><p>Selenite is Mohs 2, soft enough to scratch with a fingernail. Quartz is Mohs 7, harder than a steel knife. That's why care changes from stone to stone.</p></div>
  </div>
</section>
<section>
  <div class="wrap two">
    <div class="head" style="margin:0"><span class="eyebrow">Crystal finder</span><h2>Not sure where to start?</h2>
      <p class="lede">Pick the colors you love and the traditions that speak to you. We'll suggest a combination, with the facts and the traditions labeled.</p>
      <p><a class="btn solid" href="finder.html">Find my stones</a></p></div>
    <div class="head" style="margin:0"><span class="eyebrow">Monthly drop</span><h2>{e(DROP["name"])}</h2>
      <div class="strand" data-strand="{",".join(DROP["stones"])}" data-n="15" style="height:70px"></div>
      <p class="lede">Only {DROP["size"]} made, open for {DROP["hours"]} hours. Then the design retires.</p>
      <p><a class="btn ghost" href="drop.html">About the drop</a></p></div>
  </div>
</section>
""", desc="Handmade natural crystal jewelry by David & Octavia. Real stones, real science, tradition clearly labeled.",
         current="index.html")

    # ---------- Shop ----------
    type_btns = "".join(f'<button data-filter="{t}" aria-pressed="false">{e(v[0])}</button>' for t, v in TYPES.items())
    helix_btns = "".join(f'<button data-filter="helix-{k.lower()}" aria-pressed="false">{e(v)}</button>' for k, v in HELIX.items())
    stone_btns = "".join(f'<button data-filter="{k}" aria-pressed="false">{e(s["name"])}</button>' for k, s in STONES.items())
    page("shop.html", "Shop", head("Shop", "Every piece, made by hand.",
         "Tap a piece for its stones, the science, and how it's made. Add it to your order bag and send it to us.") + f"""
<section style="border:0;padding-top:0"><div class="wrap">
  <div class="filters" role="group" aria-label="Filter pieces">
    <button data-filter="all" aria-pressed="true">All</button>{helix_btns}{type_btns}{stone_btns}
  </div>
  <div class="grid" id="products">{"".join(piece_card(p) for p in PRODUCTS)}</div>
  <div class="themes" style="margin-top:48px"><span class="eyebrow">Coming soon</span>
    <div class="chips">{"".join(f'<span class="chip soon">{e(t)}</span>' for t in THEMES)}</div>
    <p class="note">Want one of these now? <a href="order.html">Ask us</a>.</p></div>
</div></section>
""", desc="Shop handmade natural crystal bracelets, earrings, necklaces and anklets.", current="shop.html")

    # ---------- Product pages ----------
    for p in PRODUCTS:
        sizes = {
            "bracelet": ["6 in (15 cm)", "6.5 in (16.5 cm)", "7 in (18 cm)", "7.5 in (19 cm)", "8 in (20 cm)", "Custom: I'll send my size"],
            "anklet": ["Adjustable (sliding knot)"],
            "necklace": ["16 in (41 cm)", "18 in (46 cm)", "20 in (51 cm)", "Custom: I'll send my length"],
            "earrings": ["One size"],
        }[p["type"]]
        stone_blocks = "".join(
            f'<div class="label proven"><h4>{e(STONES[k]["name"])} · Proven</h4><p>{e(STONES[k]["proven"])}</p></div>'
            f'<div class="label trad"><h4>{e(STONES[k]["name"])} · Traditional</h4><p>{e(STONES[k]["trad"])}</p></div>'
            for k in p["stones"])
        care = care_text(p["stones"])
        hardest = min(STONES[k]["mohs"] for k in p["stones"])
        price = f"${p['price']}" if p["price"] else "Ask for price"
        related = [q for q in PRODUCTS if q is not p and set(q["stones"]) & set(p["stones"])][:3]
        page(f"p/{p['slug']}.html", p["name"], f"""
<div class="wrap product">
  <div class="photo"><div class="strand" data-strand="{",".join(p["stones"])}" data-n="11" style="width:84%;height:120px"></div><small>Photo coming soon</small></div>
  <div class="info">
    <p class="crumbs"><a href="../shop.html">Shop</a> / <a href="../shop.html#{p['type']}">{e(TYPES[p['type']][0])}</a></p>
    <span class="tag">{e(stone_names(p["stones"]))}</span>
    <h1>{e(p["name"])}</h1>
    <p class="lede">{e(p["story"])}</p>
    <dl class="spec">
      <div><dt>Price</dt><dd>{price}</dd></div>
      <div><dt>Stones</dt><dd>{e(stone_names(p["stones"]))}</dd></div>
      <div><dt>Made with</dt><dd>{e(FINISH[p["type"]])}</dd></div>
      <div><dt>Softest stone</dt><dd>Mohs {hardest}</dd></div>
      {f'<div><dt>Construction</dt><dd>{e(HELIX[p["helix"]])}</dd></div>' if p.get("helix") else ""}
      {f'<div><dt>Complements</dt><dd>{e(p["matching"])}</dd></div>' if p.get("matching") else ""}
    </dl>
    <div class="field"><label for="size">Size</label>
      <select id="size">{"".join(f"<option>{e(s)}</option>" for s in sizes)}</select></div>
    <div style="display:flex;gap:12px;flex-wrap:wrap">
      <button class="btn solid" id="add-to-bag" data-slug="{p['slug']}">Add to order bag</button>
      <a class="btn ghost" href="../order.html">Go to order bag</a>
    </div>
    <p class="added" id="added" role="status"></p>
  </div>
</div>
<section><div class="wrap">
  <div class="head"><span class="eyebrow">The honest story</span><h2>What's proven, and what's tradition.</h2></div>
  <div class="labels on-page">{stone_blocks}
    <div class="label care"><h4>Care</h4><p>{e(care)}</p></div></div>
  <p class="note" style="margin-top:18px">More in the <a href="../stones.html#{p['stones'][0]}">Stone Guide</a>.</p>
</div></section>
{f'<section><div class="wrap"><div class="head"><span class="eyebrow">You may also like</span></div><div class="grid">{"".join(piece_card(q, "../") for q in related)}</div></div></section>' if related else ""}
""", desc=f"{p['name']}: handmade {stone_names(p['stones'])} {p['type']}. {p['story']}", root="../")

    # ---------- Stone guide ----------
    page("stones.html", "Stone Guide", head("Stone guide", "Every stone, honestly labeled.",
         'Each claim gets one label. <b style="color:var(--gold);font-weight:500">Proven</b> means checkable science. '
         '<b style="color:var(--lilac);font-weight:500">Traditional</b> means belief and history, shared as tradition. '
         "Then how to care for it, and what we will never claim.") + """
<section style="border:0;padding-top:0"><div class="wrap">
  <div class="stones">
    <div class="stone-list" role="tablist" aria-label="Stones" id="stone-list"></div>
    <div class="stone-detail" id="stone-detail" role="tabpanel"></div>
  </div>
</div></section>
<section class="science"><div class="wrap">
  <div><h3>Proven</h3><p>Real, checkable science: what the mineral is made of, how hard it is, and properties like quartz's piezoelectricity.</p></div>
  <div><h3>Traditional</h3><p>Centuries of use and belief. We share these because they're part of the stones' story, always labeled as tradition.</p></div>
  <div><h3>Open</h3><p>What a stone feels like to us, labeled as our experience. Never presented as a fact about you.</p></div>
</div></section>
""", desc="The Davias stone guide: real mineralogy, traditions clearly labeled, care, and what we never claim.",
         current="stones.html")

    # ---------- Drop ----------
    page("drop.html", "Monthly Drop", head("Monthly limited drop: coming soon", "One design a month, made in a small run. The first date is not set yet.",
         f"The plan: each drop is a small run, about {DROP['size']} pieces, open for a short window, and then the design retires. "
         "Join the list and you hear the date first.") + f"""
<section class="drop" style="border:0;padding-top:0"><div class="wrap">
  <div class="panel">
    <span class="tag">Planned first design</span>
    <h3>{e(DROP["name"])}</h3>
    <div class="strand" data-strand="{",".join(DROP["stones"])}" data-n="15" style="height:70px"></div>
    <p class="lede" style="font-size:16px">{e(DROP["text"])}</p>
    <div class="count" aria-label="Drop size and window">
      <div><b>{DROP["size"]}</b><small>pieces</small></div>
      <div><b>{DROP["hours"]}</b><small>hours</small></div>
      <div><b>1</b><small>run only</small></div>
    </div>
    <p class="note">No date or checkout yet. The opening date goes to the drop list first, then to Instagram and TikTok.</p>
  </div>
  <div class="head" style="margin:0">
    <h3>Be first in line</h3>
    <p class="lede">The list hears about each drop before anyone else.</p>
    <form class="join" id="join">
      <label for="join-email" class="note" style="flex-basis:100%">Your email</label>
      <input id="join-email" type="email" placeholder="you@example.com" required>
      <button class="btn solid" type="submit">Join the drop list</button>
    </form>
    <p class="note" id="join-msg" role="status"></p>
    <h3 style="margin-top:24px">How a drop works</h3>
    <ul class="prose" style="padding-left:18px">
      <li>We say exactly how many were made. Every time.</li>
      <li>The window is planned at {DROP["hours"]} hours, or until the run is gone.</li>
      <li>Each piece still comes with its honest stone story.</li>
      <li>Founders Drops are numbered, 1 to 100.</li>
    </ul>
  </div>
</div></section>
""", desc="The Davias monthly limited drop: one design, a small run, a short window.", current="drop.html")

    # ---------- Finder + FAQ ----------
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in FAQ)
    page("finder.html", "Crystal Finder", head("Crystal finder", "Find the stones that fit you.",
         "Pick what you're drawn to. You'll get a combination, with the real facts and the traditions clearly labeled.") + f"""
<section style="border:0;padding-top:0"><div class="wrap">
  <div class="finder">
    <form id="finder-form">
      <fieldset><legend>Which colors do you love?</legend><div class="opts" id="opt-color"></div></fieldset>
      <fieldset><legend>What tradition speaks to you?</legend><div class="opts" id="opt-feel"></div></fieldset>
      <fieldset><legend>How will you wear it?</legend><div class="opts" id="opt-wear"></div></fieldset>
    </form>
    <div class="result" id="finder-result" aria-live="polite"></div>
  </div>
</div></section>
<section><div class="wrap">
  <div class="head"><span class="eyebrow">Questions</span><h2>Straight answers.</h2></div>
  <div class="faq">{faq}</div>
  <p class="note" style="margin-top:20px">Another question? Ask us: {e(SITE["email"])} or DM <a href="{SITE['instagram']}">@DaviasJewelry</a>.</p>
</div></section>
""", desc="Find your crystal combination, with real science and traditions clearly labeled.", current="finder.html")

    # ---------- About ----------
    page("about.html", "Our Story", f"""
<section class="story" style="border:0"><div class="wrap">
  <img src="davias-logo.webp" alt="The Davias logo: a beaded bracelet circling the Earth, with golden threads from each bead to the planet">
  <div class="head" style="margin:0">
    <span class="eyebrow">Our story</span>
    <h1 style="font-size:clamp(40px,5vw,64px)"><span class="name">Davia</span> is David + Octavia.</h1>
    <p class="lede">Two people, bound to the Earth by the stones. We started Davias to bridge the gap between crystals and science: to show what's real, label what's tradition, and make something beautiful by hand either way.</p>
    <div class="people">
      <div><b>Octavia</b><p>The eye behind the color combinations.</p></div>
      <div><b>David</b><p>Runs the shop, the science, the stories, and everything in between.</p></div>
    </div>
  </div>
</div></section>
<section><div class="wrap two">
  <div class="prose"><span class="eyebrow">Our promise</span>
    <h3>Science first</h3><p>Every claim gets a label: Proven, Traditional, or Open. If we can't source it, we don't say it.</p>
    <h3>No medical claims, ever</h3><p>Crystals are beautiful natural minerals. They're jewelry, not medicine.</p>
    <h3>Honest names</h3><p>If a stone is often sold under another name, we tell you.</p></div>
  <div class="prose"><span class="eyebrow">How it's made</span>
    <h3>Built to last</h3><p>Bracelets and necklaces are strung on nylon-coated stainless beading wire with solid metal clasps, not the cheap stretch cord most crystal jewelry uses.</p>
    <h3>Beach and casual pieces</h3><p>Waxed cord with a sliding knot: adjustable and water-resistant.</p>
    </div>
</div></section>
""", desc="Davias is David + Octavia: handmade crystal jewelry, science first.", current="about.html")

    # ---------- Order ----------
    page("order.html", "Order", head("Order bag", "Message us. We'll make it yours.",
         "Add pieces from the shop, then send us your order by DM or email. We confirm the stones, your size, the price and shipping before anything is paid.") + f"""
<section style="border:0;padding-top:0"><div class="wrap two">
  <div>
    <div id="bag-list"></div>
    <div class="field" style="margin-top:22px"><label for="order-name">Your name</label><input id="order-name" autocomplete="name"></div>
    <div class="field" style="margin-top:14px"><label for="order-note">Anything else? (wrist size, a custom idea, a gift note)</label><input id="order-note"></div>
  </div>
  <div class="field">
    <label for="order-message">Your order message</label>
    <textarea id="order-message" readonly></textarea>
    <div style="display:flex;gap:12px;flex-wrap:wrap">
      <button class="btn solid" id="copy-order" type="button">Copy message</button>
      <a class="btn ghost" id="order-email" href="mailto:{SITE['email']}">Email it to us</a>
      <a class="btn ghost" href="{SITE['instagram']}">DM on Instagram</a>
    </div>
    <p class="note" id="copy-status" role="status"></p>
    <p class="note">Email: {e(SITE["email"])} · Phone/text: {e(SITE["phone"])}</p>
  </div>
</div></section>
""", desc="Order handmade crystal jewelry from Davias by message.", current=None)

    # ---------- 404, robots, sitemap ----------
    page("404.html", "Not found", head("Lost?", "That page isn't here.",
         '<a href="index.html">Go home</a> or <a href="shop.html">visit the shop</a>.'), desc="Page not found.")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE['domain']}/sitemap.xml\n")
    urls = ["", "shop.html", "drop.html", "stones.html", "finder.html", "about.html", "order.html"] + \
           [f"p/{p['slug']}.html" for p in PRODUCTS]
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"  <url><loc>{SITE['domain']}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    (OUT / ".htaccess").write_text("ErrorDocument 404 /404.html\n")
    print(f"Built {len(list(OUT.rglob('*')))} files into {OUT}")


if __name__ == "__main__":
    build()
