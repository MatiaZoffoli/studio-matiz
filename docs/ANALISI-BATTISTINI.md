# Analisi del sito di Patrick Battistini - spunti per il nostro

Data: 2026-10-08. Richiesta di Matia: analisi dettagliata del sito [patrickbattistini.it](https://patrickbattistini.it/) per capire cosa c'e', cosa c'e' nel nostro e decidere cosa introdurre, aggiungere o cambiare. La grafica non si copia (troppo tecnologica per Matia): si prende il breakdown dei contenuti.

**Limiti:** ho letto 7 pagine (home, servizio siti, servizio software, Chi sono, Articoli, SpiaggiApp) tramite uno strumento che riassume le pagine, non ne riporta il testo integrale. Un dato "non presente" significa non trovato nelle pagine lette. **Lo "stimatore dei lavori" citato da Matia non l'ho trovato come calcolatore di prezzo:** c'e' un "Preventivo guidato" che si apre da un pulsante in testata, ma dal contenuto letto sembra un modulo a passi (con Indietro, Ricomincia, e invio solo a fine corsa), non una stima automatica del prezzo. Vale la pena aprirlo a mano per confermare.

## 1. Come e' fatto il sito

**Menu:** Servizi, Lavori, Metodo, Articoli, "Preventivo in 24h", Contatti, "WhatsApp diretto".

**Home, nell'ordine:**
1. Hero: "Siti e software per trovare clienti e lavorare meglio", con sottotitolo su attivita' che vogliono farsi trovare, eliminare lavoro manuale e avere strumenti propri. Tre numeri: 12 progetti consegnati, 7 app pubblicate, preventivo scritto in 24h.
2. Cosa costruisco: tre servizi (siti, app mobile, gestionali), ognuno con link a una pagina dedicata e a WhatsApp.
3. Progetti reali: 4 in evidenza (con scorrimento orizzontale) e altri 10 elencati con titolo e tipo.
4. Il metodo della bottega, 4 passi: Sentiamoci (mezz'ora di chiamata o un caffe'), Preventivo scritto in 24h (prezzo chiuso), Costruisco (aggiornamenti brevi e demo funzionanti), Consegno e resto.
5. FAQ, 6 domande: quanto costa, solo Cesenatico, quanto ci vuole, da remoto, iOS e Android, come ti contatto.
6. Parliamone: modulo, telefono, email, WhatsApp.
7. Piè di pagina: privacy, articoli, chi sono, social (LinkedIn, GitHub, Instagram, Facebook), "fatto a mano in Riviera".

**Pagina servizio "siti web":** intro, 3 progetti con link, come lavoro (6 punti: codice su misura, velocita', SEO, mobile, dominio intestato al cliente, supporto), cosa realizzo con **prezzi pubblici**, perche' conviene farlo bene, per chi lavoro (settori), dove lavoro (elenco di comuni), 7 FAQ, modulo, altri servizi.
- Prezzi: landing 400-600 euro, vetrina 900-2.500, e-commerce da 1.500; hosting 50-120 euro l'anno. Tempi: landing 5-7 giorni, vetrina 2-4 settimane.
- Pagina "software su misura": tempi (tool semplice 1-2 settimane, gestionale 1-3 mesi), nessun prezzo (rimanda a un articolo), processo con consulenza iniziale gratuita e preventivo scritto.

**Contatti:** WhatsApp con testo precompilato (anche diverso a seconda della pagina), telefono con orari, email, modulo (nome, email o telefono, messaggio) con promessa "rispondo entro 24 ore". Nessun calendario per prenotare.

**Showcase:** 3 casi con screenshot e link al sito vero, altri 10 lavori (anche app per iOS e Android), pagine prodotto dedicate. La pagina di SpiaggiApp e' la piu' costruita: demo interattiva della mappa ombrelloni, 9 funzioni numerate, freemium, FAQ, e storia di origine ("nata in uno stabilimento di Cesenatico").

**Contenuti e SEO:** 36 guide in 5 categorie (Spiaggia digitale, Siti web e SEO, Software e AI, Guide e costi, Casi studio), piu' di 15 su siti per tipi di attivita' (hotel, ristoranti, stabilimenti, negozi, studi), articoli per singoli comuni, parole chiave locali, dati strutturati, scheda Google, mappa.

**Prove di credibilita':** numeri propri (12 e 7), "freelance indipendente, nessuna agenzia", pagina Chi sono con foto e tecnologie, tono artigiano ("bottega digitale", "officina"). **Non presenti:** testimonianze o recensioni di clienti, numero di clienti, video, calendario, versione in altre lingue.

## 2. Cosa ha e cosa abbiamo noi

| Elemento | Battistini | Noi oggi (`prova/index.html`) |
|---|---|---|
| Hero con promessa e numeri | Si, 3 numeri | Si, senza numeri nel hero (il numero 115 a 450 e' piu' sotto) |
| Servizi dettagliati, una pagina ciascuno | Si, 3 + prodotto | **No**: solo il percorso in 4 passi |
| Prezzi pubblici | Siti si, software no | Solo condizioni (check-up, risposta, rodaggio), niente listino |
| Tempi dichiarati | Si | No |
| Metodo in passi | Si, 4 | Si, 4 (il percorso) |
| FAQ | 6-7 per pagina | **No** |
| Showcase di progetti | 3 + 10, link ai siti | Un solo caso (societa' sportiva), senza link |
| Prodotto con demo | SpiaggiApp | No |
| Modulo di contatto | Si | Solo mailto |
| WhatsApp diretto | Ovunque | **No** |
| Prenotazione appuntamento | No | No (ma e' il nostro obiettivo principale) |
| Preventivo guidato | Si, modulo a passi | No |
| Articoli e guide | 36 | **No** |
| Chi sono con foto | Si | Si, ma foto da inserire |
| Testimonianze | No | No |
| Lingue | Solo italiano | Solo italiano (ma l'inglese e' un punto di forza di Matia) |
| Privacy e cookie | Privacy | **No** |

## 3. Le sue debolezze (che sono le nostre occasioni)

Letture mie, da confrontare con le impressioni di Matia (sito "troppo tecnico", rischio di apparire un "nerd").
- Nessuna prova sociale di clienti: solo numeri propri. Un caso con risultato misurato (115 a 450) vale piu' di "12 progetti".
- Nessuna prenotazione di un incontro: contatto solo per messaggio o modulo.
- Il suo "preventivo guidato" non da una stima, almeno da quanto letto: **un vero stimatore e' un'occasione**.
- Nessuna offerta di assistenza continuativa strutturata (ore, tempi, canone): e' il nostro punto di differenza.
- Nessuna lingua oltre l'italiano.
- Nessun check-up dell'esistente: parte sempre da zero, mai da "guardiamo cosa hai".
- Tono artigiano ma tecnico, gergo (Flutter, Firebase, codice pulito): il titolare non si sente a casa.

## 4. Proposte per il nostro sito (da decidere insieme)

Ordine per priorita' e sforzo. Nessuna e' ancora decisa.

**Prima del lancio (sito minimo credibile)**
1. **Sezione Servizi** con quattro voci: Siti e menu digitali, Automazioni, Cura continua, Check-up. Una pagina breve per ciascuna, o una sezione unica con ancore se all'inizio il materiale e' poco. Ognuna con: per chi, cosa include, tempi, fascia di prezzo (quando decisa), FAQ, pulsante di contatto.
2. **Contatti a piu' canali:** WhatsApp con messaggio precompilato per pagina, modulo breve (nome, contatto, cosa ti serve) con promessa di risposta in un giorno lavorativo, telefono, email.
3. **Prenota il primo incontro:** calendario per scegliere uno slot da 30-45 minuti (strumento gratuito a calendario), accanto al modulo. E' il gesto che vogliamo, quindi va reso il piu' facile possibile.
4. **FAQ** di 6-8 domande: quanto costa, cosa succede dopo la consegna, tempi, lavori solo in Romagna, lingue, chi sei, cosa sono le ore del canone.
5. **Chi sono con foto vera** (oggi segnaposto), con Australia, locali diretti, inglese.
6. **Privacy e cookie**, indispensabili (dati nel modulo e statistiche).

**Subito dopo**
7. **Casi / Lavori:** la pagina del caso della societa' sportiva con prima e dopo, screenshot, cosa e' stato fatto. Altri lavori man mano, anche piccoli, anche gratuiti di lancio. Se possibile un link al sito vero.
8. **Stimatore di progetto onesto:** 4-5 domande (tipo di attivita', cosa serve, lingue, assistenza) e una **fascia** di prezzo e di tempi, mai un numero secco. Si invia a Matia con le risposte. Differenzia dal "preventivo guidato" altrui.
9. **Check-up gratuito istantaneo:** si inserisce l'indirizzo del proprio sito e si riceve in pochi secondi un mini rapporto automatico (velocita', mobile, HTTPS, menu in PDF, lingue). Riusa l'automazione che Matia vuole costruire per il check-up e fa vedere il suo mestiere senza dirlo. Chi lascia l'indirizzo diventa un contatto.
10. **Testimonianze** dai primi clienti, appena ci sono.

**Piu' avanti**
11. **Guide / articoli** per la SEO locale (cinque articoli ben fatti all'inizio, non trentasei): "quanto costa un sito per un ristorante", "menu digitale: cosa serve davvero", "perche' il QR porta a un menu vecchio".
12. **Versione in inglese**, scritta da Matia: un vantaggio che il concorrente non ha.
13. **Pagine locali** (Cesenatico, Cervia, Rimini) solo quando c'e' contenuto vero, per evitare pagine vuote.

## 5. Cosa non copiare

- Il linguaggio tecnico e il tono "officina" molto marcato.
- I 36 articoli subito: meglio pochi e buoni.
- Un portfolio gonfiato: con un solo caso vero conviene raccontarlo bene e non riempire.
- Prezzi del software senza fasce: meglio una fascia onesta per ogni servizio quando i prezzi saranno decisi.

## 6. Decisioni per Matia

1. Il sito di lancio e' "minimo credibile" (punti 1-6) o vuoi gia' includere casi, stimatore e check-up (7-9)?
2. Vuoi i prezzi pubblici come fa lui (fasce), o solo le condizioni e i prezzi a richiesta?
3. Quale strumento per prenotare l'incontro (da scegliere, gratuito)?
4. Check-up automatico pubblico: lo costruiamo prima del lancio o dopo i primi clienti?
5. Inglese: sito bilingue dal giorno uno o in seconda fase?
