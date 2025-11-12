# ---------------------------- Importok ------------------------------- #
from random import randint, choice, shuffle  # Véletlen számok és elemek választása
from tkinter import *  # GUI elemek
from tkinter import messagebox  # Felugró ablak üzenetek
import pyperclip  # Vágólapra másolás

# ---------------------------- Konstansok ------------------------------- #
# Színek
WHITE = "#ffffff"

# Betűtípus beállítások
FONT_NAME = "Arial"
FONT_SIZE = 12


# ---------------------------- Jelszó generálás ------------------------------- #
def generate_password() -> None:
    # Karakter készletek a jelszó generálásához
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Véletlenszerű karakterek kiválasztása listában
    choice_chars = [choice(letters) for _ in range(randint(8, 10))]  # 8-10 betű
    choice_chars += [choice(symbols) for _ in range(randint(2, 4))]  # 2-4 szimbólum
    choice_chars += [choice(numbers) for _ in range(randint(2, 4))]  # 2-4 szám
    shuffle(choice_chars)  # Karakterek összekeverése

    # Hagyományos módszer a jelszó string előállítására
    # password = ''
    # for i in range(len(choice_chars)):
    #     password += choice_chars[i]

    # Pyhton beépített join() függvénye - tuple, dictionary, list esetén használható
    # megadható hogy milyen karatter kösse összeőket
    # pl.: "-".join(choice_chars) - ebben az esetben minden elem közzé a - karakter fűzi be
    password = "".join(choice_chars)

    password_input.delete(0, END)  # kitörli ha volt benne valami
    password_input.insert(END, password)
    save_button.focus()
    pyperclip.copy(password)  # Clipboardra helyezzük a jelszót


# ---------------------------- Jelszó mentése ------------------------------- #
def save_password() -> None:
    # Beviteli mezők tartalmának lekérdezése és szóközök eltávolítása
    website = website_input.get().strip()
    user = user_input.get().strip()
    password = password_input.get().strip()

    # Ellenőrzés: minden mező ki van-e töltve
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Figyelmeztetés",
            message="Nem adtál meg minden adatot!"
        )
        return

    # Megerősítés kérése a felhasználótól
    is_yes = messagebox.askyesno(
        title=website,
        message=f"Következő adatokat adtad meg:\n"
                f"\nEmail: {user}"
                f"\nJelszó: {password} \n"
                f"\nBiztosan elmented az adatokat?"
    )

    if is_yes:
        # Adatok hozzáfűzése a fájlhoz
        with open("data.txt", mode="a", encoding="utf-8") as file:
            file.write(f"{website} | {user} | {password}\n")

            # Beviteli mezők ürítése sikeres mentés után
            website_input.delete(0, END)
            user_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI Beállítások ------------------------------- #
# Főablak létrehozása és beállítása
window = Tk()
window.title("Jelszó kezelő")
window.config(padx=20, pady=20, bg=WHITE)

# Canvas a logo képpel
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0) # Keret nélküli vászon
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image) # Kép középre helyezése
canvas.grid(column=1, row=0, columnspan=2, sticky="w", pady=20)

# Website
website_label = Label(text="Website:", bg=WHITE, font=(FONT_NAME, FONT_SIZE))
website_label.grid(column=0, row=1, sticky="e")

website_input = Entry(width=35, font=(FONT_NAME, FONT_SIZE))
website_input.grid(column=1, row=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Email/Felhasználónév
user_label = Label(text="Email/Felhasználónév:", bg=WHITE, font=(FONT_NAME, FONT_SIZE))
user_label.grid(column=0, row=2, sticky="e")

user_input = Entry(width=35, font=(FONT_NAME, FONT_SIZE))
user_input.grid(column=1, row=2, columnspan=2, sticky="ew", padx=10, pady=5)

# Jelszó
password_label = Label(text="Jelszó:", bg=WHITE, font=(FONT_NAME, FONT_SIZE))
password_label.grid(column=0, row=3, sticky="e")

password_input = Entry(width=21, font=(FONT_NAME, FONT_SIZE))
password_input.grid(column=1, row=3, sticky="ew", padx=10, pady=5)

# Gombok
password_generate_button = Button(
    text="Jelszó generálás",
    font=(FONT_NAME, FONT_SIZE),
    command=generate_password
)
password_generate_button.grid(column=2, row=3, sticky="ew", padx=10, pady=5)

save_button = Button(
    text="Mentés",
    font=(FONT_NAME, FONT_SIZE),
    command=save_password
)
save_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=10, pady=5)

window.mainloop()
