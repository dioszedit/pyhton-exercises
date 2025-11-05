# Pong Game (Pong Játék) 🏓

Klasszikus Pong játék implementáció Python Turtle Graphics használatával, OOP elvek alapján.

## Leírás

Ez a projekt a klasszikus Pong játékot valósítja meg, ahol két játékos egymás ellen játszik. A cél 10 pontot elérni úgy, hogy megvéded a saját oldalad, és az ellenfél nem éri el a labdát. Az első játékos, aki eléri a 10 pontot, megnyeri a játékot.

## Játékszabályok

- Két játékos játszik egymás ellen (bal és jobb oldal)
- A labda folyamatosan pattog a játéktéren
- Pontot szerzel, ha az ellenfeled nem éri el a labdát (a labda eléri az ellenfél oldalfalát)
- A labda visszapattan a felső és alsó falakról
- A labda visszapattan az ütőkről és irányt vált
- Minden egyes pont után a labda visszakerül a játéktér közepére
- **A játék akkor ér véget, amikor valamelyik játékos eléri a 10 pontot**

## Irányítás

### Bal oldali játékos:
- **W**: Ütő mozgatása felfelé
- **S**: Ütő mozgatása lefelé

### Jobb oldali játékos:
- **↑ (Fel nyíl)**: Ütő mozgatása felfelé
- **↓ (Le nyíl)**: Ütő mozgatása lefelé

## Futtatás

```bash
cd pong-game
python main.py
```

## Projekt Struktúra

```
pong-game/
├── main.py          # Fő program, játék indítása
├── gameboard.py     # Gameboard osztály - játéktér és főciklus
├── ball.py          # Ball osztály - labda mozgása és pattanása
├── racket.py        # Racket osztály - ütők kezelése
├── scoreboard.py    # Scoreboard osztály - pontszám megjelenítés
├── constans.py      # Konstansok (határok, irányok, formázás)
└── README.md        # Ez a fájl
```

## Osztályok és Modulok

### `Gameboard` (gameboard.py)

A játékteret és a fő játéklogikát kezelő osztály.

**Főbb metódusok:**
- `create_net()`: Létrehozza a közép szaggatott hálóvonalat
- `racket_listener()`: Beállítja a billentyűzet eseménykezelőket
- `run()`: A játék fő ciklusa (mozgás, ütközésellenőrzés, pontszámítás)
- `show_game_over()`: Megjeleníti a "GAME OVER" üzenetet

### `Ball` (ball.py)

A labdát reprezentáló osztály.

**Főbb metódusok:**
- `move()`: Mozgatja a labdát az aktuális irányba
- `bounce_y()`: Megfordítja a labda függőleges irányát (felső/alsó fal)
- `bounce_x()`: Megfordítja a labda vízszintes irányát (ütő találat)
- `reset_position()`: Visszahelyezi a labdát a játéktér közepére új véletlenszerű iránnyal

### `Racket` (racket.py)

Az ütőket reprezentáló osztály.

**Főbb metódusok:**
- `up()`: Felfelé mozgatja az ütőt
- `down()`: Lefelé mozgatja az ütőt

### `Scoreboard` (scoreboard.py)

A pontszámot kezelő és megjelenítő osztály.

**Főbb metódusok:**
- `show_score()`: Megjeleníti a jelenlegi pontszámot
- `increase_score()`: Növeli a pontszámot eggyel

### `constans.py`

Konstansokat tartalmazó modul:
- Irányok (UP, DOWN, LEFT, RIGHT)
- Koordináta keretek (MAX_X, MIN_X, MAX_Y, MIN_Y)
- Lépésköz és formázási beállítások

### `main.py`

A játék belépési pontja, amely létrehozza a játéktáblát és elindítja a játékot.

## Főbb Funkciók

1. **Kétjátékos mód**: Két játékos egyidejű játéka egy gépen
2. **Folyamatos mozgás**: A labda automatikusan pattog a játéktéren
3. **Pontszámítás**: Mindkét játékos külön pontszámmal rendelkezik
4. **Ponthatár rendszer**: A játék 10 pontig tart, az első játékos, aki eléri, megnyeri a játékot
5. **Automatikus labda reset**: Minden pont után a labda visszakerül a középre új iránnyal
6. **Fizikai szimúláció**: Realisztikus pattanás a falakon és ütőkön
7. **Vizuális háló**: Szaggatott középvonal a játéktér elválasztására
8. **Valós idejű irányítás**: Azonnali reakció a billentyűleütésekre
9. **Játék vége detektálás**: Automatikus leállás 10 pont elérésekor

## Technikai Részletek

- **Python verzió**: 3.x
- **Használt könyvtár**: `turtle` (beépített), `time`, `random`
- **Képernyő méret**: 800x600 pixel
- **Játéktér**: -360 és 360 pixel között (x irány), -280 és 280 között (y irány)
- **Frissítési sebesség**: ~0.1 másodperc/frame
- **Ütő méret**: Téglalap (1x5 méretarány)
- **Labda méret**: Kör alakú
- **Labda lépésköz**: ±10 pixel/mozgás
- **Ütő lépésköz**: 20 pixel/mozgás

## Tanulási Témák

Ez a projekt az alábbi programozási konceptusokat gyakorolja:

- **OOP alapelvek**: Osztályok, öröklődés (Turtle osztályból), kompozíció
- **Event-driven programozás**: Billentyűzet események kezelése
- **Game loop**: Játék fő ciklus implementálása
- **Ütközésérzékelés**: Távolság számítás (`distance()` metódus), határellenőrzés
- **Fizikai szimuláció**: Pattanás logika implementálása
- **Koordináta-geometria**: Pozíciók és mozgások számítása
- **Modularitás**: Kód szétválasztása több fájlba és osztályba
- **Típus annotációk**: Type hints használata minden metódusnál
- **Dokumentáció**: Részletes docstringek és kommentek magyarul
- **Véletlenszerűség**: Random kezdő irány a labdának
- **Több objektum kezelése**: Két játékos, két scoreboard szinkron működése

## Testreszabási Lehetőségek

A játékot könnyen személyre szabhatod:

- **Ponthatár**: `gameboard.py` → `if self.person_left.score == 10 or self.person_right.score == 10:` sor módosítása
- **Labda sebessége**: `ball.py` → `x_move` és `y_move` értékek változtatása
- **Játéksebesség**: `gameboard.py` → `time.sleep(0.1)` érték módosítása
- **Színek**: Háttér, labda, ütők, háló színének megváltoztatása
- **Pálya méret**: `constans.py` → MAX/MIN koordináták módosítása
- **Ütő méret**: `racket.py` → `shapesize()` paraméterek változtatása
- **Pontszám pozíció**: `gameboard.py` → Scoreboard pozíció koordináták
- **Ütő sebessége**: `constans.py` → `MOVE_DISTANCE` érték módosítása

## Fejlesztési Ötletek

- **Állítható ponthatár**: A játék végének pontszámának testreszabása (pl. 5, 10, 15 pont)
- **Nehézségi szintek**: Növekvő labda sebesség idővel vagy pont után
- **AI ellenfél**: Egyjátékos mód számítógép ellenfél hozzáadásával
- **Hangeffektek**: Ütközés hangok hozzáadása (ütő találat, falba ütközés, pontszerzés)
- **Színes pálya témák**: Különböző színsémák választása
- **Labda effektek**: Forgó animáció, fénycsóva
- **Statisztikák**: Leghosszabb rally, átlagos ütés/perc, pontok eloszlása
- **Szünet funkció**: Játék megállítása és folytatása (Space billentyű)
- **Képernyővédő mód**: Automatikus játék AI vs AI
- **Több labda mód**: Egyszerre több labda a pályán
- **Power-up-ok**: Speciális képességek (nagyobb ütő, lassabb labda, kisebb ütő az ellenfélnél)
- **High score táblázat**: Legjobb eredmények mentése fájlba játékonként
- **Nyerő kijelzése**: Megjeleníti, hogy melyik játékos nyert (bal vagy jobb)
- **Új játék funkció**: Játék újraindítása a vége után billentyűleütéssel

## Játék Dinamika

### Pontszerzés
- Pontot akkor szerzel, amikor az ellenfeled nem éri el a labdát
- Ha a labda eléri a bal oldali falat, a jobb oldali játékos kap pontot
- Ha a labda eléri a jobb oldali falat, a bal oldali játékos kap pontot
- Minden pont után a labda visszakerül a középre új véletlenszerű iránnyal

### Játék vége
- A játék akkor ér véget, amikor valamelyik játékos eléri a 10 pontot
- A győztes az a játékos, aki először éri el a ponthatárt
- A játék végeztével megjelenik a "GAME OVER" felirat

### Stratégia
- Pozicionálás: Az ütő megfelelő magasságban tartása
- Reakcióidő: Gyors reagálás a labda irányváltozásaira
- Előrelátás: A labda pályájának előrejelzése
- Védekezés: A labda elérése, mielőtt az eléri a hátsó falat

## Licenc

Ez egy oktatási projekt, szabadon használható és módosítható.

---

**Jó játékot! 🏓**