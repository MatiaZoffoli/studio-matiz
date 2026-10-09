// Anteprime delle email con dati di fantasia. Uso: node supabase/functions/contatto/preview.ts
// Scrive i file in email/anteprime/ (HTML e testo semplice). Non invia nulla.
import { writeFileSync, mkdirSync } from "node:fs";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { confermaCliente, avvisoStudio, confermaIncontro, avvisoIncontro } from "./email.ts";

const ctx = {
  sito: "https://studio-matiz.vercel.app",
  whatsapp: "393339580381",
  emailStudio: "matiazoffoli@gmail.com",
  // nelle anteprime le immagini si leggono dai file locali; online sono quelle del sito (/email/)
  assets: pathToFileURL(resolve("prova/email")).href,
};
const it = { nome: "Anna", email: "anna@bagnoesempio.it", telefono: "+39 333 111 2222", tipo: "Stabilimento balneare", servizi: ["sito", "menu", "assistenza"], presenza: "Ho un sito vecchio", dimensione: "media", da: 1500, fino: 3200, lingua: "it" as const, secondi: 42 };
const en = { ...it, nome: "Anna", tipo: "Beach club", presenza: "I have an old website", lingua: "en" as const };

const inc = { ...it, servizi: [], dimensione: null, da: null, fino: null, fonte: "incontro" as const, modalita: "persona" as const, preferenza: "Martedì o giovedì pomeriggio" };
mkdirSync("email/anteprime", { recursive: true });
const out: [string, { subject: string; html: string; text: string }][] = [
  ["conferma-it", confermaCliente(it, ctx)],
  ["conferma-en", confermaCliente(en, ctx)],
  ["avviso-studio", avvisoStudio(it, ctx)],
  ["conferma-cura-it", confermaCliente({ ...it, servizi: ["assistenza"], dimensione: null, da: 250, fino: 250 }, ctx)],
  ["incontro-it", confermaIncontro({ ...inc, lingua: "it" }, ctx)],
  ["incontro-en", confermaIncontro({ ...inc, lingua: "en", modalita: "video" }, ctx)],
  ["avviso-incontro", avvisoIncontro(inc, ctx)],
  ["avviso-cura", avvisoStudio({ ...it, servizi: ["assistenza"], dimensione: null, da: 250, fino: 250 }, ctx)],
];
for (const [nome, m] of out) {
  writeFileSync(`email/anteprime/${nome}.html`, m.html);
  writeFileSync(`email/anteprime/${nome}.txt`, `Oggetto: ${m.subject}\n\n${m.text}\n`);
  console.log(nome, "-", m.subject);
}
