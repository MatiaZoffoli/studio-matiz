# -*- coding: utf-8 -*-
"""
Genera la versione inglese del sito (prova/en/index.html) a partire dalla pagina italiana (prova/index.html).

Fonte unica: il testo italiano vive solo in prova/index.html. Qui sotto c'e' l'elenco delle coppie
(testo italiano -> inglese). Ogni coppia deve trovare il suo testo nella pagina italiana: se un testo
italiano cambia, lo script si ferma e dice quale coppia aggiornare, cosi' le due lingue non si
allontanano di nascosto.

Uso (dalla cartella del progetto):
    python tools/build_en.py

La traduzione e' semantica, non letterale: la voce e' quella della skill voce-studio-matiz
(impersonale e precisa; prima persona solo in 'Chi sono' e nei messaggi diretti).
"""
import io, re, sys, os
from urllib.parse import quote

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "prova", "index.html")
OUT = os.path.join(ROOT, "prova", "en", "index.html")

# ---------------------------------------------------------------- testi (contenuto tra '>' e '<')
TEXT = [
# testata e menu
("Il mestiere", "The craft"),
("Il metodo", "The method"),
("Le regole", "The terms"),
("Il prezzo", "Pricing"),
("Chi sono", "About"),
("Domande", "FAQ"),
("Prenota un incontro", "Book a meeting"),
("Primo incontro", "First meeting"),
# hero
('Progettazione digitale<br class="mb"> per piccole imprese', 'Digital design<br class="mb"> for small businesses'),
("Soluzioni<br><em>su misura</em>", "Made<br><em>to measure</em>"),
("Costruzione di siti, menu digitali e automazioni per stabilimenti, ristoranti e piccole attività, con aggiornamenti, modifiche e supporto continuo.", "Websites, digital menus and automations for beach clubs, restaurants and small businesses, with regular updates, changes and ongoing support."),
("Prenota il primo incontro", "Book the first meeting"),
("Un'ora tra chiacchiere e caffè, offerta dallo studio.<br>Di persona o in video.", "One complimentary hour of coffee and conversation.<br>In person or by video."),
("Il mestiere, in quattro parti", "The craft, in four parts"),
("Studio a Cesenatico, con clienti<br>in Romagna e a distanza", "Based in Cesenatico, working with clients<br>across Romagna and remotely"),
("Siti, menu digitali, automazioni<br>e assistenza continua", "Websites, digital menus, automations<br>and ongoing support"),
("Risposte rapide<br>e dirette", "Quick, direct<br>replies"),
# costa
("Il mare cambia a ogni stagione, e una presenza online ben tenuta cambia con lui.", "The sea changes with the seasons. A well-maintained online presence keeps pace with them."),
# punto di partenza
("Il punto di partenza", "The starting point"),
("Quello che succede <em>dopo la consegna</em>", "What happens <em>after delivery</em>"),
("Costruire richiede settimane. Mantenere richiede anni, ed è la parte che in molti contratti non ha un responsabile.", "Building takes weeks. Maintaining takes years, and in many contracts it is the part nobody is responsible for."),
("Ferma al giorno della consegna", "Frozen at the moment of delivery"),
("Orari, prezzi e offerte cambiano a ogni stagione, quattro volte l'anno, e uno strumento che non cambia con loro smette di dire la verità.", "Opening hours, prices and offers change with each season, four times a year, and a website or menu that stays the same soon gives people outdated information."),
("Un canone che non dice cosa copre", "A fee that does not say what it covers"),
("Cinquanta euro al mese senza modifiche incluse fanno 600 euro l'anno: conviene sapere con precisione cosa coprono.", "Fifty euros a month with no edits included comes to 600 euros a year: worth knowing exactly what that covers."),
("Visite che non diventano richieste", "Visits that don't become enquiries"),
("Si conta quante persone arrivano, quasi mai quante scrivono, telefonano o prenotano, né dove si fermano le altre.", "Visits get counted. Enquiries, calls and bookings seldom do, and neither do the points where people leave."),
# mestiere
("Il mestiere, <em>in quattro parti</em>", "The craft, <em>in four parts</em>"),
("Ogni parte funziona da sola. Si può cominciare da una qualunque, o dalla prima e vedere come va.", "Each service stands on its own. Start with any of them, or with the first and see how it goes."),
("01 · Sito, menu, schede e profili", "01 · Website, menu, listings and profiles"),
("Presenza online", "Online presence"),
("Il problema", "The problem"),
("Quattro stagioni, quattro aggiornamenti l'anno, ciascuno da ripetere su sito, scheda Google, profili e menu. Ogni copia dimenticata è un'informazione sbagliata.", "Four seasons, four updates a year across website, Google listing, profiles and menu. Miss one, and customers get the wrong information."),
("La risposta", "The answer"),
("Un punto solo da cui si aggiorna tutto, e una prima risposta entro un giorno lavorativo a ogni richiesta di modifica.", "One place to update everything, and a first reply within one working day to every change request."),
("02 · Risposte, richieste, promemoria", "02 · Replies, requests, reminders"),
("Automazioni", "Automations"),
("Una risposta scritta a mano per cinque minuti al giorno sono più di 30 ore l'anno.",
 "A reply typed by hand for five minutes a day adds up to more than 30 hours a year."),
("Si individua il compito più ripetuto, lo si cronometra e si costruisce lo strumento che lo fa da solo. Il risultato si confronta con le ore di partenza.",
 "The most repeated task is identified and timed, and a tool is built to do it on its own. The result is compared with the starting hours."),
("03 · Aggiornamenti, sicurezza, backup", "03 · Updates, security, backups"),
("Cura continua", "Ongoing care"),
("Aggiornamenti, backup e sicurezza si rimandano finché qualcosa smette di funzionare, e a quel punto il costo è quello di un'emergenza, non di una manutenzione.",
 "Updates, backups and security get postponed until something stops working, and by then the cost is that of an emergency, not of maintenance."),
("Il primo mese a forfait, senza limite di ore, misura il consumo reale. Dal secondo, un monte ore fissato sui dati raccolti e una prima risposta entro un giorno lavorativo.", "The first month is a flat fee with unlimited hours, to measure real usage. From the second, a block of hours set on the data collected, and a first reply within one working day."),
("04 · Numeri, percorsi, priorità", "04 · Numbers, journeys, priorities"),
("Check-up", "Check-up"),
("Prima di spendere in una nuova pagina conviene sapere dove le persone si fermano. Senza questo dato ogni intervento è una scommessa.", "Before investing in a new page, it pays to know where people drop off. Without that data, every change is a gamble."),
("In tre giorni lavorativi dalla conferma e dalla ricezione degli accessi, un rapporto con la mappa delle priorità, ciascuna con il suo costo. Il costo del check-up si scala dal lavoro che segue.", "Within three working days of confirmation and receipt of access, a report with the map of priorities, each with its cost. The check-up fee is credited towards the work that follows."),
("Un messaggio su WhatsApp", "Message on WhatsApp"),
("Scorri per vedere gli altri", "Scroll to explore the services"),
("Scorri di lato", "Swipe sideways"),
# metodo
("Come si lavora", "How it works"),
("Si misura prima <em>di costruire</em>", "Measure first, <em>then build</em>"),
("Un metodo in quattro tempi, con un risultato chiuso a ogni passo e un numero da cui partire. Il percorso si adatta al servizio scelto.", "A four-step process, with a clear outcome at each stage and a baseline number to start from. The path adapts to the service chosen."),
("Un'ora per capire come si lavora e dove si perde tempo. Si decide insieme quale numero conta (richieste, prenotazioni, iscritti) e da quanto si parte.", "One hour to understand the work and where time is lost. Together, the number that matters is chosen (enquiries, bookings, members) and the baseline is set."),
("Ricerca su ciò che esiste: sito, profili, posta, gestionale, dati. In tre giorni lavorativi dalla conferma e dalla ricezione degli accessi un rapporto con la mappa delle priorità e il costo di ciascuna.", "A review of what already exists: website, profiles, email, business software, data. Within three working days of confirmation and receipt of access, a report with the map of priorities and the cost of each."),
("Costruzione", "Build"),
("Sviluppo a tappe, con due giri di correzioni e un prezzo chiuso. A ogni tappa si vede qualcosa che funziona.", "Development in stages, with two rounds of revisions and a fixed price. Every stage delivers something that works."),
("Cura", "Care"),
("Messa a punto nel tempo: si aggiorna, si regola e si rimisura. Ogni mese un resoconto confronta i numeri con il punto di partenza.", "Ongoing fine-tuning: updates, adjustments and fresh measurements. Each month a report compares the numbers with the starting point."),
# caso
("Un caso misurato", "A case in numbers"),
("Ogni obiettivo ha un numero. <em>Si parte da lì</em>", "Every goal has a number. <em>That is where to start</em>"),
("Iscritti, prenotazioni, richieste, ordini: qualunque obiettivo si voglia far crescere, si misura il punto di partenza, si costruisce, si misura di nuovo.", "Members, bookings, enquiries, orders: whatever goal needs to grow, the starting point is measured, something is built, then it is measured again."),
("Iscritti a una società sportiva", "Members of a sports club"),
("Primi due anni", "First two years"),
("Dopo una settimana", "After one week"),
("Il primo caso misurato: una società sportiva, da 115 a 450 iscritti in una settimana. Tre gli interventi: correzione nel sito di errori e logiche ormai superate, ricerca e sviluppo di un nuovo metodo di accesso ai palazzetti, traffico online riportato su una pagina ad accesso riservato al posto di servizi di terze parti.", "The first case study: a sports club, from 115 to 450 members in one week. Three changes: errors and outdated logic fixed on the website, a new way into the sports halls researched and built, and online traffic moved to a restricted-access page in place of third-party services."),
# obiettivi
("Cosa si misura", "What gets measured"),
("I numeri <em>che contano</em>", "The numbers <em>that matter</em>"),
("Tre degli obiettivi che le piccole attività inseguono più spesso, e il numero con cui si misura ciascuno.", "Three of the goals small businesses pursue most often, and the number that measures each one."),
("Iscritti", "Members"),
("Nuove iscrizioni e ritorni nel tempo. Nel caso misurato: da 115 a 450 in una settimana.", "New and returning members over time. In the case study: from 115 to 450 in one week."),
("Prenotazioni", "Bookings"),
("Richieste di tavolo o di ombrellone arrivate da sito, menu e schede, confrontate prima e dopo il lavoro.", "Table or beach umbrella requests coming from website, menu and listings, compared before and after the work."),
("Richieste", "Enquiries"),
("Messaggi e richieste di preventivo ricevuti, e tempo medio che passa prima di una risposta.", "Messages and quote requests received, along with the average time it takes to reply."),
("Un altro obiettivo, o un altro problema? Si racconta qui, e si lavora insieme per risolverlo", "Another goal, or another problem? Share it here, and work on it together"),
("Un altro obiettivo? Si racconta qui", "Another goal? Share it here"),
# regole
("Condizioni chiare, <em>scritte prima</em>", "Clear terms, <em>set out upfront</em>"),
("Ciò che è incluso è scritto prima di cominciare.", "What is included is set out before work begins."),
("Ascolto", "Listening"),
("Un'ora per ascoltare come si lavora e raccogliere i numeri di partenza. Nessuna proposta improvvisata.", "One hour to understand the work and record the starting numbers. No on-the-spot proposals."),
("Trasparenza", "Transparency"),
("Preventivo", "Quote"),
("Cosa include, quanto costa e in quanto tempo si consegna, tutto scritto prima di cominciare. Il prezzo non cambia in corsa.", "What is included, what it costs and when it will be delivered, all set out before work begins. The price does not change along the way."),
("Equità", "Fairness"),
("Il costo del check-up viene scalato dal lavoro che segue, se si prosegue.", "The check-up fee is credited towards the work that follows, if the work goes ahead."),
("Prontezza", "Promptness"),
("Risposta", "Reply"),
("Ogni messaggio riceve una prima risposta entro un giorno lavorativo.", "Every message gets a first reply within one working day."),
("Dedizione", "Dedication"),
("Tempi di consegna", "Delivery times"),
("Il massimo focus su ogni lavoro è garantito: il tempo di consegna è scritto nel preventivo ed è quello che si rispetta.", "Every project gets full attention. The delivery time is set out in the quote, and that is the time that gets met."),
("Equilibrio", "Balance"),
("Rodaggio", "Settling in"),
("Il primo mese è a forfait e senza limite di ore, per assistenza, ricerca e idee. A fine mese un resoconto con le ore reali stabilisce quante ne servono.", "The first month is a fixed fee with no cap on hours, for support, research and ideas. At the end of the month, a report of the hours actually used shows how many are needed."),
# stimatore
("Il prezzo di partenza", "The starting price"),
("Il prezzo, <em>detto prima di cominciare</em>", "The price, <em>stated before starting</em>"),
("Lo studio lavora da solo e usa strumenti che automatizzano le parti ripetitive: per questo i costi restano contenuti senza ridurre la cura. Il prezzo è scritto prima di decidere.", "One person runs the studio, and tools automate the repetitive parts: costs stay contained without cutting corners. The price is put in writing before any decision is made."),
("Quattro domande bastano per un prezzo di partenza, subito e senza telefonate.", "Four questions give an instant starting price, with no phone calls."),
("Tipo di attività", "Type of business"),
("Stabilimento balneare", "Beach club"),
("Ristorante o bar", "Restaurant or bar"),
("Hotel o struttura ricettiva", "Hotel or accommodation"),
("Negozio o artigiano", "Shop or craftsperson"),
("Studio professionale", "Professional practice"),
("Altro", "Other"),
("Cosa serve ", "What is needed "),
("Si può scegliere più di una voce.", "More than one can be chosen."),
("Un sito", "A website"),
("Un menu digitale", "A digital menu"),
("Automatizzare una parte del lavoro", "Automating part of the work"),
("Assistenza continua", "Ongoing support"),
("Da capire: serve un check-up per partire", "Not sure yet: a check-up is needed to start"),
("Presenza online oggi", "Online presence today"),
("Nessuna presenza online", "No online presence"),
("Una presenza vecchia, da rifare", "An old presence, to be redone"),
("Una presenza che nessuno segue", "A presence nobody looks after"),
("Una presenza che funziona, serve altro", "A presence that works, something else is needed"),
("Dimensione del lavoro", "Size of the job"),
("Essenziale", "Essential"),
("Poche cose, ben definite.", "A few things, well defined."),
("Completo", "Complete"),
("Più pagine o più passaggi.", "More pages or more steps."),
("Con funzioni", "With features"),
("Iscrizioni, prenotazioni, area riservata o un processo articolato.", "Sign-ups, bookings, a members' area or a complex process."),
("Dove inviare il prezzo ", "Where to send the price "),
("Nome ed email bastano per vedere subito il prezzo di partenza.", "A name and email are enough to see the starting price right away."),
("Nome", "Name"),
("Email", "Email"),
("Telefono (facoltativo)", "Phone (optional)"),
("Non compilare ", "Leave empty "),
("Ho letto l'", "I have read the "),
("informativa privacy", "privacy notice"),
("Indietro", "Back"),
("Avanti", "Next"),
("Vedi il prezzo", "See the price"),
("Prezzo di partenza", "Starting price"),
("Contattami su WhatsApp", "Message me on WhatsApp"),
("Ricomincia", "Start over"),
# chi sono
("Dalla sala <em>ai dati</em>", "From hospitality <em>to data</em>"),
("Foto di Matia da inserire", "Matia's photo to come"),
("Il mio primo ricordo dei numeri è nel negozio di mia nonna: mentre lavorava, per tenermi occupato mi dava pagine di operazioni da risolvere, a mente o con carta e penna. Trovare il risultato mi dava una sensazione di completezza che non ho mai smesso di cercare. Ancora oggi, davanti a un problema, parto dalla convinzione che una soluzione esista. E quando non la trovo, ho imparato a cambiare prospettiva: forse è la domanda a essere sbagliata.", "My first memory of numbers is in my grandmother's shop. While she worked, she would keep me busy with pages of sums to work out in my head or with pen and paper. Finding the answer gave me a sense of things falling into place that I have never stopped looking for. Even today, I approach a problem believing there is a solution. When I cannot find it, I have learned to look at things differently: perhaps the question is the wrong one."),
("A undici anni facevo caffè in un bar di Cesenatico: asciugare un cestello di bicchieri mi comprava dieci minuti con gli amici. I miei genitori gestivano attività e il lavoro, in casa, faceva parte della vita. Da lì vent'anni nella ristorazione, di cui tredici alla direzione di locali a Sydney. Ho imparato ad affrontare i problemi quando arrivano, perché dopo di te non c'è nessuno: <em>the buck stops with you</em>. E a leggere i numeri per capire cosa funziona, cosa no e dove vale la pena cambiare.", "At eleven, I was making coffee in a café in Cesenatico: drying a rack of glasses bought me ten minutes with my friends. My parents ran businesses, so work was simply part of family life. That led to twenty years in restaurants and hospitality, thirteen of them managing venues in Sydney. I learned to deal with problems as they came up, because there was no one else to pass them on to: <em>the buck stops with you</em>. And to read the numbers to see what works, what doesn't, and where change makes sense."),
("Dopo il Covid ho deciso di esserci di più per la mia famiglia, soprattutto per le mie figlie. Sono tornato a studiare, prima finanza, poi matematica e statistica, conseguendo due diplomi mentre continuavo a lavorare. Sono entrato nel mondo dei dati, lavorando per enti pubblici e grandi aziende. Dopo vent'anni di esperienza sono ripartito da principiante, ma non da zero. Mi sono portato dietro la capacità di leggere le persone, di capirle anche senza parole. Una sensibilità che davanti a uno schermo non si impara.", "After Covid, I decided to be more present for my family, especially my daughters. I went back to studying, first finance, then mathematics and statistics, earning two diplomas while continuing to work. I moved into data, working with public sector organisations and large companies. After twenty years of experience, I was a beginner again, but I was not starting from nothing. I brought with me the ability to read people, to understand what they mean even when they do not put it into words. That is something you do not learn in front of a screen."),
("Oggi aiuto le piccole attività a semplificare il lavoro attraverso dati e tecnologia, per restituire tempo alle persone, alle famiglie, alle loro passioni. Ho imparato a leggere i numeri per capire le attività, e a leggere le persone per capire cosa conta davvero. È da questo incontro che parto, prima di analizzare, esplorare le possibilità, scegliere e costruire. Con una regola: i numeri che contano sono quelli del cliente. Altrimenti la soluzione sarebbe la mia, non la sua.", "Today, I help small businesses simplify their work through data and technology, giving people more time for their families and the things they love. I have learned to read the numbers to understand a business, and to read people to understand what truly matters. Those two perspectives guide how I analyse, explore the options, choose an approach and build. With one rule: the numbers that matter are the client's. Otherwise the solution would be mine, not theirs."),
# domande
("Prima di scrivere", "Before you ask"),
("Domande <em>frequenti</em>", "Frequently<br>asked<br><em>questions</em>"),
("Quanto costa?", "How much does it cost?"),
("Dipende dal lavoro. Dopo il primo incontro arriva un prezzo scritto e chiuso, che non cambia in corsa. Il costo del check-up viene scalato dal lavoro che segue.",
 "It depends on the job. After the first meeting a written, fixed price arrives, and it does not change along the way. The cost of the check-up is deducted from the work that follows."),
("Cosa succede dopo la consegna?", "What happens after delivery?"),
("Comincia la cura continua: aggiornamenti, correzioni e prima risposta entro un giorno lavorativo. Ogni mese un resoconto mostra le ore usate, le cose fatte e i numeri di andamento.", "Ongoing care begins: updates, fixes and a first reply within one working day. Every month a report shows the hours used, the work done and the performance numbers."),
("Quanto tempo serve?", "How long until delivery?"),
("Da pochi giorni per un menu a qualche settimana per un sito completo. Il tempo è scritto nel preventivo e parte dal momento in cui arriva tutto il materiale. Il massimo focus su ogni lavoro è garantito, per una consegna nei tempi scritti.",
 "From a few days for a menu to a few weeks for a complete website. The time is written in the quote and starts from the moment all the material arrives. Maximum focus on every job is guaranteed, for delivery within the written time."),
("A chi appartengono dominio e contenuti?", "Who owns the domain and the content?"),
("Al cliente, sempre. Dominio, contenuti, dati e accessi sono intestati a lui e, se lo chiede, vengono gestiti per suo conto. Alla fine del rapporto tutto viene consegnato.",
 "The client, always. Domain, content, data and access are registered in the client's name and, on request, managed on their behalf. At the end of the relationship everything is handed over."),
("Cosa sono le ore incluse nella cura continua?", "How do the ongoing care hours work?"),
("Il tempo mensile dedicato alle richieste: modifiche ai contenuti, interventi ordinari, domande. Aggiornamenti tecnici, sicurezza e backup non lo consumano. Il primo mese è a forfait e senza limite di ore: tutto ciò che è ordinario può rientrare, e cosa includere si decide insieme in base alle esigenze. A fine mese il livello si stabilisce insieme, guardando i dati e le informazioni raccolte. I grandi sviluppi si preventivano a parte.",
 "The monthly time devoted to requests: content changes, routine work, questions. Technical updates, security and backups do not use it up. The first month is a flat fee with unlimited hours: anything routine can be included, and what to include is decided together according to needs. At the end of the month the level is set together, looking at the data and information gathered. Major developments are quoted separately."),
("Dove si lavora?", "Where is the work done?"),
("Lo studio è a Cesenatico. In Romagna ci si incontra di persona, nel resto d'Italia in video, con lo stesso metodo.",
 "The studio is in Cesenatico. In Romagna meetings are in person, elsewhere on video, with the same method."),
("Si lavora anche in inglese?", "Can the work be done in English?"),
("Sì, con piena disponibilità: siti, menu, carta dei vini, documenti e assistenza si realizzano in inglese come in italiano.", "Yes, fully: websites, menus, wine lists, documents and support are produced in English as well as Italian."),
("Quali dati vengono raccolti?", "What data is collected?"),
("Solo quelli lasciati scrivendo o prenotando, usati per rispondere. Il dettaglio è nell'", "Only what is left by writing or booking, used to reply. The detail is in the "),
# chiusura e piede
("Si comincia <em>da un numero</em>", "It starts <em>with a number</em>"),
("Il primo incontro si prenota dal calendario; in alternativa basta un messaggio, con prima risposta entro un giorno lavorativo.", "The first meeting is booked through the calendar; alternatively, a message is enough, with a first reply within one working day."),
("Contatti", "Contact"),
("Informazioni", "Information"),
("Domande frequenti", "FAQ"),
("Logo in definizione", "Logo in progress"),
("di Matia Zoffoli", "by Matia Zoffoli"),
("Pagina di prova: nome, testi e condizioni sono in bozza.", "Preview page: the name, copy and terms are still drafts."),
("Studio Matiz di Matia Zoffoli, Cesenatico.", "Studio Matiz by Matia Zoffoli, Cesenatico."),
]

# ---------------------------------------------------------------- attributi: valore -> valore
ATTR = [
("Studio Matiz, inizio pagina", "Studio Matiz, top of page"),
("Principale", "Main"),
("Presenza online", "Online presence"),
("Automazioni", "Automations"),
("Cura continua", "Ongoing care"),
("Check-up", "Check-up"),
("Scheda precedente", "Previous card"),
("Scheda successiva", "Next card"),
("Spazio riservato alla foto di Matia", "Space reserved for Matia's photo"),
("Stabilimento balneare", "Beach club"),
("Ristorante o bar", "Restaurant or bar"),
("Hotel o struttura ricettiva", "Hotel or accommodation"),
("Negozio o artigiano", "Shop or craftsperson"),
("Studio professionale", "Professional practice"),
("Altro", "Other"),
("Non ho niente online", "I have nothing online"),
("Ho un sito vecchio", "I have an old website"),
("Ho un sito che nessuno segue", "I have a website nobody looks after"),
("Ho un sito che funziona", "I have a website that works"),
]

# ---------------------------------------------------------------- messaggi precompilati di WhatsApp
def wa(s): return quote(s, safe="")
WA = [
("Ciao Matia, vorrei saperne di più su: Presenza online", "Hello Matia, I would like to know more about: Online presence"),
("Ciao Matia, vorrei saperne di più su: Automazioni", "Hello Matia, I would like to know more about: Automations"),
("Ciao Matia, vorrei saperne di più su: Cura continua", "Hello Matia, I would like to know more about: Ongoing care"),
("Ciao Matia, vorrei saperne di più su: Check-up", "Hello Matia, I would like to know more about: Check-up"),
("Ciao Matia, ho un altro obiettivo o problema di cui vorrei parlare.", "Hello Matia, I have another goal or problem I would like to talk about."),
("Ciao Matia, vorrei fissare un primo incontro.", "Hello Matia, I would like to set up a first meeting."),
]

# ---------------------------------------------------------------- stringhe dentro gli script (copia esatta)
JS = [
("['Il problema', 'La risposta']", "['The problem', 'The answer']"),
(".replace(/\\B(?=(\\d{3})+(?!\\d))/g, '.')", ".replace(/\\B(?=(\\d{3})+(?!\\d))/g, ',')"),
("b[4] === 'settimane'", "b[4] === 'weeks'"),
("'Pagina singola', 10, 'giorni'", "'Single page', 10, 'days'"),
("'Sito completo', 3, 'settimane'", "'Complete website', 3, 'weeks'"),
("'Sito con funzioni', 6, 'settimane'", "'Website with features', 6, 'weeks'"),
("'Menu digitale', 5, 'giorni'", "'Digital menu', 5, 'days'"),
("'Automazione semplice', 10, 'giorni'", "'Simple automation', 10, 'days'"),
("'Automazione articolata', 10, 'giorni'", "'Complex automation', 10, 'days'"),
("'Strumento su misura', 5, 'settimane'", "'Custom tool', 5, 'weeks'"),
("'Check-up', 3, 'giorni lavorativi'", "'Check-up', 3, 'working days'"),
("\"Manca il tipo di attività.\"", "\"The type of business is missing.\""),
("\"Manca almeno una voce da scegliere.\"", "\"At least one option needs to be chosen.\""),
("\"Manca la situazione online di oggi.\"", "\"The current online situation is missing.\""),
("\"Manca la dimensione del lavoro.\"", "\"The size of the job is missing.\""),
("\"Manca il nome.\"", "\"The name is missing.\""),
("\"L'indirizzo email non è valido.\"", "\"The email address is not valid.\""),
("'Per vedere il prezzo serve spuntare l\\'informativa privacy.'", "'To see the price, the privacy notice needs to be ticked.'"),
("b[0] === b[1] ? eur(b[0]) + ' euro' : 'da ' + eur(b[0]) + ' euro'", "b[0] === b[1] ? '€' + eur(b[0]) : 'from €' + eur(b[0])"),
("'Cura continua';\n        $('#estTime')", "'Ongoing care';\n        $('#estTime')"),
("\"Il primo mese è a forfait e senza limite di ore, per assistenza, ricerca e idee. Dal secondo mese si decide in base all'uso reale. La cifra viene indicata nel preventivo, dopo il primo incontro.\"",
 "\"The first month is a flat fee with unlimited hours, for support, research and ideas. From the second month it is decided on real usage. The figure is given in the quote, after the first meeting.\""),
("'Il check-up: ' + eur(r.lo) + ' euro' : 'Da ' + eur(r.lo) + ' euro'", "'The check-up: €' + eur(r.lo) : 'From €' + eur(r.lo)"),
("'Tempo di consegna: circa ' + r.longest[3] + ' ' + r.longest[4] + ', scritto nel preventivo.'", "'Delivery time: about ' + r.longest[3] + ' ' + r.longest[4] + ', written in the quote.'"),
("\"Da dove partire? Il check-up serve a questo: si guarda cosa c'è già e si indica cosa conviene fare per primo. Il costo viene scalato dal lavoro che segue.\"",
 "\"Where to start? The check-up is for that: it looks at what already exists and says what is best to do first. The cost is deducted from the work that follows.\""),
("\"È il prezzo di partenza per il lavoro descritto: la cifra finale dipende da quanto è articolato.\"",
 "\"This is the starting price for the work described: the final figure depends on how complex it is.\""),
("\"A questo si aggiunge la cura continua: il primo mese è a forfait e senza limite di ore, poi il livello si decide sulle ore reali.\"",
 "\"Ongoing care comes on top: the first month is a flat fee with unlimited hours, then the level is decided on the real hours.\""),
("\"Non è un preventivo: il prezzo vero viene scritto dopo il primo incontro e non cambia in corsa. IVA se dovuta.\"",
 "\"This is not a quote: the real price is written after the first meeting and does not change along the way. VAT if due.\""),
("|| 'cura continua'", "|| 'ongoing care'"),
("lingua: 'it',", "lingua: 'en',"),
("'Ciao Matia, ho visto dal sito un prezzo di partenza (' + $('#estRange').textContent + ') per: ' + nomi + '. Attività: ' + val('tipo') + '. Vorrei parlarne.'",
 "'Hello Matia, I saw a starting price on the website (' + $('#estRange').textContent + ') for: ' + nomi + '. Business: ' + val('tipo') + '. I would like to talk about it.'"),
("\"Registrazione della richiesta in corso...\"", "\"Saving the request...\""),
("\"Richiesta ricevuta. La prima risposta arriva entro un giorno lavorativo.\"", "\"Request received. A first reply arrives within one working day.\""),
("\"La richiesta non è stata registrata. Un messaggio su WhatsApp o una email arrivano comunque.\"", "\"The request was not saved. A WhatsApp message or an email will still get through.\""),
]

# ---------------------------------------------------------------- parole che restano uguali in inglese (non segnalate)
SAME = {"Logo", "Studio Matiz", "Studio", "Cesenatico", "Cesenatico, Romagna", "Check-up", "Email", "Privacy",
        "matiazoffoli@gmail.com", "WhatsApp +39 333 958 0381", "115", "450", "Romagna"}

def main():
    t = io.open(SRC, encoding="utf-8").read()
    errors = []

    # testi
    for it, en in sorted(TEXT, key=lambda p: -len(p[0])):
        rx = re.compile(">" + re.escape(it) + r"(\s*)<")
        if not rx.search(t):
            errors.append("TESTO NON TROVATO: " + it[:80]); continue
        t = rx.sub(lambda m: ">" + en + m.group(1) + "<", t)
    # attributi
    for it, en in ATTR:
        found = False
        for attr in ("aria-label", "value"):
            pat = attr + '="' + it + '"'
            if pat in t:
                t = t.replace(pat, attr + '="' + en + '"'); found = True
        if not found:
            errors.append("ATTRIBUTO NON TROVATO: " + it)
    # whatsapp
    for it, en in WA:
        if wa(it) not in t:
            errors.append("WHATSAPP NON TROVATO: " + it[:60]); continue
        t = t.replace(wa(it), wa(en))
    # script
    for it, en in JS:
        if it not in t:
            errors.append("SCRIPT NON TROVATO: " + it[:80]); continue
        t = t.replace(it, en)

    # intestazione, percorsi e lingua
    heads = [
        ('<html lang="it" class="pending">', '<html lang="en" class="pending">'),
        ("<title>Studio Matiz - Soluzioni su misura</title>", "<title>Studio Matiz - Made to measure</title>"),
        ('content="Progettazione e sviluppo di siti, automazioni e strumenti digitali per piccole imprese. Il primo incontro è offerto dallo studio."',
         'content="Design and development of websites, automations and digital tools for small businesses. The first meeting is offered by the studio."'),
        ('src="assets/', 'src="/assets/'),
        ('href="privacy.html"', 'href="/en/privacy.html"'),
        ('<a href="/" lang="it" aria-current="true">IT</a>', '<a href="/" lang="it">IT</a>'),
        ('<a href="/en/" lang="en" hreflang="en">EN</a>', '<a href="/en/" lang="en" hreflang="en" aria-current="true">EN</a>'),
        ('aria-label="Lingua"', 'aria-label="Language"'),
    ]
    for it, en in heads:
        if it not in t:
            errors.append("TESTATA NON TROVATA: " + it[:80]); continue
        t = t.replace(it, en)
    # il rinvio automatico verso l'inglese serve solo alla pagina italiana
    t, n = re.subn(r'<script id="langRedirect">.*?</script>\s*', "", t, count=1, flags=re.S)
    if n != 1:
        errors.append("SCRIPT DI RINVIO NON TROVATO")

    # controllo: testo italiano rimasto fuori dall'elenco
    body = t[t.index("<body"):]
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    body = re.sub(r"<style.*?</style>", "", body, flags=re.S)
    left = []
    for m in re.finditer(r">([^<>]*[A-Za-zÀ-ÿ][^<>]*)<", body):
        s = m.group(1).strip()
        if s and s not in SAME and re.search(r"\b(il|la|le|lo|gli|di|che|per|con|un|una|uno|è|non|si|del|della|nel|alla|ogni|più|su|da|dal|dei|delle|messaggio|prima|dopo|ore|ora|sito|foto|studio a|cosa|quando)\b", s, flags=re.I):
            left.append(s)
    for s in left:
        errors.append("ITALIANO RIMASTO: " + s[:90])

    if errors:
        print("\n".join(errors)); sys.exit(1)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    io.open(OUT, "w", encoding="utf-8", newline="").write(t)
    print("ok: scritto", os.path.relpath(OUT, ROOT))

main()
