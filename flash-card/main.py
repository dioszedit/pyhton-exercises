"""
Flash Cards - Angol-Magyar Szótanuló Alkalmazás
================================================

Ez az alkalmazás segít angol szavak megtanulásában interaktív flash card-ok segítségével.
A program véletlenszerűen választ ki szavakat, megjeleníti az angol változatot,
majd 3 másodperc múlva automatikusan megfordítja a kártyát a magyar fordítással.

Funkciók:
- Automatikus kártyaforgatás 3 másodperc után
- Tanult szavak eltávolítása a listából
- Folyamat folytatása a legutóbb abbahagyott helytől
- Vizuális visszajelzés a haladásról
"""

import os
import random
from tkinter import *  # GUI elemek
from typing import Hashable
import pandas as pd

# ============================================================================
# KONSTANSOK ÉS GLOBÁLIS VÁLTOZÓK
# ============================================================================

# Háttér szín
BACKGROUND_COLOR = "#B1DDC6"

# Betűtípus beállítások
FONT_NAME = "Arial"

# Cím szöveg beállítások (English/Magyar felirat)
FONT_SIZE_TITLE = 40
FONT_STYLE_TITLE = "italic"

# Tanulandó szó beállítások (a fő szó a kártyán)
FONT_SIZE_WORD = 40
FONT_STYLE_WORD = "bold"

# Számláló beállítások (hátralévő szavak száma)
Font_SIZE_COUNTER = 12
FONT_STYLE_COUNTER = "bold"

# Az időzítő azonosítója (a kártya automatikus megfordításához)
after_id: str | None = None

# Az aktuálisan megjelenített kártya adatai (English és Magyar kulcsokkal)
current_card: dict = {}


# ============================================================================
# ADATKEZELŐ FÜGGVÉNYEK
# ============================================================================
def read_data() -> list[dict]:
    """
    Betölti a tanulandó szavakat CSV fájlból.

    Először megpróbálja betölteni a 'words_to_learn.csv' fájlt, ami a még
    megtanulatlan szavakat tartalmazza. Ha ez nem létezik (első indításkor),
    akkor az 'english_words.csv' fájlt tölti be, ami az összes szót tartalmazza.

    Returns:
        list[dict]: A szavak listája, ahol minden elem egy dictionary
                    'English' és 'Magyar' kulcsokkal
    """
    try:
        # Megpróbáljuk betölteni a folyamatban lévő tanulási fájlt
        df = pd.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        # Ha nem létezik, betöltjük az eredeti teljes szólistát
        df = pd.read_csv("data/english_words.csv")

    # A DataFrame-et dictionary listává alakítjuk
    # Minden sor egy dict lesz: {"English": "cat", "Magyar": "macska"}
    return df.to_dict(orient="records")


# ============================================================================
# KÁRTYA KEZELŐ FÜGGVÉNYEK
# ============================================================================

def right_answer_handling() -> None:
    """
    Helyes válasz kezelése - amikor a felhasználó ismeri a szót.

    A funkció:
    1. Eltávolítja az aktuális kártyát a tanulandó szavak listájából
    2. Frissíti a számlálót
    3. Elmenti a megmaradt szavakat CSV fájlba
    4. Betölti a következő kártyát
    5. Ha minden szót megtanult, gratulációs üzenetet jelenít meg
    """
    # Eltávolítjuk az aktuális kártyát a listából (megtanultuk)
    english_words.remove(current_card)

    # Ellenőrizzük, hogy vannak-e még tanulandó szavak
    if len(english_words) == 0:
        # Ha nincs több szó, gratulációs üzenetet jelenítünk meg
        canvas.itemconfig(card, image=card_front_image)
        canvas.itemconfig(title, text="Gratulálok!", fill="black")
        canvas.itemconfig(word, text="Minden szót megtanultál!", fill="black")

        # Töröljük a words_to_learn.csv fájlt, mert már nincs mit tanulni
        if os.path.exists("data/words_to_learn.csv"):
            os.remove("data/words_to_learn.csv")

        wrong_button.grid_forget()
        right_button.grid_forget()
    else:
        # Frissítjük a számlálót a hátralévő szavak számával
        counter.config(text=f"Hátralévő szavak: {len(english_words)}")

        # Elmentjük a megmaradt szavakat CSV fájlba
        # Így ha bezárjuk az alkalmazást, folytathatjuk onnan ahol abbahagytuk
        words_to_learn_data = [item for item in english_words]
        pd.DataFrame(words_to_learn_data).to_csv("data/words_to_learn.csv", index=False)

        # Betöltjük a következő kártyát
        next_card()


def next_card() -> None:
    """
    Következő kártya megjelenítése.

    A funkció:
    1. Leállítja az előző időzítőt (ha volt)
    2. Véletlenszerűen választ egy új kártyát
    3. Megjeleníti az angol oldalt
    4. Elindít egy 3 másodperces időzítőt a megfordításhoz
    """
    global after_id
    global current_card

    # Ha van futó időzítő, leállítjuk (pl. ha a felhasználó gyorsan léptet)
    if after_id is not None:
        window.after_cancel(after_id)
        after_id = None

    # Véletlenszerűen választunk egy szót a listából
    current_card = random.choice(english_words)

    # Megjelenítjük a kártya elülső oldalát (angol)
    canvas.itemconfig(card, image=card_front_image)
    canvas.itemconfig(word, text=current_card["English"], fill="black")
    canvas.itemconfig(title, text="English", fill="black")

    # Elindítunk egy időzítőt: 3000 ms (3 másodperc) múlva meghívja a back_card függvényt
    after_id = window.after(3000, func=back_card)


def back_card() -> None:
    """
    Kártya megfordítása - a magyar fordítás megjelenítése.

    Automatikusan meghívódik 3 másodperc elteltével a next_card() függvény után.
    Megváltoztatja a kártya hátterét és megjeleníti a magyar fordítást fehér szöveggel.
    """
    # Beállítjuk a kártya hátsó oldalát (magyar)
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(title, text="Magyar", fill="white")
    canvas.itemconfig(word, text=current_card["Magyar"], fill="white")


# ============================================================================
# ALKALMAZÁS INICIALIZÁLÁSA
# ============================================================================

# Szótár betöltése
# Ez a lista tartalmazza az összes tanulandó szót
english_words: list[dict[Hashable, str]] = read_data()

# ============================================================================
# FELHASZNÁLÓI FELÜLET KIALAKÍTÁSA
# ============================================================================

# Főablak létrehozása és beállítása
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Számláló címke létrehozása
# Mutatja a hátralévő szavak számát a jobb felső sarokban
counter = Label(
    text=f"Hátralévő szavak: {len(english_words)}",
    font=(FONT_NAME, Font_SIZE_COUNTER, FONT_STYLE_COUNTER),
    fg="white",
    bg=BACKGROUND_COLOR,
)
counter.grid(column=1, row=0, columnspan=2, sticky="e", padx=10, pady=10)

# Canvas létrehozása a kártya megjelenítéséhez
# A Canvas lehetővé teszi képek és szövegek elhelyezését ugyanazon a felületen
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Kártya képek betöltése
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

# Kártya kép elhelyezése a Canvas közepén
card = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=1, columnspan=2)

# Kártyán szereplő szövegek létrehozása
# Címke (English/Magyar)
title = canvas.create_text(
    400, 150,
    text="",
    font=(FONT_NAME, FONT_SIZE_TITLE, FONT_STYLE_TITLE)
)

# Fő szó (a tanulandó szó vagy fordítás)
word = canvas.create_text(
    400, 263,
    text="",
    font=(FONT_NAME, FONT_SIZE_WORD, FONT_STYLE_WORD)
)

# Első kártya betöltése
next_card()

# ============================================================================
# GOMBOK LÉTREHOZÁSA
# ============================================================================

# "Nem tudom" gomb (bal oldal)
# Amikor megnyomják, új kártyát tölt be, de nem távolítja el a szót a listából
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(
    image=wrong_image,
    highlightthickness=0,
    borderwidth=0,
    command=next_card
)
wrong_button.grid(column=0, row=2)

# "Tudom" gomb (jobb oldal)
# Amikor megnyomják, eltávolítja a szót a listából (megtanultuk)
right_image = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_image,
    highlightthickness=0,
    borderwidth=0,
    command=right_answer_handling
)
right_button.grid(column=1, row=2)

# ============================================================================
# ALKALMAZÁS FUTTATÁSA
# ============================================================================

# Az alkalmazás főciklusa - ez tartja futva az ablakot
window.mainloop()
