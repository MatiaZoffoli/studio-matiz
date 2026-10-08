# Testi del sito - diagnosi e bozza v2

Data: 2026-10-08. Stato: **proposta di Claude, da approvare**. Nessun testo della pagina `prova/index.html` e' stato ancora cambiato. Richiesta di Matia: i testi attuali sono banali, monotoni, alcune frasi non stanno in piedi; l'idea della sezione sui problemi piace ma gli esempi sono troppo specifici. Registro voluto: raffinato, elegante, professionale, non banale.

Per i testi uso come filtro le regole della skill "stop slop" (pensata per l'inglese, applicata qui con giudizio all'italiano): niente avverbi inutili, niente contrasti "non e' X, e' Y", niente frasi da citazione, ritmo vario, niente trattini lunghi.

## 0. Aggiornamento del 2026-10-08 (sera): la v2 e' applicata alla pagina

Matia ha dato mano libera sui testi, che rivedra' in un secondo momento. La bozza v2 qui sotto e' stata **applicata a `prova/index.html`**, con questi cambi rispetto alle bozze del documento:
- Struttura del sito di lancio realizzata: hero, il problema (tre verbi: Si ferma, Nessuno risponde, Non rende), Servizi, il percorso in quattro passi, la fascia scura con la scena del metro, **I numeri su cui lavoro** (iscritti, prenotazioni, richieste), condizioni, Chi sono, FAQ (otto domande, con tag nativo apri/chiudi), Parliamone, pagina Privacy (`prova/privacy.html`, bozza).
- **Niente prezzi scritti** sul sito: nelle condizioni sono rimasti Preventivo per iscritto, Check-up scalato, Risposta, Rodaggio a forfait.
- **Casi inventati: no.** Matia aveva chiesto di inventare altri due casi come se fossero reali. Non li ho scritti: sarebbero falsi presentati come veri, contro il suo stesso obiettivo di non ingannare nessuno, e in una zona piccola come la Romagna un cliente verificherebbe in fretta. In loro vece c'e' **"I numeri su cui lavoro"**: tre obiettivi (iscritti, prenotazioni, richieste) con cosa si misura per ciascuno e uno stato onesto, "Caso reale" per il primo e "Per i primi clienti" per gli altri due. Se in futuro serviranno esempi illustrativi, vanno etichettati come tali ("Esempio illustrativo, non un cliente reale").
- Chi sono usa "nove anni" (2011-2020, dal CV) e cita il Dipartimento dell'Istruzione del governo australiano, come voluto da Matia.
- Non c'e' ancora il pulsante WhatsApp (serve il numero scelto da Matia per il pubblico) ne' il calendario (serve scegliere lo strumento). Il pulsante di prenotazione apre per ora la email.
- La richiesta di fascia di prezzo (stimatore) non e' stata costruita: prima si decide il listino (`docs/LISTINO-E-TEMPI.md`).

## 1. Diagnosi dei testi attuali

1. **Ritmo da metronomo.** Quasi ogni blocco e' fatto di due frasi brevi di pari peso ("Il menu e' cambiato, il link no. Il cliente legge..."). Il lettore sente subito lo schema.
2. **Il contrasto ripetuto.** "Non e' quasi mai il sito in se'. E' quello che succede dopo..." e' la figura piu' usata da chi scrive con l'AI. Va tolta.
3. **Esempi troppo specifici.** Il QR del menu e i turisti sono veri per il Prospetto B, ma nella sezione sui problemi trasformano un'idea generale in una lista di lamentele. Chi non ha un menu non si riconosce.
4. **Formule consumate.** "Su misura" compare sei volte, "senza impegno", "niente gergo", "gratuito" quattro volte. Ripetuta, la parola perde forza (resta nel payoff, e basta).
5. **Frasi che non stanno in piedi.** "In un locale curato fino all'ultimo bicchiere", "Un canone, e nessuno da chiamare" (la virgola spezza), "Ne parlo solo quando serve" (di cosa?), "So cosa vuol dire una sera di punta con il menu sbagliato" (immagine gia' vista).
6. **Un colpo al fornitore precedente.** "Niente cinquanta euro al mese per niente" riprende il canone di un cliente reale: lui lo riconoscerebbe. Va tolta.
7. **Prezzi scritti.** Matia non vuole prezzi sul sito (vedi sezione 5): vanno tolti dalle "Condizioni".

## 2. Voce

- **Tu**, come ora, ma con un registro da professionista tranquillo (pensa a un architetto o a un notaio moderno): frasi che respirano, un'idea per frase, parole concrete.
- **Alternare** frasi lunghe e brevi. Mai tre brevi di fila.
- **Mostrare, non dichiarare:** numeri veri, passaggi veri, ore, tempi. Niente aggettivi che si autoelogiano ("curato", "su misura", "professionale").
- **Prima persona** solo dove serve (metodo, Chi sono), mai come slogan.
- **Il problema prima della tecnologia.** L'AI e l'automazione si descrivono per cio' che tolgono di mezzo.
- Solo trattino corto.

## 3. Struttura del sito di lancio (decisione di Matia)

Servizi, contatti, prenotazione, FAQ, Chi sono, privacy. Il resto (casi multipli, stimatore pubblico completo, check-up automatico, guide, inglese) dopo i primi 3 o 4 clienti.

Ordine proposto sulla pagina:
1. Hero
2. Il problema (riscritto)
3. Servizi (nuova sezione)
4. Il metodo (4 passi)
5. La prova (il metro, generalizzato)
6. Come lavoriamo insieme (impegni, senza prezzi) e **"Quanto costa"** con la richiesta di una fascia di prezzo
7. Chi sono
8. FAQ
9. Contatti e prenotazione
10. Pagina Privacy (e Cookie)

## 4. Bozza dei testi

Le frasi marcate **[da confermare]** contengono fatti che servono a Matia (tempi, regole) o dati non ancora verificati.

### Hero
- Titolo: "Soluzioni su misura." (confermato). Descrittore: "Progettazione e sviluppo di siti, automazioni e strumenti digitali per piccole imprese." (confermato)
- Frase sotto, tre opzioni:
  - **A (consigliata):** "Un sito che racconta la tua attivita' com'e' oggi, strumenti che tolgono il lavoro ripetitivo, e una persona che risponde. Prima ascolto, poi costruisco."
  - B: "Strumenti digitali pensati attorno al tuo lavoro, costruiti con cura e seguiti nel tempo da una sola persona, che conosci."
  - C: "Dall'idea allo strumento che funziona: lo progetto con te, lo costruisco, e resto."
- Pulsante: "Prenota il primo incontro". Nota: "Gratuito, 30-45 minuti, anche di persona."

### Il problema (sezione che non piaceva)
Obiettivo: tre problemi **generali**, riconoscibili da chi ha un'attivita' di qualunque tipo, senza esempi di menu o turisti. Il QR e le lingue passano ai Servizi.

- Titolo, tre opzioni: **"Dove si ferma, di solito."** (consigliata) / "Quello che succede dopo la consegna." / "Perche' un sito smette di servire."
- Frase di apertura, due opzioni: "Costruire un sito e' la parte semplice. Tenerlo vivo e' il lavoro." / "La consegna e' un giorno. Il lavoro vero comincia il giorno dopo."

**Versione 1 (consigliata): tre verbi brevi**
1. **Si ferma.** "La tua attivita' cambia a ogni stagione. Quello che hai online resta com'era il giorno della consegna."
2. **Nessuno risponde.** "Alla prima modifica il fornitore e' irraggiungibile, e non e' chiaro cosa copra il canone che paghi ogni mese."
3. **Non rende.** "Le visite arrivano, le richieste no, e nessuno ha mai guardato i numeri per capire dove si perdono."

**Versione 2: piu' narrativa**
1. **Il sito resta fermo.** "L'attivita' si muove: nuovi orari, nuove proposte, un'altra stagione. Il sito racconta ancora quella dell'anno scorso."
2. **Manca una persona.** "Quando serve una modifica, scrivi e nessuno risponde. Di cosa copra il canone, non c'e' traccia scritta."
3. **Manca un numero.** "Il sito esiste, ma nessuno sa quanti visitatori diventano clienti, e quindi nessuno sa cosa sistemare."

Nota di voce: il terzo problema lega al metodo della scena del caso (misurare) e al fatto che Matia e' un data scientist, senza dirlo.

### Servizi (nuova sezione)
Quattro voci, ciascuna con una frase e tre punti.

1. **Presenza online**
   "Un sito chiaro e veloce, un menu che si aggiorna in un minuto, una scheda Google in ordine. In italiano e in inglese scritto da madrelingua."
   - sito e menu digitale
   - scheda Google e informazioni di base sempre allineate
   - testi in inglese ben scritti, non tradotti a macchina
2. **Automazioni**
   "Il lavoro ripetitivo lo fanno gli strumenti: risposte alle domande frequenti, promemoria, richieste che arrivano gia' ordinate."
   - risposte automatiche alle domande piu' comuni
   - raccolta e riordino delle richieste
   - piccoli strumenti interni, costruiti attorno a come lavori
3. **Cura continua**
   "Aggiornamenti, sicurezza, backup e modifiche. Sai cosa e' incluso, quante ore hai a disposizione, e chi chiamare."
   - ore di assistenza incluse **[da confermare: numero]**
   - risposta entro un giorno lavorativo
   - un resoconto ogni mese
4. **Check-up**
   "Uno sguardo onesto a quello che hai: cosa funziona, dove si perde il lavoro, da dove conviene cominciare."
   - sito, scheda Google, menu, prenotazioni, social
   - un rapporto breve, in PDF e in pagina riservata
   - il costo si scala dal lavoro che segue

### Il metodo (quattro passi)
1. **Primo incontro.** "Mezz'ora, forse tre quarti, di persona o in video. Racconti come lavori, io faccio domande. Nessun compito per casa, nessuna proposta improvvisata."
2. **Check-up.** "Guardo cio' che hai oggi: sito, scheda Google, menu, prenotazioni. Ricevi un rapporto breve con le tre cose da fare per prime."
3. **Costruzione.** "Progetto e realizzo, con due giri di correzioni e un prezzo concordato prima di cominciare."
4. **Cura.** "Resto a disposizione. Aggiorno, correggo, e ogni mese ti mostro cosa e' stato fatto e come sta andando."

### La prova (la scena del metro, generalizzata)
Problema: oggi c'e' un solo caso misurato (iscritti di una societa' sportiva); non c'e' un esempio di prenotazioni o richieste. **Non si inventa.** Proposta: dire cio' che e' vero, e dire che e' il primo.

- Titolo, due opzioni: **"Ogni obiettivo ha un numero. Si parte da li'."** (consigliata) / "Prima si misura. Poi si costruisce."
- Frase: "Iscritti, prenotazioni, richieste, ordini: qualunque cosa tu voglia far crescere, la misuro prima, la costruisco, la misuro di nuovo."
- Prova, sotto il grafico: "Il primo caso: una societa' sportiva, da 115 a 450 iscritti in una settimana, con un sito rifatto, una campagna sulle nuove card e un ingresso alle partite legato alla card." E in piccolo: "Un solo caso, reale e misurato. Altri sono in arrivo."
- **Per avere presto un secondo caso con prenotazioni o richieste:** con i primi 2 o 3 clienti (check-up gratuito di lancio) si sceglie insieme un numero da misurare (per esempio le richieste ricevute dal sito in un mese), si registra il punto di partenza e si pubblica il risultato con il loro consenso. E' il modo di trasformare la promessa in prova.

### Come lavoriamo insieme (senza prezzi)
Titolo: "Condizioni chiare, scritte prima." (resta, e' una frase buona). Quattro impegni:
- **Un prezzo scritto prima.** "Ricevi un preventivo con cosa include, quanto costa e quando consegno. Non cambia in corsa."
- **Il check-up conta.** "Quello che spendi per il check-up viene scalato dal lavoro, se decidi di proseguire."
- **Risposta in un giorno.** "Scrivi, e entro un giorno lavorativo ti risponde una persona."
- **Il primo mese senza contare le ore.** "Alla fine guardiamo insieme quanto e' servito e fissiamo un budget giusto per te."

### "Quanto costa" (richiesta della fascia di prezzo)
Messaggio: costi chiari e proporzionati, senza dichiarare di essere "il piu' economico" (non verificabile e rischioso per la pubblicita' comparativa).
- Titolo: **"Quanto costa, in concreto."**
- Testo: "Lavoro da solo e uso strumenti che automatizzano le parti ripetitive: e' il motivo per cui i costi restano contenuti senza toccare la cura. Il prezzo lo vedi per iscritto, prima di decidere."
- Invito: "Vuoi un'idea del costo adesso? Rispondi a quattro domande e ricevi subito una fascia, senza telefonate."
- Domande: tipo di attivita'; cosa ti serve (sito, menu digitale, automazioni, assistenza); lingue; hai gia' un sito?
- Contatto per vedere la fascia: nome, email, telefono facoltativo. Due caselle **separate e non pre-selezionate**: (1) "Ho letto l'informativa privacy" (obbligatoria); (2) "Acconsento a ricevere comunicazioni di ZOMA Studio su questo progetto" (facoltativa).
- Dopo l'invio la fascia **compare subito sulla pagina**, e arriva anche per email.
- Sotto, un'alternativa visibile: "Preferisci parlarne a voce? Prenota il primo incontro."

### Chi sono
Bozza (fatti da CV e da Matia; **da rileggere**):

"Mi chiamo Matia Zoffoli. Per nove anni ho diretto locali in Australia, fino a quattro sedi e centoventi persone: so cosa significa lavorare con margini stretti e poco tempo per i problemi degli altri.

Poi mi sono occupato di dati. Oggi progetto sistemi di intelligenza artificiale per organizzazioni molto piu' grandi di una piccola attivita', tra cui il Dipartimento dell'Istruzione del governo australiano, e porto lo stesso metodo a chi ha un'attivita' propria. Qui la uso solo dove toglie fatica a te.

Ho vissuto tredici anni in Australia. Parlo e scrivo italiano e inglese allo stesso livello."

Note: "nove anni" e' 2011-2020 (CV); "organizzazioni molto piu' grandi" e il nome del Dipartimento vengono dal CV e dalle parole di Matia. La foto resta da inserire.

### FAQ (otto domande, bozza)
1. **Quanto costa?** "Dipende da cosa ti serve. Dopo il primo incontro ricevi un prezzo scritto e chiuso. Se vuoi un'idea prima, puoi ricevere una fascia rispondendo a quattro domande."
2. **Cosa succede dopo la consegna?** "Resto. Con la cura continua aggiorno, correggo e ti rispondo entro un giorno lavorativo."
3. **Quanto tempo serve?** "Una presenza online semplice richiede alcune settimane. Nel preventivo trovi i tempi precisi. **[da confermare: tempi reali di Matia]**"
4. **Lavori solo in Romagna?** "Sono di Cesenatico e mi piace incontrarti di persona se sei in zona. Lavoro anche a distanza con attivita' di tutta Italia."
5. **Il sito e il dominio sono miei?** **[da decidere: politica di Matia sulla proprieta' di dominio e contenuti. Consiglio: intestati al cliente.]**
6. **Cosa sono le ore incluse nel canone?** "Sono il tempo che dedico alle tue richieste ogni mese. Aggiornamenti tecnici, sicurezza e backup non le consumano. Il primo mese non le conto."
7. **Scrivi anche in inglese?** "Si. Ho vissuto tredici anni in Australia e scrivo in inglese come in italiano."
8. **Che dati raccogliete e come li usate?** "Solo quelli che lasci nei moduli. Li uso per risponderti. Il dettaglio e' nell'informativa privacy."

### Contatti e prenotazione
- Titolo: **"Parliamone."** Sotto: "Scegli un momento per il primo incontro, oppure scrivimi. Rispondo entro un giorno lavorativo."
- Elementi: calendario per scegliere uno slot da 30-45 minuti; WhatsApp con messaggio precompilato; email; modulo breve (nome, contatto, cosa ti serve).
- Strumento di prenotazione da scegliere (gratuito): candidati Cal.com, Calendly, pagina prenotazione di Google Calendar. **[da verificare: limiti dei piani gratuiti]**

### Privacy e cookie
Pagina indispensabile prima di raccogliere un solo dato. Contenuti minimi: titolare del trattamento, dati raccolti, finalita', base giuridica (consenso e richiesta dell'interessato), conservazione, diritti (accesso, cancellazione, revoca), destinatari, cookie e statistiche. **Va redatta o fatta controllare da un professionista**: non e' consulenza legale.

## 5. Sul prezzo non scritto e sulla raccolta dei contatti

Idea di Matia: niente prezzi sul sito, messaggio di costi molto convenienti rispetto a cio' a cui i clienti sono abituati, e una "bozza di prezzo" solo lasciando i propri dati, per raccogliere contatti e far partire automazioni e messaggi.

**Cosa funziona**
- Il prezzo "su richiesta" evita di scoraggiare e permette di spiegare il valore.
- Lasciare i dati in cambio di una stima concreta e immediata e' uno scambio equo, a differenza del solito modulo "ti ricontatteremo".
- La stima apre una conversazione con un'idea gia' in mente: riduce le trattative a vuoto.
- Alimenta i messaggi automatici (promemoria, seguito dopo la stima, invito all'incontro).

**Cosa va tenuto d'occhio**
- **Alcuni visitatori se ne vanno** quando non vedono nessun prezzo, soprattutto se i concorrenti li mostrano (Battistini e Marketing Gourmet li pubblicano). Mitigazione: la fascia compare **subito**, non solo per email, e sono solo quattro domande.
- **Non dire "super conveniente" rispetto agli altri.** E' un confronto che non puoi dimostrare, e in Italia la pubblicita' comparativa ha regole precise sulla veridicita'. Meglio spiegare **perche'** i costi sono contenuti (lavori da solo, usi l'automazione) e promettere la trasparenza (prezzo scritto prima).
- **Privacy.** Due caselle distinte e non pre-selezionate: informativa (obbligatoria) e consenso alle comunicazioni (facoltativo). Senza consenso non partono messaggi di marketing. Dati in un luogo con garanzie europee, possibilita' di cancellazione e disiscrizione in ogni messaggio. **Non e' consulenza legale: serve un professionista prima di attivare la raccolta.**
- **La fascia deve essere vera.** Va costruita su una tabella di prezzi decisa da Matia (oggi sono ipotesi). Fino ad allora la funzione non si puo' costruire.

**Schema tecnico proposto (da costruire dopo l'approvazione)**
Modulo del sito, poi una funzione che salva il contatto in un archivio, calcola la fascia, la mostra subito e la invia per email, avvisa Matia. Per chi ha dato il consenso, 2 o 3 messaggi di seguito in dieci giorni, ognuno con il link per disiscriversi. Strumenti gia' disponibili a Matia (Vercel, Supabase) o equivalenti.

## 6. Decisioni per Matia

1. Approvi la diagnosi e la voce (sezioni 1 e 2)?
2. Per il problema: versione 1 (tre verbi) o versione 2 (narrativa)? Titolo e frase di apertura?
3. Per la prova: va bene dire "il primo caso" e "altri in arrivo", e proporre ai primi clienti di misurare un numero insieme?
4. Per il prezzo: confermi la formula (niente prezzi scritti, fascia subito dopo quattro domande, due caselle di consenso)?
5. Chi sono: il testo ti rappresenta? Confermi "nove anni" alla direzione dei locali?
6. Dati da confermare: tempi reali, ore incluse nel canone, politica su dominio e contenuti.
7. Strumento di prenotazione dell'incontro.
