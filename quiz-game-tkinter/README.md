# Quiz Game - True or False

Egy egyszerű grafikus felületű kvízjáték alkalmazás Python-ban, amely igaz/hamis kérdéseket tesz fel egy online API-ból.

## Funkciók

- Igaz/Hamis kérdések az Open Trivia Database API-ból
- Grafikus felhasználói felület (Tkinter)
- Valós idejű pontszám követés
- Vizuális visszajelzés (zöld/piros színek)
- Automatikus kérdésváltás 2 másodperc után

## Telepítés

### Követelmények

- Python 3.10 vagy újabb
- `requests` könyvtár

## Használat

Futtasd a `main.py` fájlt:

```bash
python main.py
```

A program automatikusan betölt 10 kérdést az Open Trivia Database API-ból, és megjelenik a grafikus felület.

### Irányítás

- **Zöld gomb (✓)**: Igaz válasz
- **Piros gomb (✗)**: Hamis válasz

## Projekt szerkezete

```
quiz-game/
│
├── main.py                 # Belépési pont
├── question_data.py        # API kommunikáció és adatbetöltés
├── question_model.py       # Question osztály definíciója
├── quiz_brain.py          # Kvíz logika
├── quiz_ui.py             # Grafikus felhasználói felület
└── README.md              # Projekt dokumentáció
```

### Fájlok leírása

#### `main.py`

Az alkalmazás belépési pontja. Inicializálja a kérdéseket, a kvíz logikát és a GUI-t.

#### `question_data.py`

A `QuestionData` osztály felelős a kérdések letöltéséért az Open Trivia Database API-ból.

**Főbb funkciók:**

- Kérdések letöltése az API-ból
- HTML entitások dekódolása
- Hibakezelés és újrapróbálkozás

#### `question_model.py`

Egyszerű `Question` osztály, amely egy kvízkérdést reprezentál.

**Attribútumok:**

- `text`: A kérdés szövege
- `answer`: A helyes válasz (True/False)

#### `quiz_brain.py`

A `QuizBrain` osztály kezeli a kvíz logikáját.

**Főbb funkciók:**

- Kérdések nyomon követése
- Pontszám kezelés
- Válaszok ellenőrzése

#### `quiz_ui.py`

A `QuizUI` osztály létrehozza a grafikus felületet Tkinter használatával.

**Főbb funkciók:**

- Kérdések megjelenítése
- Gombok kezelése
- Vizuális visszajelzés
- Pontszám megjelenítés

## Testreszabás

### Kérdések számának módosítása

A `main.py` fájlban változtasd meg a számot:

```python
question_bank = QuestionData(20)  # 20 kérdés betöltése
```

### Színek módosítása

A `quiz_ui.py` fájlban módosíthatod a színeket:

```python
THEME_COLOR = "#375362"  # Háttérszín
```

### Kérdéstípusok módosítása

A `question_data.py` fájlban módosíthatod az API paramétereket:

```python
params = {
    "amount": q_num,
    "type": "boolean",
    "category": 18,  # Például: Computer Science kategória
    "difficulty": "easy"  # Nehézségi szint
}
```

Elérhető kategóriák: https://opentdb.com/api_category.php

## Felhasznált technológiák

- **Python 3.10+**: Programozási nyelv
- **Tkinter**: GUI framework
- **Requests**: HTTP könyvtár
- **Open Trivia Database API**: Kérdések forrása

## API Részletek

Az alkalmazás az [Open Trivia Database](https://opentdb.com/) ingyenes API-ját használja.

**API végpont:** `https://opentdb.com/api.php`

**Paraméterek:**

- `amount`: Kérdések száma
- `type`: Kérdés típusa (boolean)

## Hibakezelés

- Az API válasz kód ellenőrzése
- Automatikus újrapróbálkozás 1 másodperc késleltetéssel
- HTML entitások automatikus dekódolása

## Fejlesztési lehetőségek

- [ ] Többféle kérdéstípus támogatása (multiple choice)
- [ ] Kategória választás a GUI-ban
- [ ] Nehézségi szint beállítása
- [ ] Statisztikák mentése fájlba
- [ ] Legjobb eredmények tárolása
- [ ] Időlimit hozzáadása kérdésenként
- [ ] Hangeffektek
- [ ] Többjátékos mód

## Licenc

Ez a projekt oktatási célokra készült.

