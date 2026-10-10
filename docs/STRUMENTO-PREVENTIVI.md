# Strumento per i preventivi

Creato il 2026-10-10. Compila un preventivo in PDF, nello stile del sito, da **un solo file di dati** per cliente. Sostituisce la compilazione a mano dei modelli statici in `modelli/` (`preventivo.html` resta come riferimento di stile).

## Come si usa

1. Copiare il modello dei dati nella cartella del cliente:
   `modelli/esempio-preventivo.json` in `clienti/<nome-cliente>/preventivo.json`
2. Compilare il file (nomi, lavori, importi, tempi, scelte facoltative). Lasciare fuori `numero`: lo assegna lo strumento.
3. Dalla cartella del progetto:

```bash
python tools/preventivo.py clienti/<nome-cliente>/preventivo.json
```

Lo strumento scrive nella stessa cartella `preventivo-<numero>.pdf` e `.html`, e stampa totale, acconto e saldo, piu' l'elenco dei campi rimasti vuoti (nel PDF sono evidenziati in giallo).

Un esempio compilato, con dati di fantasia, e' `modelli/preventivo-2026-000.pdf`.

## Cosa calcola da solo

- **Numero:** formato anno-numero (2026-001, 2026-002...). Il progressivo sta in `clienti/_registro.json`. Il numero viene scritto nel file dei dati, cosi' rilanciando lo strumento il preventivo ha sempre lo stesso numero.
- **Totale:** somma dei lavori, meno lo sconto se c'e'. Con `iva_aliquota` (es. 22) mostra imponibile, IVA e totale; senza, scrive "IVA se dovuta".
- **Acconto 50% alla firma e saldo 50% alla consegna** (decisione del 2026-10-10).
- Le voci non usate spariscono: sconto, opzioni, cura continua, tempi per lavoro.
- Il documento si impagina da solo (di solito 2 pagine) con numero di pagina e "Bozza da far controllare" nel piede.

## I campi del file dei dati

| Campo | Cosa e' | Obbligatorio |
|---|---|---|
| `lingua` | `it` o `en` | no (predefinita `it`) |
| `numero`, `data`, `validita_giorni` | numero (automatico), data `aaaa-mm-gg` (oggi se manca), validita' (30) | no |
| `cliente` | `nome`, `attivita`, `indirizzo`, `piva_cf` | si' |
| `referente` | `nome`, `ruolo`, `email`, `telefono` | si' |
| `capito` | due o tre frasi su quanto emerso nel primo incontro | si' |
| `lavori` | elenco: `titolo`, `importo`, `include` (elenco puntato), `tempi` (testo facoltativo) | si' |
| `non_incluso` | testo o elenco di cio' che non si fa | consigliato |
| `sconto` | `etichetta` e `importo` (es. il check-up scalato) | no |
| `iva_aliquota` | numero, es. 22 | no |
| `opzioni` | scelte facoltative fuori dal totale: `titolo`, `descrizione`, `importo` (numero o testo, es. "da 150 a 400 euro") | no |
| `tempi` | `giorni`, `correzioni` (2), `inizio`, `consegna` (date), oppure `testo` libero | si' |
| `serve` | cosa serve dal cliente per cominciare | si' |
| `cura` | `forfait` (250), `canone` ("100-150"), `ore_incluse` (2); se manca, la sezione non compare | no |
| `hosting` | costo annuo di dominio e hosting, testo ("50-120") | no |
| `giorni_fattura`, `giorni_consegna_dati` | 10 e 10 | no |

## Dati dello Studio

In `modelli/dati-studio.json`: indirizzo, partita IVA, IBAN, email, telefono, logo (percorso dell'immagine) e `bozza`. Finche' un campo e' vuoto compare in giallo nel PDF. **Mettere `"bozza": false` solo quando il testo e' stato controllato da un professionista** (vedi `docs/PREVENTIVO-E-CONTRATTO.md`, "Prima di usarlo con un cliente vero").

## Cartella dei clienti

`clienti/` e' esclusa dal repository (`.gitignore`): contiene dati di persone e di attivita'. Non viene salvata su GitHub: i preventivi e i dati dei clienti vanno tenuti in un backup tuo.

## Da sapere

- Il PDF si genera con Chrome, che deve essere installato nel percorso predefinito.
- L'**Accordo di servizio** (`modelli/accordo-di-servizio.pdf`) si allega a mano, una volta per cliente.
- La versione inglese usa gli stessi campi: i testi dei lavori e il resto li scrivi tu nella lingua del documento.
- Le due cifre da rivedere dopo il primo caso reale (sito 2.500-3.000, avvio profilo social 400-600) stanno in `docs/LISTINO-E-TEMPI.md`.
