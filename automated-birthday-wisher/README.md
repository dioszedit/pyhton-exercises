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

## 🎯 Használat

### Egyszerű futtatás

```bash
python main.py
```

### Kimenet példa

```
1 db mai születésnap találva!
Email küldése: János (janos@example.com)
✓ Email sikeresen elküldve: János

Kész! Minden email elküldve.
```

Ha nincs ma születésnap:

```
Nincs ma szülinap.
```

### Automatizálás

#### PythonAnywhere - Ingyenes felhő megoldás

A [PythonAnywhere](https://www.pythonanywhere.com/) egy ingyenes Python hosting szolgáltatás, amely ideális ehhez a
projekthez.

**Miért jó?**

- ✅ Ingyenes (Basic account elegendő)
- ✅ Nincs szükség saját számítógépre, ami egész nap fut
- ✅ Beépített ütemezett feladat (scheduled task) funkció
- ✅ Egyszerű webes felület

**Beállítás lépésről lépésre:**

1. **Regisztráció**
    - Menj a [pythonanywhere.com](https://www.pythonanywhere.com/) oldalra
    - Hozz létre egy ingyenes fiókot (Beginner account)

2. **Fájlok feltöltése**
    - Kattints a **Files** menüpontra
    - Hozz létre egy új mappát: `birthday-wisher`
    - Töltsd fel a projektfájlokat:
        - `main.py`
        - `birthdays.csv`
        - `.env` (a kitöltött környezeti változókkal!)
        - `letter_templates/` mappa tartalmával

3. **Ütemezett feladat beállítása**
    - Kattints a **Tasks** menüpontra
    - **Daily scheduled task** résznél:
        - **Time (UTC):** `07:00` (Ez 9:00 magyar idő szerint)
        - **Command:**

```bash
       cd /home/felhasznalonev/birthday-wisher && python3 main.py
```

       (Cseréld ki a `felhasznalonev`-et a saját PythonAnywhere felhasználónevedre!)

- Kattints a **Create** gombra

4. **Teszt futtatás**
    - A Bash konzolban futtasd manuálisan:

```bash
     cd birthday-wisher
     python3 main.py
```

- Ellenőrizd, hogy minden rendben működik-e

**Megjegyzések:**

- Az ingyenes fiók UTC időzónában működik, ezért +1 vagy +2 órát kell számolni (nyári/téli időszámítás szerint)
- Az ütemezett feladat minden nap ugyanabban az időpontban fut
- A log kimenet megtekinthető a **Tasks** oldalon

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
