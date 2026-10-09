# Studio Matiz

**Posizione del progetto (dal 2026-10-08):** `C:\Users\gisel\dev\studio-matiz`, un repository git. Prima stava in OneDrive (`Documents\MZ Business Consultancy`): quella cartella e' una vecchia copia, da non usare e da cancellare quando Matia ha controllato che tutto sia a posto. Il nome "MZ Business Consultancy" era provvisorio.

Questo file e' la memoria permanente del progetto. Si legge all'apertura di ogni sessione e si aggiorna nel momento in cui emerge un'informazione nuova, non a fine lavoro. Le parti marcate **[DA DEFINIRE]** sono domande aperte, non fatti.

Ultimo aggiornamento: 2026-10-07

## All'apertura di ogni sessione

1. Leggere questo file.
2. Leggere `docs/STATO-DEI-LAVORI.md` e `docs/BACKLOG.md`.
3. Dire a Matia in cinque righe dove siamo e cosa si propone di fare, senza fargli ripetere niente.

Mappa completa dei file in [README.md](README.md). Le scelte prese stanno in `docs/DECISIONI.md`.

---

## 1. Stato del progetto

- **Fase attuale:** definizione dell'idea, prima di operare. Nessun brand, partita IVA o cliente pagante ancora.
- **Piano approvato da Matia (2026-10-07):** partire dal settore balneare e ristorazione della costa romagnola, con offerte confezionate (primo incontro gratuito, check-up, presenza su misura, cura continua).
- **Esito principale della ricerca** (`docs/CONCORRENTI.md`, dati da verificare): il vuoto reale sono gli stabilimenti balneari; la manutenzione dei concorrenti e' vaga; pochi pubblicano i prezzi. Concorrenti piu' vicini: Marketing Gourmet (ristoranti, 250-600 euro/mese, modifiche illimitate) e Patrick Battistini (Cesenatico, vetrina 900-2.500 euro).
- **Sito online (2026-10-09):** `https://studio-matiz.vercel.app` (Vercel, collegato al repository: un push su `main` lo aggiorna), in italiano (`/`) e in inglese (`/en/`, generato da `python tools/build_en.py`; dopo ogni modifica al testo italiano si rigenera). Dettagli in `docs/INGLESE.md`. Testo italiano chiuso da Matia.
- **Vincolo di tempo:** il progetto procede in parallelo a un lavoro a tempo pieno, quindi serve un'offerta gestibile a poche ore a settimana.
- **Dettaglio dello stato, del prossimo passo e delle decisioni aperte:** `docs/STATO-DEI-LAVORI.md` e `docs/BACKLOG.md`. Non si duplicano qui.

## 2. Chi e' il fondatore

- **Nome:** Matia Zoffoli
- **Email:** matiazoffoli@gmail.com
- **Come si descrive:** buone conoscenze di business in generale, intelligenza, common sense, abilita' IT tra intelligenza artificiale e automazione.
- **Motivazione dichiarata:** "e' ora di creare un nuovo business"; ci pensa da tempo e ritiene sia il momento di capitalizzare sulle proprie conoscenze.

### Situazione di partenza (dichiarata da Matia, 2026-10-07)

- **Paese e lingua:** opera in Italia, lavora con i clienti principalmente in italiano.
- **Base e raggio:** vive e lavora a Cesenatico (il CV indica Cesena). Puo' allargarsi oltre la Romagna senza problemi, quindi anche lavoro a distanza con altre regioni.
- **Lavoro attuale:** ha un lavoro a tempo pieno, svolto al computer. Il business si sviluppa **in parallelo**, durante la giornata lavorativa, con la possibilita' di ore extra nei weekend.
- **Esperienza recente:** negli ultimi mesi ha lavorato con un cliente (una squadra/societa' sportiva) per sistemargli il sito web e creare un meccanismo di accesso alle partite della societa'. Lavoro lato IT, non orientato all'AI.
- **Osservazione di mercato:** parlando e ricercando in giro ha notato un malumore generale verso le aziende che costruiscono e mantengono siti web, ancora ferme a un decennio fa, mentre oggi le cose sono piu' facili, veloci, immediate e costano meno.
- **Prospetti:** ha gia' un paio di potenziali clienti (dettagli da raccogliere).

### Profilo professionale (fonte: CV "Matia Zoffoli March 2026 v1", sede Cesena)

- **Titolo:** Data Scientist e AI Specialist; **lavoro attuale:** Senior Consultant, AI Data Scientist presso Capgemini (Insight & Data, Italia), da marzo 2024. Dal CV risultano anche due ruoli paralleli: Data Scientist AI presso il NSW Department of Education (Australia, da luglio 2022) e Founding Data Scientist part-time presso CurriculLM, startup EdTech (da gennaio 2024).
- **Competenze AI dimostrate:** LLM e NLP (OpenAI, Hugging Face, LangChain), sistemi RAG con database vettoriali, fine-tuning, prompt engineering, voce (TTS e voice cloning), ML end-to-end dal prototipo alla produzione su Azure, AWS e GCP, Databricks, Python, SQL, Power BI.
- **Risultati citati nel CV:** piattaforma GenAI per piu' di 1 milione di utenti e oltre 1000 scuole (NSW); assistente Text-to-SQL; framework di test automation (80% dei test automatizzati, -60% di lavoro QA); motore di automazione commissioni (200+ ore di analisti risparmiate per ciclo); chatbot RAG multilingue per retail, telecom e settore pubblico.
- **Background business:** Director e General Manager di Vitadolce Pty Ltd (Australia, 2011-2020), quattro locali e fino a 120 dipendenti, settore hospitality. Prima ancora, esperienze in operations e customer service in Italia e Australia (2006-2011). Poi Data Analyst (Telus, Finkey Capital).
- **Formazione:** diploma in Mathematics - Statistics, diploma in Share Trading and Investment; certificazioni DP-100 (Azure), Databricks AI Engineer Associate, DeepLearning.AI Machine Learning.
- **Lingue:** italiano e inglese fluenti. Matia ha vissuto 13 anni all'estero, in Australia, e parla l'inglese come l'italiano (dichiarato da lui, 2026-10-08). Ha lavorato per il Dipartimento dell'Istruzione del governo australiano (NSW). E' un punto di forza come persona e professionista, e un servizio concreto: testi e traduzioni in inglese ben scritti per siti e menu (vedi `docs/BRAND.md`).

### Come Matia descrive il proprio valore

- Approccio molto pratico. Grazie al background in hospitality e da business owner ha un'idea chiara dei problemi e dei pain point dei piccoli business e ha buone idee per risolverli.
- Usa Claude come "braccio destro" per colmare le lacune tecniche. Ha abbonamenti a Claude Code, Cursor e ChatGPT.
- **Non e' un web designer.** Sviluppa i siti con vibe-coding. Sa che sul web c'e' una curva di apprendimento e non la teme.
- Nel lavoro attuale ricerca, sperimenta e sviluppa PoC e MVP. L'obiettivo e' portare quel metodo a risolvere problemi reali per persone reali.
- Si promuove bene tramite passaparola, con persone che conosce e non.
- **SEO:** l'ha gia' fatta per il suo cliente (societa' sportiva), quindi la SEO locale entra nel check-up e nel perfezionamento tecnico dei siti. Cosa abbia fatto di preciso non e' ancora stato raccolto.

### Vincoli e risorse

- **Tempo:** almeno un paio d'ore al giorno, piu' qualcosa nei weekend (non ha voluto quantificare con precisione).
- **Budget:** spendere il meno possibile all'inizio, reinvestire i primi ricavi. Piccole spese ok, non migliaia di euro. Gli strumenti AI li ha gia'.
- **Contratto di lavoro:** Matia dichiara che non ci sono clausole di esclusiva o non concorrenza e chiede di non preoccuparsene. Va trattato come acquisito.
- **Obiettivo a 12 mesi:** un reddito extra che si somma a quello del lavoro in Italia, dato da un ricavo mensile ricorrente (supporto) piu' progetti una tantum da nuovi clienti.

### Ancora da raccogliere **[DA DEFINIRE]**

- Dettaglio dei due prospetti (vedi sezione 4)
- Cose che preferisce evitare: nessun settore escluso. Accetta chiamate fuori orario e nei weekend come "sacrificio iniziale" (da regolare con tempi di risposta chiari quando il portafoglio cresce)
- Cosa ha fatto di preciso sulla SEO per il primo cliente, e conoscenze su hosting e dominio e strumenti web usati
- Soglia di reddito mensile che renderebbe l'attivita' "valsa la pena"

## 3. L'idea di business (versione iniziale, grezza)

Matia agira' come **consulente per piccole e medie imprese** su due aree principali:

1. **Problemi logistici e pratici**, risolti soprattutto con l'uso dell'AI (e dell'automazione).
2. **Creazione e miglioramento di siti web**, esposizione online e presenza in generale.

Note di Matia: e' l'idea iniziale, va studiata, dettagliata e perfezionata prima di partire.

### Domande aperte sull'idea **[DA DEFINIRE]**

- Le due aree sono un'unica offerta o due linee separate? Una e' la porta d'ingresso per l'altra?
- Consulenza pura (analisi e consigli) o anche realizzazione (implemento io)?
- Modello di ricavo: a progetto, a ore, abbonamento mensile, manutenzione ricorrente, misto?
- Cosa rende l'offerta diversa da un freelance web o da un'agenzia AI generica?
- Quali problemi concreti vendo, in una frase che il cliente capisce senza sentire la parola "AI"?

### Primo caso: sito di una societa' sportiva (portfolio)

Cliente amico di Matia, societa' sportiva. Lavoro di circa un mese, a tempo perso, qualche ora al giorno non tutti i giorni. Le richieste iniziali erano un paio. Lavorando Matia ha individuato molti altri difetti e miglioramenti e li ha fatti di sua iniziativa.

- **Piattaforma:** WordPress. Sistemato l'aspetto delle pagine, che contenevano numerosi errori.
- **Nuove sezioni:** pagine partite, calendari e risultati, e una sezione "dirette" con i video YouTube (live e non), costruite con Claude.
- **Bug trovato e corretto:** il sistema non registrava i nuovi utenti.
- **Sponsor:** pagina rifatta con link ai canali social di ogni sponsor e visibilita' in piu' sezioni del sito.
- **Meccanismo di accesso alle partite:** pagina privata che permette agli addetti all'ingresso di spuntare i nuovi tesserati con ricerca per codice o cognome. Il codice arriva via email all'iscrizione. La card, consegnata al primo ingresso dopo l'iscrizione, funziona da biglietto per tutte le partite in casa.
- **Risultato misurabile:** iscritti da 115 (nei primi due anni) a 450 in una sola settimana. Leve: dirette dietro iscrizione, campagna social sulle nuove card, ingresso al palazzetto gratuito solo con la card.
- **Pagamento:** non ancora avvenuto. Si e' deciso con l'amico di "mettersi a posto" in seguito. **[DA DEFINIRE: cifra e forma]**
- **Nota:** il sito raccoglie dati personali di 450 iscritti, quindi vale per lui l'attenzione privacy/GDPR (vedi sezione 6).

## 4. Clienti target

Dato di partenza: piccole e medie imprese italiane. Ipotesi da verificare: il segmento piu' caldo e' quello con un sito vecchio o mal mantenuto da fornitori "fermi a dieci anni fa". Tutto il resto e' **[DA DEFINIRE]**:

**Prospetti attuali (2):** conoscenti con attivita' balneari (stabilimento e ristorante), che hanno visto il lavoro fatto per il primo cliente. Entrambi scontenti dei servizi web ricevuti:

- Prospetto A: ha chiuso il sito perche' nessuno lo seguiva e non voleva pagare un servizio "inesistente". Pagava 1500-2000 euro una tantum + 50 euro/mese per niente (irreperibile, nessuna modifica inclusa). Spenderebbe volentieri se avesse un ritorno e qualcuno disponibile quando serve.
- Prospetto B: ha un menu digitale ma senza supporto per le modifiche. Il QR code porta a un menu non aggiornato, in contrasto con un locale curato e vini costosi. Vuole qualcosa di funzionante **e di qualita'**, coerente con l'immagine dello stabilimento, e potenzialmente ha molti altri aspetti del business da migliorare o automatizzare (qui entra l'offerta AI/logistica).

Pattern comune: il dolore non e' creare il sito, e' **la manutenzione assente**. Ipotesi di lavoro: la leva commerciale e' "ti tengo tutto aggiornato", non "ti faccio un bel sito".

- Settori prioritari (e settori da evitare). Candidato naturale: hospitality e balneare, dove Matia ha esperienza diretta
- Dimensione (dipendenti, fatturato)
- Area geografica e lingua di lavoro
- Chi decide l'acquisto (titolare, responsabile operativo)
- Maturita' digitale tipica e dolori ricorrenti
- Dove si trovano e come li si raggiunge
- Cliente ideale: descrizione di 1 o 2 profili concreti

## 5. Offerta e prezzi **[DA DEFINIRE]**

Ipotesi di Matia, da validare, per i progetti web:

1. **Una tantum:** cifra fissa per il lavoro svolto.
2. **Manutenzione continuativa:** a richiesta, in base alle necessita'.
3. **Pacchetto annuale:** cifra fissa che comprende n nuove funzionalita' piu' manutenzione e aggiornamento costante di quello che c'e' gia'.

**Cifre ipotizzate da Matia per il caso della societa' sportiva** (da validare):

- Una tantum per il lavoro svolto: 500-800 euro + IVA
- Manutenzione senza nuove funzionalita': 100-150 euro + IVA al mese

**Riferimento di mercato emerso dal Prospetto A:** il suo fornitore precedente chiedeva 1500-2000 euro per realizzare il sito e 50 euro al mese di "manutenzione" in cui nulla era incluso (non reperibile, nessuna modifica). Il cliente spenderebbe volentieri di piu' per un servizio con un ritorno concreto e una persona disponibile quando serve.

**Principio:** il canone mensile si giustifica per cio' che include in modo esplicito e per la disponibilita' reale. Va definito cosa comprende (aggiornamenti tecnici, backup, sicurezza, ore di modifiche contenuti, tempi di risposta) in modo che non sia un altro "50 euro per nulla".

**Regole del check-up decise da Matia (2026-10-07 e 2026-10-08):** primo incontro offerto di 1 ora (durata cambiata il 2026-10-09, era 30-45 minuti). Il check-up costa 200 euro, scontati dagli sviluppi successivi: sconto pieno se il cliente conferma sul momento o entro 2-3 giorni lavorativi, meta' entro 30 giorni, nulla oltre. **Per ora gratuito per amici e conoscenti** (in cambio di aiuto a costruire il brand), **a pagamento per chi arriva da un cliente gia' servito**. Il rapporto riporta sempre il valore. Dettagli in `docs/OFFERTE.md`.

**Regole del canone decise da Matia (2026-10-07):** poche ore incluse, salvo diversa definizione iniziale; **primo mese a ore illimitate** (rodaggio) per misurare l'uso e stimare il budget del resto dell'anno; le ore non usate si perdono; ore extra a tariffa oraria trasparente; risposta entro un giorno lavorativo. Dettagli e cifre in `docs/OFFERTE.md`.

- Servizi in elenco, con cosa e' incluso e cosa no
- Pacchetti o prodotti "confezionati" (es. audit iniziale a prezzo fisso)
- Prezzi, margini, costi di strumenti e licenze
- Condizioni contrattuali tipo

## 6. Aspetti legali, fiscali e amministrativi **[DA DEFINIRE]**

- Matia pensa di operare con **partita IVA italiana**. Scelta del regime (forfettario o ordinario) da verificare con un commercialista: se forfettario non si addebita IVA, quindi le cifre "+ IVA" cambierebbero. Le regole di compatibilita' con il lavoro dipendente vanno controllate sulla norma vigente. Nessuna consulenza fiscale da parte di Claude.
- Forma giuridica e regime fiscale, paese di residenza e di fatturazione
- Partita IVA e codici di attivita'
- Contratto tipo, privacy e GDPR (si trattano dati dei clienti con strumenti AI), responsabilita' sull'output dell'AI
- Assicurazione professionale

## 7. Marketing e acquisizione clienti **[DA DEFINIRE]**

- Nome e identita' del brand (il nome provvisorio "MZ Business Consultancy" e' superato: il nome e' Studio Matiz). **Brief, personalita', direzioni di nome, direzione visiva e verifica dei domini in `docs/BRAND.md`.**
- **Decisioni di brand gia' prese da Matia (2026-10-08):** il nome puo' essere legato alla sua persona; l'AI non va nel nome; il messaggio e' "consulenza per le piccole imprese, su misura"; colori caldi (marroni, crema, bianchi, grigi), equilibrio, geometria e numeri ma accogliente; l'AI si presenta con attenzione, senza spaventare.
- **Feedback di Matia (2026-10-08):** "Studio Zoffoli" non e' male. La frase "Consulenza su misura per le piccole imprese" e' troppo generica: deve parlare di automazione e di design e sviluppo di soluzioni. La palette era troppo flat e pesante (serve brillantezza, vita, un tocco di lusso) e il carattere con le grazie e' noioso (vuole moderno, tagliente, alternativo, ma leggibile). Gli aggettivi preciso, accogliente e concreto vanno bene come tono delle pagine ma **non fanno parte del brand**.
- **Decisioni di brand prese (2026-10-08, dettagli in `docs/BRAND.md`):** payoff "Soluzioni su misura." e descrittore "Progettazione e sviluppo di siti, automazioni e strumenti digitali per piccole imprese."; direzione grafica A (ottone e petrolio, Instrument Serif + Manrope, titoli e numeri in JetBrains Mono) con un tocco di ambra, da valutare in una sezione scura separata.
- **Infrastruttura contatti (2026-10-08):** progetto Supabase `matiz-studio` (identificativo `mtdfpcwdzjweyqpgpdvp`, Francoforte), tabella `contatti`, funzione `contatto`. Dettagli e cose da fare in `docs/SUPABASE-CONTATTI.md`. Le credenziali (chiave di servizio, chiavi di invio email) non si scrivono nei file: le inserisce Matia dal pannello. Calendario di prenotazione: `https://calendar.app.google/NUp3xit8MwxWQWkK6` (account personale, da cambiare con un account Business). Lo stimatore mostra solo il prezzo di partenza.
- **Ricerca marchio su TMview (2026-10-08):** nessun MATIZ attivo in Italia o UE nelle classi 9, 35, 38, 42 tra i primi risultati; il marchio registrato in classe 42 ("MATIZ DESIGN STUDIO") e' messicano. Esito completo in `docs/BRAND.md` sezione 4e. WhatsApp pubblico e' un account Business. Calendario: Google. Stimatore costruito: `docs/STIMATORE.md`.
- **Nome scelto da Matia (2026-10-08): "Studio Matiz", di Matia Zoffoli** (scrittura del logo, confermata da Matia; prima si scriveva "MATIZ Studio", forma da non usare piu'). Logo in `logo/`, ritagli in `prova/assets/`. Gia' sulla pagina di prova. Ricerca ufficiale su TMview ancora da fare prima di spendere (esiste un "Matiz Studio" di interior design in Spagna, stessa classe 42); dominio proposto matizstudio.it (libero). WhatsApp pubblico: +39 333 958 0381. Dettagli in `docs/BRAND.md` sezione 4e. Le righe sotto su ZOMA sono storia della scelta.
- **(Storico) Nome proposto da Matia: "ZOMA Studio" di Matia Zoffoli.** Il controllo preliminare ha trovato **ZOMA Brand Agency (Irlanda, siti e branding)**: rischio alto, in attesa di verifica ufficiale su TMview. Niente acquisti ne' stampe prima.
- **Regole di comunicazione del sito (Matia, 2026-10-08):** niente prezzi scritti; messaggio di costi chiari e contenuti, mai "il piu' economico"; fascia di prezzo in cambio dei contatti, con due caselle di consenso distinte (informativa obbligatoria, comunicazioni facoltativa). Testi: raffinati, eleganti, professionali, non banali; bozza v2 in `docs/TESTI-SITO.md`.
- **Candidato di nome (Matia, 2026-10-08): ZOMA** (Zo da Zoffoli, Ma da Matia), con una parola accanto da scegliere. Analisi, domini e rischi in `docs/BRAND.md` (sezione 4c): domini principali occupati, esiste una startup Zoma a Tel Aviv nell'automazione, serve il controllo del marchio. Consiglio di Claude: marchio ZOMA con "di Matia Zoffoli" sotto, descrittore solo dove serve.
- **Contenuti del sito:** da `docs/ANALISI-BATTISTINI.md` (spunti dal sito di Patrick Battistini, senza copiarne la grafica); le decisioni su pagine e strumenti sono in attesa.
- **Ancora aperto (versione precedente):** il nome. "Studio Zoffoli" non e' confermato. Alternative proposte: Atelier Zoffoli, Bottega Zoffoli, Cifra, Zoffoli Bespoke, Matia Zoffoli. Nota: Zoffoli Mappamondi e' un noto marchio di mappamondi di Rimini (1949), serve verifica del marchio. Nessun dominio acquistato.
- **Il punto di forza umano:** Matia si descrive come un profilo IT "diverso", non il classico tecnico goffo: l'esperienza con le persone gli permette di capirle. Il **primo incontro informale e gratuito** (di persona se serve) serve a mostrare questo prima di qualsiasi preventivo.
- **Posizionamento dichiarato da Matia:** rapporto umano, il cliente non e' un numero, specialmente all'inizio. Il valore aggiunto e' l'empatia nel capire i pain point e il progettare soluzioni custom e ad-hoc per ogni cliente. E' cio' che lo differenzia dagli altri. Il brand e il tono di ogni comunicazione devono riflettere questo.
- **Livello di qualita' richiesto da Matia (2026-10-08):** marchio, impaginazione e materiali semplici da leggere e da interpretare, ma di qualita' estremamente bella e raffinata, fatti bene. Ne' troppo tecnico (come Battistini) ne' fermo nel tempo (come Vincenzi): moderno, chiaro, con una persona vera dietro.
- **Automazione come metodo di lavoro:** Matia vuole automatizzare controlli, rapporti, messaggi e gestione clienti, con AI. Lui rivede e decide, l'automazione prepara. Si costruisce insieme al sito (`docs/PROCEDURE.md`, `docs/MODELLO-CHECKUP.md`).
- Sito proprio come primo biglietto da visita
- Canali: rete personale, LinkedIn, referral, outreach, contenuti
- Primo cliente: chi, come, a che condizioni

## 8. Regole di lavoro con Matia

Preferenze emerse nelle sessioni precedenti e valide anche qui:

- **Lingua:** italiano.
- **Trattini:** nei testi usare solo il trattino corto (-), mai quello lungo.
- **Documenti e proposte:** impostarli come proposte.
- **Requisiti:** quando Matia dichiara un requisito, si esegue. Se ha un costo, lo si esegue e lo si dice, non lo si negozia.
- **Regole generali, non pezze:** davanti a un difetto segnalato, risolvere con una regola valida sempre, non con un ritocco puntuale.
- **Link:** ogni passo operativo porta con se' il link completo e apribile.
- **Aggiornare, non riscrivere:** se esiste gia' un documento o una decisione sull'argomento, si aggiorna quello.
- **Memoria:** le informazioni ricorrenti di questo progetto si scrivono qui, nel momento in cui emergono.
- **Standard:** lavorare da professionisti, in modo efficiente, con consegne di qualita' molto alta.

## 9. Come ci organizziamo

Il progetto si tiene come un repository: una struttura di file chiara, aggiornata nel momento in cui emerge un'informazione, cosi' il contesto puo' crescere senza perdersi. Matia lo ha chiesto esplicitamente (2026-10-07). Struttura approvata e creata:

- `CLAUDE.md` - questo file: regole, profilo, fatti stabili
- `README.md` - mappa della cartella
- `docs/STATO-DEI-LAVORI.md` - dove siamo
- `docs/BACKLOG.md` - decisioni aperte e cose da fare
- `docs/DECISIONI.md` - scelte prese e perche'
- `docs/PROCEDURE.md` - come si fanno le cose ricorrenti, percorso del cliente
- `docs/OFFERTE.md`, `docs/RICERCA-DI-MERCATO.md`, `docs/CONCORRENTI.md`, `docs/PRIMO-INCONTRO.md`, `docs/MODELLO-CHECKUP.md` - contenuti di lavoro
- da creare quando servono: `clienti/<nome>/`, `marketing/`, `archivio/`

**Dove va ogni informazione:** fatti stabili e regole di lavoro in questo file; scelte in `docs/DECISIONI.md`; stato e prossimi passi in `docs/STATO-DEI-LAVORI.md`; cose da fare in `docs/BACKLOG.md`; contenuti nei file dedicati. Non si duplica: ogni cosa vive in un posto solo e gli altri file rimandano.

## 10. Registro delle decisioni

Spostato in `docs/DECISIONI.md`.
