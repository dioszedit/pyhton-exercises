import pandas

# CSV fájl beolvasása
read_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Szótár létrehozása: betű -> NATO kód párok
phonetic_dict = {row.letter: row.code for (index, row) in read_data.iterrows()}

# Felhasználói bemenet
word = input("Enter a word: ").upper()

# Fonetikus lista létrehozása - CSAK a szótárban lévő betűkkel
# Az 'if letter in phonetic_dict' rész kiszűri az érvénytelen karaktereket
output_list = [phonetic_dict[letter] for letter in word if letter in phonetic_dict]

print(output_list)
