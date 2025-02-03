# BICF Booking Bot

BICF Booking Bot è un bot automatico basato su Selenium che consente di prenotare un posto in una biblioteca o struttura tramite un'interfaccia web. Il bot può essere eseguito immediatamente o programmato per avviarsi automaticamente alle 7:00 del mattino.

## Dipendenze e requisiti

- **Versione di python:** `3.*` (testato su versioni da `3.8.*` a `3.11.*`)
- **Installare le dipendenze:** `pip install -r dependencies.txt`
- **Google Chrome** installato
- **chromedriver** compatibili con la propria versione di Chrome (https://sites.google.com/chromium.org/driver/)

## Configurazione

Prima di eseguire il bot, assicurati di configurare corettamente il file `data.py`.

## Utilizzo 

Esempio di utilizzo:
```
python main.py --time-amount 2 --session-start "08:00" --scheduled "y"
```

Assicurati di essere all'interno della directory `src` quando esegui il comando.

### Argomenti

- `--time-amount` (obbligatorio): Specifica la durata della prenotazione in ore.

- `--session-start` (obbligatorio): Specifica l'orario di inizio della sessione nel formato HH:MM.

- `--scheduled` (opzionale): Se impostato su y, il bot attenderà fino alle 07:00 AM per eseguire la prenotazione.

Se l'argomento `--scheduled` è omesso o impostato su un valore diverso da **y**, il bot verrà eseguito immediatamente.

## Note

Il bot continuerà a riprovare fino a quando al prenotazione non viene confermata.

Il bot si basa sull'utilizzo della sezione **riprenota** del sito interessato.

## Struttura del progetto 

```
bicf_booking_bot
│── driver
│   └── chromedriver.exe          # WebDriver per Chrome
│── src
│   ├── booking_bot.py            # Funzioni di supporto per il bot
│   ├── data.py                   # Configurazione e credenziali
│   ├── main.py                   # Script principale del bot
├── dependencies.txt              # File che mostra le dipendenze
└── README.md                     # Documentazione
```