# Mérföld-kilométer átváltó alkalmazás Tkinter GUI-val
from tkinter import *


def validate_number(input_text: str) -> bool:
    """
    Ellenőrzi, hogy az input csak számokat és tizedesjegyet tartalmaz-e

    Args:
        input_text (str): A validálandó szöveg

    Returns:
        bool: True ha érvényes szám, False ha nem
    """
    # Csak számok, pont és vessző engedélyezett
    if input_text.replace(",", "").replace(".", "").isdigit():
        return True
    return False


def calculate() -> None:
    """
    Átváltja a mérföldet kilométerre
    1 mérföld = 1.60934 kilométer
    """
    if miles_entry.get() == "" or miles_entry.get() == "0" or not validate_number(miles_entry.get()):
        cancel_or_reset()
    else:
        # Vessző helyett pont használata a float konverzióhoz
        miles = float(miles_entry.get().replace(",", "."))
        # Átváltás és kerekítés 2 tizedesjegyre
        km = round(miles * 1.60934, 2)
        # Eredmény megjelenítése
        label_result_num.config(text=f"{km} km")


def cancel_or_reset() -> None:
    """
    Törli az input mezőt és visszaállítja az eredményt nullára
    """
    miles_entry.delete(0, END)
    miles_entry.insert(END, "0")
    label_result_num.config(text="0 km")

# ===== ABLAK LÉTREHOZÁSA ÉS KONFIGURÁLÁSA =====

# Tk() objektum létrehozása - ez a fő ablak
window = Tk()

# Ablak címének beállítása (az ablak tetején látható szöveg)
window.title("Mérföld - kilóméter átváltó")

# Minimum ablak méret beállítása pixelben (szélesség x magasság)
window.minsize(width=300, height=250)
# Az ablak széleknél távolságot (padding) állítunk be
# padx = vízszintes, pady = függőleges belső margó
window.config(padx=20, pady=20)

# Grid rendszer konfigurálása - 2 oszlop létrehozása
# weight=1 azt jelenti, hogy az oszlop kitölti a rendelkezésre álló helyet
window.columnconfigure(0, weight=1)  # Bal oszlop
window.columnconfigure(1, weight=1)  # Jobb oszlop

# ===== FELSŐ RÉSZ - INPUT KOMPONENSEK =====

# Label widget - A mérföld input mező címkéje
# A Label egy egyszerű szöveges címke, amely nem szerkeszthető
miles_label = Label(text="Mérföld*", font=("Arial", 10, "bold"))
# Grid pozícionálás: 0. sor, 0. oszlop, 2 oszlopon át (columnspan)
# sticky="w" = west, balra igazítás
miles_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

# Grid sticky paraméterei lehetnek pl.:
#
# "n" = north (fent, középen)
# "ne" = northeast (jobb felső sarok)
# "e" = east (jobb oldal, középen)
# "se" = southeast (jobb alsó sarok)
# "s" = south (lent, középen)
# "sw" = southwest (bal alsó sarok)
# "w" = west (bal oldal, középen)
# "nw" = northwest (bal felső sarok)
# "ew" = east-west, vízszintesen kitölti a cellát
# "nsew" = mind a négy irányba nyújtás (kitölti a cellát)
#
# A padx és pady paraméterek belső margót adnak
# pady=(0, 10) azt jelenti: fent 0px, lent 10px margó

# Entry - Egysoros szövegbeviteli mező
# A felhasználó ide írhatja be a mérföld értéket
miles_entry = Entry(width=40, relief="solid", borderwidth=1)
miles_entry.insert(END, "0")  # Alapértelmezett "0" érték beillesztése
# Grid pozícionálás: 1. sor, 0. oszlop, 2 oszlopon át
miles_entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))
miles_entry.focus()  # Automatikus focus az inputra (kurzor ide kerül)

# "Számold ki!" gomb - Az átváltást végző gomb (bal oldal)
button_calculate = Button(
    text="Számold ki!",
    font=("Arial", 10),
    bg="white",
    relief="solid", # Keret stílusa
    borderwidth=1, # Keret vastagsága
    padx=10,
    pady=5,
    command=calculate  # A függvény, ami lefut kattintáskor
)
button_calculate.grid(row=2, column=0, sticky="ew", padx=(0, 5), pady=(0, 10))

# "Mégse" gomb - Törli az inputot és nullázza az eredményt (jobb oldal)
button_cancel = Button(
    text="Mégse",
    font=("Arial", 10),
    bg="white",
    relief="solid",
    borderwidth=1,
    padx=10,
    pady=5,
    command=cancel_or_reset
)
button_cancel.grid(row=2, column=1, sticky="ew", padx=(5, 0), pady=(0, 10))

# ===== ALSÓ RÉSZ - Sötét háttér =====

# Frame widget - Konténer a sötét háttérű eredmény részhez
# majd pack() GUI manager használat a Frame-en belüli elemeknél
result_frame = Frame(bg="#3a3f47", padx=20, pady=20)
result_frame.grid(row=3, column=0, columnspan=2, sticky="nsew")

# "Eredmény" felirat (narancsos színnel)
label_result = Label(
    result_frame,
    text="Eredmény:",
    font=("Arial", 12, "bold"),
    bg="#3a3f47",
    fg="#ff6b4a",
    anchor="w"
)
# Ez a Frame-en belül van, ezért pack()-t használunk
label_result.pack(anchor="w")

# Az eredmény pl.: "4,8 km" az átváltott érték fehér színnel, nagy betűmérettel
label_result_num = Label(
    result_frame,
    text="0 km", # Kezdeti érték
    font=("Arial", 32, "bold"),
    bg="#3a3f47",
    fg="white",
    anchor="w"
)
label_result_num.pack(anchor="w")

# A 3. sor (eredmény Frame) rugalmasan kitölti a rendelkezésre álló függőleges helyet
# weight=1 azt jelenti, hogy ha az ablakot nagyítjuk, ez a sor növekszik
window.rowconfigure(3, weight=1)

# ===== PROGRAM FUTTATÁSA =====

# mainloop() - Kint tartja a képernyőn az ablakot és figyeli az eseményeket
# Ez egy végtelen ciklus (event loop), amely mindaddig fut,
# amíg be nem zárjuk az ablakot
window.mainloop()
