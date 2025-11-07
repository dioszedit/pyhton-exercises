# ============================================================================
# CSV FELDOLGOZÁS PANDAS KÖNYVTÁRRAL
# ============================================================================
# A Pandas egy hatékony adatelemzési könyvtár nagyobb adatmennyiség kezelésére
# Dokumentáció: https://pandas.pydata.org/docs/
import pandas as pd

# CSV FÁJL BEOLVASÁSA
data = pd.read_csv('weather_data.csv')

# ============================================================================
# PANDAS ALAPFOGALMAK
# ============================================================================
# A Pandas két elsődleges adatszerkezetet használ:
#
# 1. DataFrame (2D adatszerkezet) - olyan mint egy táblázat
#    - Sorok és oszlopok
#    - Minden oszlop egy Series
#    - type(data) -> pandas.core.frame.DataFrame
#
# 2. Series (1D adatszerkezet) - olyan mint egy lista, de fejlettebb
#    - Egy oszlop a DataFrame-ből
#    - Indexekkel és címkékkel
#    - type(data['hőmérséklet']) -> pandas.core.series.Series

print("=== TELJES DATAFRAME ===")
print(data)
# Eredmény:
#          nap  hőmérséklet időjárás
# 0      Hétfő           12    Napos
# 1       Kedd           14     Esős
# 2     Szerda           15     Esős
# 3  Csütörtök           14   Felhős
# 4     Péntek           21    Napos
# 5    Szombat           22    Napos
# 6   Vasárnap           24    Napos

# ============================================================================
# OSZLOPOK ELÉRÉSE ÉS KONVERTÁLÁSA
# ============================================================================
# Egy oszlop kiválasztása Series objektumot ad vissza
# A to_list() metódus Python listává alakítja
temperatures = data['hőmérséklet'].to_list()  # Hőmérsékleti adatok kinyerése és listává alakítása
print(f"\n=== HŐMÉRSÉKLET LISTA ===")
print(temperatures)
# Eredmény: [12, 14, 15, 14, 21, 22, 24]

# ============================================================================
# STATISZTIKAI SZÁMÍTÁSOK - HAGYOMÁNYOS MÓDSZER
# ============================================================================
# Python beépített függvényeivel számolunk
avr_temp = sum(temperatures) / len(temperatures)  # Átlag számítás
print(f"\n=== HAGYOMÁNYOS SZÁMÍTÁS ===")
print(f"\nHeti átlag hőmérséklet: {avr_temp}")

# ============================================================================
# STATISZTIKAI SZÁMÍTÁSOK - PANDAS MÓDSZER
# ============================================================================
# A Pandas beépített statisztikai függvényei gyorsabbak és egyszerűbbek

print(f"\n=== PANDAS BEÉPÍTETT FÜGGVÉNYEK ===")
avr_temp = data['hőmérséklet'].mean()  # mean() - átlag számítás
print(f"\nHeti átlag hőmérséklet: {avr_temp}")
max_temp = data['hőmérséklet'].max()  # max() - legnagyobb érték
print(f"Heti maximum: {max_temp}")
min_temp = data['hőmérséklet'].min()  # min() - legkisebb érték
print(f"Heti minimum: {min_temp}")

# ============================================================================
# OSZLOPOK ELÉRÉSE - KÉT MÓDSZER
# ============================================================================
# Mind a két módszer ugyanazt az eredményt adja:
print(f"\n=== OSZLOP ELÉRÉSI MÓDSZEREK ===")

# 1. Szótár szintaxis (ajánlott, mert mindig működik)
print("Első módszer (szótár): ", data["hőmérséklet"])

# 2. Attribútum szintaxis (rövidebb, de nem mindig használható)
print("Második módszer (attribútum): ", data.hőmérséklet)
# Megjegyzés: Ha az oszlopnévben szóköz van, csak az első módszer működik!
# Például: data["átlag hőmérséklet"] működik, data.átlag hőmérséklet nem!

# ============================================================================
# SOROK SZŰRÉSE - FELTÉTELES LEKÉRDEZÉSEK
# ============================================================================
print(f"\n=== SOROK SZŰRÉSE FELTÉTELEK ALAPJÁN ===")

# Egy adott nap adatainak lekérése
# A data.nap == "Hétfő" egy boolean Series-t ad vissza (True/False értékekkel)
# A data[boolean_series] csak a True sorokat adja vissza
print("\n1. Hétfői adatok:")
print(data[data.nap == "Hétfő"])
# Eredmény:
# Adat sor kinyerése
#      nap  hőmérséklet időjárás
# 0  Hétfő           12    Napos

# A legmelegebb nap megkeresése
# data.hőmérséklet.max() előbb megkeresi a legnagyobb értéket (24)
# majd data.hőmérséklet == 24 szűri ki azt a sort
print("\n2. Legmelegebb nap:")
print(data[data.hőmérséklet == data.hőmérséklet.max()])
# Eredmény:
# Adat sor kinyerése
#         nap  hőmérséklet időjárás
# 6  Vasárnap           24    Napos

# Összetett feltétel: napos napok, ahol 20°C felett van
print("\n3. Meleg napos napok (>20°C):")
napos_es_meleg = data[(data.időjárás == "Napos") & (data.hőmérséklet > 20)]
print(napos_es_meleg)
# Megjegyzés: & = ÉS, | = VAGY logikai operátorok
# Eredmény:
#         nap  hőmérséklet időjárás
# 4    Péntek           21    Napos
# 5   Szombat           22    Napos
# 6  Vasárnap           24    Napos

# ============================================================================
# ADATOK FELDOLGOZÁSA - PÉLDA
# ============================================================================
print(f"\n=== HŐMÉRSÉKLET KONVERZIÓ ===")

# 1. Kiválasztjuk a hétfői sort
hetfo = data[data.nap == "Hétfő"]

# 2. Az első elem hőmérsékletét kinyerjük
#    hetfo.hőmérséklet egy Series, a [0] az első elemét adja vissza
celsius = hetfo.hőmérséklet[0]
# 3. Celsius -> Fahrenheit konverzió
#    Képlet: F = (C × 9/5) + 32
fahrenheit = float((celsius * 9 / 5) + 32)
print(f"Hétfői hőmérséklet: {celsius}°C = {fahrenheit}°F")

# ============================================================================
# TOVÁBBI HASZNOS PANDAS MŰVELETEK
# ============================================================================
print(f"\n=== HASZNOS PANDAS MŰVELETEK ===")

# DataFrame információk
print("\n1. DataFrame információk:")
print(f"   Sorok száma: {len(data)}")
print(f"   Oszlopok: {data.columns.tolist()}")
print(f"   Alakja (shape): {data.shape} - (sorok, oszlopok)")  # (sorok, oszlopok)

# Első/utolsó sorok megjelenítése
print("\n2. Első 3 sor:")
print(data.head(3))

print("\n3. Utolsó 2 sor:")
print(data.tail(2))

# ============================================================================
# DATAFRAME LÉTREHOZÁSA DICTIONARY-BŐL
# ============================================================================
print(f"\n=== DATAFRAME LÉTREHOZÁSA DICTIONARY-BŐL ===")
# Dictionary létrehozása
# Kulcs = oszlopnév, érték = lista az adatokkal
data_dict = {
    "játékosok": ["István", "Anna", "Péter"],
    "pontok": [81, 76, 90]
}

# DataFrame létrehozása a dictionary-ből
panda_df = pd.DataFrame(data_dict)
print(panda_df)
# Eredmény:
#   játékosok  pontok
# 0    István      81
# 1      Anna      76
# 2     Péter      90

# ============================================================================
# ADATOK EXPORTÁLÁSA CSV FÁJLBA
# ============================================================================
# A to_csv() metódus DataFrame-et ír ki CSV fájlba
# index=False: ne írja ki az indexeket (0, 1, 2, ...) külön oszlopként
panda_df.to_csv("verseny.csv", index=False)
