# -*- coding: utf-8 -*-
"""
Immagini delle email: banner con la scena 3D del sito e grana di carta.

Come si ricavano:
 1. Con il sito in locale, si apre in Chrome senza interfaccia l'indirizzo  .../index.html#email-banner  (mostra solo la scena 3D del hero)
    chrome --headless=new --hide-scrollbars --force-device-scale-factor=2 --window-size=2000,900 --virtual-time-budget=16000 \
           --screenshot=banner_raw.png "http://localhost:5174/index.html#email-banner"
 2. python tools/email_assets.py banner_raw.png
Scrive prova/email/banner.jpg (1200x520, mostrato a 600 px) e prova/email/grain.png (tessera di grana trasparente).
Richiede Pillow e numpy.
"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "prova", "email")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)

# ---- banner
raw = Image.open(sys.argv[1]).convert("RGB")
W, H = raw.size                      # atteso 4000 x 1800
x1 = W - 100; x0 = x1 - 2900; y0 = int(H * .134); y1 = y0 + 1256
crop = raw.crop((x0, y0, x1, y1)).resize((1200, 520), Image.LANCZOS)
a = np.asarray(crop).astype(np.float32)
# velo scuro a sinistra, dove sta il nome dello studio
xs = np.linspace(0, 1, 1200, dtype=np.float32)[None, :, None]
veil = np.clip(1 - xs / .42, 0, 1) ** 1.6
a = a * (1 - .35 * veil) + np.array([22, 18, 16], np.float32) * (.35 * veil)
# filo d'ottone sul bordo basso
a[-3:, :, :] = np.array([168, 133, 79], np.float32)
# grana fine
a += rng.normal(0, 4.2, a.shape[:2])[:, :, None]
Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(os.path.join(OUT, "banner.jpg"), quality=84, optimize=True, progressive=True)

# ---- grana di carta: tessera 128x128, grigio a opacita' bassa
n = rng.normal(0, 1, (128, 128))
alpha = np.clip(np.abs(n) * 9, 0, 22).astype(np.uint8)
shade = np.where(n > 0, 255, 70).astype(np.uint8)
tile = np.dstack([shade, shade, np.where(n > 0, 250, 60).astype(np.uint8), alpha])
Image.fromarray(tile, "RGBA").save(os.path.join(OUT, "grain.png"), optimize=True)
print("ok:", os.listdir(OUT))


