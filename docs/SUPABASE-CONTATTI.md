# Contatti dello stimatore su Supabase (Europa)

Data: 2026-10-08. Matia ha chiesto di collegare i contatti con Supabase in Europa. Fatto e provato dal vivo.

## Cosa e' stato creato

- **Progetto Supabase `matiz-studio`**, identificativo `mtdfpcwdzjweyqpgpdvp`, regione **eu-central-1 (Francoforte, Germania)**, piano gratuito, costo 0 euro al mese. Indirizzo: `https://mtdfpcwdzjweyqpgpdvp.supabase.co`.
  - **Nota:** l'unica organizzazione dell'account si chiama "Ghetto Ponente" (l'altro progetto di Matia, in pausa, e' nella stessa). Il progetto di Studio Matiz sta quindi nella stessa organizzazione, ma e' separato: ha un suo database e i suoi dati. Se Matia vorra' separare anche la fatturazione, si puo' creare un'organizzazione nuova e trasferire il progetto.
- **Tabella `contatti`** (schema `public`), con la sicurezza a livello di riga attiva e **nessuna regola di accesso pubblico**: ne' scrivibile ne' leggibile con le chiavi pubbliche. Controllato: una richiesta senza chiave riceve 401. Si legge solo dal pannello di Supabase o con la chiave di servizio.
  - Campi: id, data di creazione, nome, email, telefono, tipo di attivita', servizi, presenza online, dimensione, prezzo di partenza mostrato, tetto interno della fascia (non mostrato al cliente), consenso all'informativa, consenso alle comunicazioni, versione dell'informativa, fonte, stato (nuovo, contattato, incontro, cliente, archiviato), note.
  - Controlli sul formato dei dati (lunghezze, valori ammessi). **Non si registra l'indirizzo IP.**
- **Funzione `contatto`** (indirizzo `.../functions/v1/contatto`), pubblica di proposito (la pagina e' statica e non ha un accesso con login). Le protezioni sono nel codice:
  - accetta solo richieste POST in formato JSON, di massimo 8 KB;
  - **campo trappola** nascosto che le persone non compilano e **tempo minimo di compilazione** di 2,5 secondi: se scattano, risponde "ok" senza salvare, cosi' i bot non imparano;
  - controlla nome, email, valori ammessi per servizi e dimensione, e che l'informativa privacy sia spuntata;
  - **limiti di frequenza:** al massimo 3 invii dalla stessa email in 10 minuti e 40 in totale al minuto;
  - nessun dato personale scritto nei registri della funzione.
- **Avviso a Matia (opzionale, non ancora attivo):** la funzione e' pronta a inviare un'email tramite Resend se tra i segreti della funzione ci sono `RESEND_API_KEY` e `NOTIFY_EMAIL` (e facoltativamente `NOTIFY_FROM`). **Servono credenziali che puo' inserire solo Matia dal pannello di Supabase**, quindi non le ho toccate.

## Come si leggono i contatti

Dal pannello Supabase: Table Editor, tabella `contatti`, ordinata per data. In alternativa si puo' costruire una vista semplice nell'area riservata del sito (da fare insieme al sito vero).

## Prove eseguite

- Richiesta valida: salvata con tutti i campi corretti (poi cancellata, era una prova).
- Senza informativa: rifiutata. Email non valida: rifiutata.
- Campo trappola e compilazione troppo veloce: risposta "ok" ma nessuna riga salvata.
- Prova completa dal browser: la pagina ha inviato lo stimatore alla funzione e mostrato "Ho ricevuto la tua richiesta" (riga cancellata subito dopo).
- Controllo di sicurezza di Supabase: unico avviso informativo, "RLS attiva senza regole", che e' voluto (tabella chiusa al pubblico).

## Da fare

1. **Restringere l'origine** quando c'e' il dominio del sito: impostare `ALLOWED_ORIGINS` (per esempio `https://matizstudio.it`) tra i segreti della funzione. Oggi accetta qualunque origine, che serve per le prove.
2. **Attivare l'avviso a Matia** (Resend o altro) con i segreti sopra.
3. **Conservazione:** decidere i periodi (proposta: richieste senza seguito 12 mesi, con consenso fino alla revoca e comunque 24 mesi dall'ultima interazione) e programmare la cancellazione automatica.
4. **Messaggi di seguito** per chi ha dato il consenso: da costruire dopo la scelta del servizio di invio. Si filtrano con `consenso_comunicazioni = true`.
5. **Richieste dei clienti sui propri dati** (accesso, cancellazione): procedura semplice da scrivere in `docs/PROCEDURE.md`.
6. **Informativa privacy** da far controllare a un professionista (gia' aggiornata con Supabase a Francoforte, Google Calendar e WhatsApp Business).
