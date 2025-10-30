# Quiz Game - OOP alapú kvízjáték

Ez egy Python-ban írt kvízjáték, amely objektumorientált programozási (OOP) elveket használ.

## Leírás

A Quiz Game egy interaktív konzol alapú kvízjáték, amely igaz/hamis kérdéseket tesz fel a felhasználónak. A játék OOP alapelvek szerint van felépítve, különböző osztályokkal a kérdések, a kvíz logika és az adatok kezelésére.

## Jellemzők

- Objektumorientált felépítés
- Igaz/Hamis (True/False) kérdések
- Automatikus pontszámítás
- Végső eredmény megjelenítése
- Könnyen bővíthető kérdésbank

## Fájlstruktúra

- `main.py` - A program belépési pontja, inicializálja és futtatja a kvízjátékot
- `question_model.py` - A Question osztály definíciója
- `quiz_brain.py` - A QuizBrain osztály, amely a kvíz logikáját kezeli
- `data.py` - A kérdések adatbázisa

## Használat

A program futtatásához egyszerűen futtasd a main.py fájlt:

```bash
python main.py
```

## Működés

1. A program betölti a kérdéseket a data.py fájlból
2. Létrehozza a Question objektumokat minden kérdéshez
3. A QuizBrain kezeli a kvíz folyamatát
4. A felhasználó válaszol a kérdésekre
5. A program kiértékeli a válaszokat és megmutatja a végső pontszámot

## Testreszabás

Új kérdések hozzáadásához módosítsd a data.py fájlt a következő formátumban:

```
{
    "text": "Kérdés szövege?",
    "answer": "True"  # vagy "False"
}
```

## OOP Koncepciók

A projekt az alábbi OOP elveket alkalmazza:
- **Osztályok és objektumok**: Question, QuizBrain
- **Enkapszuláció**: Az adatok és metódusok egy osztályban
- **Modularitás**: Különálló fájlok különböző felelősségi körökkel


## Megjegyzések

A program egy egyszerű parancssori alkalmazás, amely oktatási célokra készült az OOP koncepciók bemutatására.