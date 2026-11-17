import pathlib, re, io, base64
import segno

base = pathlib.Path(__file__).parent
index = base / "index.html"

# Front artwork: ORIGINAL logo with light purple-to-blue gradient lettering.
# The gold recolor was a mistake (user, 2026-11-10) — do not use
# davias-logo-gold-letters.jpg. Always use the untouched original.
orig = base / "media" / "davias-logo.jpg"
assert orig.exists(), "original logo file missing"
logo = "data:image/jpeg;base64," + base64.b64encode(orig.read_bytes()).decode()
gold = orig  # for the print label below

qr = segno.make("https://www.instagram.com/DaviasJewelry", error="m")
buf = io.BytesIO()
qr.save(buf, kind="png", scale=20, border=1, dark="#141414", light="#ffffff")
qr_uri = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

font_file = base / "media" / "PinyonScript-Regular.ttf"
font_uri = "data:font/ttf;base64," + base64.b64encode(font_file.read_bytes()).decode()

# Bell MT is proprietary and not available; Playfair Display Bold is the
# closest free elegant Didone serif, used for "Feel the Power".
playfair_file = base / "media" / "PlayfairDisplay-Bold.ttf"
playfair_uri = "data:font/ttf;base64," + base64.b64encode(playfair_file.read_bytes()).decode()

cinzel_file = base / "media" / "Cinzel-Bold.ttf"
assert cinzel_file.exists(), "Cinzel Bold font missing"
cinzel_uri = "data:font/ttf;base64," + base64.b64encode(cinzel_file.read_bytes()).decode()

template = (base / "template.html").read_text()
html = template.replace("__LOGO_DATA_URI__", logo).replace("__QR_DATA_URI__", qr_uri).replace("__FONT_DATA_URI__", font_uri).replace("__PLAYFAIR_DATA_URI__", playfair_uri).replace("__CINZEL_DATA_URI__", cinzel_uri)
index.write_text(html)
print("written", len(html), "qr bytes", len(buf.getvalue()), "front:", gold.name if gold.exists() else "original")
