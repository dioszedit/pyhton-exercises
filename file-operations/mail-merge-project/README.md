# Levélküldő Program

Ez egy Python projekt, amely automatikusan készít személyre szabott meghívó leveleket egy sablon alapján.

## Leírás

A program beolvassa a levélsablont és a meghívottak neveit, majd minden személy számára elkészít egy egyedi levelet, amelyben a `[name]` helyőrző ki van cserélve a tényleges névre.

## Mappa Struktúra

A projekt futtatása előtt győződj meg róla, hogy a következő mappa struktúra létezik:

```
project/
│
├── main.py
│
├── input/
│   ├── Letters/
│   │   └── letter_text.txt
│   └── names/
│       └── invited_names.txt
│
└── output/
    └── ready-to-send/
        └── (ide kerülnek a generált levelek)
```

## Fájlok

### input/Letters/letter_text.txt
A levél sablonfájl. Tartalmazzon egy `[name]` helyőrzőt, amit a program majd kicserél a tényleges névre.

**Példa:**
```
Kedves [name],

Meghívlak a szombati születésnapi bulimra.

Remélem tudsz jönni!

P.
```

### input/names/invited_names.txt
A meghívottak nevei, soronként egy-egy név.

**Példa:**
```
Aang
Zuko
Appa
Katara
Sokka
Momo
Uncle Iroh
Toph
```

## Használat

1. **Hozd létre a szükséges mappákat** (ha még nem léteznek)
2. **Töltsd ki a sablonfájlt** (`input/Letters/letter_text.txt`) a levél szövegével
3. **Add meg a neveket** (`input/names/invited_names.txt`) soronként
4. **Futtasd a programot:**

```bash
python main.py
```

## Kimenet

A program az `output/ready-to-send/` mappában létrehozza a személyre szabott leveleket.

A fájlnevek formátuma: `letter_for_név.txt`

**Példa fájlnevek:**
- `letter_for_aang.txt`
- `letter_for_zuko.txt`
- `letter_for_uncle_iroh.txt` (szóközök helyett alsóvonás, kisbetűk)

## Működés

A program három fő lépésben működik:

1. **Sablon beolvasása**: Beolvassa a levél sablon teljes tartalmát
2. **Nevek beolvasása**: Beolvassa az összes meghívott nevét egy listába
3. **Levelek generálása**: Végigmegy a neveken, és minden névhez:
   - Létrehoz egy új fájlt
   - Kicseréli a `[name]` helyőrzőt a tényleges névre
   - Elmenti a személyre szabott levelet

## Megjegyzések

- A program automatikusan eltávolítja a felesleges szóközöket és sortöréseket a nevekből
- A generált fájlnevek kisbetűsek lesznek
- A nevekben lévő szóközök alsóvonásra (`_`) cserélődnek a fájlnevekben

## Követelmények

- Python 3.x

## Tanulási Célok

Ez a projekt segít megérteni:
- Fájlok olvasását és írását Pythonban
- A `with open()` kontextuskezelő használatát
- String metódusok használatát (`strip()`, `replace()`, `lower()`)
- Ciklusok alkalmazását listákon
- F-string formázást