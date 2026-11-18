# Davias website

- `src/` is the source. Edit `src/data.py` (products, prices, stones, contact, the top notice), then run:

      cd website/src && python3 build.py

- `site/` is the finished website: plain HTML, CSS and JS. Nothing to install on the server.

## Put it on Bluehost (daviasearthboundjewelry.love)

Only after the owner says go.

1. Log in to Bluehost → **Websites** → your site → **File Manager** (or cPanel → File Manager).
2. Open **public_html**. Move any old placeholder files into a backup folder.
3. Upload everything inside `website/site/` (including the `p/` folder and the hidden `.htaccess`).
   The easiest way: zip the contents of `site/`, upload the zip, then right-click → **Extract**.
4. Visit https://daviasearthboundjewelry.love and check Home, Shop, a product and the Order bag.
5. In Bluehost, turn on the free SSL certificate so the site loads on https.

## Before launch (owner decisions)

- Real product photos (replace the bead drawings).
- Prices: set `price` per product in `src/data.py` (currently "Ask for price").
- Payment method; then online checkout can be added.
- Drop opening date.
- The drop list currently opens an email to the company Gmail. A real mailing list
  (e.g. Mailchimp or Bluehost email marketing) can replace it.
