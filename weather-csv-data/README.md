# Időjárási Adatok Feldolgozása Python-ban

Ez a projekt bemutatja, hogyan lehet CSV fájlokat feldolgozni Python-ban két különböző módszerrel: a beépített `csv` modullal és a `pandas` könyvtárral.

## Fájlok

### Adat fájlok
- **`idojaras_adatok.csv`** - Mintaadatok heti időjárási információkkal

### Python scriptek
- **`csv_package.py`** - CSV modul használata (alapszintű)
- **`pandas_package.py`** - Pandas könyvtár használata (haladó)
- **`verseny.csv`** - Pandas által generált kimeneti fájl

---

## Tanulási Célok

### 1. CSV Modul (`csv_package.py`)
- ✅ CSV fájlok beolvasása
- ✅ Sorok iterálása
- ✅ Adatok lista formátumban való tárolása
- ✅ Szöveg → szám konverzió
- ✅ Fejléc kezelés

### 2. Pandas Könyvtár (`pandas_package.py`)
- ✅ DataFrame és Series fogalmak
- ✅ CSV beolvasás és exportálás
- ✅ Statisztikai függvények (átlag, max, min)
- ✅ Adatok szűrése feltételek alapján
- ✅ Oszlopok elérése többféle módon
- ✅ Hőmérséklet konverzió (Celsius → Fahrenheit)
- ✅ DataFrame létrehozása dictionary-ből

---

## Adatszerkezet

### `idojaras_adatok.csv` tartalma:

```csv
nap,hőmérséklet,időjárás
Hétfő,12,Napos
Kedd,14,Esős
Szerda,15,Esős
Csütörtök,14,Felhős
Péntek,21,Napos
Szombat,22,Napos
Vasárnap,24,Napos
```

**Oszlopok:**
- `nap` - A hét napja (string)
- `hőmérséklet` - Celsius fokban (integer)
- `időjárás` - Időjárási viszonyok (string)

---

## Használat

### Előfeltételek

```bash
# Pandas telepítése (csak a pandas_package.py-hoz kell)
pip install pandas
```

### Futtatás

#### CSV modul verzió:
```bash
python csv_package.py
```

#### Pandas verzió:
```bash
python pandas_package.py
```
---

## Módszerek Összehasonlítása

| Szempont | CSV Modul | Pandas |
|----------|-----------|-------|
| **Telepítés** | Beépített | Külső csomag |
| **Sebesség** | Lassabb (kis adatnál OK) | Gyors |
| **Kód hossza** | Hosszabb | Rövidebb |
| **Statisztika** | Manuális számítás | Beépített függvények |
| **Adatszűrés** | For ciklussal | Egyszerű szintaxis |
| **Memóriahasználat** | Kevés | Több |

### Mikor melyiket használjuk?

#### CSV Modul használata:
- Kis adatmennyiség (< 100 sor)
- Egyszerű feladatok
- Nincs szükség statisztikákra
- Külső függőség nélkül kell működnie

#### Pandas használata:
- Nagy adatmennyiség (> 100 sor)
- Komplex adatelemzés
- Statisztikai számítások
- Adatvizualizáció előkészítése
- Több fájl összevonása

---

## Kódrészletek

### CSV modul - Alapvető hőmérséklet kinyerés

```python
import csv

with open('idojaras_adatok.csv', encoding='UTF8') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    temperatures = []
    for row in list(csv_data)[1:]:  # Fejléc kihagyása
        temperatures.append(int(row[1]))
    print(temperatures)
```

### Pandas - Statisztikák

```python
import pandas as pd

data = pd.read_csv('idojaras_adatok.csv')

# Gyors statisztikák
print(f"Átlag: {data['hőmérséklet'].mean()}")
print(f"Maximum: {data['hőmérséklet'].max()}")
print(f"Minimum: {data['hőmérséklet'].min()}")
```

### Pandas - Adatok szűrése

```python
# Egy adott nap kiválasztása
hetfo = data[data.nap == "Hétfő"]

# Feltételes szűrés
meleg_napok = data[data.hőmérséklet > 20]

# Összetett feltétel
napos_es_meleg = data[(data.időjárás == "Napos") & (data.hőmérséklet > 20)]
```

---

## További Tanulási Források

### Hivatalos Dokumentációk:
- [Python CSV modul](https://docs.python.org/3/library/csv.html)
- [Pandas dokumentáció](https://pandas.pydata.org/docs/)
- [Pandas 10 perces tutorial](https://pandas.pydata.org/docs/user_guide/10min.html)

### Hasznos Pandas Műveletek:

```python
# DataFrame információk
data.info()                    # Oszlopok és típusok
data.describe()                # Statisztikai összefoglaló
data.head()                    # Első 5 sor
data.tail()                    # Utolsó 5 sor
data.shape                     # (sorok, oszlopok)

# Adatmanipuláció
data.sort_values('hőmérséklet') # Rendezés
data.drop_duplicates()         # Duplikátumok törlése
data.isnull().sum()            # Hiányzó értékek
data.fillna(0)                 # Hiányzó értékek pótlása

# Új oszlop létrehozása
data['fahrenheit'] = (data['hőmérséklet'] * 9/5) + 32
```

## Licenc

Ez egy oktatási projekt. Szabadon használható és módosítható tanulási célokra.

## GYIK (Gyakran Ismételt Kérdések)

**K: Melyik módszert érdemes megtanulni először?**  
V: Kezdd a CSV modullal, hogy megértsd az alapokat, majd térj át a Pandasra.

**K: A Pandas lassítja a programot?**  
V: Kis adatoknál (< 1000 sor) nincs jelentős különbség. Nagy adatoknál a Pandas gyorsabb!

**K: Kell-e telepítenem valamit?**  
V: A CSV modulhoz nem, de a Pandashoz igen: `pip install pandas`

**K: Mi történik, ha rossz az oszlopnév?**  
V: KeyError hibát kapsz. Használd a `data.columns` parancsot az oszlopnevek listázására.

---
**Jó tanulást!**