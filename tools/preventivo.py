# -*- coding: utf-8 -*-
"""
Compila un preventivo (PDF) nello stile del sito, a partire da un solo file di dati.

Uso (dalla cartella del progetto):
    python tools/preventivo.py clienti/<nome-cliente>/preventivo.json

Cosa fa
- legge il file dei dati del cliente (modello: modelli/esempio-preventivo.json) e i dati dello Studio (modelli/dati-studio.json);
- se il numero non c'e', assegna il successivo (anno-numero, es. 2026-001) e lo scrive nel file, cosi' una seconda esecuzione da' lo stesso numero;
- calcola totale, acconto (50%), saldo (50%), IVA se indicata;
- le voci non usate (sconto, opzioni, cura continua, IVA) spariscono;
- i campi vuoti restano evidenziati in giallo, per accorgersene;
- scrive HTML e PDF nella cartella del file, con Chrome.

Lingue: "it" (predefinita) o "en", dal campo "lingua".
Dettagli e campi in docs/STRUMENTO-PREVENTIVI.md.
"""
import io, json, os, re, subprocess, sys, tempfile, datetime
from html import escape

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
MODELLI = os.path.join(ROOT, "modelli")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# ---------------------------------------------------------------- testi
T = {
  "it": {
    "lang": "it", "eyebrow": "Proposta di lavoro", "titolo": "Preventivo", "n": "n.", "data": "Data", "valido": "Valido per", "giorni": "giorni",
    "per": "Per", "referente": "Referente", "piva_cf": "P. IVA o C.F.",
    "capito": "Cosa abbiamo capito", "realizza": "Cosa si realizza", "non_incluso": "Non incluso:",
    "costa": "Quanto costa", "voce": "Voce", "importo": "Importo", "sconto": "Sconto", "imponibile": "Imponibile", "iva": "IVA", "totale": "Totale",
    "iva_se_dovuta": "IVA se dovuta", "iva_esclusa": "IVA esclusa",
    "opzioni": "Opzioni, non comprese nel totale", "opz_nota": "Si decidono ora o dopo: il prezzo resta quello scritto qui.",
    "chiuso": "Prezzo chiuso:", "chiuso_t": "non cambia in corsa. Se durante il lavoro serve qualcosa in più, viene segnalato subito e scritto prima di procedere.",
    "hosting": "Dominio e hosting (circa {h} euro l'anno) sono a parte, intestati al cliente e pagati con il suo metodo di pagamento.",
    "quando": "Quando",
    "quando_t": "Consegna in <b>{g} giorni</b> dal momento in cui arriva tutto il materiale (testi, foto, accessi).{date} Sono compresi <b>{c} giri di correzioni</b>. Il massimo focus su ogni lavoro è garantito, per rispettare i tempi; un ritardo nel consegnare il materiale sposta la data di pari durata.",
    "inizio": "Inizio", "consegna_prev": "consegna prevista",
    "serve": "Cosa serve per cominciare", "riferimento": "Una persona di riferimento che risponda entro 2-3 giorni lavorativi",
    "dopo": "Dopo la consegna",
    "cura_t": "<b>Cura continua</b>, facoltativa. Il primo mese è un <b>rodaggio</b> a forfait di <b>{f}</b> euro, senza limite di ore, per assistenza, ricerca e idee (esclusi i nuovi sviluppi). A fine mese un resoconto con le ore reali stabilisce, insieme, il livello: <b>canone Base {c}</b> euro al mese con <b>{o}</b> ore incluse; oltre, <b>50 euro l'ora</b>, a blocchi di 30 minuti, sempre comunicate prima. Il rodaggio è senza vincolo. Vedi Accordo di servizio, articolo 4.",
    "paga": "Come si paga",
    "acconto": "Acconto del 50% alla firma", "saldo": "Saldo del 50% alla consegna",
    "bonifico": "Bonifico a {iban}, intestato a Matia Zoffoli, entro {g} giorni dalla fattura.",
    "resta": "Cosa resta al cliente",
    "resta_t": "Dominio, contenuti, dati e accessi restano sempre al cliente, con una licenza d'uso perpetua sul lavoro consegnato. Alla fine del rapporto tutto viene consegnato entro {g} giorni.",
    "accetta": "Accettazione",
    "accetta_t": "Per accettare basta rispondere «Accetto» a questa email, oppure firmare qui sotto. L'<b>Accordo di servizio</b> allegato vale per questo lavoro e per quelli futuri.",
    "per_cliente": "Per il cliente", "data_min": "data",
    "piede": "Studio Matiz · Preventivo n. {n}", "pagina": "Pagina", "di": "di", "bozza": "Bozza da far controllare", "euro": "euro", "mese": "al mese",
    "studio_sede": "Cesenatico", "studio_di": "di Matia Zoffoli", "p_iva": "P. IVA", "per_riga": "per", "preventivo": "Preventivo",
    "mesi": ["gennaio","febbraio","marzo","aprile","maggio","giugno","luglio","agosto","settembre","ottobre","novembre","dicembre"],
  },
  "en": {
    "lang": "en", "eyebrow": "Work proposal", "titolo": "Quote", "n": "no.", "data": "Date", "valido": "Valid for", "giorni": "days",
    "per": "For", "referente": "Contact person", "piva_cf": "VAT or tax no.",
    "capito": "What we understood", "realizza": "What will be built", "non_incluso": "Not included:",
    "costa": "What it costs", "voce": "Item", "importo": "Amount", "sconto": "Discount", "imponibile": "Subtotal", "iva": "VAT", "totale": "Total",
    "iva_se_dovuta": "VAT if due", "iva_esclusa": "excl. VAT",
    "opzioni": "Options, not included in the total", "opz_nota": "They can be decided now or later: the price stays as written here.",
    "chiuso": "Fixed price:", "chiuso_t": "it does not change along the way. If something extra is needed during the work, it is flagged straight away and written down before going ahead.",
    "hosting": "Domain and hosting (about {h} euro a year) are separate, registered in the client's name and paid with the client's own payment method.",
    "quando": "When",
    "quando_t": "Delivery within <b>{g} days</b> of the moment all the material arrives (texts, photos, access).{date} <b>{c} rounds of revisions</b> are included. Every job gets full attention, to keep to the schedule; a delay in providing the material moves the date by the same amount.",
    "inizio": "Start", "consegna_prev": "expected delivery",
    "serve": "What is needed to start", "riferimento": "A contact person who replies within 2-3 working days",
    "dopo": "After delivery",
    "cura_t": "<b>Ongoing care</b>, optional. The first month is a <b>settling-in month</b> at a flat fee of <b>{f}</b> euro, with no cap on hours, for support, research and ideas (new developments excluded). At the end of the month a report with the real hours sets the level together: <b>Base fee {c}</b> euro a month with <b>{o}</b> hours included; beyond that, <b>50 euro an hour</b>, in blocks of 30 minutes, always communicated beforehand. The settling-in month carries no commitment. See Service agreement, article 4.",
    "paga": "How to pay",
    "acconto": "Deposit of 50% on signing", "saldo": "Balance of 50% on delivery",
    "bonifico": "Bank transfer to {iban}, in the name of Matia Zoffoli, within {g} days of the invoice.",
    "resta": "What stays with the client",
    "resta_t": "Domain, content, data and access always stay with the client, with a perpetual licence to use the delivered work. At the end of the relationship everything is handed over within {g} days.",
    "accetta": "Acceptance",
    "accetta_t": "To accept, reply \"I accept\" to this email, or sign below. The attached <b>Service agreement</b> applies to this job and to future ones.",
    "per_cliente": "For the client", "data_min": "date",
    "piede": "Studio Matiz · Quote no. {n}", "pagina": "Page", "di": "of", "bozza": "Draft to be reviewed", "euro": "euro", "mese": "a month",
    "studio_sede": "Cesenatico, Italy", "studio_di": "by Matia Zoffoli", "p_iva": "VAT no.", "per_riga": "for", "preventivo": "Quote",
    "mesi": ["January","February","March","April","May","June","July","August","September","October","November","December"],
  },
}

LINGUA = ["it"]
PH_EN = {"indirizzo": "address", "partita IVA": "VAT number", "numero": "number", "data": "date", "nome": "name", "nome del cliente": "client name",
         "nome e ruolo": "name and role", "email": "email", "telefono": "phone", "anno-numero": "year-number", "IBAN": "IBAN",
         "lavoro e cosa si consegna": "job and what is delivered"}

def f(testo, vuoto=""):
    """Campo da completare: evidenziato se vuoto."""
    if LINGUA[0] == "en": vuoto = PH_EN.get(vuoto, vuoto)
    testo = (testo or "").strip() if isinstance(testo, str) else testo
    if testo in (None, "", []):
        return '<span class="f">%s</span>' % escape(vuoto or "da completare")
    return escape(str(testo))

def somma_fmt(n, lang):
    n = round(float(n), 2)
    s = ("%.2f" % n) if n != int(n) else str(int(n))
    intero, _, dec = s.partition(".")
    sep = "." if lang == "it" else ","
    intero = re.sub(r"\B(?=(\d{3})+(?!\d))", sep, intero)
    out = intero + (("," if lang == "it" else ".") + dec if dec else "")
    return out + " €" if lang == "it" else "€" + out

def data_fmt(d, t):
    if not d: return ""
    y, m, g = (int(x) for x in d.split("-"))
    return "%d %s %d" % (g, t["mesi"][m - 1], y)

def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "cliente"

def prossimo_numero(anno):
    reg = os.path.join(ROOT, "clienti", "_registro.json")
    os.makedirs(os.path.dirname(reg), exist_ok=True)
    d = json.load(io.open(reg, encoding="utf-8")) if os.path.exists(reg) else {}
    d[str(anno)] = d.get(str(anno), 0) + 1
    json.dump(d, io.open(reg, "w", encoding="utf-8"), indent=1)
    return "%d-%03d" % (anno, d[str(anno)])

def costruisci(d, studio):
    lang = d.get("lingua", "it"); t = T[lang]; LINGUA[0] = lang
    oggi = datetime.date.today()
    data = d.get("data") or oggi.isoformat()
    numero = d.get("numero") or ""
    avvisi = []

    lavori = d.get("lavori") or []
    totale_lavori = sum(float(l.get("importo", 0)) for l in lavori)
    sconto = d.get("sconto") or None
    sc = float(sconto["importo"]) if sconto else 0
    imponibile = totale_lavori - sc
    aliquota = d.get("iva_aliquota")
    iva = round(imponibile * float(aliquota) / 100, 2) if aliquota not in (None, "", 0) else 0
    totale = imponibile + iva
    acconto = round(totale / 2)
    saldo = totale - acconto

    m = lambda n: somma_fmt(n, lang)
    cl = d.get("cliente") or {}; rf = d.get("referente") or {}
    bozza = studio.get("bozza", True)

    # ---- intestazione
    meta = '<b>Studio Matiz</b>, %s<br>%s<br>%s<br>%s %s<br>%s · %s' % (
        t["studio_di"], t["studio_sede"], f(studio.get("indirizzo"), "indirizzo"), t["p_iva"], f(studio.get("partita_iva"), "partita IVA"),
        escape(studio.get("email", "matiazoffoli@gmail.com")), escape(studio.get("telefono", "+39 333 958 0381")))
    logo = '<img src="%s" alt="Studio Matiz" style="height:14mm;width:auto">' % escape(studio["logo"]) if studio.get("logo") else '<span class="logo-ph">Logo</span>'

    righe_lavori = "".join(
        "<li><b>%s</b>%s</li>" % (escape(l["titolo"]),
          ("<ul>" + "".join("<li>%s</li>" % escape(x) for x in l.get("include", [])) + "</ul>") if l.get("include") else "")
        for l in lavori)
    if not lavori: righe_lavori = "<li>%s</li>" % f("", "lavoro e cosa si consegna")
    non_incl = d.get("non_incluso")
    non_incl_html = ('<p style="margin-top:2mm"><b>%s</b> %s</p>' % (t["non_incluso"], escape(non_incl if isinstance(non_incl, str) else "; ".join(non_incl)))) if non_incl else ""

    tab = "".join("<tr><td>%s</td><td>%s</td></tr>" % (escape(l["titolo"]), m(l.get("importo", 0))) for l in lavori)
    if sconto:
        tab += "<tr><td>%s <span class=\"nota\">%s</span></td><td>- %s</td></tr>" % (escape(sconto.get("etichetta", t["sconto"])), "", m(sc))
    if aliquota not in (None, "", 0):
        tab += '<tr><td>%s</td><td>%s</td></tr><tr><td>%s %s%%</td><td>%s</td></tr>' % (t["imponibile"], m(imponibile), t["iva"], escape(str(aliquota)), m(iva))
        etichetta_tot = t["totale"]
    else:
        etichetta_tot = '%s <span class="nota">(%s)</span>' % (t["totale"], t["iva_se_dovuta"])
    tab += '<tr class="tot"><td>%s</td><td>%s</td></tr>' % (etichetta_tot, m(totale))

    opz = d.get("opzioni") or []
    opz_html = ""
    if opz:
        opz_html = '<h3 style="margin:4mm 0 1mm">%s</h3><table>%s</table><p class="nota">%s</p>' % (
            t["opzioni"],
            "".join("<tr><td><b>%s</b>%s</td><td>%s</td></tr>" % (escape(o["titolo"]),
                    ("<br><span class=\"nota\">%s</span>" % escape(o["descrizione"])) if o.get("descrizione") else "", escape(o["importo"]) if isinstance(o.get("importo"), str) else m(o.get("importo", 0))) for o in opz),
            t["opz_nota"])

    hosting = d.get("hosting", "50-120")
    t_d = d.get("tempi") or {}
    date_txt = ""
    if t_d.get("inizio") or t_d.get("consegna"):
        date_txt = " %s %s, %s %s." % (t["inizio"], f(data_fmt(t_d.get("inizio"), t), "data"), t["consegna_prev"], f(data_fmt(t_d.get("consegna"), t), "data"))
    giorni_html = f(t_d.get("giorni"), "numero")
    if t_d.get("testo"):
        quando = "<p>%s</p>" % escape(t_d["testo"])
    else:
        quando = "<p>" + t["quando_t"].format(g=giorni_html if "<span" in giorni_html else escape(str(t_d.get("giorni"))), c=escape(str(t_d.get("correzioni", 2))), date=date_txt) + "</p>"
    tempi_lav = [l for l in lavori if l.get("tempi")]
    if tempi_lav:
        quando += "<ul>" + "".join("<li><b>%s:</b> %s</li>" % (escape(l["titolo"]), escape(l["tempi"])) for l in tempi_lav) + "</ul>"

    serve = d.get("serve") or []
    serve_html = "".join("<li>%s</li>" % escape(x) for x in serve) + "<li>%s</li>" % t["riferimento"]

    cura = d.get("cura")
    iban = f(studio.get("iban"), "IBAN")
    gfatt = escape(str(d.get("giorni_fattura", 10)))
    paga = "<li>%s: <b>%s</b></li><li>%s: <b>%s</b></li><li>%s</li>" % (t["acconto"], m(acconto), t["saldo"], m(saldo), t["bonifico"].format(iban=iban, g=gfatt))

    # numerazione sezioni
    sez = []
    def S(h, body): sez.append((h, body))
    S(t["capito"], "<p>%s</p>" % f(d.get("capito"), "due o tre frasi su quanto emerso nel primo incontro" if lang == "it" else "two or three sentences from the first meeting"))
    S(t["realizza"], "<ul>%s</ul>%s" % (righe_lavori, non_incl_html))
    S(t["costa"], "<table><tr><th>%s</th><th>%s</th></tr>%s</table><p class=\"nota\"><b>%s</b> %s %s</p>%s" % (
        t["voce"], t["importo"], tab, t["chiuso"], t["chiuso_t"], t["hosting"].format(h=escape(str(hosting))), opz_html))
    S(t["quando"], quando)
    S(t["serve"], "<ul>%s</ul>" % serve_html)
    if cura: S(t["dopo"], "<p>%s</p>" % t["cura_t"].format(f=escape(str(cura.get("forfait", 250))), c=escape(str(cura.get("canone", "100-150"))), o=escape(str(cura.get("ore_incluse", 2)))))
    S(t["paga"], "<ul>%s</ul>" % paga)
    S(t["resta"], "<p>%s</p>" % t["resta_t"].format(g=escape(str(d.get("giorni_consegna_dati", 10)))))
    S(t["accetta"], "<p>%s</p><div class=\"firme\"><div>%s, %s · %s</div><div>Matia Zoffoli · %s</div></div>" % (
        t["accetta_t"], t["per_cliente"], f(cl.get("nome") and (rf.get("nome") or cl.get("nome")), "nome"), t["data_min"], t["data_min"]))
    blocchi = "".join('<div class="sez%s"><span class="n">%02d</span><div><h2>%s</h2>%s</div></div>' % (" ultima" if i == len(sez) - 1 else "", i + 1, h, b) for i, (h, b) in enumerate(sez))

    piede_testo = t["piede"].format(n=escape(numero)) + (' · <span class="bozza">%s</span>' % t["bozza"] if bozza else "")
    html = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{titolo} {numero} - Studio Matiz</title>
<link rel="stylesheet" href="{css}">
<style>
  @page {{ size: A4; margin: 16mm 18mm 20mm; @bottom-left {{ content: "{pl}"; font: 300 7pt Manrope, sans-serif; color: #6B6057; }} @bottom-right {{ content: "{pag} " counter(page) " {di} " counter(pages); font: 300 7pt Manrope, sans-serif; color: #6B6057; }} }}
  @page :first {{ margin-top: 12mm; }}
  body {{ background: none; font-size: 9.2pt; line-height: 1.5; }}
  .doc {{ width: auto; margin: 0; padding: 0; }}
  .sez ul ul {{ margin: .6mm 0 1.2mm; }}
  .sez {{ break-inside: auto; margin-bottom: 3.8mm; }}
  .sez h2 {{ break-after: avoid; }}
  .sez p, .sez li {{ orphans: 2; widows: 2; }}
  table {{ break-inside: avoid; }}
  tr {{ break-inside: avoid; }}
  .sez.ultima, .firme {{ break-inside: avoid; }}
</style>
</head>
<body>
<div class="doc">
  <header class="top">
    {logo}
    <div class="meta">{meta}</div>
  </header>

  <div class="titolo">
    <div><span class="eyebrow">{eyebrow}</span><h1 style="margin-top:3mm">{titolo} <em>{n} {numero_f}</em></h1></div>
    <div class="num">{data_l} <b>{data_v}</b><br>{valido} <b>{val} {giorni}</b></div>
  </div>

  <div class="due">
    <div><span class="eyebrow">{per}</span><b>{cliente_nome}</b><br>{cliente_ind}<br>{piva_cf} {cliente_piva}</div>
    <div><span class="eyebrow">{referente}</span>{ref_nome}<br>{ref_email} · {ref_tel}</div>
  </div>

  {blocchi}
</div>
</body>
</html>""".format(
        lang=lang, titolo=t["titolo"], numero=escape(numero), css="modelli.css" if False else "file:///" + os.path.join(MODELLI, "modelli.css").replace("\\", "/"),
        pl=re.sub(r"<[^>]+>", "", t["piede"].format(n=numero)).replace('"', "") + (" · " + t["bozza"] if bozza else ""), pag=t["pagina"], di=t["di"],
        logo=logo, meta=meta, eyebrow=t["eyebrow"], n=t["n"], numero_f=f(numero, "anno-numero"),
        data_l=t["data"], data_v=escape(data_fmt(data, t)), valido=t["valido"], val=escape(str(d.get("validita_giorni", 30))), giorni=t["giorni"],
        per=t["per"], cliente_nome=f(cl.get("nome"), "nome del cliente") + ((", " + escape(cl["attivita"])) if cl.get("attivita") else ""),
        cliente_ind=f(cl.get("indirizzo"), "indirizzo"), piva_cf=t["piva_cf"], cliente_piva=f(cl.get("piva_cf"), "numero"),
        referente=t["referente"], ref_nome=f((rf.get("nome") or "") + ((", " + rf["ruolo"]) if rf.get("ruolo") else ""), "nome e ruolo"),
        ref_email=f(rf.get("email"), "email"), ref_tel=f(rf.get("telefono"), "telefono"), blocchi=blocchi)
    # controlli: campi lasciati vuoti
    vuoti = re.findall(r'<span class="f">(.*?)</span>', html)
    return html, vuoti, numero, totale, acconto, saldo

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    path = os.path.abspath(sys.argv[1])
    d = json.load(io.open(path, encoding="utf-8"))
    sp = os.path.join(MODELLI, "dati-studio.json")
    studio = json.load(io.open(sp, encoding="utf-8")) if os.path.exists(sp) else {}
    studio = {k: v for k, v in studio.items() if not k.startswith("_")}
    if not d.get("numero"):
        anno = int((d.get("data") or datetime.date.today().isoformat())[:4])
        d["numero"] = prossimo_numero(anno)
        json.dump(d, io.open(path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        print("Numero assegnato:", d["numero"])
    html, vuoti, numero, totale, acconto, saldo = costruisci(d, studio)
    cartella = os.path.dirname(path)
    base = os.path.join(cartella, "preventivo-%s" % numero)
    io.open(base + ".html", "w", encoding="utf-8").write(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
                    "--print-to-pdf=" + base + ".pdf", "file:///" + base.replace("\\", "/") + ".html"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("PDF:", os.path.relpath(base + ".pdf", ROOT))
    print("Totale %.2f, acconto %d, saldo %d" % (totale, acconto, saldo))
    if vuoti:
        print("\nCampi ancora da completare (evidenziati in giallo nel PDF):")
        for v in vuoti: print(" -", v)

if __name__ == "__main__":
    main()
