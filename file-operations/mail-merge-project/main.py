# FELADAT: Készíts személyre szabott leveleket a letter_text.txt sablonból
# minden egyes névhez az invited_names.txt fájlból.
# Cseréld ki a [name] helyőrzőt a tényleges névre.
# Mentsd el a leveleket a "ReadyToSend" mappába.

# Tipp1: Ez a módszer segíteni fog: https://www.w3schools.com/python/ref_file_readlines.asp
# Tipp2: Ez a módszer is hasznos lesz: https://www.w3schools.com/python/ref_string_replace.asp
# Tipp3: Ez a módszer szintén segít: https://www.w3schools.com/python/ref_string_strip.asp


# 1. LÉPÉS: A levél sablon beolvasása
# A 'with open()' automatikusan bezárja a fájlt a használat után
with open('input/Letters/letter_text.txt') as letter:
    # A teljes levél tartalmának beolvasása egyetlen szövegként
    letter_contents = letter.read()

# 2. LÉPÉS: A meghívott nevek beolvasása
with open('input/names/invited_names.text') as names:
    # A readlines() metódus minden sort külön listaelem ként olvas be
    # Így names_contents egy lista lesz a nevekkel
    names_contents = names.readlines()

# 3. LÉPÉS: Személyre szabott levelek létrehozása minden meghívottnak
# A for ciklus végigmegy az összes néven a listában
for name in names_contents:
    # Új fájl létrehozása minden névhez
    # Az f-string segítségével a fájlnév tartalmazza a meghívott nevét
    # A strip() eltávolítja a felesleges szóközöket és sortöréseket a név elejéről és végéről
    with open(f'output/ready-to-send/letter_for_{name.strip().lower().replace(' ', '_')}.txt', 'w') as new_letter:
        # A replace() metódus kicseréli a [name] helyőrzőt a tényleges névre
        # A strip() itt is eltávolítja a whitespace karaktereket, kisbetűsítem és a nevkben találhat space helyettesítjük _ karakterre
        # pl.: John Small -> letter_for_john_small.txt lesz a fájl neve
        # Az így elkészült személyre szabott levelet írjuk ki a fájlba
        new_letter.write(letter_contents.replace('[name]', name.strip()))