// Email dello stimatore: conferma al cliente (A1) e avviso a Matia (A2), con la grafica del sito.
// Funzioni pure: restituiscono oggetto, HTML e testo semplice. Tutto cio' che arriva dal modulo viene "escapato".
// Le email usano tabelle e stili in linea, perche' i programmi di posta non leggono i fogli di stile del sito.

export type Lingua = "it" | "en";

export type Richiesta = {
  nome: string;
  email: string;
  telefono: string | null;
  tipo: string | null;
  servizi: string[];
  presenza: string | null;
  dimensione: string | null;
  da: number | null;
  fino: number | null;
  lingua: Lingua;
  secondi: number | null;
};

export type Contesto = {
  calendario: string;
  sito: string;          // es. https://studio-matiz.vercel.app
  whatsapp: string;      // solo cifre, es. 393339580381
  emailStudio: string;
  assets?: string;       // cartella delle immagini (predefinita: sito + /email)
  logo?: string;         // indirizzo dell'immagine del logo (chiara su fondo scuro); senza, si usa il nome in carattere
};

// ---------------------------------------------------------------- colori e caratteri (gli stessi del sito)
const C = {
  sand: "#EFE8DB", card: "#FBF9F4", ink: "#241E1A", soft: "#6B6057", line: "#E2D9C8",
  gold: "#A8854F", goldText: "#735522", goldLight: "#D4B27C", night: "#161210", cream: "#F5EFE3", tint: "#F1E9DA",
};
const SERIF = "'Bodoni Moda','Bodoni 72',Didot,'Playfair Display',Georgia,'Times New Roman',serif";
const SANS = "Manrope,'Helvetica Neue',Helvetica,Arial,sans-serif";

export function esc(v: unknown): string {
  return String(v ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]!));
}

function migliaia(n: number, l: Lingua): string {
  return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, l === "en" ? "," : ".");
}

export function prezzo(da: number | null, fino: number | null, l: Lingua): string {
  if (!da) return "-";
  const uguale = fino !== null && fino === da;
  if (l === "en") return (uguale ? "" : "from ") + "€" + migliaia(da, l);
  return (uguale ? "" : "da ") + migliaia(da, l) + " euro";
}

const SERVIZI: Record<Lingua, Record<string, string>> = {
  it: { sito: "Un sito", menu: "Un menu digitale", auto: "Automatizzare una parte del lavoro", assistenza: "Assistenza continua", nonso: "Da capire: serve un check-up" },
  en: { sito: "A website", menu: "A digital menu", auto: "Automating part of the work", assistenza: "Ongoing support", nonso: "Not sure yet: a check-up is needed" },
};
const DIM: Record<Lingua, Record<string, string>> = {
  it: { piccola: "Essenziale", media: "Completo", grande: "Con funzioni" },
  en: { piccola: "Essential", media: "Complete", grande: "With features" },
};
function servizi(r: Richiesta, l: Lingua): string {
  return r.servizi.map((s, i) => {
    const t = SERVIZI[l][s] ?? s;
    return i === 0 ? t : t.charAt(0).toLowerCase() + t.slice(1);
  }).join(", ") || "-";
}

// ---------------------------------------------------------------- pezzi di grafica
function btn(url: string, label: string, pieno = true): string {
  const bg = pieno ? C.ink : "transparent";
  const col = pieno ? C.cream : C.ink;
  return `<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="display:inline-table;margin:0 10px 10px 0"><tr><td bgcolor="${pieno ? C.ink : C.card}" style="background:${bg};border:1px solid ${C.ink};border-radius:999px"><a href="${esc(url)}" style="display:inline-block;padding:13px 26px;font:600 12px/1 ${SANS};letter-spacing:.14em;text-transform:uppercase;color:${col};text-decoration:none">${esc(label)}</a></td></tr></table>`;
}

function riga(etichetta: string, valore: string): string {
  return `<tr><td style="padding:11px 0;border-bottom:1px solid ${C.line};font:600 10px/1.4 ${SANS};letter-spacing:.16em;text-transform:uppercase;color:${C.soft};width:38%;vertical-align:top">${esc(etichetta)}</td><td style="padding:11px 0;border-bottom:1px solid ${C.line};font:400 15px/1.5 ${SANS};color:${C.ink};vertical-align:top">${esc(valore)}</td></tr>`;
}

function passo(n: string, testo: string): string {
  return `<tr><td style="padding:9px 14px 9px 0;font:600 11px/1.5 ${SANS};letter-spacing:.14em;color:${C.goldText};vertical-align:top;width:34px">${n}</td><td style="padding:9px 0;font:400 15px/1.55 ${SANS};color:${C.ink}">${testo}</td></tr>`;
}

function prezzoBox(etichetta: string, valore: string, nota: string): string {
  return `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:26px 0 8px"><tr><td bgcolor="${C.tint}" style="background:${C.tint};background-image:linear-gradient(135deg,#F7F0E1 0%,#EADFC8 100%);padding:22px 26px 22px 24px;border-left:3px solid ${C.gold};box-shadow:0 22px 34px -24px rgba(36,30,26,.55)">
        <div style="font:600 10px/1.4 ${SANS};letter-spacing:.2em;text-transform:uppercase;color:${C.goldText}">${esc(etichetta)}</div>
        <div style="margin-top:6px;font:450 36px/1.1 ${SERIF};letter-spacing:-.02em;color:${C.ink}">${esc(valore)}</div>
        <div style="margin-top:10px;font:300 13px/1.6 ${SANS};color:${C.soft}">${esc(nota)}</div>
      </td></tr></table>`;
}

function filo(): string {
  return `<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:30px 0 0"><tr><td height="1" bgcolor="${C.line}" style="height:1px;line-height:1px;font-size:1px;background:${C.line};background-image:linear-gradient(90deg,${C.gold} 0%,rgba(168,133,79,0) 100%)">&nbsp;</td></tr></table>`;
}

function cornice(opts: { l: Lingua; anteprima: string; eyebrow: string; titolo: string; corpo: string; piede: string; assets: string; logo?: string }): string {
  const { l, anteprima, eyebrow, titolo, corpo, piede, assets, logo } = opts;
  const banner = `${assets}/header.jpg`;
  const marchio = logo
    ? `<img src="${esc(logo)}" width="220" alt="Studio Matiz" style="display:block;margin:0 auto;border:0;height:auto">`
    : `<div style="font:450 34px/1.1 ${SERIF};letter-spacing:-.01em;color:${C.cream}">Studio Matiz</div>`;
  const grana = `${assets}/grain.png`;
  return `<!doctype html>
<html lang="${l}" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light only">
<meta name="supported-color-schemes" content="light only">
<title>${esc(titolo.replace(/<[^>]+>/g, ""))}</title>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..700&family=Manrope:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>@media (max-width:620px){.wrap{width:100%!important}.pad{padding-left:24px!important;padding-right:24px!important}.h1{font-size:30px!important}.ban{height:150px!important}}</style>
</head>
<body style="margin:0;padding:0;background:${C.sand}">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:${C.sand}">${esc(anteprima)}&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="${C.sand}" style="background:${C.sand};background-image:url('${grana}')"><tr><td align="center" style="padding:30px 12px 36px">
  <table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;box-shadow:0 46px 70px -42px rgba(22,18,16,.7)">
    <tr><td class="ban" background="${banner}" bgcolor="${C.night}" align="center" valign="middle" height="170" style="background:${C.night} url('${banner}') center center / cover no-repeat;height:170px;text-align:center;border-bottom:2px solid ${C.gold}">
      <!--[if gte mso 9]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:600px;height:170px"><v:fill type="frame" src="${banner}" color="${C.night}" /><v:textbox inset="0,0,0,0"><![endif]-->
      <div class="pad" style="padding:0 40px;text-align:center">
        ${marchio}
        <div style="margin:12px auto 0;width:34px;height:1px;background:${C.gold}">&nbsp;</div>
        <div style="margin-top:12px;font:600 10px/1.5 ${SANS};letter-spacing:.24em;text-transform:uppercase;color:${C.goldLight}">${l === "en" ? "by Matia Zoffoli" : "di Matia Zoffoli"} &middot; Cesenatico</div>
      </div>
      <!--[if gte mso 9]></v:textbox></v:rect><![endif]-->
    </td></tr>
    <tr><td class="pad" bgcolor="${C.card}" style="background:${C.card};background-image:url('${grana}');padding:42px 40px 36px">
      <div style="font:600 10px/1.4 ${SANS};letter-spacing:.22em;text-transform:uppercase;color:${C.goldText}">&#9679;&nbsp; ${esc(eyebrow)}</div>
      <h1 class="h1" style="margin:14px 0 18px;font:450 36px/1.06 ${SERIF};letter-spacing:-.02em;color:${C.ink}">${titolo}</h1>
      ${corpo}
    </td></tr>
    <tr><td class="pad" bgcolor="${C.night}" style="background:${C.night};padding:26px 40px 28px;border-top:2px solid ${C.gold};font:400 12px/1.8 ${SANS};color:#CFC5B3">${piede}</td></tr>
  </table>
</td></tr></table>
</body>
</html>`;
}

// ---------------------------------------------------------------- A1: conferma al cliente
export function confermaCliente(r: Richiesta, ctx: Contesto): { subject: string; html: string; text: string } {
  const l = r.lingua;
  const T = l === "en"
    ? {
        subject: `Request received: your starting price${r.tipo ? ` for ${r.tipo}` : ""}`,
        pre: "Your request has arrived. A first reply comes within one working day.",
        eyebrow: "Request received",
        titolo: "Your request <em style=\"font-style:normal;color:" + C.goldText + "\">has arrived</em>",
        hello: `Hello ${r.nome},`,
        intro: "This is an automatic reply. Matia replies personally, with a first reply within one working day.",
        riepilogo: "What you entered",
        attivita: "Business", serve: "What is needed", dim: "Size of the job", prezzoL: "Starting price",
        nota: "This is a starting point, not a quote: the real price is written after the first meeting and does not change along the way. VAT if due.",
        come: "What happens next",
        p1: "<b>A first reply</b> from Matia, within one working day.",
        p2: "<b>The first meeting</b>: one hour over coffee and conversation, offered by the studio, in person or by video.",
        p3: "<b>A written quote</b>, with a fixed price and the delivery time.",
        cta: "Book the first meeting", alt: "Or simply reply to this email.",
        piede1: "You are receiving this message because you asked for a starting price on the website.",
        privacy: "Privacy notice", firma: "Studio Matiz, by Matia Zoffoli",
      }
    : {
        subject: `Richiesta ricevuta: il prezzo di partenza${r.tipo ? ` per ${r.tipo}` : ""}`,
        pre: "La richiesta è arrivata. Una prima risposta entro un giorno lavorativo.",
        eyebrow: "Richiesta ricevuta",
        titolo: "La richiesta <em style=\"font-style:normal;color:" + C.goldText + "\">è arrivata</em>",
        hello: `Ciao ${r.nome},`,
        intro: "Questa è una risposta automatica. Matia risponde di persona, con una prima risposta entro un giorno lavorativo.",
        riepilogo: "Quanto hai indicato",
        attivita: "Attività", serve: "Cosa serve", dim: "Dimensione del lavoro", prezzoL: "Prezzo di partenza",
        nota: "È un punto di partenza, non un preventivo: il prezzo vero viene scritto dopo il primo incontro e non cambia in corsa. IVA se dovuta.",
        come: "Come continua",
        p1: "<b>Una prima risposta</b> di Matia, entro un giorno lavorativo.",
        p2: "<b>Il primo incontro</b>: un'ora tra chiacchiere e caffè, offerta dallo studio, di persona o in video.",
        p3: "<b>Un preventivo scritto</b>, con prezzo chiuso e tempo di consegna.",
        cta: "Prenota il primo incontro", alt: "In alternativa basta rispondere a questa email.",
        piede1: "Ricevi questo messaggio perché hai chiesto un prezzo di partenza sul sito.",
        privacy: "Informativa privacy", firma: "Studio Matiz, di Matia Zoffoli",
      };
  const prezzoTxt = prezzo(r.da, r.fino, l);
  const privacyUrl = ctx.sito + (l === "en" ? "/en/privacy.html" : "/privacy.html");
  const righe = [
    r.tipo ? riga(T.attivita, r.tipo) : "",
    riga(T.serve, servizi(r, l)),
    r.dimensione && DIM[l][r.dimensione] ? riga(T.dim, DIM[l][r.dimensione]) : "",
  ].join("");

  const corpo = `
      <p style="margin:0 0 6px;font:400 16px/1.6 ${SANS};color:${C.ink}">${esc(T.hello)}</p>
      <p style="margin:0 0 26px;font:300 16px/1.65 ${SANS};color:${C.ink}">${esc(T.intro)}</p>

      <div style="font:600 10px/1.4 ${SANS};letter-spacing:.2em;text-transform:uppercase;color:${C.soft};margin:0 0 4px">${esc(T.riepilogo)}</div>
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid ${C.ink}">${righe}</table>

      ${prezzoBox(T.prezzoL, prezzoTxt, T.nota)}

      ${filo()}
      <div style="margin:22px 0 4px;font:600 10px/1.4 ${SANS};letter-spacing:.2em;text-transform:uppercase;color:${C.soft}">${esc(T.come)}</div>
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid ${C.line}">${passo("01", T.p1)}${passo("02", T.p2)}${passo("03", T.p3)}</table>

      <div style="margin:28px 0 10px">${btn(ctx.calendario, T.cta)}</div>
      <p style="margin:0 0 6px;font:300 14px/1.6 ${SANS};color:${C.soft}">${esc(T.alt)}</p>`;

  const piede = `<span style="font:450 16px/1.4 ${SERIF};color:${C.cream}">${esc(T.firma)}</span><br>Cesenatico &middot; <a href="mailto:${esc(ctx.emailStudio)}" style="color:${C.goldLight};text-decoration:none">${esc(ctx.emailStudio)}</a> &middot; <a href="https://wa.me/${esc(ctx.whatsapp)}" style="color:${C.goldLight};text-decoration:none">WhatsApp +39 333 958 0381</a><br><span style="font-size:11px;color:#9C9283">${esc(T.piede1)} <a href="${esc(privacyUrl)}" style="color:#9C9283">${esc(T.privacy)}</a>.</span>`;

  const html = cornice({ l, anteprima: T.pre, eyebrow: T.eyebrow, titolo: T.titolo, corpo, piede, assets: ctx.assets ?? `${ctx.sito}/email`, logo: ctx.logo });

  const text = [
    T.hello, "", T.intro, "",
    T.riepilogo + ":",
    r.tipo ? `- ${T.attivita}: ${r.tipo}` : "",
    `- ${T.serve}: ${servizi(r, l)}`,
    r.dimensione && DIM[l][r.dimensione] ? `- ${T.dim}: ${DIM[l][r.dimensione]}` : "",
    `- ${T.prezzoL}: ${prezzoTxt}`, "",
    T.nota, "",
    T.come + ":",
    "01 " + T.p1.replace(/<[^>]+>/g, ""), "02 " + T.p2.replace(/<[^>]+>/g, ""), "03 " + T.p3.replace(/<[^>]+>/g, ""), "",
    `${T.cta}: ${ctx.calendario}`, T.alt, "",
    T.firma, `Cesenatico - ${ctx.emailStudio} - WhatsApp +39 333 958 0381`, `${T.privacy}: ${privacyUrl}`,
  ].filter((x, i, a) => !(x === "" && a[i - 1] === "")).join("\n");

  return { subject: T.subject, html, text };
}

// ---------------------------------------------------------------- A2: avviso a Matia (sempre in italiano)
export function avvisoStudio(r: Richiesta, ctx: Contesto): { subject: string; html: string; text: string } {
  const l: Lingua = "it";
  const prezzoTxt = prezzo(r.da, r.fino, l);
  const tetto = r.fino && r.fino !== r.da ? `${migliaia(r.fino, l)} euro` : "-";
  const cifre = (r.telefono || "").replace(/[^\d]/g, "");
  const wa = cifre ? `https://wa.me/${cifre.length <= 10 && !cifre.startsWith("39") ? "39" + cifre : cifre}` : "";
  const oggetto = `Nuova richiesta: ${r.tipo ?? "attività"}${r.da ? `, ${prezzoTxt}` : ""}`;
  const righe = [
    riga("Email", r.email), r.telefono ? riga("Telefono", r.telefono) : "",
    r.tipo ? riga("Attività", r.tipo) : "", r.presenza ? riga("Presenza online oggi", r.presenza) : "",
    riga("Cosa serve", servizi(r, l)), r.dimensione && DIM[l][r.dimensione] ? riga("Dimensione", DIM[l][r.dimensione]) : "",
    riga("Pagina", r.lingua === "en" ? "inglese" : "italiano"),
  ].join("");
  const corpo = `
      <p style="margin:0 0 22px;font:300 16px/1.65 ${SANS};color:${C.ink}">Ha chiesto un prezzo di partenza dallo stimatore${r.secondi !== null ? `, compilato in ${r.secondi} secondi` : ""}.</p>
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-top:1px solid ${C.ink}">${righe}</table>
      ${prezzoBox("Prezzo mostrato", prezzoTxt, `Tetto interno: ${tetto}. Il cliente vede solo il prezzo di partenza.`)}
      <p style="margin:24px 0 14px;font:400 15px/1.6 ${SANS};color:${C.ink}"><b>Da fare:</b> rispondere entro un giorno lavorativo e proporre il primo incontro.</p>
      <div>${btn(`mailto:${r.email}?subject=${encodeURIComponent("Il tuo prezzo di partenza - Studio Matiz")}`, "Rispondi per email")}${wa ? btn(wa, "Scrivi su WhatsApp", false) : ""}</div>`;
  const piede = `<span style="font:450 16px/1.4 ${SERIF};color:${C.cream}">Studio Matiz</span><br><span style="font-size:11px;color:#9C9283">Avviso automatico dello stimatore del sito</span>`;
  const html = cornice({ l, anteprima: `${r.nome}: ${prezzoTxt}`, eyebrow: "Nuova richiesta", titolo: esc(r.nome), corpo, piede, assets: ctx.assets ?? `${ctx.sito}/email`, logo: ctx.logo });
  const text = [
    `${r.nome} ha chiesto un prezzo di partenza${r.secondi !== null ? ` (compilato in ${r.secondi} secondi)` : ""}.`, "",
    `Email: ${r.email}`, r.telefono ? `Telefono: ${r.telefono}` : "",
    r.tipo ? `Attività: ${r.tipo}` : "", r.presenza ? `Presenza online oggi: ${r.presenza}` : "",
    `Cosa serve: ${servizi(r, l)}`, r.dimensione && DIM[l][r.dimensione] ? `Dimensione: ${DIM[l][r.dimensione]}` : "",
    `Pagina: ${r.lingua === "en" ? "inglese" : "italiano"}`, "",
    `Prezzo mostrato: ${prezzoTxt} (tetto interno: ${tetto})`, "",
    "Da fare: rispondere entro un giorno lavorativo e proporre il primo incontro.",
  ].filter((x, i, a) => !(x === "" && a[i - 1] === "")).join("\n");
  return { subject: oggetto, html, text };
}
