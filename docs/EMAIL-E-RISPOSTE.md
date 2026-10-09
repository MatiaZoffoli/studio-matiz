# Email, risposte automatiche e messaggi

Data: 2026-10-09. Stato: **bozza nella voce di Studio Matiz** (skill `.claude/skills/voce-studio-matiz`), da rivedere da Matia. I testi si usano così come sono, oppure si copiano nello strumento di invio quando sarà collegato (vedi in fondo).

**Regole di voce per le comunicazioni dirette:** si dà del **tu**, tono preciso, una cosa per messaggio, un numero o un fatto per riga, firma. Le **risposte automatiche** si dichiarano per quello che sono e firmano come Studio Matiz, mai come Matia in tempo reale. Niente punti esclamativi, niente "gratuito", niente "contattaci". I campi tra doppie graffe sono variabili: `{{nome}}`, `{{tipo}}`, `{{servizi}}`, `{{prezzo}}`, `{{tempo}}`, `{{link_calendario}}`.

Indice: A. dal sito (automatiche) · B. scritte da Matia lungo il percorso · C. WhatsApp · D. Come si collegano · E. Controllo prima di inviare.

---

## A. Dal sito (automatiche)

### A1. Conferma dello stimatore (al cliente, subito)

**Oggetto:** Richiesta ricevuta: il prezzo di partenza per {{tipo}}

> Ciao {{nome}},
>
> questa è una risposta automatica: la richiesta è arrivata, e Matia risponde di persona entro un giorno lavorativo.
>
> Il riepilogo di quanto indicato:
> - Attività: {{tipo}}
> - Cosa serve: {{servizi}}
> - Prezzo di partenza: da {{prezzo}} euro
> - Tempo di consegna indicativo: {{tempo}}
>
> È un punto di partenza, non un preventivo: il prezzo vero viene scritto dopo il primo incontro e non cambia in corsa. IVA se dovuta.
>
> Il primo incontro dura un'ora, di persona o in video, ed è offerto dallo studio. Si prenota da qui: {{link_calendario}}. In alternativa basta rispondere a questa email.
>
> Studio Matiz, di Matia Zoffoli
> Cesenatico · +39 333 958 0381

### A2. Notifica interna (a Matia, per ogni richiesta)

**Oggetto:** Nuova richiesta: {{tipo}}, da {{prezzo}} euro

> {{nome}} ha chiesto un prezzo di partenza.
>
> - Email: {{email}} · Telefono: {{telefono}}
> - Attività: {{tipo}} · Presenza online oggi: {{presenza}}
> - Cosa serve: {{servizi}} · Dimensione: {{dimensione}}
> - Prezzo di partenza mostrato: da {{prezzo}} euro (tetto interno: {{prezzo_fino_a}} euro)
> - Compilata in {{secondi}} secondi, alle {{ora}}
>
> Da fare: rispondere entro {{scadenza}} (un giorno lavorativo) e proporre il primo incontro.

### A3. Risposta automatica di assenza (email)

**Oggetto:** Messaggio ricevuto

> Ciao,
>
> questa è una risposta automatica. Il messaggio è arrivato e Matia risponde entro un giorno lavorativo. Nei giorni di chiusura la risposta arriva il primo giorno utile.
>
> Se la richiesta non può aspettare, un messaggio su WhatsApp (+39 333 958 0381) è il canale più rapido.
>
> Studio Matiz, di Matia Zoffoli

### A4. Conferma del primo incontro (dopo la prenotazione sul calendario)

**Oggetto:** Primo incontro: {{giorno}} alle {{ora}}

> Ciao {{nome}},
>
> il primo incontro è fissato per {{giorno}} alle {{ora}}, per un'ora, {{luogo_o_link}}.
>
> Non serve preparare niente. Aiuta avere sotto mano tre cose: l'indirizzo del sito o dei profili che già esistono, un esempio di giornata tipica di lavoro e un numero che si vorrebbe migliorare (richieste, prenotazioni, iscritti, ore perse).
>
> Se serve spostare l'incontro, basta rispondere a questa email.
>
> Studio Matiz, di Matia Zoffoli

### A5. Promemoria del giorno prima (automatico)

**Oggetto:** Domani alle {{ora}}: primo incontro

> Ciao {{nome}}, un promemoria: domani alle {{ora}} c'è il primo incontro, {{luogo_o_link}}. Un'ora, senza compiti da fare prima.
>
> Studio Matiz

---

## B. Scritte da Matia lungo il percorso

### B1. Dopo il primo incontro: riepilogo e passo successivo

**Oggetto:** Dopo l'incontro: i numeri di partenza e il passo successivo

> Ciao {{nome}},
>
> grazie per l'ora di ieri. In sintesi, quello che è emerso:
> - Dove si perde tempo: {{punto_1}}
> - Il numero da misurare: {{numero}}, da cui si parte oggi con {{valore_di_partenza}}
> - Cosa conviene fare per primo: {{priorita}}
>
> Il passo successivo può essere un check-up (200 euro, scalati dal lavoro che segue; rapporto in tre giorni lavorativi) oppure direttamente un preventivo scritto, se la direzione è già chiara. Dimmi quale preferisci.
>
> Matia

### B2. Invio del check-up

**Oggetto:** Check-up di {{attività}}: tre priorità

> Ciao {{nome}},
>
> in allegato il rapporto del check-up, anche nella pagina riservata: {{link}}.
>
> In breve: tre cose da fare per prime, con il costo di ciascuna, in ordine di effetto sul numero scelto ({{numero}}). Il costo del check-up ({{importo}} euro) viene scalato dal lavoro che segue, con lo sconto previsto dalla data di conferma.
>
> Se si vuole procedere, il preventivo scritto arriva entro tre giorni lavorativi dalla risposta.
>
> Matia

### B3. Invio del preventivo

**Oggetto:** Preventivo n. {{numero}} per {{attività}}

> Ciao {{nome}},
>
> in allegato il preventivo n. {{numero}} e l'accordo di servizio. Il prezzo è chiuso, il tempo di consegna parte dal momento in cui arriva tutto il materiale, e due giri di correzioni sono compresi.
>
> Per accettare basta rispondere «Accetto», o firmare l'ultima pagina. Il preventivo vale fino al {{scadenza}}.
>
> Matia

### B4. Promemoria gentile sul preventivo (dopo sette giorni)

**Oggetto:** Preventivo n. {{numero}}: valido fino al {{scadenza}}

> Ciao {{nome}},
>
> un promemoria sul preventivo n. {{numero}}, valido fino al {{scadenza}}. Se qualcosa non torna, un dubbio sul prezzo o sui tempi, la risposta arriva entro un giorno lavorativo. Se il momento non è questo, nessun problema: il materiale resta, e si riprende quando serve.
>
> Matia

### B5. Benvenuto dopo l'accettazione

**Oggetto:** Si parte: cosa serve e le prime date

> Ciao {{nome}},
>
> grazie per la fiducia. Questa è la sequenza:
> - Entro {{data_1}}: il materiale necessario ({{elenco_materiale}}) e gli accessi.
> - Da quando arriva tutto: {{tempo}} per la consegna, con un aggiornamento a metà lavoro.
> - Alla consegna: due giri di correzioni, e subito dopo parte il mese di rodaggio.
>
> Per qualsiasi dubbio, WhatsApp o questa email: la risposta arriva entro un giorno lavorativo.
>
> Matia

### B6. Consegna e avvio del rodaggio

**Oggetto:** Consegna di {{lavoro}} e inizio del rodaggio

> Ciao {{nome}},
>
> il lavoro è pronto: {{link}}. Due giri di correzioni sono compresi e partono da adesso.
>
> Da oggi comincia anche il primo mese di cura continua, a forfait e senza limite di ore: tutto ciò che è ordinario può rientrare, e cosa includere si decide insieme in base alle esigenze. A fine mese un resoconto con le ore reali stabilisce il livello per i mesi successivi.
>
> Matia

### B7. Resoconto mensile (accompagna il PDF)

**Oggetto:** Resoconto di {{mese}}: {{ore}} ore, {{numero_voci}} interventi

> Ciao {{nome}},
>
> in allegato il resoconto di {{mese}}. In sintesi: {{ore}} ore usate su {{incluse}} incluse, {{numero_voci}} interventi, e i tre numeri di andamento nella quarta sezione. A fondo pagina il consiglio per il mese prossimo, con il costo.
>
> Matia

### B8. Fine rodaggio (accompagna il resoconto di fine primo mese)

**Oggetto:** Fine rodaggio: cosa abbiamo imparato e il livello consigliato

> Ciao {{nome}},
>
> il primo mese è finito. In allegato il resoconto: ore reali usate ({{ore}}), richieste gestite ({{richieste}}), e il livello che consiglio da adesso ({{livello}}, {{canone}} euro al mese, {{ore_incluse}} ore incluse).
>
> Se il livello va bene, basta una risposta e parte dal {{data}}. Se serve un altro equilibrio, se ne parla in una telefonata di dieci minuti.
>
> Matia

### B9. Richiesta di testimonianza e di permesso a raccontare il caso

**Oggetto:** Due righe sul lavoro fatto, e un permesso

> Ciao {{nome}},
>
> come concordato all'inizio, due richieste a lavoro concluso. La prima: due o tre righe su com'è andata, con le parole che preferisci. La seconda: il permesso di raccontare il caso sul sito e sui social, con il nome dell'attività e i numeri ({{numero}}: da {{prima}} a {{dopo}}). Prima della pubblicazione arriva il testo definitivo, e si pubblica solo con un «ok» scritto.
>
> Matia

### B10. Richiesta fuori ambito (rifiuto cortese)

**Oggetto:** Sulla richiesta di {{argomento}}

> Ciao {{nome}},
>
> grazie per il messaggio. {{argomento}} non rientra in quello che si fa qui: siti, menu digitali, automazioni e strumenti per piccole attività. Per questo non sarebbe un buon lavoro, e meglio dirlo subito.
>
> Se utile, una direzione verso chi può aiutare: {{indicazione}}. E per qualsiasi altra cosa nei campi sopra, la porta è aperta.
>
> Matia

---

## C. WhatsApp Business

### C1. Messaggio di benvenuto (automatico, alla prima scrittura)

> Ciao, questo è Studio Matiz, di Matia Zoffoli. Il messaggio è arrivato e la risposta arriva entro un giorno lavorativo. Per un primo incontro di un'ora, offerto, il calendario è qui: {{link_calendario}}.

### C2. Messaggio di assenza (fuori orario)

> Ciao, grazie del messaggio. Al momento lo studio è chiuso: la risposta arriva il primo giorno lavorativo utile. Per fissare un incontro si può usare già adesso il calendario: {{link_calendario}}.

### C3. Risposte rapide (da richiamare con una scorciatoia)

- **/incontro** - Il primo incontro dura un'ora, di persona o in video, ed è offerto. Si prenota qui: {{link_calendario}}. Non serve preparare niente.
- **/prezzo** - Il prezzo viene scritto dopo il primo incontro e non cambia in corsa. Per una stima subito, lo stimatore sul sito dà un prezzo di partenza in quattro domande: {{link_sito}}.
- **/tempi** - I tempi sono scritti nel preventivo e partono dal momento in cui arriva tutto il materiale: da pochi giorni per un menu a qualche settimana per un sito completo.
- **/checkup** - Il check-up è una ricerca su ciò che esiste già: rapporto in tre giorni lavorativi con le tre priorità e il costo di ciascuna. Il costo viene scalato dal lavoro che segue.
- **/cura** - La cura continua comprende aggiornamenti, sicurezza, backup e modifiche, con un tempo di assistenza ogni mese. Il primo mese è a forfait e senza limite di ore, per capire quanto serve davvero.

---

## D. Come si collegano

- **A1 e A2** possono partire dalla funzione `contatto` su Supabase (vedi `docs/SUPABASE-CONTATTI.md`) appena si crea un account Resend (o servizio simile) e si inseriscono `RESEND_API_KEY` e `NOTIFY_EMAIL` tra i segreti. Sono messaggi di servizio legati alla richiesta, quindi non richiedono consenso (art. 6, lett. b). L'indirizzo mittente va verificato sul dominio dello studio (quando esiste); fino ad allora si può usare quello personale.
- **A3, A4, A5**: l'assenza e le conferme si impostano nel client di posta e nel calendario Google (la conferma di Google Calendar parte comunque: A4 si può usare come testo della descrizione dell'evento).
- **B1-B10** sono modelli da incollare, con la firma di Matia. Nessuna di queste parte in automatico.
- **C1-C3**: si impostano nell'app WhatsApp Business (strumenti per l'attività, messaggio di benvenuto, messaggio di assenza, risposte rapide).
- **Niente follow-up automatici di marketing**: la decisione è che non si inviano senza un consenso separato, che oggi non si chiede. B4 è un promemoria su un preventivo già inviato, mandato a mano.
- **Tracciamento:** nessun pixel di apertura, nessun link accorciato. I link sono quelli veri.

## E. Controllo prima di inviare

- [ ] L'oggetto dice cosa c'è dentro, senza punti esclamativi.
- [ ] La prima riga dice il motivo del messaggio.
- [ ] Un'azione chiara, una sola, con il link.
- [ ] Un numero, un tempo o un fatto per ogni riga importante.
- [ ] Le risposte automatiche dichiarano di essere automatiche e dicono quando risponde Matia.
- [ ] Nessuna parola della lista da evitare (soluzioni, gratuito, contattaci, scopri, senza impegno).
- [ ] Firma: "Matia" nelle comunicazioni personali, "Studio Matiz, di Matia Zoffoli" in quelle automatiche.
