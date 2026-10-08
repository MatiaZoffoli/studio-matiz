---
name: Studio Zoffoli (nome provvisorio, non confermato)
description: Soluzioni su misura - un righello da sarto su avorio, petrolio e ottone, con una fascia scura attraversata da luce d'ambra.
colors:
  ivory: "#FAF6EE"
  ivory-deep: "#F2EBDD"
  espresso: "#2B1D16"
  ink-soft: "#5E4C40"
  petrol: "#1F4D4A"
  petrol-deep: "#173B39"
  brass: "#B8913A"
  brass-line: "rgba(184, 145, 58, .85)"
  amber: "#E9A23B"
  amber-light: "#F0B657"
  amber-glow: "#FFD58A"
  night: "#221712"
  night-text: "#F6EEDF"
  night-soft: "#D9CCB6"
  night-line: "rgba(205, 191, 168, .22)"
typography:
  display:
    fontFamily: "Instrument Serif, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(3.4rem, 11.4vw, 6rem)"
    fontWeight: 400
    lineHeight: 0.98
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "Instrument Serif, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(2.4rem, 5.2vw, 4rem)"
    fontWeight: 400
    lineHeight: 1.02
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Instrument Serif, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(1.6rem, 2.6vw, 2.05rem)"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Manrope, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  lede:
    fontFamily: "Manrope, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(1.25rem, 2.2vw, 1.625rem)"
    fontWeight: 500
    lineHeight: 1.4
  label:
    fontFamily: "Manrope, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.01em"
  figure:
    fontFamily: "JetBrains Mono, ui-monospace, Consolas, monospace"
    fontSize: "clamp(1.6rem, 2.6vw, 2.1rem)"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "-0.02em"
  figure-large:
    fontFamily: "JetBrains Mono, ui-monospace, Consolas, monospace"
    fontSize: "clamp(2.4rem, 5vw, 4rem)"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "-0.03em"
  mono-small:
    fontFamily: "JetBrains Mono, ui-monospace, Consolas, monospace"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1
rounded:
  sm: "2px"
  full: "50%"
spacing:
  gutter: "clamp(1.25rem, 5vw, 4rem)"
  section: "clamp(4.5rem, 9vw, 8.5rem)"
  grid-gap: "2rem"
  row: "2rem"
  sm: "0.75rem"
  md: "1rem"
components:
  button-primary:
    backgroundColor: "{colors.petrol}"
    textColor: "{colors.ivory}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "15px 24px"
  button-primary-hover:
    backgroundColor: "{colors.petrol}"
  button-amber:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.night}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "15px 24px"
  button-amber-hover:
    backgroundColor: "{colors.amber-light}"
  band:
    backgroundColor: "{colors.night}"
    textColor: "{colors.night-text}"
  ledger-figure:
    textColor: "{colors.amber}"
    typography: "{typography.figure}"
  tape-number:
    textColor: "{colors.amber-glow}"
    typography: "{typography.figure-large}"
  ruler-read:
    backgroundColor: "{colors.petrol}"
    textColor: "{colors.ivory}"
    typography: "{typography.mono-small}"
    rounded: "{rounded.sm}"
    padding: "5px 8px"
  portrait:
    backgroundColor: "{colors.ivory-deep}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.mono-small}"
    width: "20rem"
---

# Design System: Studio Zoffoli

Nota sul nome: "Studio Zoffoli" e' un segnaposto non confermato (vedi `docs/BRAND.md`). Il sistema descrive la pagina `prova/index.html` cosi' com'e' stata costruita dopo il passaggio overdrive (GSAP 3.13 con ScrollTrigger e SplitText da jsdelivr, shader WebGL); il nome puo' cambiare senza toccare i token.

## Overview

**Creative North Star: "Il righello da sarto"**

"Su misura" preso alla lettera: la pagina e' un foglio avorio su cui qualcuno prende le misure, e la misura segue il lettore. Un righello con tacche d'ottone corre sotto il titolo e un indicatore petrolio legge i cm al passaggio del puntatore; un secondo righello, laterale, scorre con la pagina e legge la posizione. Dove un sito comune metterebbe contenitori, qui ci sono righe a filetto: registro, non vetrina.

Dopo l'overdrive l'ambra non e' piu' un colore da dosare ma una luce: nella fascia scura un fondo WebGL a luce d'ambra respira e segue il puntatore, le tacche d'ottone si accendono dove passa, in alto a destra nell'hero un bagliore caldo scalda il foglio. Su tutto una grana di carta fissa. Gli oggetti hanno peso concreto: pulsanti con ombra a offset e luce interna, il ritratto come stampa fotografica appoggiata e inclinata. Il movimento e' ricco ma ha un lessico per sezione, sempre con curve esponenziali, senza rimbalzi.

La densita' resta ariosa; serif display tagliente contro sans caldo, monospazio riservato alle cifre e alle misure.

**Key Characteristics:**
- Fogli avorio, inchiostro espresso, azioni in petrolio; ottone solo come segno.
- Ambra come luce: shader nella fascia scura, bagliore dell'hero, riflesso sul pulsante, evidenziatore che si traccia.
- Grana di carta fissa su tutta la pagina.
- Rilievi concreti: ombre a offset sui pulsanti, ritratto come stampa con ombra e inclinazione 3D.
- Bordo a zig zag da forbici dentate in cima alla fascia scura.
- Righe a filetto al posto di card e riquadri per i contenuti (elenchi, passi, condizioni).
- Monospazio solo per cifre, indici e misure; angoli a 2px.

## Colors

Palette calda e minerale: carta, inchiostro, patina di ottone, un verde petrolio profondo e una fascia notturna dove l'ambra e' luce.

### Primary
- **Verde Petrolio** (#1F4D4A): pulsanti, h2 sui fondi chiari, indici dei passi, lettura del righello, focus ring, link email, attivazione delle righe del percorso. Il pulsante usa un gradiente verticale da #2A6360 a petrolio; in hover resta petrolio con ombra piu' ampia. **Petrolio Profondo** (#173B39): ombra colorata dei pulsanti.

### Secondary
- **Ottone Antico** (#B8913A): filetti, tacche dei righelli, linea che si traccia sui problemi (3px), barra d'accento dei passi, sottolineature di navigazione, scrollbar. Variante **Filetto d'Ottone** (rgba 184,145,58,.85) per le righe del registro e il bordo della testata.

### Tertiary
- **Ambra** (#E9A23B): luce e cifre sul fondo scuro (cifre del registro, barra del metro, pulsante ambra, tacche del righello laterale sulla fascia, progress bar telefono). **Ambra Chiara** (#F0B657): evidenziatore sotto "su misura", selezione del testo, hover del pulsante ambra, tacche accese nella fascia. **Ambra Bagliore** (#FFD58A): riflesso del pulsante ambra, picco dell'evidenziatore, cifra grande del metro, bagliore dell'hero.

### Neutral
- **Avorio** (#FAF6EE): foglio principale e testata; l'hero sfuma da #FFFCF6 ad avorio.
- **Avorio Profondo** (#F2EBDD): sezioni alternate (percorso, chiusura) e fondo del ritratto.
- **Espresso** (#2B1D16): inchiostro del testo.
- **Inchiostro Tenue** (#5E4C40): testo secondario, etichette, note.
- **Notte** (#221712): fondo della fascia scura e della testata quando vi passa sopra. **Testo Notte** (#F6EEDF); **Notte Soft** (#D9CCB6, schiarito rispetto alla versione statica per reggere il contrasto sulla luce) per paragrafi e etichette del metro; **Linea Notte** (rgba 205,191,168,.22).

### Named Rules
**The Brass Is A Mark Rule.** L'ottone disegna linee, tacche e bordi; non compare mai come colore di testo (non ha contrasto sufficiente sull'avorio).
**The Amber Is Light Rule.** L'ambra e' luce, non testo corrente: vive come bagliore su avorio, come shader, tacche e cifre su Notte, come evidenziatore dietro testo espresso, come pulsante con testo Notte. Mai come colore di testo su avorio.
**The Amber Ceiling Rule.** Nello shader la miscela notte-ambra non supera k = 0,34 (`clamp(k, 0, .34)`): e' il limite che tiene Notte Soft leggibile (circa 5:1 nel punto piu' luminoso, stima) sopra la luce. Un aumento della luce va ricontrollato sul contrasto, non fatto a occhio.
**The Petrol Acts Rule.** Ogni cosa cliccabile o attiva e' petrolio sul chiaro, ambra sullo scuro.

## Typography

**Display Font:** Instrument Serif (con Iowan Old Style, Georgia, serif)
**Body Font:** Manrope (con system-ui, sans-serif)
**Label/Mono Font:** JetBrains Mono (con ui-monospace, Consolas)

**Character:** Un serif display elegante, affilato nel corsivo, contro un sans umano e leggibile; il monospazio porta il registro del sarto, cifre e centimetri.

### Hierarchy
- **Display** (400, clamp 3.4rem-6rem, 0.98): h1 dell'hero; il corsivo con evidenziatore cade solo su "su misura". Le lettere salgono in ingresso.
- **Headline** (400, clamp 2.4rem-4rem, 1.02): h2 di sezione, petrolio sul chiaro e Testo Notte nella fascia; il caso sale a clamp 2.6rem-5rem (max 16ch), la chiusura a clamp 2.8rem-5.25rem.
- **Title** (400, clamp 1.6rem-2.05rem, 1.2): h3 dei problemi e dei passi; nel registro scuro le etichette sono serif 1.5-1.8rem.
- **Body** (400, 1.0625rem, 1.6): testo corrente, 62ch nel blocco "chi sono", 34-56ch altrove.
- **Lede** (500, clamp 1.25rem-1.625rem, 1.4, max 34ch): descrittore sotto il righello.
- **Label** (600, 0.9375rem, +0.01em): pulsanti; link di navigazione 500 a 0.9375rem.
- **Figure** (mono 500, clamp 1.6rem-2.1rem): cifre del registro scuro. **Figure large** (mono 500, clamp 2.4rem-4rem, Ambra Bagliore): numero del metro. Mono 0.75rem per etichette e letture dei righelli (0.6875rem sul righello laterale); mono 1rem per indici dei passi.

### Named Rules
**The Numbers Are Mono Rule.** Solo cifre, indici e misure usano JetBrains Mono; nessun testo discorsivo.
**The Serif Speaks Rule.** I titoli sono sempre Instrument Serif a peso 400, e soltanto i titoli; il grassetto non entra nei titoli.

## Layout

Griglia a 12 colonne in un contenitore di 1360px, margini laterali fluidi (clamp 1.25rem-4rem), gap 2rem. Ritmo verticale fluido (clamp 4.5rem-8.5rem). Sequenza: hero avorio, problemi, percorso (avorio profondo), fascia scura (condizioni e caso), chi sono, chiusura (avorio profondo). L'hero mette il titolo su 8 colonne e l'azione su 4; il righello corre a tutta larghezza. Il registro divide la riga in colonne fisse: indice 1, titolo 4, testo 6 (passi); cifra 3, etichetta 3, testo 5 (condizioni).

Il caso e' una sezione alta 280vh (240vh sotto 900px) con un pannello sticky a tutto schermo: mentre si scorre, il metro cresce da 115 a 450. Con altezza sotto 700px o reduced motion diventa una sezione normale, senza sticky.

Righello laterale: da 1100px, 26px fissi a sinistra, tacche che scorrono con lo scroll (40px = 1 cm) e lettura mono verticale in cm; sotto 1100px lo sostituisce una barra di avanzamento da 3px in cima, in ambra. Sotto 900px la griglia passa a colonna unica, spariscono i link testuali e "di Matia Zoffoli", le etichette pari del righello si nascondono. Sotto 480px il pulsante in testata si restringe.

## Elevation & Depth

Sistema ibrido: filetti e cambi di fondo separano le sezioni, ma gli oggetti toccabili hanno peso fisico e la luce e' un materiale. La profondita' si legge in quattro registri: la luce (bagliore dell'hero, shader, alone sotto il cursore), la grana di carta fissa su tutto (opacita' .5, sopra ogni cosa e non cliccabile), il rilievo degli oggetti, il taglio del bordo scuro.

### Shadow Vocabulary
- **Pulsante petrolio** (`inset 0 1px 0 rgba(255,255,255,.22), 0 10px 22px -10px rgba(23,59,57,.6)`): a riposo; hover `0 16px 28px -10px rgba(23,59,57,.7)` con salita di 2px.
- **Pulsante ambra** (`inset 0 1px 0 rgba(255,255,255,.5), 0 12px 30px -10px rgba(233,162,59,.65)`): ombra a offset color ambra e riflesso interno; hover `0 18px 38px -10px rgba(233,162,59,.85)`.
- **Ritratto come stampa** (`0 1px 1px rgba(43,29,22,.14), 0 22px 44px -20px rgba(43,29,22,.5)`): stampa appoggiata, ruotata di -1,2 gradi; con puntatore fine si inclina in 3D fino a 6 gradi per asse e una luce calda (rgba 255,233,180,.5) ne segue il passaggio.
- **Barra del metro** (`drop-shadow(0 8px 14px rgba(233,162,59,.45))`): la barra ambra emette luce.

### Named Rules
**The Weight Is Offset Rule.** Le ombre sono sempre a offset verticale con raggio negativo (stretto in larghezza), mai un alone uniforme grigio; sono calde, tinte del colore dell'oggetto o dell'espresso.
**The Raised Means Touchable Rule.** Rilievo solo su cio' che si preme (pulsanti) o che e' un oggetto fisico (ritratto). Righe, titoli e sezioni restano piatti.

## Shapes

Geometria da strumento di misura: angoli a 2px su pulsanti, lettura del righello e focus; unica forma tonda e' la capocchia da 7px del marcatore. Filetti da 1px in ottone per righe e ritratto, 3px per i fili d'accento (problemi, barra dei passi); pulsanti con bordo 1.5px. I righelli sono gradienti ripetuti: sull'hero tacche da 1px ogni 8px (alte 8px), ogni 40px (16px), ogni 80px (28px, 2px di spessore); 40px equivalgono a 1 cm. Il metro del caso usa la stessa scala in percentuale (1,25%, 2,5%, 25%) su Notte.

**Il bordo a zig zag.** In cima alla fascia scura un bordo a denti di sega (triangoli 24px x 12px, colore Notte) imita tessuto tagliato con forbici dentate. E' l'unico bordo non rettilineo della pagina.

## Components

### Buttons
- **Shape:** quasi vivo (2px), padding .95rem x 1.5rem, bordo 1.5px, freccia opzionale che scorre di 3px in hover.
- **Primary:** petrolio con gradiente verticale e luce interna sul bordo alto; ombra a offset (vedi Elevation); hover: sale di 2px; press: scala .985.
- **Amber:** nella fascia scura e nella testata quando passa sulla fascia; gradiente da Ambra Bagliore ad Ambra, testo Notte, riflesso interno.
- **Si disegna a matita (effetto di hover):** al passaggio del puntatore il pulsante perde il riempimento e viene ridisegnato come uno schizzo: due contorni a mano libera, leggermente diversi e con le sbavature agli angoli (grafite, spessore 1,3 e 0,9px), poi un tratteggio a zig zag in diagonale che lo riempie come una campitura a matita (circa 0,75s, senza easing). Il testo passa al colore dello schizzo. A fine disegno lo schizzo sfuma (0,5s) nel pulsante pieno. Il tracciato e' diverso a ogni passaggio. Grafite espresso sul chiaro, ambra chiara con testo chiaro sul fondo scuro. Solo con puntatore fine e senza reduced motion; senza JavaScript il pulsante resta pieno.
- **Magnetico:** i pulsanti con `data-magnet` (hero, fascia, chiusura) seguono il puntatore con spostamento al 22% in x e 30% in y (power3, 0,6s) e tornano a zero; solo con puntatore fine e senza reduced motion; in quel caso niente salita in hover.
- **Focus:** contorno 2px petrolio con offset 3px; ambra nella fascia.

### Navigation
Testata sticky avorio: nome in serif 1.65rem con "di Matia Zoffoli" accanto; link Manrope 500 con sottolineatura ottone da 1.5px che si disegna da sinistra; CTA compatta. Filetto ottone inferiore dopo lo scroll. Sopra la fascia scura la testata diventa Notte con testo chiaro e CTA ambra (transizione .5s).

### Il righello dell'hero (firma)
Scala a tacche d'ottone con etichette mono in cm ogni 160px (4 cm). Un marcatore petrolio da 1px con capocchia segue il puntatore e mostra la lettura ("3,5 cm"). Un riflesso chiaro (soft-light) scorre sull'ottone ogni 7 secondi. In ingresso il righello si srotola da sinistra. Nascosto il marcatore su touch; decorativo (aria-hidden).

### Il righello laterale
Righello fisso a sinistra (da 1100px) che scorre con lo scroll e legge i cm della posizione; ottone e petrolio sul chiaro, ambra sulla fascia scura (i colori passano in .4s). Sotto 1100px: barra di avanzamento ambra da 3px in cima alla pagina.

### La fascia a luce d'ambra
Fondo Notte con un canvas WebGL a bassa risoluzione (meta' dei pixel, ~40 fps) che disegna rumore frattale caldo; la luce segue il puntatore con inerzia, e cresce con l'avanzare del metro (`uBoost`). Sopra, tacche d'ottone ogni 40px visibili solo in un cerchio di 300px attorno al puntatore. Si disegna solo con la fascia in vista.

### Il registro a filetti
Righe separate da filetti (ottone sul chiaro, Linea Notte sullo scuro), senza riquadri. Passi: indice mono petrolio, titolo serif, testo; sopra ogni riga una barra ottone da 3px che al passaggio si estende e vira in petrolio, con il testo da opacita' .55 a 1. Condizioni: cifra mono ambra (200 conta da 0), etichetta serif, testo Notte Soft. Problemi: tre colonne con filo ottone da 3px che si traccia.

### Il metro del caso (il metro che diventa dato)
Sezione sticky: scala su Notte, barra ambra che cresce con lo scroll, numero mono grande (Ambra Bagliore) che sale da 115 a 450 portato in cima alla barra; etichette 100-500. Poi il metro si abbassa sulla linea di base e le tacche diventano le barre di un grafico a due barre: 115 ("primi due anni", sabbia e ottone spenti) e 450 ("dopo una settimana", ambra), con la frase "quasi quattro volte" in serif corsivo. Solo i due dati reali: nessuna curva intermedia, perche' non esistono dati giornalieri. Le barre crescono animando la variabile CSS --g. Il testo del caso resta sotto.

### La quotatura (linea di quota)
Il metro dell'hero e' diventato anche linguaggio di disegno tecnico. Linea di quota sottile con frecce piene alle estremita', linee di estensione tratteggiate e misura in JetBrains Mono (px diviso 40 = cm).
- **Fissa sul titolo:** sopra "su misura", disegnata a fine introduzione (barre che si aprono dal centro, frecce, cifra che sale). Solo su desktop (nascosta sotto 900px).
- **Al passaggio del mouse, solo sui titoli principali e sul ritratto:** i sei titoli di sezione (h2) e la foto. Mai su pulsanti, descrittori o altri blocchi. Sui titoli misura il testo vero (larghezza della riga piu' lunga, non del blocco). Sul ritratto compaiono larghezza e altezza. Colore petrolio sul chiaro, ambra chiara sulla fascia scura. Su touch compaiono al tocco per circa 2 secondi.
- **Mai sopra un altro elemento:** all'attivazione si controlla (elementFromPoint) che la fascia della quota sia libera; si prova sotto, poi sopra (sul ritratto anche a destra, poi a sinistra); se non c'e' posto la quota non appare.
- **Regola:** la quotatura e' un gesto raro e pulito, non un righello su tutta la pagina.

### Il cilindro dei servizi
Le quattro card di "Cosa faccio" sono le quattro facce di un cilindro (a pianta quadrata, 90 gradi tra una faccia e l'altra) che gira davanti a chi guarda. Non c'e' scorrimento orizzontale: ruota con le frecce, con i quattro nomi sotto, trascinando (mouse e dito), con lo scorrimento orizzontale del trackpad o Maiusc con la rotella, e con le frecce della tastiera. Lo scroll verticale della pagina non viene mai intercettato.
- **Geometria:** prospettiva 1700px, raggio pari a meta' della larghezza piu' 9px, rotazione con expo.out in 1,15s; la rotazione e' sempre continua (dopo l'ultima faccia si prosegue verso la prima).
- **Spessore:** ogni faccia e' una lastra di 18px, con bordi in ottone (piu' chiaro sopra, piu' scuro sotto) e un retro scuro con tacche, visibile solo durante la rotazione.
- **Luce:** ogni faccia si scurisce con l'angolo (da 0 a 78% di nero a 90 gradi) e riceve un riflesso morbido (soft-light) che scorre mentre ruota; sotto il cilindro c'e' un'ombra a terra sfumata.
- **Contenuto:** la card in primo piano si apre da sola dopo che la rotazione si ferma (la copertura a otturatore sale e lascia una fascia col titolo e il bordo a tacche), e si apre anche al passaggio del mouse. Le altre facce sono inerti (non focalizzabili, senza clic) finche' non arrivano davanti.
- **Alternative:** senza JavaScript le card sono una griglia che si adatta alla larghezza, con lo stesso effetto di apertura al passaggio; con reduced motion la rotazione e' istantanea.

### Il ritratto
Stampa appoggiata (4:5, max 20rem, 14rem sotto 900px) con fondo Avorio Profondo e filetto ottone; oggi e' un segnaposto ("Foto di Matia da inserire") e non c'e' fotografia. Si apre come tenda dall'alto in ingresso.

## Motion

Curve: `expo.out` per le entrate, `expo.inOut` per aperture e righello, `power3.inOut` per tracciati e evidenziatore, `power3` per magnetismo e inclinazione, `power2.out` per i conteggi, `none` per tutto cio' che e' legato allo scroll (scrub). Nei CSS `cubic-bezier(.16, 1, .3, 1)` e' l'unica curva per hover e transizioni. Nessun rimbalzo ne' elastico.

Lessico per sezione:
- **Hero:** lettere che salgono (stagger .035, 1,25s) e evidenziatore che si traccia e riluce; righello che si srotola (1,6s); poi azione e testi salgono. Il titolo scorre al 10% piu' lento dello scroll.
- **Problemi:** il titolo sale per parole; il filo ottone si traccia, il testo si mette a fuoco da blur 10px.
- **Percorso:** titolo con parole che si ribaltano (rotazione X -88 gradi); le righe si accendono una a una.
- **Fascia:** titoli a lettere che si mettono a fuoco (blur 12px); righe che entrano da sinistra; la cifra sale contando.
- **Caso:** il metro cresce con lo scroll (scrub .6).
- **Chi sono:** ritratto che si apre come tenda (clip-path, 1,5s), testo le cui parole si accendono con lo scroll (da .35 a 1).
- **Chiusura:** parole che si assestano da scala 1,35 e blur; pulsanti magnetici.

Alternative, tutte parte del sistema:
- **Reduced motion:** niente animazioni di entrata, nessun movimento dello shader (frame fermo), nessun riflesso o deriva, caso senza sticky, scorrimento non morbido.
- **Telefono (sotto 760px) o puntatore non preciso:** niente WebGL; al suo posto due aloni d'ambra CSS che derivano lentamente. Su touch la luce si muove da sola.
- **Senza JavaScript o con CDN assente:** l'hero e' visibile (noscript, e rete di sicurezza di 3,5s); i contenuti restano tutti leggibili, senza animazioni.

## Do's and Don'ts

### Do:
- **Do** tenere l'ottone (#B8913A) a linee, tacche e bordi, e il petrolio (#1F4D4A) a pulsanti, h2 e indici.
- **Do** trattare l'ambra come luce: sfondo, riflesso, evidenziatore, cifre su Notte.
- **Do** tenere k dello shader a 0,34 al massimo e ricontrollare il contrasto di Notte Soft se la luce cresce.
- **Do** costruire elenchi come righe a filetto in colonne fisse della griglia a 12.
- **Do** usare JetBrains Mono per ogni cifra o misura mostrata come dato.
- **Do** mantenere angoli a 2px, ombre calde a offset sui pulsanti e curve esponenziali.
- **Do** dare a ogni nuova sezione un movimento proprio dal lessico sopra e prevedere reduced motion, telefono e assenza di JavaScript.

### Don't:
- **Don't** usare ottone o ambra come colore di testo su avorio.
- **Don't** raggruppare contenuti in card arrotondate o riquadri: le righe a filetto sono la forma; rilievo solo per pulsanti e oggetti fisici (stampe).
- **Don't** usare il monospazio per frasi o titoli.
- **Don't** usare Instrument Serif in grassetto o per testo corrente.
- **Don't** animare con rimbalzi o elasticita'; non eseguire effetti che non abbiano una versione ferma per reduced motion.
- **Don't** usare il trattino lungo nei testi: solo il corto (-).

---

## Sistema grafico v2 "boutique" (2026-10-08, in vigore: sostituisce quanto sopra)

Il resto di questo file descrive il sistema v1 (righello, ottone e petrolio, ambra), archiviato in `archivio/index-v1-ottone-petrolio.html`. Il sistema in vigore e' questo. Riferimenti: `design-ideas/` (Mercurior, Nestora, Renova, MeLABS, Nomad) e il logo in `logo/`.

**Elementi in comune dei riferimenti:** fondo caldo quasi bianco, nero caldo per testo e blocchi scuri, un solo accento sobrio, tantissimo spazio, linee sottili, numeri 01-02-03, etichette piccole in maiuscolo spaziato, titoli grandi e raffinati con una parola in corsivo, immagini a blocchi sfalsati, un blocco scuro per cambiare ritmo, scritta gigante nel piede, link con sottolineatura e freccia.

**Colori:** carta `#F7F3EC`, sabbia `#EFE8DC` e `#E3D9C9`, scheda `#FBF9F4`, inchiostro `#241E1A`, testo morbido `#6B6057`, linea `rgba(36,30,26,.16)`, champagne `#A8854F` (testo piccolo `#86672F`), notte `#161210`, testo su notte `#F3ECE0`, champagne chiaro `#D4B27C`.

**Caratteri:** Bodoni Moda (titoli, numeri, corsivo per l'accento) e Manrope 300-600 (testo; etichette in maiuscolo con spaziatura .14-.2em).

**Componenti:** pulsante a pillola con contorno, disegnato da una penna stilografica a pennino largo e poi riempito d'inchiostro (variante chiara sulle sezioni scure); link con sottolineatura; pagine dei servizi (arte su sabbia a sinistra, pannello scuro a destra con "Il problema" e "Cosa faccio") che scorrono da destra a sinistra con prospettiva; righe del percorso che si accendono; sezione scura con luce calda; stimatore su scheda chiara con campi a filo.

**Regole:** niente ombre pesanti ne' bagliori; un solo accento (champagne) usato con parsimonia; i titoli sono sempre Bodoni, mai grassetto; il movimento serve a mostrare (disegno che si traccia, pagine che scorrono, numero che sale), mai a decorare; con "riduci movimento" la sezione dei servizi diventa una pila di card.

### Rifinitura v2.1 (2026-10-08, sera): contrasto, volume, colore

Feedback di Matia: il sito era "flat", il corsivo difficile da leggere, servono immagini e colori "crispy" ma eleganti (riferimento: Renova in `design-ideas/`).

- **Corsivo tolto dai titoli:** la parola chiave resta in tondo e diventa dorata (`--gold-text` su chiaro, `--gold-light` su scuro). Il corsivo non si usa piu' nei titoli ne' nei numeri.
- **Hero scuro con anelli d'ottone in 3D** (Three.js, `#heroGl`): tre fasce di ottone con riflessi veri e una linea di luce interna, che ruotano piano e seguono il mouse e lo scroll. Ambiente generato da un canvas con pannelli di luce calda. Alternativa senza WebGL: due anelli in CSS. Con "riduci movimento" il disegno e' fermo.
- **Fascia fotografica** (`#costa`, `prova/assets/coast.svg`): tramonto sulla costa con cielo prugna, corallo e ambra. E' un **segnaposto**, da sostituire con una fotografia vera di Cesenatico. Scorre piu' piano della pagina.
- **Pagine dei servizi:** arte su fondo scuro con alone caldo e linee chiare con tratti dorati luminosi; scheda a destra chiara. Piu' contrasto tra i due lati.
- **Logo:** si usa il logo vero della suite (`logo/logo-suite-opt-1`): `prova/assets/logo-lockup.png` (scuro) e `logo-lockup-light.png` (chiaro), `logo-seal.png` e `logo-seal-light.png`. La testata passa da una versione all'altra secondo lo sfondo.
- **Ritmo:** hero scuro, fascia a colori, pagine chiare, blocco scuro caldo.
- **Da fare:** colori dei blocchi scuri piu' ricchi (luce calda anche nel blocco "casi" e "regole"), un possibile secondo colore profondo, immagini vere.

### Rifinitura v2.2 (2026-10-08)

- **Pulsanti:** nessuna penna. Un filo dorato (conic-gradient mascherato, proprieta' CSS `--a`) disegna il contorno in un secondo, l'inchiostro sale da sinistra e un riflesso attraversa il pulsante. Solo CSS, vale per ogni `.btn`; variante `.btn--light` sulle sezioni scure.
- **Stimatore:** scheda con spessore (dieci ombre a gradino), riflesso, filo dorato in alto, inclinazione `perspective` che segue il puntatore, sfondo con luce calda.
- **Chiusura:** sezione scura con gli stessi anelli 3D dell'hero, continua nel piede scuro; la testata resta scura fino in fondo.
