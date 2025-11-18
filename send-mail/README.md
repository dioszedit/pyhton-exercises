# Motivációs Idézetek Email Küldő

## Projekt Leírása

Ez a Python script automatikusan küld motivációs idézeteket email-ben hétfőnként. A program beolvassa a magyar nyelvű
motivációs idézeteket egy szöveges fájlból, véletlenszerűen kiválaszt egyet, és elküldi a megadott email címre SMTP
protokollon keresztül.

## Tanulás célok

Ez egy tanulási célú projekt, amely bemutatja a következő Python koncepciókat:

- Fájlkezelés (file I/O)
- Email küldés SMTP-n keresztül
- Környezeti változók használata
- Dátum és idő kezelés
- Véletlenszerű választás

## Telepítés

### Projekt letöltése

Töltsd le a projekt fájljait egy mappába:

- `send_motivation_quotes.py` - A fő script
- `idezetek_magyarul.txt` - A motivációs idézetek fájlja

### .env fájl létrehozása

Hozz létre egy `.env` fájlt a projekt mappájában a következő tartalommal:

```
MAIL_SMTP=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=te_email_cimed@gmail.com
MAIL_PASSWORD=titkos_jelszavad
```

**FONTOS BIZTONSÁGI MEGJEGYZÉSEK:**

- A `.env` fájl tartalmazza az érzékeny adatokat (jelszavakat)
- **SOHA** ne töltsd fel a `.env` fájlt verziókezelő rendszerbe (Git, GitHub)

### Szükséges Python könyvtárak

```bash
pip install python-dotenv
```

A következő modulok beépítettek a Python-ban, nem kell külön telepíteni:

- `datetime`
- `os`
- `random`
- `smtplib`
- `email`

## Konfiguráció

### Email címek beállítása

Nyisd meg a `send_motivation_quotes.py` fájlt és módosítsd a következő sorokat:

```python
sender_email = "kuldo@mailproba.com"  # Cseréld le a saját email címedre
sender_name = "Küldő Neve"  # Adj meg egy nevet
receiver_email = "fogado@mailproba.com"  # Cseréld le a címzett email címére
receiver_name = "Fogadó Neve"  # A címzett neve
```

### Napok beállítása

A script jelenleg **hétfőn** küld emailt (mivel `day_of_week == 0`).

A hét napjainak számai:

- `0` = Hétfő
- `1` = Kedd
- `2` = Szerda
- `3` = Csütörtök
- `4` = Péntek
- `5` = Szombat
- `6` = Vasárnap

**Több napra is küldéshez:**

```python
if day_of_week in [0, 3]:  # Hétfő és csütörtök
```

## Használat

### Futtatás parancssorból

```bash
python send_motivation_quotes.py
```

### Automatikus futtatás beállítása

#### Linux - Cron

1. Nyisd meg a crontab szerkesztőt:

```bash
crontab -e
```

2. Add hozzá a következő sort (hétfő reggel 9:00-kor):

```bash
0 9 * * 1 cd /teljes/utvonal/projekt/mappához && python3 send_motivation_quotes.py
```

A cron formátum magyarázata:

```
* * * * *
│ │ │ │ │
│ │ │ │ └─── Hét napja (0-6, 0=vasárnap, 1=hétfő)
│ │ │ └───── Hónap (1-12)
│ │ └─────── A hónap napja (1-31)
│ └───────── Óra (0-23)
└─────────── Perc (0-59)
```

## Fájlstruktúra

```
projekt_mappa/
│
├── send_motivation_quotes.py    # Fő Python script
├── idezetek_magyarul.txt         # Motivációs idézetek fájlja
├── .env                          # Környezeti változók (érzékeny adatok)
├── .gitignore                    # Git kizárási lista
└── README.md                     # Ez a dokumentáció
```

## Továbbfejlesztési lehetőségek

- **HTML formátumú emailek:** Szebb megjelenítés HTML formátummal
- **Többszörös címzettek:** Lista használata több címzetthez
- **Napló (logging):** Nyomon követés, hogy mikor került email küldésre
- **Hibakezelés:** Try-except blokkok hozzáadása a robusztusság érdekében
- **Email csatolmányok:** Képek vagy fájlok csatolása az emailhez

## Licenc

Ez egy oktatási célú projekt, szabadon felhasználható és módosítható.

## Kapcsolódó linkek

- [Python smtplib dokumentáció](https://docs.python.org/3/library/smtplib.html)
- [Python email dokumentáció](https://docs.python.org/3/library/email.html)
- [Python-dotenv dokumentáció](https://pypi.org/project/python-dotenv/)