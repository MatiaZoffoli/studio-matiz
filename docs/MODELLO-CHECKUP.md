# Check-up digitale - modello

Stato: **bozza di Claude, da correggere con Matia**. Aggiornata il 2026-10-07.

Questo file ha due parti: la **procedura** (come si esegue il check-up, per Matia) e il **modello del rapporto** (cosa riceve il cliente). La checklist deriva dai difetti piu' ricorrenti emersi in `docs/CONCORRENTI.md`, sezione 5.

## Parte 1 - Procedura

**Tempo previsto:** circa 1 ora di visita (se on-site) piu' circa 3 ore di preparazione e stesura. Da misurare sui primi casi e correggere.

**Prima della visita**
1. Compilare la checklist sotto, per la parte che si controlla da fuori: sito, menu, Google, social.
2. Eseguire i controlli tecnici con strumenti gratuiti:
   - velocita' e mobile: [PageSpeed Insights](https://pagespeed.web.dev/)
   - sicurezza del certificato: aprire il sito e verificare il lucchetto (HTTPS), oppure [SSL Labs](https://www.ssllabs.com/ssltest/)
   - scheda Google: cercare il nome del locale su Google e su Google Maps, da telefono
   - ricerca locale: cercare 3 frasi che userebbe un cliente (per esempio "ristorante di pesce Cesenatico", "bagno con ristorante Cervia") e annotare dove compare il locale
3. Fare screenshot di quanto osservato, da mettere nel rapporto.

**Durante la visita**
- Guardare con il titolare il sito e il menu **dal suo telefono**, come un cliente.
- Chiedere cosa fa a mano ogni giorno e cosa vorrebbe risolvere: e' la parte che apre le possibilita' di automazione.
- Non dare soluzioni complete a voce: stanno nel rapporto.

**Dopo la visita**
- Compilare il rapporto, scrivere la proposta, consegnare entro 3-5 giorni lavorativi.
- Salvare tutto in `clienti/<nome-cliente>/checkup.md`.

**Tono del rapporto**
- Linguaggio semplice, nessun gergo. Ogni problema spiegato come lo vive un cliente del locale.
- Mai giudicare il lavoro dei fornitori precedenti. Si descrive lo stato attuale e cosa conviene fare.
- Sempre qualcosa di positivo da dire: ogni locale ha qualcosa che funziona.
- Pochi punti chiari, in ordine di importanza. Meglio 3 cose fatte bene che 20 elencate.

## Parte 2 - Modello del rapporto

Il rapporto consegnato al cliente segue questa struttura. Va tenuto breve: 4-6 pagine.

### Pagina 1 - In sintesi

- Nome del locale, data, chi ha fatto il check-up
- **Cosa funziona** (2-3 punti)
- **Le tre cose da fare per prime**, ciascuna con una frase su perche' conta per i clienti
- Valutazione generale con un semaforo: verde (a posto), giallo (migliorabile), rosso (da sistemare), per ciascuna area sotto

### Pagina 2-4 - Checklist

Per ogni voce: **esito** (verde, giallo, rosso, non verificato) e una nota breve. La colonna "perche' conta" e' per Matia, nel rapporto va tradotta in linguaggio da cliente.

| Area | Cosa si controlla | Perche' conta |
|---|---|---|
| **Lingue** | Il sito esiste in italiano, inglese e, in zona turistica, tedesco | Meta' dei clienti in alta stagione non e' italiana |
| **Orari e contatti** | Orari chiari in home e aggiornati, telefono cliccabile da telefono, WhatsApp, indirizzo, mappa incorporata | Chi cerca "aperto adesso" deve trovare la risposta in pochi secondi |
| **Menu** | Leggibile da telefono come pagina web e non solo PDF, con prezzi, con data o stagione, QR che porta alla versione aggiornata, versione stampabile coerente | E' il difetto piu' frequente e il piu' visibile ai clienti |
| **Prenotazione** | Si puo' prenotare un tavolo o un servizio online o con un solo tocco (telefono, WhatsApp, modulo), non solo chiamando | Meno telefonate, piu' prenotazioni anche fuori orario |
| **Mobile e velocita'** | Il sito si legge bene su telefono e carica in pochi secondi (punteggio PageSpeed) | La maggioranza dei visitatori arriva da telefono |
| **Contenuti aggiornati** | Niente offerte scadute, copyright corrente, stagione giusta, nessuna sezione vuota, nessun link o immagine rotta | Un sito trascurato fa pensare a un locale trascurato |
| **Sicurezza e manutenzione** | HTTPS attivo, sito e plugin aggiornati, backup attivi, chi se ne occupa | Un sito non aggiornato rischia di bloccarsi o essere violato |
| **Ricerca locale (SEO)** | Il locale compare cercando le frasi dei clienti; titoli e descrizioni delle pagine; scheda Google completa e con foto, orari, categoria, recensioni gestite; coerenza di nome, indirizzo e telefono ovunque | Chi cerca "dove mangiare a..." deve trovarvi prima degli altri |
| **Social** | Profili attivi e collegati al sito, foto coerenti con lo stile del locale | Il cliente guarda Instagram prima di venire |
| **Immagine e coerenza** | Il sito e il menu sono all'altezza del locale reale (qualita' foto, stile, tono) | Chi spende molto vuole trovare la stessa cura anche online |
| **Dipendenze** | Su quali piattaforme esterne si appoggia (gestionale, widget prenotazioni) e a chi appartengono dominio e sito | Chi controlla il dominio controlla la presenza online |

### Pagina 5 - Dove si perde tempo (automazione)

Nasce dalla chiacchierata, non dai controlli. Elenco di cose che il titolare fa a mano e che si potrebbero semplificare, con stima di tempo risparmiato e difficolta'. Esempi:

- risposte alle stesse domande ricorrenti (orari, menu, prenotazioni)
- aggiornamento del menu in piu' posti
- raccolta e risposta alle recensioni
- gestione di prenotazioni, ordini, turni o scorte

Si descrive il problema, non la tecnologia. Non si propone AI se non serve.

### Pagina 6 - Piano d'azione e proposta

Tabella delle azioni, in ordine di priorita':

| Azione | Impatto (alto/medio/basso) | Sforzo (ore stimate) | Chi la fa |
|---|---|---|---|
| ... | ... | ... | Matia / cliente |

Poi una proposta chiara:
- cosa conviene fare per prima, con prezzo e tempi
- cosa conviene tenere per dopo
- **sconto del check-up**: come e' stato definito (formula scelta in `docs/OFFERTE.md`) e fino a quando vale
- la proposta di assistenza continuativa, spiegata con cosa include

## Regole per i prezzi nel rapporto

- Ogni voce della proposta ha un prezzo e un tempo, mai "a preventivo" senza dire quando arriva.
- Il prezzo del check-up e lo sconto sul progetto stanno scritti nella proposta, non solo a voce.
- Se il cliente non prosegue, il rapporto resta suo.

## Automazione del check-up (decisione di Matia, 2026-10-08)

Matia vuole automatizzare i controlli prima della visita e la stesura del rapporto. Lui rivede e decide sempre: l'automazione prepara, non consegna da sola al cliente.

**Si automatizza bene** (strumenti gratuiti o a basso costo):
- velocita' e punteggio mobile, con l'interfaccia di PageSpeed Insights
- HTTPS e certificato
- lettura delle pagine: lingue dichiarate, titoli e descrizioni, presenza di telefono cliccabile, mappa incorporata, anno del copyright, menu in PDF, link rotti e immagini mancanti
- screenshot del sito su telefono e computer
- bozza dell'esito di ogni voce della checklist, scritta da un assistente AI sulla base di quanto raccolto

**Semi-automatico** (serve un controllo di Matia):
- scheda Google e ricerca locale: ci sono strumenti a pagamento per le posizioni sui risultati, ma all'inizio si guarda a mano da telefono, e' veloce
- giudizio su coerenza di immagine, qualita' delle foto, tono dei testi: la bozza AI la scrive, Matia la corregge

**Durante la visita:** Matia annota a voce o in note rapide sul telefono. Le note vengono trascritte e trasformate in elenco di problemi e opportunita' da inserire nel rapporto.

**Uscita:** dallo stesso contenuto si generano **due formati**, scelta di Matia:
- **PDF stampabile**, da portare e lasciare sul tavolo, con spazio per annotare
- **pagina web riservata** con link privato, piu' moderna e che mostra il mestiere

**Impaginazione e marchio:** semplici da leggere e da interpretare, ma molto belli e raffinati, fatti bene (richiesta di Matia). Si decidono insieme al brand.

**Quando costruirlo:** quando c'e' il brand e il sito. Per i primissimi check-up (gratuiti, amici e conoscenti) si puo' partire con la checklist compilata a mano e un modello di PDF semplice, e costruire l'automazione mentre si fanno i primi casi, cosi' si costruisce quello che serve davvero.

## Cosa comporta la SEO nel check-up

La SEO locale e' il lavoro che fa comparire un locale quando qualcuno cerca "dove mangiare a Cesenatico" o "bagno con ristorante Cervia". Nel check-up si **controlla soltanto**, non si fa:

- la scheda Google (nome, categoria, orari, foto, recensioni con risposta)
- se nome, indirizzo e telefono sono uguali ovunque (sito, Google, social, portali)
- se il sito contiene le parole che usa il cliente, in titoli e testi
- velocita' e adattamento a telefono, che Google considera
- se il sito e' sicuro (HTTPS)

I controlli sono in buona parte automatizzabili. **Farla**, cioe' correggere, scrivere i testi giusti, ottenere recensioni, e' un servizio a parte (parte del progetto o del canone). Nel check-up basta dire cosa manca e quanto conta.

## Cose da decidere

- Il marchio e l'aspetto grafico del rapporto, insieme al brand.
- Quanto si approfondisce la SEO nel check-up base e quando diventa un servizio a parte: ipotesi di Claude, la SEO nel check-up e' solo controllo, farla e' lavoro da progetto o da canone.
