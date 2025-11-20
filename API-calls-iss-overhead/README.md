# ISS Tracker - Nemzetközi Űrállomás Követő és Email Értesítő

## Projekt Leírás

Ez egy Python tanuló projekt, amely bemutatja az API-k használatát paraméterekkel és anélkül. A program figyeli a
Nemzetközi Űrállomás (ISS - International Space Station) pozícióját, és email értesítést küld, ha az űrállomás éjszaka a
megadott földrajzi koordináták közelében halad át.

## Tanulási Célok

Ez a projekt a következő Python technológiák és konceptusok megértését segíti:

- **API hívások**:
    - Paraméter nélküli API hívás (ISS pozíció lekérdezés)
    - Paraméterekkel való API hívás (napkelte/napnyugta időpontok)
- **Környezeti változók** kezelése `.env` fájlból
- **Email küldés** SMTP protokollon keresztül
- **Datetime** objektumok használata és időzónák kezelése
- **HTTP kérések** a `requests` library-vel
- **Exception handling** (hibakezelés)
- **JSON** adatformátum feldolgozása

## Funkciók

1. **Napkelte/napnyugta ellenőrzés**: A program lekérdezi a megadott koordinátákhoz tartozó napkelte és napnyugta
   időpontokat
2. **Éjszakai működés**: Csak éjszaka fut le a program (nappal automatikusan leáll)
3. **ISS pozíció követés**: Valós időben lekérdezi a Nemzetközi Űrállomás aktuális pozícióját
4. **Közelség ellenőrzés**: ±5 fokos pontossággal ellenőrzi, hogy az ISS a közelünkben van-e
5. **Email értesítés**: Ha minden feltétel teljesül, emailben értesíti a felhasználót

## Beállítás

### 1. Hozz létre egy `.env` fájlt a projekt gyökérkönyvtárában

Használd a `.env.example` fájlt sablonként:

```bash
cp .env.example .env
```

### 2. Töltsd ki a `.env` fájlt a saját adataiddal

```env
# API URL-ek
SUNRISE_SUNSET_API_URL=https://api.sunrise-sunset.org/json
ISS_POSITION_API_URL=http://api.open-notify.org/iss-now.json

# Saját pozíció (földrajzi koordináták)
MY_POSITION_LATITUDE=46.2530  # Példa: Szeged
MY_POSITION_LONGITUDE=20.1414
TIMEZONE=Europe/Budapest

# Email szerver beállítások
MAIL_SMTP=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=te@example.com
MAIL_PASSWORD=titkos_jelszó_vagy_app_jelszó
SENDER_EMAIL=te@example.com
SENDER_NAME=Te Neved
```

### Alapvető futtatás

```bash
python main.py
```

### Hogyan működik a program?

1. **Betölti a környezeti változókat** a `.env` fájlból
2. **Lekérdezi a napkelte/napnyugta időket** a megadott koordinátákhoz
3. **Ellenőrzi az aktuális időt**:
    - Ha nappal van → leállítja a programot
    - Ha éjszaka van → tovább fut
4. **Lekérdezi az ISS aktuális pozícióját**
5. **Ellenőrzi a távolságot**:
    - Ha az ISS ±5 fokon belül van → email küldés
    - Egyébként → nem történik semmi

### Automatizálás (opcionális)

Linux/Mac rendszeren beállíthatsz egy cron job-ot, hogy óránként fusson:

```bash
crontab -e
```

Add hozzá ezt a sort:

```
0 * * * * cd /út/a/projekthez && /usr/bin/python3 main.py
```

Windows-on használhatsz Task Scheduler-t hasonló célból.

## API Dokumentáció

### 1. Sunrise-Sunset API

**URL**: `https://api.sunrise-sunset.org/json`

**Paraméterek**:

- `lat` (float): Földrajzi szélesség
- `lng` (float): Földrajzi hosszúság
- `formatted` (int): 0 = ISO 8601 formátum, 1 = 12 órás formátum
- `tzid` (string): Időzóna (pl. "Europe/Budapest")

**Példa válasz**:

```json
{
  "results": {
    "sunrise": "2025-11-20T05:46:09+00:00",
    "sunset": "2025-11-20T15:32:18+00:00",
    ...
  },
  "status": "OK"
}
```

### 2. Open Notify ISS Position API

**URL**: `http://api.open-notify.org/iss-now.json`

**Paraméterek**: Nincsenek

**Példa válasz**:

```json
{
  "iss_position": {
    "latitude": "45.1234",
    "longitude": "19.5678"
  },
  "timestamp": 1732099200,
  "message": "success"
}
```

### Koordináták beállítása

A saját koordinátáidat megtalálhatod:

- https://www.latlong.net oldalon

## Kód Struktúra

```
iss-tracker/
│
├── main.py              # Fő program fájl
├── .env                 # Környezeti változók (NEM verziókezelve!)
├── .env.example         # Példa konfiguráció
├── README.md            # Ez a fájl
└── requirements.txt     # Python függőségek
```

## Licenc

Ez a projekt oktatási célokra készült és szabadon felhasználható.
