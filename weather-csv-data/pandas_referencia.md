## Pandas Gyors Referencia Kártya
- Claude AI-val generálva - Használata csak saját felelőségre


## Importálás és Beolvasás

```python
import pandas as pd

# CSV beolvasás
data = pd.read_csv('file.csv')
data = pd.read_csv('file.csv', encoding='UTF8')  # ékezetes karakterekkel
data = pd.read_csv('file.csv', sep=';')          # pontosvessző elválasztó

# Excel beolvasás
data = pd.read_excel('file.xlsx')

# JSON beolvasás
data = pd.read_json('file.json')
```

## Exportálás

```python
# CSV exportálás
data.to_csv('output.csv', index=False)           # index nélkül
data.to_csv('output.csv', encoding='UTF8')       # ékezetes karakterekkel

# Excel exportálás
data.to_excel('output.xlsx', index=False)

# JSON exportálás
data.to_json('output.json')
```

## DataFrame Vizsgálat

```python
# Alapvető információk
data.head()          # Első 5 sor
data.head(10)        # Első 10 sor
data.tail()          # Utolsó 5 sor
data.shape           # (sorok, oszlopok) tuple
data.columns         # Oszlopnevek listája
data.dtypes          # Oszlopok adattípusai
data.info()          # Részletes információk
data.describe()      # Statisztikai összefoglaló

# Méret
len(data)            # Sorok száma
data.shape[0]        # Sorok száma
data.shape[1]        # Oszlopok száma
```

## Oszlopok Elérése

```python
# Egy oszlop (Series)
data['oszlopnév']
data.oszlopnév                    # Ha nincs szóköz a névben

# Több oszlop (DataFrame)
data[['oszlop1', 'oszlop2']]

# Összes oszlop kivéve egyet
data.drop('oszlopnév', axis=1)
```

## Sorok Elérése

```python
# Index alapján
data.iloc[0]         # Első sor
data.iloc[0:5]       # Első 5 sor
data.iloc[-1]        # Utolsó sor
data.iloc[[0, 5, 10]] # 0., 5., 10. sor

# Címke alapján
data.loc[0]          # 0 indexű sor
data.loc[0:5]        # 0-5 közötti sorok (végpont is benne!)

# Feltételes kiválasztás
data[data.oszlop > 10]
data[data.oszlop == 'érték']
```

## Szűrés (Filtering)

```python
# Egy feltétel
data[data.kor > 18]
data[data.nev == 'János']

# Több feltétel ÉS kapcsolattal (&)
data[(data.kor > 18) & (data.város == 'Budapest')]

# Több feltétel VAGY kapcsolattal (|)
data[(data.nev == 'János') | (data.nev == 'Anna')]

# NEM logikai operátor (~)
data[~(data.kor > 18)]  # 18 év alattiak

# Tartalmaz (contains)
data[data.nev.str.contains('ová')]

# Lista alapján (isin)
data[data.város.isin(['Budapest', 'Szeged', 'Debrecen'])]
```

## Statisztikai Függvények

```python
# Alapvető statisztikák
data['oszlop'].mean()     # Átlag
data['oszlop'].median()   # Medián
data['oszlop'].mode()     # Módusz (leggyakoribb)
data['oszlop'].std()      # Szórás
data['oszlop'].var()      # Variancia
data['oszlop'].min()      # Minimum
data['oszlop'].max()      # Maximum
data['oszlop'].sum()      # Összeg
data['oszlop'].count()    # Elemek száma

# Kvantilisek
data['oszlop'].quantile(0.25)  # Alsó kvartilis
data['oszlop'].quantile(0.75)  # Felső kvartilis

# Egyedi értékek
data['oszlop'].unique()        # Egyedi értékek tömbje
data['oszlop'].nunique()       # Egyedi értékek száma
data['oszlop'].value_counts()  # Gyakoriság számolás
```

## Új Oszlop Létrehozása

```python
# Konstans értékkel
data['új_oszlop'] = 0

# Számítással
data['összeg'] = data['oszlop1'] + data['oszlop2']
data['arány'] = data['számláló'] / data['nevező']

# Feltételes érték
data['kategória'] = data['kor'].apply(lambda x: 'felnőtt' if x >= 18 else 'gyerek')

# Másik oszlop alapján
data['fahrenheit'] = (data['celsius'] * 9/5) + 32
```

## Törlés

```python
# Oszlop törlése
data.drop('oszlopnév', axis=1, inplace=True)
data = data.drop(['oszlop1', 'oszlop2'], axis=1)

# Sor törlése (index alapján)
data.drop(0, axis=0, inplace=True)
data = data.drop([0, 1, 2], axis=0)

# Duplikátumok törlése
data.drop_duplicates(inplace=True)
```

## Rendezés

```python
# Egy oszlop szerint növekvő
data.sort_values('oszlop')

# Egy oszlop szerint csökkenő
data.sort_values('oszlop', ascending=False)

# Több oszlop szerint
data.sort_values(['oszlop1', 'oszlop2'])

# Index szerint
data.sort_index()
```

## Hiányzó Értékek Kezelése

```python
# Ellenőrzés
data.isnull()           # Boolean DataFrame
data.isnull().sum()     # Hiányzó értékek száma oszloponként
data.notnull()          # Ellentéte az isnull()-nak

# Törlés
data.dropna()           # Sorok törlése, ha van benne NaN
data.dropna(axis=1)     # Oszlopok törlése, ha van benne NaN

# Pótlás
data.fillna(0)          # NaN-okat 0-ra cseréli
data.fillna(method='ffill')  # Előző értékkel tölti ki
data.fillna(method='bfill')  # Következő értékkel tölti ki
data.fillna(data.mean())     # Átlaggal tölti ki
```

## Csoportosítás (GroupBy)

```python
# Alapvető csoportosítás
data.groupby('kategória').mean()
data.groupby('kategória').sum()
data.groupby('kategória').count()

# Több oszlop szerint
data.groupby(['kategória1', 'kategória2']).mean()

# Egyedi aggregáció
data.groupby('kategória').agg({
    'oszlop1': 'mean',
    'oszlop2': 'sum',
    'oszlop3': 'count'
})
```

## Adatok Összevonása (Merge & Join)

```python
# Merge (mint SQL JOIN)
pd.merge(df1, df2, on='közös_oszlop')
pd.merge(df1, df2, left_on='oszlop1', right_on='oszlop2')

# Concat (egymás alá/mellé rakás)
pd.concat([df1, df2])              # Alá
pd.concat([df1, df2], axis=1)      # Mellé
```

## Adattípus Konverzió

```python
# Egész szám
data['oszlop'] = data['oszlop'].astype(int)

# Lebegőpontos szám
data['oszlop'] = data['oszlop'].astype(float)

# Szöveg
data['oszlop'] = data['oszlop'].astype(str)

# Dátum
data['dátum'] = pd.to_datetime(data['dátum'])
```

## Dátumok Kezelése

```python
# Dátum konverzió
data['dátum'] = pd.to_datetime(data['dátum'])

# Dátum részek kinyerése
data['év'] = data['dátum'].dt.year
data['hónap'] = data['dátum'].dt.month
data['nap'] = data['dátum'].dt.day
data['hét_napja'] = data['dátum'].dt.day_name()

# Dátum számítás
data['holnap'] = data['dátum'] + pd.Timedelta(days=1)
```

## Szöveg Műveletek

```python
# Kisbetű/nagybetű
data['oszlop'].str.lower()
data['oszlop'].str.upper()
data['oszlop'].str.capitalize()

# Tartalmaz
data['oszlop'].str.contains('szöveg')
data['oszlop'].str.startswith('kezdet')
data['oszlop'].str.endswith('vége')

# Csere
data['oszlop'].str.replace('régi', 'új')

# Szóköz eltávolítás
data['oszlop'].str.strip()

# Szöveg hossz
data['oszlop'].str.len()
```

## DataFrame Létrehozás

```python
# Dictionary-ből
data = pd.DataFrame({
    'oszlop1': [1, 2, 3],
    'oszlop2': ['a', 'b', 'c']
})

# Lista listákból
data = pd.DataFrame([
    [1, 'a'],
    [2, 'b'],
    [3, 'c']
], columns=['oszlop1', 'oszlop2'])

# NumPy tömbből
import numpy as np
data = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
```

## Hasznos Tippek

```python
# Oszlopnevek átnevezése
data.rename(columns={'régi_név': 'új_név'}, inplace=True)

# Index visszaállítása
data.reset_index(drop=True, inplace=True)

# Oszlop index-nek beállítása
data.set_index('oszlop', inplace=True)

# Másolat készítése (ne referencia)
data_copy = data.copy()

# Random minták kiválasztása
data.sample(5)           # 5 véletlen sor
data.sample(frac=0.1)    # 10% véletlen sor

# Unique értékek számolása
data.nunique()           # Oszloponként

# Korrelációs mátrix
data.corr()
```

## Gyakori Kombinációk

```python
# Átlag számítás csoportonként
data.groupby('kategória')['érték'].mean()

# Top 10 legnagyobb érték
data.nlargest(10, 'oszlop')

# Top 10 legkisebb érték
data.nsmallest(10, 'oszlop')

# Feltételes átlag
data[data.kategória == 'A']['érték'].mean()

# Pivot table
data.pivot_table(values='érték', index='sor', columns='oszlop', aggfunc='mean')
```

## Gyakori Hibák Elkerülése

```python
# ❌ ROSSZ: Módosítás az eredeti adaton
filtered = data[data.kor > 18]
filtered['új_oszlop'] = 1  # SettingWithCopyWarning!

# ✅ JÓ: Másolat készítése
filtered = data[data.kor > 18].copy()
filtered['új_oszlop'] = 1

# ❌ ROSSZ: Chained indexing
data[data.kor > 18]['új_oszlop'] = 1

# ✅ JÓ: loc használata
data.loc[data.kor > 18, 'új_oszlop'] = 1
```

## 🏃 Teljesítmény Optimalizálás

```python
# Kategóriák használata szöveg helyett
data['kategória'] = data['kategória'].astype('category')

# Chunk-ok olvasása nagy fájloknál
for chunk in pd.read_csv('nagy_file.csv', chunksize=1000):
    process(chunk)

# Memória használat ellenőrzése
data.memory_usage(deep=True)

# Adattípusok optimalizálása
data['int_oszlop'] = data['int_oszlop'].astype('int32')  # 64 helyett 32 bit
```

---
** További info:** https://pandas.pydata.org/docs/