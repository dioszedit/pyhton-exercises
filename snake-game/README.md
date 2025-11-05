# Snake Game (Kígyós Játék) 🐍

Klasszikus Snake játék implementáció Python Turtle Graphics használatával, objektumorientált programozási elvek alapján.

## Leírás

Ez a projekt a klasszikus Snake játékot valósítja meg, ahol a játékos egy folyamatosan mozgó kígyót irányít. A cél minél
több ételt összeszedni anélkül, hogy a kígyó nekiütközne a falnak vagy saját testének.

## Játékszabályok

- A kígyó folyamatosan mozog a kiválasztott irányba
- A nyilakkal lehet irányítani a kígyót
- Minden elfogyasztott étel után a kígyó megnő és a pontszám nő
- A játék véget ér, ha a kígyó:
    - Nekiütközik a falnak (kilép a -300 és 300 pixel közötti területről)
    - Nekiütközik saját testének (a fejétől eltekintve)

## Irányítás

- **↑ (Fel nyíl)**: Kígyó mozgatása felfelé
- **↓ (Le nyíl)**: Kígyó mozgatása lefelé
- **← (Bal nyíl)**: Kígyó mozgatása balra
- **→ (Jobb nyíl)**: Kígyó mozgatása jobbra

**Fontos:** A kígyó nem tud 180°-ot fordulni, nem mehet vissza saját testébe!

## Futtatás

```bash 
cd snake-game python main.py
```

## Projekt Struktúra

```
snake-game/ 
├── main.py # Fő program, játék loop és ütközésérzékelés 
├── snake.py # Snake osztály - a kígyó logikája és mozgása 
├── food.py # Food osztály - az étel megjelenítése és pozíciója 
├── scoreboard.py # Scoreboard osztály - pontszám kezelés és megjelenítés 
└── README.md # Ez a fájl
```

## Osztályok és Modulok

### `Snake` (snake.py)

A kígyót reprezentáló osztály.

**Főbb metódusok:**

- `create_snake()`: Inicializálja a kígyó kezdő testét (3 szegmens)
- `move()`: Mozgatja a kígyót előre
- `extend()`: Meghosszabbítja a kígyót egy szegmenssel
- `up()`, `down()`, `left()`, `right()`: Irányváltás metódusok
- `head()`: Visszaadja a kígyó fejét

### `Food` (food.py)

Az ételt reprezentáló osztály.

**Főbb metódusok:**

- `refresh()`: Új véletlenszerű pozícióba helyezi az ételt

### `Scoreboard` (scoreboard.py)

A pontszámot kezelő osztály.

**Főbb metódusok:**

- `show_score()`: Megjeleníti a jelenlegi pontszámot
- `increase_score()`: Növeli a pontszámot
- `show_game_over()`: Megjeleníti a "GAME OVER" üzenetet

### `main.py`

A játék főprogramja, amely összeköti az összes modult és tartalmazza:

- Játéktér beállítása
- Játék loop
- Eseménykezelés (billentyűzet input)
- Ütközésérzékelés (fal, saját test, étel)

## Főbb Funkciók

1. **Folyamatos mozgás**: A kígyó automatikusan halad előre
2. **Növekedés**: Étel elfogyasztása után a kígyó hosszabbodik
3. **Pontszámítás**: Minden étel +1 pont
4. **Ütközésérzékelés**:
    - Fal detektálás (játéktér határai)
    - Önütközés detektálás (testbe ütközés)
5. **Valós idejű irányítás**: Nyilakkal történő azonnali irányváltás

## Technikai Részletek

- **Python verzió**: 3.x
- **Használt könyvtár**: `turtle` (beépített), `random`
- **Képernyő méret**: 600x600 pixel
- **Játéktér**: -300 és 300 pixel között (x és y irányban)
- **Frissítési sebesség**: ~0.1 másodperc/frame
- **Kígyó szegmens méret**: 20x20 pixel
- **Étel méret**: 10x10 pixel

## Tanulási Témák

Ez a projekt az alábbi programozási konceptusokat gyakorolja:

- **OOP alapelvek**: Osztályok, öröklődés (Turtle osztályból)
- **Event-driven programozás**: Billentyűzet események kezelése
- **Game loop**: Játék fő ciklus implementálása
- **Ütközésérzékelés**: Távolság számítás, határellenőrzés
- **Lista műveletek**: Kígyó test kezelése listával
- **Koordináta-geometria**: Pozíciók és mozgások számítása
- **Modularitás**: Kód szétválasztása több fájlba
- **Típus annotációk**: Type hints használata
- **Dokumentáció**: Docstringek és kommentek

## Testreszabási Lehetőségek

A játékot könnyen személyre szabhatod:

- Kígyó színe: `snake.py` → `segment.color("white")`
- Étel színe: `food.py` → `self.color("blue")`
- Háttérszín: `main.py` → `screen.bgcolor("black")`
- Játéksebesség: `main.py` → `time.sleep(0.1)` érték változtatása
- Nehézségi szint: Kezdő szegmensek száma, pálya méret módosítása

## Fejlesztési Ötletek

- Nehézségi szintek (növekvő sebesség)
- High score mentése fájlba
- Akadályok hozzáadása a pályához
- Különböző típusú ételek (extra pontokért)
- Szünet funkció
- Menü rendszer
- Hangeffektek

## Licenc

Ez egy oktatási projekt, szabadon használható és módosítható.

---

**Jó játékot!**
