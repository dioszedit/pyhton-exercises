# Flash Cards - Angol-Magyar Szótanuló Alkalmazás

## Leírás

Ez egy interaktív **flashcard (memóriakártya)** alkalmazás, amely segít angol szavak megtanulásában. A program Python
nyelvben íródott, Tkinter GUI könyvtárat használ, és egyszerű, intuitív felületet biztosít a hatékony szótanuláshoz.

### Főbb jellemzők:

- ✅ Grafikus felhasználói felület (GUI)
- ✅ Automatikus kártyaforgatás 3 másodperc után
- ✅ Tanult szavak eltávolítása a listából
- ✅ Haladás mentése és folytatása
- ✅ Vizuális visszajelzés (számláló)

## Funkciók

### 1. **Automatikus Kártyaforgatás**

- A kártya elülső oldalán az **angol szó** jelenik meg
- 3 másodperc múlva automatikusan megfordul
- A hátsó oldalon a **magyar fordítás** látható

### 2. **Interaktív Gombok**

- **❌ Piros gomb (bal)**: "Nem tudom" - Új kártyát tölt be, a szó a listában marad
- **✅ Zöld gomb (jobb)**: "Tudom" - Eltávolítja a szót a listából, mert megtanultad

### 3. **Haladás Követése**

- A jobb felső sarokban látható a **hátralévő szavak száma**
- A program automatikusan menti a még tanulandó szavakat
- Folytathatod a tanulást ott, ahol abbahagytad

### 4. **Gratulációs Üzenet**

- Ha minden szót megtanultál, megjelenik egy gratulációs üzenet
- A program törli a haladási fájlt és kész vagy az újrakezdésre

### Követelmények

```bash
Python 3.7+
pandas könyvtár
tkinter (általában alapból telepítve van a Python-nal)
```

### Projekt Struktúra Létrehozása

```
flash-cards/
│
├── main.py                          # Fő program fájl
│
├── data/
│   ├── english_words.csv            # Eredeti szólista
│   └── words_to_learn.csv           # Még tanulandó szavak (automatikusan generálódik)
│
└── images/
    ├── card_front.png               # Kártya elülső oldal képe
    ├── card_back.png                # Kártya hátsó oldal képe
    ├── right.png                    # Zöld "tudom" gomb képe
    └── wrong.png                    # Piros "nem tudom" gomb képe
```

### CSV Fájlok Formátuma

**english_words.csv** példa:

```csv
English,Magyar
cat,macska
dog,kutya
house,ház
book,könyv
```

### Futtatás

```bash
python main.py
```

## Projekt Struktúra

### Fő Komponensek

#### 1. **Konstansok és Globális Változók**

```python
BACKGROUND_COLOR = "#B1DDC6"  # Kellemes zöld háttér
FONT_NAME = "Arial"  # Alapértelmezett betűtípus
after_id  # Időzítő azonosító
current_card  # Aktuális kártya adatai
```

#### 2. **Adatkezelő Függvények**

**`read_data()`**

- Betölti a tanulandó szavakat
- Először a `words_to_learn.csv` fájlt keresi
- Ha nem létezik, az `english_words.csv` fájlt tölti be

#### 3. **Kártya Kezelő Függvények**

**`next_card()`**

- Véletlenszerűen választ egy új kártyát
- Megjeleníti az angol szót
- Elindít egy 3 másodperces időzítőt

**`back_card()`**

- Megfordítja a kártyát
- Megjeleníti a magyar fordítást

**`right_answer()`**

- Eltávolítja a szót a listából
- Frissíti a számlálót
- Elmenti a haladást
- Betölti a következő kártyát

#### 4. **GUI Elemek**

- **Canvas**: A kártya megjelenítéséhez
- **Label**: Számláló megjelenítéséhez
- **Button**: Interakciós gombok

## Hogyan Működik?

### 1. Indításkor

```
Program indul
    ↓
Betölti a szavakat
(words_to_learn.csv VAGY english_words.csv)
    ↓
Megjelenít egy véletlenszerű angol szót
    ↓
3 másodperc múlva megfordítja a kártyát
    ↓
Várja a felhasználó választását
```

### Felhasználó Választása

```
❌ Piros gomb (Nem tudom)
    ↓
A szó MARAD a listában
    ↓
Új kártyát tölt be

✅ Zöld gomb (Tudom)
    ↓
Eltávolítja a szót a listából
    ↓
Elmenti a words_to_learn.csv fájlt
    ↓
Frissíti a számlálót
    ↓
Új kártyát tölt be
```

### 3. Haladás Mentése

A program automatikusan menti a még tanulandó szavakat a `data/words_to_learn.csv` fájlba minden alkalommal, amikor a
zöld gombot megnyomod. Így ha bezárod az alkalmazást, legközelebb folytathatod ott, ahol abbahagytad.

## Tanulási Célok

Ez a projekt kiváló példa a következő programozási fogalmak gyakorlására:

### 1. **Python Alapok**

- ✅ Függvények definiálása és használata
- ✅ Globális változók kezelése
- ✅ Típushintingek (`-> None`, `list[dict]`)
- ✅ Docstring-ek használata (dokumentációs szövegek)

### 2. **GUI Programozás (Tkinter)**

- ✅ Ablak létrehozása és konfigurálása
- ✅ Canvas használata képek és szövegek megjelenítéséhez
- ✅ Gombok és események kezelése
- ✅ Layout kezelés (grid)

### 3. **Adatkezelés (Pandas)**

- ✅ CSV fájlok olvasása és írása
- ✅ DataFrame használata
- ✅ Dictionary konverziók

### 4. **Hibakezelés**

- ✅ Try-except blokkok használata
- ✅ Fájl létezés ellenőrzése (`os.path.exists`)

### 5. **Időzítés**

- ✅ `window.after()` metódus használata késleltetett függvényhíváshoz
- ✅ Időzítő leállítása (`window.after_cancel()`)

### 6. **Véletlenszerűség**

- ✅ `random.choice()` használata véletlen elem kiválasztásához

## Licence

Ez a projekt oktatási célokra készült és szabadon használható tanulási célokra.
