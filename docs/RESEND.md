# Resend: email automatiche dal sito

Data: 2026-10-09. Serve a due cose: **A2**, l'avviso a Matia per ogni richiesta dello stimatore, e **A1**, la conferma automatica al cliente (testi in `docs/EMAIL-E-RISPOSTE.md`). La funzione aggiornata e' gia' scritta in `supabase/functions/contatto/index.ts`, ma **non e' ancora distribuita**: il sito usa ancora la versione precedente, che salva le richieste e non invia email.

Cosa serve da Matia (le credenziali le inserisce solo lui, mai in chat e mai nei file):

## Fase 1 - Avviso a Matia (si puo' fare subito, senza dominio)

1. **Account Resend** con l'email `matiazoffoli@gmail.com`: https://resend.com/signup (piano gratuito: 3.000 email al mese, 100 al giorno). Importante registrarsi con quell'email: fino a quando non c'e' un dominio verificato, Resend consente di inviare solo all'indirizzo dell'account.
2. **Chiave API**: https://resend.com/api-keys, "Create API Key", nome `studio-matiz-sito`, permesso "Sending access". La chiave si vede una volta sola: copiarla subito.
3. **Segreti della funzione su Supabase**: https://supabase.com/dashboard/project/mtdfpcwdzjweyqpgpdvp/functions/secrets, "Add new secret", due righe:
   - `RESEND_API_KEY` = la chiave copiata al punto 2
   - `NOTIFY_EMAIL` = `matiazoffoli@gmail.com`
4. **Distribuire la funzione aggiornata.** Matia scrive "distribuisci la funzione" e io la pubblico, poi facciamo il test insieme. In alternativa a mano, dal terminale con la CLI di Supabase: `supabase functions deploy contatto --project-ref mtdfpcwdzjweyqpgpdvp`.
5. **Test**: compilare lo stimatore su https://studio-matiz.vercel.app (con un'email vera, anche la propria; il campo "Non compilare" resta vuoto). Deve arrivare l'avviso a Matia entro pochi secondi. Se non arriva, i log sono qui: https://supabase.com/dashboard/project/mtdfpcwdzjweyqpgpdvp/functions/contatto/logs (cercare `resend:`).

L'avviso arriva dal mittente `Studio Matiz <onboarding@resend.dev>` e ha come "rispondi a" l'email del cliente: basta rispondere dalla posta.

## Fase 2 - Conferma automatica al cliente (serve il dominio)

Resend invia a indirizzi qualunque solo da un **dominio verificato**. Quando Matia ha il dominio:

1. https://resend.com/domains, "Add Domain", inserire il dominio (meglio un sottodominio di invio, ad esempio `mail.nomedominio.it`). Se Resend lo offre, scegliere la regione **Irlanda (eu-west-1)** per tenere i dati in Europa.
2. Copiare i record DNS che Resend mostra (SPF, DKIM, e se richiesto DMARC) nel pannello DNS del dominio (se il dominio e' gestito da Vercel: https://vercel.com/dashboard/domains). Attendere la verifica, da pochi minuti a qualche ora.
3. Aggiungere due segreti su Supabase (stessa pagina della Fase 1):
   - `NOTIFY_FROM` = `Studio Matiz <avvisi@mail.nomedominio.it>`
   - `CONFIRM_FROM` = `Studio Matiz <ciao@mail.nomedominio.it>` (con questo si attiva la conferma al cliente, in italiano o in inglese secondo la pagina in cui ha compilato)
4. Restringere la funzione al sito vero: segreto `ALLOWED_ORIGINS` = `https://nomedominio.it,https://www.nomedominio.it` (se serve anche `https://studio-matiz.vercel.app`). Cosi' nessun altro sito puo' inviare richieste.
5. Aggiornare l'informativa privacy: indicare Resend come fornitore di posta (e dove tiene i dati) e aggiornare l'elenco dei fornitori in `prova/privacy.html` e `prova/en/privacy.html`.

## Gli altri messaggi di `docs/EMAIL-E-RISPOSTE.md`

- **A3 (risposta di assenza):** non passa da Resend. Si imposta in Gmail: Impostazioni, Risposta automatica, con il testo A3.
- **A4 (conferma del primo incontro):** la manda Google Calendar quando qualcuno prenota dalla pagina di appuntamenti; il testo personalizzato si inserisce nelle impostazioni della pagina di prenotazione.
- **B e C:** testi che Matia invia di persona.

## Le email (aggiornamento del 2026-10-09)

Avviso a Matia e conferma al cliente sono email HTML con la grafica del sito, e portano anche la versione in testo semplice. Codice in `supabase/functions/contatto/email.ts`; anteprime con dati di fantasia in `email/anteprime/` (si rigenerano con `node supabase/functions/contatto/preview.ts`). La versione con la nuova grafica **non e' ancora distribuita**: dopo il via di Matia si pubblica insieme a `index.ts` (la funzione ora e' formata da due file).

## Cosa fa la funzione, in breve

- Salva ogni richiesta nella tabella `contatti` (come prima), con le stesse protezioni (campo trappola, tempo minimo, limite di frequenza).
- Se `RESEND_API_KEY` e `NOTIFY_EMAIL` ci sono: invia l'avviso A2.
- Se c'e' anche `CONFIRM_FROM`: invia la conferma A1 al cliente. Senza, la salta.
- Non scrive mai dati personali nei log. Se Resend non risponde, la richiesta resta comunque salvata e il cliente vede il messaggio di conferma.
- La pagina inglese manda `lingua: "en"`: l'avviso a Matia lo indica e la conferma al cliente parte in inglese.
