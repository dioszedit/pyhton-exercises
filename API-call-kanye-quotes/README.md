# Kanye Says... 🎤

Egy egyszerű Python GUI alkalmazás, amely véletlenszerű Kanye West idézeteket jelenít meg
a [Kanye Rest API](https://api.kanye.rest/) segítségével.

## Leírás

Ez egy Tkinter-alapú desktop alkalmazás, amely lekérdez és megjelenít véletlenszerű Kanye West idézeteket. A felhasználó
egyszerűen rákattinthat Kanye fejére, és egy új inspiráló (vagy éppen vitatható) idézetet kap.

## Funkciók

- Grafikus felhasználói felület (GUI) Tkinter-rel
- Valós idejű API kommunikáció
- Véletlenszerű Kanye West idézetek
- Egyszerű, intuitív használat - csak kattints Kanye fejére!
- Magyar nyelvű kommentek (oktatási célból)

## Követelmények

- Python 3.x
- `tkinter` (általában a Python telepítéssel együtt jön)
- `requests` library

## Használat

Futtasd a programot:

```bash
python main.py
```

Az alkalmazás elindulásakor automatikusan lekér egy idézetet. Új idézetért kattints Kanye fejére!

## Projekt struktúra

```
kanye-quotes/
│
├── main.py           # Fő alkalmazás kód
├── background.png    # Háttér buborék kép
├── kanye.png        # Kanye West portré
└── README.md        # Ez a fájl
```

## Tanulási célok

Ez a projekt remek példa a következő koncepciók gyakorlására:

- GUI fejlesztés Tkinter-rel
- HTTP API kérések kezelése
- JSON adatok feldolgozása
- Fájl elérési utak kezelése
- Event-driven programozás (gomb események)

## API információ

Az alkalmazás a [Kanye Rest API](https://api.kanye.rest/)-t használja:

- Endpoint: `https://api.kanye.rest/`
- Visszatérési érték: JSON objektum `quote` kulccsal
- Példa válasz: `{"quote": "I feel like I'm too busy writing history to read it."}`

## Licensz

Ez egy oktatási célú projekt, szabadon felhasználható és módosítható.

---

**Megjegyzés:** Ez a projekt csak szórakozásból és tanulási célból készült. Nem áll kapcsolatban Kanye West-tel vagy
képviselőivel.