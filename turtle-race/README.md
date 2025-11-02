# Teknőc Verseny Szimuláció 🐢

## Leírás
Ez egy interaktív Python program, amely a `turtle` modult használva szimulál egy versenyt 6 különböző színű teknőc között. A felhasználó megtippelheti, melyik teknőc fogja megnyerni a versenyt, majd élőben követheti az eseményeket.

## Tanulási célok

- **Turtle Graphics**: grafikus objektumok létrehozása és kezelése
- **OOP alapok**: több objektum létrehozása, listában tárolása és metódusaik használata
- **Ciklusok**: `for` és `while` ciklusok gyakorlása
- **Véletlen számok**: `random.randint()` használata véletlenszerű mozgáshoz
- **Felhasználói input**: interakció popup ablakkal
- **Feltételes logika**: verseny végének detektálása és győztes meghatározása

## Hogyan működik?

### 1. Inicializálás
- Létrehozunk egy 500x400 pixeles ablakot
- Bekérjük a felhasználó tippjét egy színre

### 2. Teknőcök beállítása
- 6 teknőc jön létre különböző színekkel: piros, narancssárga, sárga, zöld, kék, lila
- Minden teknőc a képernyő bal oldalán indul, egymás alatt 50 pixel távolságra

### 3. A verseny
- Minden körben minden teknőc véletlenszerűen halad előre 0-10 pixel között
- Az első teknőc, amely eléri az x=230 koordinátát, megnyeri a versenyt
- A program kiírja, hogy a felhasználó nyert vagy veszített

### 4. Eredmény
- Ha a felhasználó jól tippelt, gratulációs üzenetet kap
- Ha rosszul tippelt, értesül a vereségről és a győztes színéről

## Követelmények
- Python 3.x
- `turtle` modul (beépített)
- `random` modul (beépített)

## Futtatás
```bash 
python turtle_race.py
```

## Használat
1. Indítsd el a programot
2. A megjelenő ablakban írd be a színt, amelyikre tippelsz (angolul: red, orange, yellow, green, blue, purple)
3. Figyeld a versenyt!
4. Az eredmény a konzolban jelenik meg

## Lehetséges továbbfejlesztések
- Több teknőc hozzáadása
- Akadályok beépítése a pályára
- Grafikus célvonal rajzolása
- Eredmény megjelenítése az ablakban (nem csak a konzolon)
- Újrajátszás lehetőség beépítése
- Különböző pályahosszúságok
- Pontrendszer több kör alapján

## Tanulási tippek
- Próbáld módosítani a színeket
- Változtasd meg a teknőcök kezdőpozícióját
- Állítsd be más sebességtartományt a véletlenszerű mozgáshoz
- Add hozzá a saját funkcióidat!

---
*Ez a projekt a Python Turtle Graphics tanulásához készült, kezdő programozók számára.*