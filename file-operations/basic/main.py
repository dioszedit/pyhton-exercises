
# 1. Módszer -  Fájl olvasáshoz
file = open("test/my_file2.txt", encoding="utf-8")
contents = file.read()
print(contents)
# Bezárás a fájlnak - memória felszabadítás miatt
file.close()

# 2. Módszer - Fájl művelethez - with-et használva a program automatikusan bezárja a fájlt, amikor érzékeli, hogy nincs vele több dolga
# with open("my_file.txt", mode="w", encoding="utf-8") as file:
#     # felülírunk mindent a fájlban
#     file.write("Új szöveg.")

# Ha az írandó fájl nem létezik, akkor létrehozza írásra
# with open("my_file2.txt", mode="w", encoding="utf-8") as file:
#     file.write("Új fájl tartalma")

with open("my_file.txt", mode="a", encoding="utf-8") as file:
    file.write("\nVégére hozzá adja ezt a szöveget.")