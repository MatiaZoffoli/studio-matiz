# -*- coding: utf-8 -*-
"""
Titoli e cifre delle email come immagini, con i caratteri veri del sito (Bodoni Moda).

Perche': Gmail e molti altri programmi di posta non caricano i caratteri web e mostrano un carattere di ripiego.
I titoli (uguali per tutti) e le cifre del prezzo (un insieme finito di valori) si disegnano quindi una volta sola, qui,
con Chrome e gli stessi caratteri del sito, e le email li usano come immagini con il testo alternativo.
Il testo corrente resta testo vero: nei programmi che caricano i caratteri web (Apple Mail, iOS, Outlook per Mac) e'
in Manrope, altrove in Helvetica o Arial.

Uso (dalla cartella del progetto):  python tools/email_type.py
Scrive prova/email/t/*.png (titoli e marchio), prova/email/p/*.png (prezzi) e supabase/functions/contatto/imgsizes.ts.
Richiede Chrome, Pillow e numpy.
"""
import io, os, subprocess, sys, tempfile, itertools, json
from urllib.request import pathname2url
from PIL import Image
import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT_T = os.path.join(ROOT, "prova", "email", "t")
OUT_P = os.path.join(ROOT, "prova", "email", "p")
SIZES = os.path.join(ROOT, "supabase", "functions", "contatto", "imgsizes.ts")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
os.makedirs(OUT_T, exist_ok=True); os.makedirs(OUT_P, exist_ok=True)

INK, GOLD, CREAM = "#241E1A", "#86672F", "#F3ECE0"

# ---- i prezzi possibili dello stimatore (stessa tabella di prova/index.html, BANDS)
SITO = {"piccola": 500, "media": 1200, "grande": 2500}
AUTO = {"piccola": 500, "media": 900, "grande": 2000}
MENU = 300
def euro(n, l):
    s = f"{n:,}".replace(",", "." if l == "it" else ",")
    return (f"{s} euro") if l == "it" else f"\u20ac{s}"
valori = set([200])  # check-up da solo: prezzo secco, senza "da"
da = set()
for size in SITO:
    for sito, menu, auto in itertools.product([0, 1], repeat=3):
        if not (sito or menu or auto): continue
        da.add(sito * SITO[size] + menu * MENU + auto * AUTO[size])
righe = []   # (nome file, html, colore)
for l in ("it", "en"):
    for n in sorted(da):
        testo = (f"da {euro(n, 'it')}" if l == "it" else f"from {euro(n, 'en')}")
        righe.append((f"p/{l}-{n}", testo, CREAM, 36))
    righe.append((f"p/{l}-200", euro(200, l), CREAM, 36))  # il check-up, senza prefisso
    righe.append((f"p/{l}-250", euro(250, l), CREAM, 36))  # forfait del primo mese di cura continua, senza prefisso
# ---- titoli e marchio
em = lambda a, b: f'{a} <em>{b}</em>'
righe += [
    ("t/wordmark", "Studio Matiz", CREAM, 34),
    ("t/h-conferma-it", em("La richiesta", "è arrivata"), INK, 36),
    ("t/h-conferma-en", em("Your request", "has arrived"), INK, 36),
    ("t/h-avviso", em("Nuova", "richiesta"), INK, 36),
    # etichette dei bottoni, in Manrope come sul sito (una riga con la sigla 's' nel quarto campo)
    ("t/btn-prenota-it", "Prenota il primo incontro", CREAM, 12, "s"),
    ("t/btn-prenota-en", "Book the first meeting", CREAM, 12, "s"),
    ("t/btn-rispondi", "Rispondi per email", CREAM, 12, "s"),
    ("t/btn-whatsapp", "Scrivi su WhatsApp", INK, 12, "s"),
]
righe = [r if len(r) == 5 else r + ("d",) for r in righe]

CSS = """
html,body{margin:0;background:transparent}
.r{height:150px;display:flex;align-items:center;padding:0 30px}
span{font-family:"Bodoni Moda",Georgia,serif;font-weight:500;font-optical-sizing:none;font-variation-settings:"opsz" 18;letter-spacing:-.02em;line-height:1.1;white-space:nowrap}
span.p{font-variation-settings:"opsz" 14}
span.s{font-family:Manrope,Arial,sans-serif;font-weight:600;font-variation-settings:normal;letter-spacing:.14em;text-transform:uppercase;line-height:1.1}
em{font-style:normal;color:%s}
""" % GOLD
HEAD = '<meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..700&family=Manrope:wght@600&display=swap" rel="stylesheet"><style>' + CSS + "</style>"

def render(batch, tmp):
    rows = "".join(f'<div class="r"><span class="{"s" if k == "s" else ("p" if n.startswith("p/") else "d")}" style="font-size:{px}px;color:{col}">{txt}</span></div>' for n, txt, col, px, k in batch)
    html = os.path.join(tmp, "r.html"); png = os.path.join(tmp, "r.png")
    io.open(html, "w", encoding="utf-8").write(f"<!doctype html><html><head>{HEAD}</head><body>{rows}</body></html>")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--default-background-color=00000000",
                    "--force-device-scale-factor=2", f"--window-size=1000,{150 * len(batch)}", "--virtual-time-budget=15000",
                    f"--screenshot={png}", "file:///" + html.replace("\\", "/")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return Image.open(png).convert("RGBA")

def trim(im):
    a = np.asarray(im)[:, :, 3]
    ys, xs = np.where(a > 8)
    pad = 6
    return im.crop((max(xs.min() - pad, 0), max(ys.min() - pad, 0), min(xs.max() + pad + 1, im.width), min(ys.max() + pad + 1, im.height)))

sizes = {}
with tempfile.TemporaryDirectory() as tmp:
    for i in range(0, len(righe), 10):
        batch = righe[i:i + 10]
        sheet = render(batch, tmp)
        for k, (nome, _, _, _, _) in enumerate(batch):
            row = sheet.crop((0, k * 300, sheet.width, (k + 1) * 300))   # 150 px css = 300 px a doppia risoluzione
            im = trim(row)
            im.save(os.path.join(ROOT, "prova", "email", nome + ".png"), optimize=True)
            sizes[nome.split("/")[1] if nome.startswith("p/") else nome.replace("/", "-")] = [round(im.width / 2), round(im.height / 2)]
ts = "// Generato da tools/email_type.py: dimensioni (in pixel mostrati) delle immagini dei titoli e dei prezzi.\nexport const IMG: Record<string, [number, number]> = " + json.dumps(sizes, indent=1) + ";\n"
io.open(SIZES, "w", encoding="utf-8").write(ts)
print("ok:", len(sizes), "immagini")
