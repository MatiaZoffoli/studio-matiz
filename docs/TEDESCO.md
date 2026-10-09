# Versione tedesca del sito

Aggiunta il 2026-10-10. Stesso meccanismo dell'inglese (vedi `docs/INGLESE.md`): il testo italiano di `prova/index.html` e' la fonte unica, la pagina tedesca si genera.

## Come funziona

- `python tools/build_de.py` scrive `prova/de/index.html`. Il generatore e' in `tools/build_en.py` (funzione `build`); le coppie (testo italiano -> tedesco) stanno in `tools/build_de.py`.
- Se un testo italiano cambia, va aggiornata la coppia in **entrambi** i file (`build_en.py` e `build_de.py`) e vanno rigenerate le due pagine. Lo script si ferma e dice quale coppia manca; segnala anche il testo italiano rimasto.
- Informativa privacy tedesca: `prova/de/privacy.html` (traduzione della bozza inglese, da far rivedere insieme alle altre).
- Selettore della lingua: menu a tendina con bandiera, ora con Italiano, English, Deutsch. Chi sceglie una lingua la ritrova alla visita successiva (memoria nel browser).
- Il modulo e lo stimatore inviano `lingua: 'de'` alla funzione `contatto`, che manda la conferma al cliente in tedesco (`confermaCliente` e `confermaIncontro` in `supabase/functions/contatto/email.ts`) e segnala a Matia che la pagina era in tedesco.
- Immagini delle email in tedesco (titoli, prezzi "ab 1.500 €", pulsanti): `python tools/email_type.py`.

## Scelte di voce

- Impersonale e preciso come in italiano; prima persona solo in "Chi sono" e nelle firme. Nel modulo, forma impersonale, niente "Sie" diretto dove si puo' evitare; nelle email "Ihre Angaben" quando serve.
- Payoff: "Nach Maß." (equivalente di "Made to measure").
- Prezzi nel formato tedesco: 1.500 €, "ab" al posto di "da".
- La domanda sulle lingue di lavoro resta "Wird auch auf Englisch gearbeitet?" (non si promette il tedesco come lingua di lavoro).

## Da fare

- **Rilettura da madrelingua tedesca**, prima di mostrare la pagina a clienti: la traduzione e' mia e non e' stata rivista da una persona. Punti sensibili: la sezione "Über mich", le risposte alle domande frequenti, l'informativa privacy.
- Decidere se Matia vuole offrire davvero il tedesco come lingua di lavoro (oggi non lo promette).
- Con il dominio: `hreflang` tra le tre versioni e indirizzi definitivi.
