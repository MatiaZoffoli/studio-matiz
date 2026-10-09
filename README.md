# Studio Matiz

Cartella del progetto: `C:\Users\gisel\dev\studio-matiz` (repository git, spostata da OneDrive il 2026-10-08). Il nome era "MZ Business Consultancy", provvisorio: il brand e' Studio Matiz.

Consulenza per piccole e medie imprese italiane: siti web, menu digitali, assistenza continuativa e, dove serve, automazione e AI. Si parte dagli stabilimenti balneari e dai ristoranti della costa romagnola. Fondatore: Matia Zoffoli.

## Da dove cominciare

1. [CLAUDE.md](CLAUDE.md) - regole di lavoro, profilo, fatti stabili. Si legge sempre per primo.
2. [docs/STATO-DEI-LAVORI.md](docs/STATO-DEI-LAVORI.md) - dove siamo.
3. [docs/BACKLOG.md](docs/BACKLOG.md) - cosa c'e' da fare e cosa aspetta una decisione.

## Mappa della cartella

| File | Cosa contiene |
|---|---|
| [CLAUDE.md](CLAUDE.md) | Profilo del fondatore, caso di riferimento, clienti target, regole di lavoro |
| [docs/STATO-DEI-LAVORI.md](docs/STATO-DEI-LAVORI.md) | Fase attuale, fatto, prossimo passo |
| [docs/BACKLOG.md](docs/BACKLOG.md) | Decisioni aperte, cose da fare, idee |
| [docs/DECISIONI.md](docs/DECISIONI.md) | Registro delle scelte prese |
| [docs/PROCEDURE.md](docs/PROCEDURE.md) | Percorso del cliente, registro ore, come si tiene aggiornato il progetto |
| [docs/OFFERTE.md](docs/OFFERTE.md) | Bozza delle offerte e dei prezzi |
| [docs/RICERCA-DI-MERCATO.md](docs/RICERCA-DI-MERCATO.md) | Prima ricerca su settore, prezzi e rischi |
| [docs/CONCORRENTI.md](docs/CONCORRENTI.md) | Mappatura dei concorrenti locali e audit di 13 siti |
| [docs/PRIMO-INCONTRO.md](docs/PRIMO-INCONTRO.md) | Scaletta del primo incontro e scheda cliente |
| [docs/MODELLO-CHECKUP.md](docs/MODELLO-CHECKUP.md) | Procedura e modello del rapporto di check-up |
| [docs/BRAND.md](docs/BRAND.md) | Brief del brand, personalita', direzioni di nome (incluso ZOMA), domini, direzione visiva |
| [docs/SUPABASE-CONTATTI.md](docs/SUPABASE-CONTATTI.md) | Archivio dei contatti dello stimatore su Supabase (Francoforte): tabella, funzione, protezioni, cosa resta da fare |
| [docs/PREVENTIVO-E-CONTRATTO.md](docs/PREVENTIVO-E-CONTRATTO.md) | Bozza del modello di preventivo, dell'accordo di servizio (con cura continua e GDPR) e del resoconto mensile |
| [modelli/](modelli/) | Documenti dello studio da compilare e stampare: `preventivo.html` e `.pdf` (2 pagine), `accordo-di-servizio.html` e `.pdf` (3 pagine) e `esempio-preventivo.html` e `.pdf` (preventivo compilato con dati di fantasia), `resoconto-mensile.html` e `.pdf` (modello a due pagine: resoconto del mese e resoconto di fine rodaggio) con `esempio-resoconto-mensile.html` e `.pdf` (compilato), con il logo e lo stile del sito. Si modificano gli `.html` e si rigenerano i PDF |
| [.claude/skills/voce-studio-matiz/](.claude/skills/voce-studio-matiz/SKILL.md) | La voce di Studio Matiz come skill: carattere, ritmo, lessico da preferire e da evitare, filtro finale, e in `esempi.md` i testi del sito sbagliati con le alternative. Si usa per sito, email, risposte automatiche, messaggi, documenti |
| [docs/EMAIL-E-RISPOSTE.md](docs/EMAIL-E-RISPOSTE.md) | Email e messaggi nella voce di Studio Matiz: risposte automatiche dal sito, conferme del primo incontro, messaggi lungo il percorso (riepilogo, check-up, preventivo, rodaggio, testimonianza), WhatsApp Business e risposte rapide |
| [docs/CHI-SONO.md](docs/CHI-SONO.md) | Il materiale per la biografia: fatti, mentalita', motivazioni e valori di Matia, nelle sue parole, con le regole di tono (prima persona, umile) e di riservatezza |
| [docs/LOGO-PROMPT.md](docs/LOGO-PROMPT.md) | Prompt per generare alternative di logo (brief comune e cinque opzioni) |
| [docs/STIMATORE.md](docs/STIMATORE.md) | Come funziona lo stimatore a fasce del sito, come calcola, cosa manca per collegarlo ai contatti |
| [docs/LISTINO-E-TEMPI.md](docs/LISTINO-E-TEMPI.md) | Proposta di listino a fasce, tempi di consegna, forfait del primo mese, proprieta' di dominio e contenuti |
| [docs/INGLESE.md](docs/INGLESE.md) | Versione inglese: come si genera (`tools/build_en.py`), scelte di traduzione da confermare |
| [modelli/en/](modelli/en/) | Documenti dello studio in inglese: `quote`, `service-agreement`, `monthly-report` e gli esempi compilati (`example-quote`, `example-monthly-report`), in `.html` e `.pdf`; traduzione degli originali italiani, che fanno fede |
| [email/](email/) | Anteprime delle email automatiche (`anteprime/`, con dati di fantasia) e firme di Matia in HTML (`firma-it.html`, `firma-en.html`) |
| [docs/EMAIL-AND-REPLIES-EN.md](docs/EMAIL-AND-REPLIES-EN.md) | Email e messaggi in inglese (A3-A5, B1-B10, C1-C3) |
| [docs/RESEND.md](docs/RESEND.md) | Email automatiche dal sito: passi, link e segreti per collegare Resend |
| [docs/RICERCA-MARCHIO.md](docs/RICERCA-MARCHIO.md) | Come fare la ricerca marchio completa su TMview, e l'esito della ricerca del 2026-10-09 |
| [docs/CONSULENTE-MARCHIO.md](docs/CONSULENTE-MARCHIO.md) | Elenco per il consulente in proprieta' industriale: cosa portare, domande, chi contattare in zona, bozza di messaggio |
| [supabase/functions/contatto/index.ts](supabase/functions/contatto/index.ts) | Funzione dei contatti con avviso e conferma via Resend (da distribuire) |
| [prova/privacy.html](prova/privacy.html) | Bozza dell'informativa privacy (da completare e far controllare) |
| [docs/TESTI-SITO.md](docs/TESTI-SITO.md) | Diagnosi dei testi, voce, struttura del sito di lancio, bozza v2 dei testi, schema della richiesta di fascia di prezzo |
| [docs/ANALISI-BATTISTINI.md](docs/ANALISI-BATTISTINI.md) | Analisi del sito del concorrente piu' vicino e proposte per contenuti, pagine e strumenti del nostro |
| [PRODUCT.md](PRODUCT.md) | Fatti del prodotto per Impeccable (utenti, posizionamento, vincoli di brand) |
| [DESIGN.md](DESIGN.md) | Sistema grafico ricavato dalla pagina di prova (colori, caratteri, componenti, regole) |
| [prova/index.html](prova/index.html) | Pagina di prova del sito, una pagina in HTML statico (nome, testi e condizioni in bozza) |
| `.impeccable/` | File di lavoro di Impeccable: contratto della pagina, schede, schermate di controllo (non si modificano a mano) |

## Cartelle da creare quando servono

- `clienti/<nome>/` - una cartella per cliente: scheda, check-up, registro ore, proposte
- `marketing/` - sito proprio, materiali, contenuti
- `archivio/` - versioni superate dei documenti

## Regola d'oro

Quando emerge un'informazione che servira' ancora, si scrive subito nel file giusto. La conversazione si perde, i file no.
