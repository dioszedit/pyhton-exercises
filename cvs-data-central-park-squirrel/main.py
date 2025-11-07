# ============================================================================
# NEW YORK CENTRAL PARK MÓKUS FELMÉRÉS - ADATELEMZÉS
# ============================================================================
#
# Adatforrás: NYC Open Data
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data
#
# A 2018-as Central Park Mókus Népszámlálás adatait elemzi, és összesíti
# a mókusok számát bundaszín szerint (szürke, vörös/fahéj, fekete)
# ============================================================================
import pandas as pd

# ============================================================================
# 1. ADATOK BEOLVASÁSA
# ============================================================================
# A read_csv() függvény beolvassa a teljes mókus felmérési adatbázist
# Ez a fájl több mint 3000 mókus megfigyelést tartalmaz a Central Parkból
df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# ============================================================================
# 2. ADATOK SZŰRÉSE BUNDASZÍN SZERINT
# ============================================================================
# A DataFrame szűrése boolean indexeléssel történik:
# df["Primary Fur Color"] == "Gray" egy boolean Series-t ad vissza
# df[boolean_series] csak azokat a sorokat adja vissza, ahol True az érték

# SZÜRKE MÓKUSOK szűrése
# A "Gray" értékkel rendelkező összes mókus kiválasztása
grey_squirrels = df[df["Primary Fur Color"] == "Gray"]

# VÖRÖS/FAHÉJ SZÍNŰ MÓKUSOK szűrése
# Az adatbázisban "Cinnamon" (fahéj) néven szerepel a vörös szín
red_squirrels = df[df["Primary Fur Color"] == "Cinnamon"]

# FEKETE MÓKUSOK szűrése
# A "Black" értékkel rendelkező összes mókus kiválasztása
black_squirrels = df[df["Primary Fur Color"] == "Black"]

# ============================================================================
# 3. MÓKUSOK MEGSZÁMLÁLÁSA
# ============================================================================
# Dictionary létrehozása az összesített adatokkal
# Két oszlop lesz: "Fur Color" (bundaszín) és "Count" (darabszám)
squirrel_count_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    # A.shape[0] visszaadja a DataFrame sorainak számát
    # Ez megegyezik az adott színű mókusok számával
    "Count": [grey_squirrels.shape[0], red_squirrels.shape[0], black_squirrels.shape[0]],
}

# Alternatív módszer a számolásra:
# len(grey_squirrels) - ugyanaz az eredmény
# grey_squirrels["Primary Fur Color"].count()

# ============================================================================
# 4. EREDMÉNY DATAFRAME LÉTREHOZÁSA
# ============================================================================
# A dictionary-ből DataFrame objektumot készítünk
# Ez egy táblázatos formátumot hoz létre két oszloppal
squirrel_count_df = pd.DataFrame(squirrel_count_dict)

# A DataFrame így néz ki:
#   Fur Color  Count
# 0      gray   2473
# 1       red    392
# 2     black    103

# ============================================================================
# 5. EREDMÉNY MENTÉSE CSV FÁJLBA
# ============================================================================
# A to_csv() metódus elmenti a DataFrame-et CSV fájlba
# Alapértelmezetten a sor indexeket is kiírja (0, 1, 2)
# Ha nem akarjuk az indexeket: to_csv("squirrel_count.csv", index=False)
squirrel_count_df.to_csv("squirrel_count.csv")
