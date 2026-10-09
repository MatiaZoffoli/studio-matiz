# Versione inglese del sito

Data: 2026-10-09. Stato: **prima traduzione fatta, da rivedere insieme a Matia.**

## Come funziona

- Il testo italiano vive solo in `prova/index.html`. La pagina inglese, `prova/en/index.html`, **si genera** da quella con `python tools/build_en.py`: non si modifica a mano.
- Nel file `tools/build_en.py` c'e' l'elenco delle coppie "italiano -> inglese". Se un testo italiano cambia, lo script si ferma e dice quale coppia aggiornare, e segnala anche l'italiano rimasto senza traduzione. Cosi' le due lingue non si allontanano di nascosto.
- Il selettore **IT | EN** e' nella testata, in alto a destra (sul telefono accanto al pulsante). La scelta si ricorda: chi sceglie l'inglese ritrova l'inglese quando riapre l'indirizzo principale.
- L'informativa privacy inglese e' `prova/en/privacy.html` (bozza, con rimando al testo italiano come riferimento).
- Sito online: `/` italiano e `/en/` inglese, entrambi su Vercel.

**Dopo ogni modifica al testo italiano:** `python tools/build_en.py`, poi commit di tutti e due i file.

## Come si e' tradotto

Traduzione semantica, nella voce della skill (impersonale e precisa; prima persona solo in "About" e nei messaggi diretti). Niente "tailor-made", "solutions" e simili, che la skill vieta anche in inglese.

## Scelte da confermare con Matia

1. **Payoff:** "Soluzioni su misura" -> **"Made to measure"** (non "Tailor-made solutions", parole vietate dalla skill).
2. **Menu:** The craft, The method, The terms, Pricing, About, Questions. Primo incontro -> "First meeting". "Le regole" -> "The terms" (alternativa piu' vicina: "The rules").
3. **"Stabilimenti balneari":** "beach clubs".
4. **"Dalla sala ai dati":** "From the dining room to the data". Alternativa: "From the floor to the data".
5. **"Dove si lavora?":** in italiano dice "nel resto d'Italia in video". In inglese ho scritto "elsewhere on video", perche' un lettore inglese puo' essere all'estero. **Da confermare che e' vero.**
6. **FAQ sull'inglese:** in italiano "Si lavora anche in inglese?". Sulla pagina inglese la domanda e' stata rivolta: "Is the work available in both Italian and English?".
7. **Formati:** euro con il simbolo davanti ("from €1,200"), migliaia con la virgola.
8. **Biografia:** "ristorazione" -> "restaurants and hospitality"; "enti pubblici" -> "public bodies".
9. **Messaggi di WhatsApp precompilati** e testi dello stimatore: tradotti.
10. **Dati dello stimatore:** sulla pagina inglese i valori scelti (tipo di attivita', presenza online) arrivano nel database in inglese; i codici di servizio e dimensione restano gli stessi. La funzione riceve anche la lingua (`lingua`), vedi `docs/RESEND.md`.

## Da fare

- Revisione insieme a Matia, frase per frase.
- Quando c'e' il dominio: `hreflang` e indirizzo canonico per le due lingue (oggi la pagina e' `noindex`).
- Tradurre i modelli di `modelli/` (preventivo, accordo, resoconto), le email di `docs/EMAIL-E-RISPOSTE.md` e il testo dell'informativa quando sara' rivisto da un professionista.
- Testi del selettore e meta descrizione sono gia' fatti; il titolo della scheda inglese e' "Studio Matiz - Made to measure".
