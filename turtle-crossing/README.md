# 🐢 Turtle Crossing - Autó Kerülgetős Játék

Egy egyszerű, Python Turtle grafikus könyvtárral készült ügyességi játék kezdőknek.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Turtle Graphics](https://img.shields.io/badge/turtle-graphics-orange.svg)

## 📖 Projekt Leírása

A **Turtle Crossing** egy klasszikus "átkelős" játék, ahol a játékos egy teknőst irányít, és megpróbál átjutni az úton
anélkül, hogy nekimenne a jobbról balra száguldó autóknak. Minden sikeres átkelés után a játék nehezedik - az autók
egyre gyorsabban mozognak!

Ez egy **oktatási célú projekt**, amelyet Python kezdők számára készült, hogy bemutassa:

- Objektum-orientált programozást (OOP)
- Turtle grafikus könyvtár használatát
- Játék logika implementálását
- Ütközés detektálást
- Egyszerű animációt

## Játékmenet

### Cél

Irányítsd a teknőst a képernyő aljától a tetejéig úgy, hogy elkerülöd az autókat!

### Irányítás

- **↑ (Fel nyíl)**: Mozgatás felfelé
- **↓ (Le nyíl)**: Mozgatás lefelé

### Szabályok

1. Minden sikeres átkelés után a **szint nő**
2. Magasabb szinteken az **autók gyorsabban** mozognak
3. Ha nekimész egy autónak, **vége a játéknak**
4. Az autók véletlenszerűen jelennek meg és balra mozognak

## Indítás

### Rendszerkövetelmények

- Python 3.8 vagy újabb
- Turtle könyvtár (alapértelmezetten a Pythonnal települ)

### Futtatás

```bash
cd turtle-crossing python main.py
```

Ennyi! Nincs szükség extra csomagok telepítésére, mivel a Turtle könyvtár a Python standard library része.

## Fájlstruktúra

```
turtle-crossing/
│
├── main.py              # Főprogram - játéklogika
├── player.py            # Játékos teknős osztálya
├── car_manager.py       # Autók kezelése (létrehozás, mozgatás)
├── scoreboard.py        # Szint megjelenítés
└── README.md            # Ez a fájl
```

### Fájlok részletes leírása

#### `main.py`

A játék főprogramja. Tartalmazza:

- Képernyő beállítását
- Játék ciklust (game loop)
- Billentyűzet kezelést
- Ütközés ellenőrzést
- Szintlépés logikát

#### `player.py`

A játékos teknőst reprezentáló osztály:

- `move_up()`: felfelé mozgatás
- `move_down()`: lefelé mozgatás
- `reset_position()`: visszahelyezés a kezdőpozícióba

#### `car_manager.py`

Az autók kezelését végző osztály:

- `create_car()`: új autó létrehozása véletlenszerű színnel és pozícióval
- `move_cars()`: összes autó mozgatása és törlése, ha kimennek a képernyőről
- `increase_speed()`: játék sebességének növelése

#### `scoreboard.py`

Szint megjelenítő osztály:

- `show_level()`: aktuális szint kiírása
- `increase_level()`: szint növelése
- `show_game_over()`: játék vége üzenet megjelenítése

## Amit Megtanulhatsz Ebből a Projektből

### 1. Objektum-Orientált Programozás (OOP)

- Osztályok létrehozása és öröklés (`Player(Turtle)`)
- Metódusok definiálása
- Attribútumok használata

### 2. Turtle Graphics

- Alakzatok rajzolása és mozgatása
- Képernyő beállítások
- Eseménykezelés (billentyűzet)

### 3. Játékfejlesztés Alapok

- Játék ciklus (game loop)
- Ütközés detektálás
- Nehézségi szint szabályozás
- FPS (Frame Per Second) kezelés

### 4. Python Módszerek

- Random számok generálása
- Lista műveletek
- Time/sleep használat
- Type hints használata

## Testreszabási Lehetőségek

### Autók színeinek megváltoztatása

`car_manager.py` fájlban:

```python
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# Adj hozzá új színeket vagy változtasd meg a meglévőket!
```

### Játék sebességének módosítása

`car_manager.py` fájlban:

```python
MOVE_INCREMENT = 10  # Csökkentsd lassabb, növeld gyorsabb autókért
```

### Kezdő sebesség változtatása

`car_manager.py` fájlban az `__init__` metódusban:

```python
self.car_speed = 0.2  # Nagyobb érték = lassabb játék kezdés
```

### Autók megjelenési gyakoriságának módosítása

`main.py` fájlban:

```python
if random.randint(0, 2) == 1:  # Változtasd meg a tartományt!
    car_manager.create_car()
# Például: random.randint(0, 5) == 1 → ritkábban jelennek meg autók
```

## Ismert Problémák és Megoldások

### Windows platformon lassú a játék

**Probléma**: Windows rendszeren a `time.sleep()` felbontása ~15-16 ms.

**Megoldás**: A kód már optimalizálva van erre, lásd `car_manager.py` `increase_speed()` metódusát.

### Autók átfednek egymással

**Normális viselkedés**: Az autók véletlenszerűen jelennek meg, néha átfedhetnek. Ez nem befolyásolja a játékmenetet.

### Fejlesztési ötletek

- [ ] Hang effektek hozzáadása
- [ ] Életpontok rendszer (3 esély)
- [ ] High score mentés fájlba
- [ ] Különböző pályák (éjszakai mód, autópálya, stb.)
- [ ] Power-up-ok (lassítás, pajzs)
- [ ] Több sáv különböző sebességű autókkal

## Licenc

Ez a projekt szabadon felhasználható oktatási célokra.

---

**Jó játékot! 🐢**