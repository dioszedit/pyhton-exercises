from tkinter import *
import requests
import os


# Ez a függvény kéri le az idézetet az API-tól
def get_quote():
    # HTTP GET kérés küldése a Kanye Rest API-nak
    response = requests.get(url="https://api.kanye.rest/")
    # Hiba dobása, ha a kérés sikertelen (pl. 404 vagy 500-as hiba)
    response.raise_for_status()

    # A válasz átalakítása JSON formátumból Python szótárrá (dictionary)
    data = response.json()
    # A "quote" kulcs értékének kinyerése az adatokból
    quote = data["quote"]
    # A canvas-on lévő szöveg frissítése az új idézettel
    canvas.itemconfig(quote_text, text=quote)


# Az aktuális szkript könyvtárának meghatározása, hogy a képeket biztosan megtalálja
script_dir = os.path.dirname(os.path.abspath(__file__))

# A fő ablak létrehozása és beállítása
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Canvas (rajzvászon) létrehozása a háttérképhez és a szöveghez
canvas = Canvas(width=300, height=414)

# Háttérkép betöltése (az útvonalat dinamikusan rakjuk össze)
background_img_path = os.path.join(script_dir, "background.png")
background_img = PhotoImage(file=background_img_path)
canvas.create_image(150, 207, image=background_img)

# Szöveg létrehozása a canvas-on, amit később frissíteni fogunk
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Kanye fejét ábrázoló gomb létrehozása
kanye_img_path = os.path.join(script_dir, "kanye.png")
kanye_img = PhotoImage(file=kanye_img_path)
# A gomb megnyomásakor meghívódik a get_quote függvény
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Azonnal lekérünk egy idézetet indításkor, hogy ne az alapértelmezett szöveg látszódjon
get_quote()

# Az ablak nyitva tartása
window.mainloop()
