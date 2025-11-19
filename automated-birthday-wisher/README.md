# 🎂 Automatikus Születésnapi Üdvözlő

Automatikus email küldő program, amely a mai dátumhoz tartozó születésnapokra véletlenszerű levélsablonokkal küld
üdvözletet.

## Funkciók

- ✅ Automatikus születésnapi ellenőrzés CSV fájlból
- ✅ Véletlenszerű levélsablon kiválasztás
- ✅ Személyre szabott üdvözletek (név behelyettesítés)
- ✅ Biztonságos email küldés SMTP-n keresztül
- ✅ Környezeti változók használata érzékeny adatok tárolására

## Beállítások

### Szükséges csomagok telepítése

**Telepítendő csomagok:**

- `pandas` - CSV fájl kezelésére
- `python-dotenv` - környezeti változók betöltésére

### Környezeti változók beállítása

Másold le a `.env.example` fájlt `.env` néven:

```bash
cp .env.example .env
```

Nyisd meg a `.env` fájlt és töltsd ki a saját adataiddal:

```env
MAIL_USERNAME="temail@gmail.com"
MAIL_PASSWORD="app_password"
MAIL_SMTP="smtp.gmail.com"
MAIL_PORT=587

SENDER_EMAIL="temail@gmail.com"
SENDER_NAME="Neved"
```

### Születésnapok hozzáadása

Szerkeszd a `birthdays.csv` fájlt és add hozzá az embereket:

```csv
név,email,év,hónap,nap
Anya,mam@example.com,1965,10,1
Apa,dad@example.com,1963,2,15
Öcsém,bro@example.com,1990,11,20
```

**Oszlopok:**

- `név` - A személy neve (ez jelenik meg az emailben)
- `email` - Email cím
- `év` - Születési év
- `hónap` - Születési hónap (1-12)
- `nap` - Születési nap (1-31)

### Levél sablonok testreszabása

A `letter_templates/` mappában 3 sablon található:

- `letter_1.txt`
- `letter_2.txt`
- `letter_3.txt`

Szerkeszd a sablon fájlokat tetszés szerint. A `[NAME]` placeholder automatikusan lecserélődik a címzett nevére.

**Példa sablon:**

```
Szia [NAME]!

Boldog születésnapot!

Minden jót kívánok az idei évre!

Üdvözlettel,
Angela
```

## Használat

### Egyszerű futtatás

```bash
python main.py
```

### Kimenet példa

```
1 db mai születésnap van!
Email sikeresen elküldve: János

Kész! Minden email elküldve.
```

Ha nincs ma születésnap:

```
Nincs ma szülinap.
```

### Automatizálás

#### macOS/Linux - Cron

Nyisd meg a crontab szerkesztőt:

```bash
crontab -e
```

Add hozzá a következő sort (minden nap reggel 9:00-kor):

```bash
0 9 * * * cd /path/to/birthday-wisher && /usr/bin/python3 main.py
```

## Projekt struktúra

```
birthday-wisher/
│
├── main.py                 # Fő program
├── birthdays.csv           # Születésnapok adatbázisa
├── .env                    # Környezeti változók (TITKOS!)
├── .env.example            # Környezeti változók mintája
├── .gitignore              # Git kizárási lista
├── README.md               # Dokumentáció
│
└── letter_templates/       # Levél sablonok mappája
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt
```

## Licenc

Ez a projekt oktatási és személyes használatra készült.
