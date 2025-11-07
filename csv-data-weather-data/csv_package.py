# CSV modul importálása - ez a beépített Python könyvtár CSV fájlok kezelésére
import csv

# Kis mennyiségű adatnál használható módszer
# A 'with' utasítás automatikusan bezárja a fájlt a blokk végén
# Az 'encoding='UTF8'' paraméter biztosítja a magyar ékezetes karakterek helyes kezelését
with open('idojaras_adatok.csv', encoding='UTF8') as csv_file:
    # csv.reader() objektum létrehozása, amely soronként olvassa a CSV fájlt
    # delimiter=',' paraméter határozza meg, hogy vessző választja el az oszlopokat
    csv_data = csv.reader(csv_file, delimiter=',')

    # Üres lista létrehozása a hőmérsékleti értékek tárolására
    temperatures = []

    # A CSV fájl összes sorának bejárása, KIVÉVE az első sort (fejléc)
    # list(csv_data) - az összes sort listává alakítja
    # [1:] - a lista szeletelése: az 1. indextől (második sor) a végéig
    # Ez kihagyja a 0. indexű sort, amely a fejléc (nap,hőmérséklet,időjárás)
    for row in list(csv_data)[1:]:
        # Minden sor egy lista, ahol:
        # row[0] = nap neve (pl. "Hétfő")
        # row[1] = hőmérséklet (szövegként, pl. "12")
        # row[2] = időjárás (pl. "Napos")

        # row[1] értékét integer-ré (egész számmá) alakítjuk és hozzáadjuk a listához
        # int() függvény: szövegből számot csinál ("12" -> 12)
        temperatures.append(int(row[1]))

    # A begyűjtött hőmérsékleti értékek listájának kiírása
    # Eredmény: [12, 14, 15, 14, 21, 22, 24]
    print(temperatures)

# Alternatív megoldás dictionary-vel (szótár):
# with open('idojaras_adatok.csv', encoding='UTF8') as csv_file:
#     csv_data = csv.DictReader(csv_file)
#     for row in csv_data:
#         print(row['hőmérséklet'])  # Oszlopnévvel hivatkozhatunk
