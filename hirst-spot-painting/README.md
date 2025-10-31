
# Hirst Spot Painting - Pöttyös Festmény Generátor

Ez a projekt egy Damien Hirst-stílusú pöttyös festményt generál Python turtle grafikával. A program egy képfájlból nyeri ki a színeket, majd azokat használva egy négyzetrács elrendezésben rajzol színes pöttyöket.

## Damien Hirst Spot Paintings

Damien Hirst "Spot Paintings" sorozata 1986-ban kezdődött és a konceptuális művészet ikonikus alkotásai közé tartozik. 
A festmények jellegzetessége:

- Szabályos elrendezésű, egyenlő méretű körök
- Minden pötty más színű
- Véletlenszerű színelrendezés
- Nincs két egyforma szín egy műalkotáson belül (a programban használt színpaletta ezt nem fedi le)

Ez a projekt ezt a koncepciót reprodukálja programozottan, bemutatva, hogyan lehet művészetet és programozást ötvözni.

### Főbb Funkciók

- **Színkinyerés képből**: A `colorgram` könyvtár segítségével domináns színeket nyer ki egy képfájlból
- **Rács alapú rajzolás**: Szabályos négyzetrács elrendezésben helyezi el a pöttyöket
- **Véletlenszerű színválasztás**: Minden pötty véletlenszerűen választott színű a kinyert palettából
- **Testreszabható paraméterek**: Könnyen módosítható rács méret, pötty méret és távolság

## Fájlok

- **`hirst_spot_painting.py`** - A fő program, amely a festményt generálja
- **`hirst_colors.webp`** - A forrás kép, amelyből a színpaletta származik

## Követelmények

### Python verzió
- Python 3.x

### Függőségek

A program a következő csomagokat használja:

```bash  
pip install colorgram.py
```
**Beépített modulok** (telepítés nem szükséges):
- `turtle` - Grafikus rajzoláshoz
- `random` - Véletlenszerű színválasztáshoz

## Használat

### Futtatás
```bash
cd hirst-spot-painting python hirst_spot_painting.py
```

A program egy ablakot nyit meg és elkezdi rajzolni a pöttyös festményt. Az ablak bezárásához kattints rá az egérrel.

### Testreszabás

A program elején található konstansok módosításával testre szabhatod a festményt:
```python 
GRID_SIZE: int = 10 # A rács mérete (10x10 pötty) 
DOT_SPACING: int = 50 # Pöttyök közötti távolság pixelben 
DOT_SIZE: int = 20 # Egy pötty átmérője pixelben
```


**Példák:**

- **Nagyobb festmény**: `GRID_SIZE = 15` (15x15 pötty)
- **Sűrűbb elrendezés**: `DOT_SPACING = 30`
- **Nagyobb pöttyök**: `DOT_SIZE = 30`

### Saját színpaletta használata

Ha saját képpel szeretnél dolgozni:

1. Helyezz egy képfájlt a `hirst-spot-painting` mappába
2. Módosítsd a fájlnevet a `hirst_colors()` függvényben:
   ```python
   list_colors = colorgram.extract('sajat_kep.jpg', 15)
   ```
3. A második paraméter (15) határozza meg, hány színt nyerjen ki

## Tanulási Célok

Ez a projekt az alábbi programozási konceptusokat mutatja be:

- **Külső könyvtárak használata**: `colorgram` csomag integrálása
- **Képfeldolgozás alapjai**: Színek kinyerése képekből
- **Turtle graphics használata**: Komplex pozicionálás és rajzolás
- **Típus annotációk**: Modern Python típusdeklarációk
- **Függvények tervezése**: Moduláris, újrafelhasználható kód
- **Konstansok használata**: Konfigurálható paraméterek
- **RGB színkezelés**: Színek reprezentálása és használata
- **Matematikai pozicionálás**: Rács alapú koordináta-rendszer
