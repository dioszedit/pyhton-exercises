# 🐿️ Central Park Mókus Felmérés 2018 - Adatelemzés

Python script a 2018-as New York-i Central Park Mókus Népszámlálás adatainak elemzésére és összesítésére.

![Squirrel](https://img.shields.io/badge/Squirrels-3000%2B-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Required-orange)

## Projekt Leírása

Ez a projekt a 2018-as Central Park Mókus Népszámlálás adatait elemzi, amely New York City egyik legnagyobb állampolgári tudományos projektje volt. A script megszámolja a mókusokat bundaszín szerint, és egy egyszerű összesítő táblázatot készít az eredményekről.

### Mit csinál a program?

1. ✅ Beolvassa a teljes mókus felmérési adatbázist
2. ✅ Szétválogatja a mókusokat bundaszín szerint (szürke, vörös, fekete)
3. ✅ Megszámolja az egyes kategóriákba tartozó mókusokat
4. ✅ Létrehoz egy összesítő táblázatot
5. ✅ Elmenti az eredményt CSV fájlba

---

## Adatforrás

**Hivatalos adatbázis:**  
[NYC Open Data - 2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data)

### Felmérés Részletei:

- **Időpont:** 2018. október 6-20. (14 nap)
- **Helyszín:** Central Park, Manhattan, New York
- **Résztvevők:** 300+ önkéntes
- **Rögzített mókusok:** 3,000+
- **Adatpontok:** 31 különböző adat mókusonként

### Rögzített Adatok:

A teljes adatbázis többek között az alábbiakat tartalmazza:
- Egyedi mókus azonosító
- GPS koordináták
- Bundaszín (elsődleges és kiemelő színek)
- Életkor becslés (adult/juvenile)
- Tevékenységek (futás, evés, mászás stb.)
- Hangok (csiripelés, nyögés stb.)
- Viselkedések (farokcsóválás, közeledés stb.)

---

## Fájlstruktúra

```
projekt-mappa/
│
├── main.py                                           
├── README.md                                         
│
├── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv  # Bemeneti adat
└── squirrel_count.csv                                # Kimeneti eredmény
```

---

## Használat

### Előfeltételek

```bash
# Python 3.x telepítése (ha még nincs)
# Ellenőrzés:
python --version

# Pandas telepítése
pip install pandas
```

### Futtatás

**Futtasd a scriptet:**
   ```bash
   python main.py
   ```

**Eredmény:**
   A program létrehoz egy `squirrel_count.csv` fájlt az alábbi tartalommal:

   ```csv
   ,Fur Color,Count
   0,gray,2473
   1,red,392
   2,black,103
   ```

## Tanulási Célok

Ez a projekt kiváló gyakorlási lehetőség az alábbi készségek fejlesztésére:

- ✅ **Pandas alapok:** DataFrame műveletek, szűrés, aggregáció
- ✅ **Adatelemzés:** Valós adatok feldolgozása és összesítése
- ✅ **CSV kezelés:** Fájlok olvasása és írása

---

## További Információk

### Hasznos Linkek:

- [Pandas Dokumentáció](https://pandas.pydata.org/docs/)
- [NYC Open Data Platform](https://opendata.cityofnewyork.us/)

## Licenc

Ez egy oktatási projekt, amely a NYC Open Data nyilvános adatait használja.

**Adatlicenc:** [NYC Open Data Terms of Use](https://opendata.cityofnewyork.us/overview/#termsofuse)