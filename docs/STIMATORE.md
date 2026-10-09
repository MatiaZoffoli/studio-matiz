# Stimatore a fasce - come funziona e cosa manca

Data: 2026-10-08. Sezione "Quanto costa, in concreto" di `prova/index.html` (ancora `#stima`). Prezzi e tempi presi da `docs/LISTINO-E-TEMPI.md`, confermati da Matia "per ora".

## Come funziona per chi lo usa

Quattro domande, una alla volta, poi nome ed email, poi la fascia **subito sulla pagina**.
1. Che tipo di attivita' hai? (stabilimento, ristorante o bar, hotel, negozio o artigiano, studio professionale, altro)
2. Cosa ti serve? Si puo' scegliere piu' di una cosa: un sito, un menu digitale, automatizzare una parte del lavoro, assistenza continua, oppure "non lo so, voglio capire da dove partire" (esclude le altre).
3. Com'e' oggi la tua presenza online? (niente, sito vecchio, sito che nessuno segue, sito che funziona)
4. Quanto e' grande il lavoro? Essenziale, completo, su misura con funzioni. **Appare solo se ha scelto un sito o un'automazione**: negli altri casi le domande sono tre piu' i contatti.
5. Contatti: nome, email, telefono facoltativo, casella dell'informativa privacy (obbligatoria per vedere la fascia) e casella del consenso alle comunicazioni (facoltativa, separata).

## Come calcola la fascia

La fascia e' la somma delle fasce dei lavori scelti. Tutte prese da `docs/LISTINO-E-TEMPI.md`:

| Scelta | Dimensione | Fascia | Tempo mostrato |
|---|---|---|---|
| Sito | essenziale | 500-900 (pagina singola) | 10 giorni |
| Sito | completo | 1.200-2.500 (sito completo) | 3 settimane |
| Sito | su misura | 2.500-5.000 (sito con funzioni) | 6 settimane |
| Menu digitale | - | 300-700 | 5 giorni |
| Automazione | essenziale | 500-900 (automazione semplice) | 10 giorni |
| Automazione | completo | 900-1.500 (automazione articolata) | 10 giorni |
| Automazione | su misura | 2.000-6.000 (strumento su misura) | 5 settimane |
| "Non lo so" | - | 200 (check-up), scalati dal lavoro | 3 giorni lavorativi |
| Assistenza continua | - | nessuna cifra: primo mese a forfait, poi si decide | - |

- Il **tempo mostrato** e' il piu' lungo tra i lavori scelti, e rimanda al preventivo per la data precisa. E' il "tempo garantito" (via di mezzo tra ottimale e medio).
- Con una sola cosa scelta si mostra la sua fascia; con piu' cose, il totale e la lista dei singoli lavori con la loro fascia.
- Con la sola assistenza continua non c'e' cifra: il testo spiega il forfait del primo mese e dice che la cifra arriva nel preventivo.
- Sotto la fascia: "e' una fascia indicativa, non un preventivo", prezzo vero scritto dopo il primo incontro e fisso, IVA se dovuta.
- Due pulsanti: **Prenota il primo incontro** (per ora apre la email con il riepilogo) e **Scrivimi su WhatsApp** (con un messaggio che riporta la fascia e i lavori).

Per cambiare prezzi o tempi basta modificare la tabella `BANDS` nello script della pagina.

## Aggiornamento del 2026-10-08 (notte)

- **Si mostra solo il prezzo di partenza** ("Da 1.500 euro"), non la fascia. Decisione di Matia: i numeri alti scoraggiano. Il tetto della fascia (somma dei massimi) resta nei dati interni (`prezzo_fino_a`) e nel preventivo. Nota di Claude: un "da" funziona se il prezzo vero non si allontana troppo; conviene tenere d'occhio i primi preventivi, e se spesso superano di molto il prezzo di partenza, alzare il "da" o aggiungere una frase onesta sul fatto che dipende dall'ampiezza.
- **I contatti vengono salvati** in Supabase a Francoforte tramite la funzione `contatto` (vedi `docs/SUPABASE-CONTATTI.md`). Se il salvataggio fallisce, la pagina lo dice e invita a scrivere su WhatsApp. La sezione "Cosa non e' ancora collegato" qui sotto e' storica.
- Prenotazione: il pulsante porta al calendario Google di Matia.

## Cosa non e' ancora collegato (stato precedente)

- **Nessun dato viene salvato.** La pagina mostra un avviso "Versione di prova". Il modulo e' pronto a inviare i dati a un indirizzo (`window.MATIZ_LEAD_ENDPOINT`): se e' impostato, spedisce un riepilogo (tipo di attivita', servizi, presenza, dimensione, nome, email, telefono, consenso alle comunicazioni, fascia, data); se non e' impostato, non spedisce nulla.
- **Serve un archivio dei contatti e un invio di email.** Proposta: una funzione sul sito che riceve il modulo, lo salva in una tabella (su un servizio con dati in Europa) e avvisa Matia; poi, solo per chi ha dato il consenso, due o tre messaggi di seguito. Strumenti gia' a disposizione di Matia: Vercel e Supabase. Va decisa prima la parte privacy (vedi `prova/privacy.html` e `docs/BACKLOG.md`).
- **Prenotazione:** il pulsante usera' il link della pagina di prenotazione di Google Calendar non appena Matia la crea.
- **Antispam:** per un modulo pubblico serve una protezione (campo nascosto o servizio di verifica) prima di collegarlo.
- Un errore nel risultato non e' stato visto in test: i controlli di validazione (tipo, almeno un servizio, nome, email, informativa) e il calcolo delle fasce funzionano. Non e' stato provato su telefono vero.

## Aggiornamento del 2026-10-10 (dopo la prova di Matia)

- **La sola assistenza continua ora ha una cifra** (prima mostrava solo il testo "Cura continua", che si leggeva come gratuito): "250 euro il primo mese" (forfait) e, in lista, "Dal secondo mese, da 100 euro al mese". Costanti `CURA = [250, 100]` accanto a `BANDS` nello script; sono le cifre della proposta in `docs/LISTINO-E-TEMPI.md`, da confermare. Il prezzo del lavoro non cambia; nel salvataggio, per la sola cura, `prezzo_da` e `prezzo_fino_a` valgono 250.
- **Cura con altri lavori:** la cura continua non si somma al totale del lavoro; compare in lista con le sue due cifre, e una frase dice che si aggiunge.
- **Layout del risultato:** piu' respiro sopra l'etichetta, che toccava il filo sottile; i risultati che sono testo ("250 euro il primo mese", "Il check-up: 200 euro") hanno una dimensione minore delle cifre del prezzo.
- **Da rivedere (proposte in `docs/BACKLOG.md`):** una sola dimensione per sito e automazione insieme; tempo mostrato come il piu' lungo e non come la somma; la domanda sulla presenza online non pesa sul prezzo; lavori del listino non presenti nello stimatore (testi in inglese, scheda Google).
