# 🍅 Pomodoro Timer

Egy egyszerű Pomodoro időzítő alkalmazás Python Tkinter-rel, ami segít a produktív munkavégzésben.

## Mi az a Pomodoro technika?

A Pomodoro technika egy időgazdálkodási módszer, amit Francesco Cirillo fejlesztett ki az 1980-as években:

1. **25 perc munka** (1 Pomodoro)
2. **5 perc rövid szünet**
3. Ismételd 4-szer
4. **20 perc hosszú szünet**

Ez összesen 4 munka periódust jelent rövid szünetekkel, majd egy hosszabb pihenőt.

## Funkciók

- **Vizuális időzítő**: Paradicsom grafika a háttérben
- **Automatikus váltás**: Munka → Szünet → Munka ciklusok
- **Haladás követés**: Jelölések mutatják a befejezett körök számát
- **Színkódolt állapotok**:
    - Zöld = Munka periódus
    - Rózsaszín = Rövid szünet
    - Piros = Hosszú szünet
- **Start/Mégse gombok**: Könnyű kezelés

## Technológiák

- **Python 3.x**
- **Tkinter** (beépített GUI könyvtár)

## Futtatás

```bash
python main.py
```

## Projekt struktúra

```
pomodoro-timer/
│
├── main.py              # Főprogram - GUI és eseménykezelés
├── pomodoro_timer.py    # PomodoroTimer osztály - logika
├── constants.py         # Konstansok (színek, időtartamok, betűtípus)
├── tomato.png          # Paradicsom ikon
└── README.md           # Ez a fájl
```

## Fájlok részletesen

### `main.py`

A felhasználói felület és az eseménykezelés. Tartalmazza:

- Ablak létrehozása és beállítása
- GUI elemek (címke, gombok, canvas)
- `proceed_timer()` függvény - másodpercenkénti frissítés

### `pomodoro_timer.py`

A `PomodoroTimer` osztály, amely tartalmazza a timer logikáját:

- `start()` - Timer indítása
- `reset()` - Visszaállítás alaphelyzetbe
- `processing()` - Másodpercenkénti feldolgozás
- `timer_text()` - Időformázás ("05:00" formátum)
- `level_text()` - Befejezett körök száma
- `timer_status_data()` - Aktuális állapot (cím, szín)

## Használat

1. **Indítás**: Kattints a **"Start"** gombra
2. **Munka**: 25 percig dolgozz (zöld "Munka" felirat)
3. **Szünet**: 5 perc pihenés (rózsaszín "Szünet")
4. **Ismétlés**: Ez folytatódik automatikusan
5. **Hosszú szünet**: 4 munka periódus után 20 perc pihenés (piros "Szünet")
6. **Leállítás**: A **"Mégse"** gomb újraindítja az egészet

### Vizuális jelzések

- **Cím színe**: Mutatja az aktuális állapotat
- **Pipa jelek (✓)**: Minden befejezett munka periódus után egy újabb
- **Időzítő**: "00:00" formátumban a hátralévő idő

## Testreszabás

A `constants.py` fájlban módosíthatod:

```python
# Rövidebb teszteléshez:
WORK_MIN = 1  # 1 perc munka
SHORT_BREAK_MIN = 1  # 1 perc rövid szünet
LONG_BREAK_MIN = 2  # 2 perc hosszú szünet

# Klasszikus Pomodoro:
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

## Tanulási célok

Ez a projekt példa az alábbiak gyakorlására:

- ✅ OOP (Object-Oriented Programming) - osztályok használata
- ✅ Tkinter GUI programozás
- ✅ Időzítők kezelése
- ✅ Canvas widget használata képekkel
- ✅ Típus annotációk (Type hints)
- ✅ String formázás (f-strings)
- ✅ Moduláris kódszervezés

## További fejlesztési ötletek

- Hang lejátszása a periódusok végén
- Statisztikák mentése (hány Pomodoro-t teljesítettél ma)
- Beállítások ablak (egyedi időtartamok)

## Licenc

Ez egy tanulási projekt. Szabadon használhatod és módosíthatod.
