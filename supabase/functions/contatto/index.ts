import { createClient } from "npm:@supabase/supabase-js@2";

// Riceve le richieste dallo stimatore del sito Studio Matiz e le salva nella tabella `contatti`.
// Pubblica di proposito (nessun accesso con login): le protezioni sono nel codice qui sotto.
//
// Variabili (segreti della funzione, dal pannello di Supabase). Tutte opzionali:
//   ALLOWED_ORIGINS  elenco di origini consentite, separate da virgole (es. https://studiomatiz.it,https://studio-matiz.vercel.app)
//   RESEND_API_KEY   chiave di Resend: senza, nessuna email parte
//   NOTIFY_EMAIL     dove arriva l'avviso per ogni nuova richiesta (A2 in docs/EMAIL-E-RISPOSTE.md)
//   NOTIFY_FROM      mittente dell'avviso, es. "Studio Matiz <onboarding@resend.dev>" (predefinito) o un indirizzo del dominio verificato
//   CONFIRM_FROM     mittente della conferma al cliente (A1), es. "Studio Matiz <ciao@studiomatiz.it>". Serve un dominio verificato su Resend:
//                    se manca, la conferma al cliente non parte e resta solo l'avviso a Matia.

const SERVIZI = ["sito", "menu", "auto", "assistenza", "nonso"];
const DIMENSIONI = ["piccola", "media", "grande"];
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const allowed = (Deno.env.get("ALLOWED_ORIGINS") ?? "*").split(",").map((s) => s.trim()).filter(Boolean);

function corsHeaders(origin: string | null) {
  const ok = allowed.includes("*") || (origin !== null && allowed.includes(origin));
  return {
    "Access-Control-Allow-Origin": ok ? (allowed.includes("*") ? "*" : origin!) : "null",
    "Access-Control-Allow-Headers": "content-type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Vary": "Origin",
  };
}

function reply(body: unknown, status: number, origin: string | null) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...corsHeaders(origin), "Content-Type": "application/json" },
  });
}

function text(v: unknown, max: number): string | null {
  if (typeof v !== "string") return null;
  const t = v.trim().replace(/[\u0000-\u001f\u007f]/g, " ");
  return t ? t.slice(0, max) : null;
}

function int(v: unknown): number | null {
  const n = Number(v);
  return Number.isFinite(n) && n >= 0 && n <= 1000000 ? Math.round(n) : null;
}

function migliaia(n: number, lingua: "it" | "en"): string {
  return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, lingua === "en" ? "," : ".");
}

// Invia una email con Resend. Non scrive mai dati personali nei log.
async function invia(chiave: string, corpo: Record<string, unknown>) {
  try {
    const r = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: { Authorization: `Bearer ${chiave}`, "Content-Type": "application/json" },
      body: JSON.stringify(corpo),
    });
    if (!r.ok) console.error("resend: risposta", r.status);
  } catch {
    console.error("resend: invio non riuscito");
  }
}

Deno.serve(async (req: Request) => {
  const origin = req.headers.get("origin");
  if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: corsHeaders(origin) });
  if (req.method !== "POST") return reply({ ok: false, errore: "metodo non consentito" }, 405, origin);
  if (!allowed.includes("*") && (origin === null || !allowed.includes(origin))) {
    return reply({ ok: false, errore: "origine non consentita" }, 403, origin);
  }

  let raw = "";
  try {
    raw = await req.text();
  } catch {
    return reply({ ok: false, errore: "richiesta non valida" }, 400, origin);
  }
  if (raw.length > 8000) return reply({ ok: false, errore: "richiesta troppo grande" }, 413, origin);

  let b: Record<string, unknown>;
  try {
    b = JSON.parse(raw);
  } catch {
    return reply({ ok: false, errore: "richiesta non valida" }, 400, origin);
  }

  // Antispam: campo trappola che le persone non compilano, e tempo minimo di compilazione.
  // Se scatta rispondiamo "ok" senza salvare, cosi' i bot non imparano.
  if (typeof b.sito_web === "string" && b.sito_web.trim() !== "") return reply({ ok: true }, 200, origin);
  const t = Number(b.tempo_compilazione_ms);
  if (Number.isFinite(t) && t < 2500) return reply({ ok: true }, 200, origin);

  const nome = text(b.nome, 120);
  const email = text(b.email, 200)?.toLowerCase() ?? null;
  if (!nome) return reply({ ok: false, errore: "nome mancante" }, 400, origin);
  if (!email || !EMAIL_RE.test(email)) return reply({ ok: false, errore: "email non valida" }, 400, origin);
  if (b.consenso_privacy !== true) return reply({ ok: false, errore: "serve l'informativa privacy" }, 400, origin);

  const servizi = Array.isArray(b.servizi) ? b.servizi.filter((s) => typeof s === "string" && SERVIZI.includes(s)).slice(0, 5) : [];
  const dimensione = typeof b.dimensione === "string" && DIMENSIONI.includes(b.dimensione) ? b.dimensione : null;
  const lingua: "it" | "en" = b.lingua === "en" ? "en" : "it";

  const riga = {
    nome,
    email,
    telefono: text(b.telefono, 40),
    tipo_attivita: text(b.tipo_attivita, 80),
    servizi,
    presenza: text(b.presenza, 80),
    dimensione,
    prezzo_da: int(b.prezzo_da),
    prezzo_fino_a: int(b.prezzo_fino_a),
    consenso_privacy: true,
    consenso_comunicazioni: b.consenso_comunicazioni === true,
    versione_informativa: text(b.versione_informativa, 40) ?? "bozza",
    fonte: "stimatore",
  };

  const db = createClient(Deno.env.get("SUPABASE_URL")!, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, {
    auth: { persistSession: false },
  });

  // Limiti di frequenza: massimo 3 invii dalla stessa email in 10 minuti, 40 in totale al minuto.
  const dieciMinuti = new Date(Date.now() - 10 * 60 * 1000).toISOString();
  const unMinuto = new Date(Date.now() - 60 * 1000).toISOString();
  const [perEmail, totale] = await Promise.all([
    db.from("contatti").select("id", { count: "exact", head: true }).eq("email", email).gte("creato_il", dieciMinuti),
    db.from("contatti").select("id", { count: "exact", head: true }).gte("creato_il", unMinuto),
  ]);
  if ((perEmail.count ?? 0) >= 3 || (totale.count ?? 0) >= 40) {
    return reply({ ok: false, errore: "troppe richieste, riprova tra poco" }, 429, origin);
  }

  const { error } = await db.from("contatti").insert(riga);
  if (error) {
    console.error("inserimento fallito:", error.code);
    return reply({ ok: false, errore: "non sono riuscito a salvare la richiesta" }, 500, origin);
  }

  // Email, solo se Resend e' configurato.
  const chiave = Deno.env.get("RESEND_API_KEY");
  const a = Deno.env.get("NOTIFY_EMAIL");
  if (chiave && a) {
    const da = riga.prezzo_da;
    const serviziTxt = servizi.join(", ") || "-";
    const secondi = Number.isFinite(t) ? Math.round(t / 1000) : null;

    // A2. Avviso a Matia (sempre in italiano, con la lingua della pagina indicata).
    await invia(chiave, {
      from: Deno.env.get("NOTIFY_FROM") ?? "Studio Matiz <onboarding@resend.dev>",
      to: [a],
      reply_to: email,
      subject: `Nuova richiesta: ${riga.tipo_attivita ?? "attivita'"}${da ? `, da ${migliaia(da, "it")} euro` : ""}`,
      text: [
        `${nome} ha chiesto un prezzo di partenza.`,
        "",
        `Email: ${email} - Telefono: ${riga.telefono ?? "-"}`,
        `Attivita': ${riga.tipo_attivita ?? "-"} - Presenza online oggi: ${riga.presenza ?? "-"}`,
        `Cosa serve: ${serviziTxt} - Dimensione: ${dimensione ?? "-"}`,
        `Prezzo di partenza mostrato: ${da ? `da ${migliaia(da, "it")} euro` : "-"} (tetto interno: ${riga.prezzo_fino_a ?? "-"} euro)`,
        `Lingua della pagina: ${lingua === "en" ? "inglese" : "italiano"}${secondi !== null ? ` - compilata in ${secondi} secondi` : ""}`,
        "",
        "Da fare: rispondere entro un giorno lavorativo e proporre il primo incontro.",
      ].join("\n"),
    });

    // A1. Conferma al cliente, nella lingua della pagina. Parte solo con un mittente di un dominio verificato.
    const conferma = Deno.env.get("CONFIRM_FROM");
    if (conferma) {
      const link = Deno.env.get("CALENDAR_URL") ?? "https://calendar.app.google/NUp3xit8MwxWQWkK6";
      const it = {
        subject: `Richiesta ricevuta: il prezzo di partenza${riga.tipo_attivita ? ` per ${riga.tipo_attivita}` : ""}`,
        body: [
          `Ciao ${nome},`,
          "",
          "questa e' una risposta automatica: la richiesta e' arrivata, e Matia risponde di persona entro un giorno lavorativo.",
          "",
          "Il riepilogo di quanto indicato:",
          `- Attivita': ${riga.tipo_attivita ?? "-"}`,
          `- Cosa serve: ${serviziTxt}`,
          `- Prezzo di partenza: ${da ? `da ${migliaia(da, "it")} euro` : "-"}`,
          "",
          "E' un punto di partenza, non un preventivo: il prezzo vero viene scritto dopo il primo incontro e non cambia in corsa. IVA se dovuta.",
          "",
          `Il primo incontro dura un'ora, di persona o in video, ed e' offerto dallo studio. Si prenota da qui: ${link}. In alternativa basta rispondere a questa email.`,
          "",
          "Studio Matiz, di Matia Zoffoli",
          "Cesenatico - +39 333 958 0381",
        ].join("\n"),
      };
      const en = {
        subject: `Request received: your starting price${riga.tipo_attivita ? ` for ${riga.tipo_attivita}` : ""}`,
        body: [
          `Hello ${nome},`,
          "",
          "this is an automatic reply: your request has arrived, and Matia will reply personally within one working day.",
          "",
          "A summary of what you entered:",
          `- Business: ${riga.tipo_attivita ?? "-"}`,
          `- What is needed: ${serviziTxt}`,
          `- Starting price: ${da ? `from €${migliaia(da, "en")}` : "-"}`,
          "",
          "This is a starting point, not a quote: the real price is written after the first meeting and does not change along the way. VAT if due.",
          "",
          `The first meeting lasts one hour, in person or on video, and is offered by the studio. It can be booked here: ${link}. Alternatively, just reply to this email.`,
          "",
          "Studio Matiz, by Matia Zoffoli",
          "Cesenatico - +39 333 958 0381",
        ].join("\n"),
      };
      const m = lingua === "en" ? en : it;
      await invia(chiave, { from: conferma, to: [email], reply_to: a, subject: m.subject, text: m.body });
    }
  }

  return reply({ ok: true }, 200, origin);
});
