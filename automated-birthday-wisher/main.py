"""
Automatikus születésnapi üdvözlő email küldő program

Ez a program automatikusan ellenőrzi a birthdays.csv fájlban található születésnapokat,
és a mai napra esők esetén véletlenszerű levélsablonnal email üdvözletet küld.

Használat:
    1. Töltsd ki a .env fájlt a saját email beállításaiddal
    2. Adj hozzá személyeket a birthdays.csv fájlhoz
    3. Futtasd a scriptet: python main.py
"""

import random  # Véletlenszerű választáshoz (levél sablon kiválasztása)
import pandas as pd  # CSV fájl kezeléséhez
import datetime as dt  # Dátum és idő kezelésére
import os  # Operációs rendszer funkcióihoz való hozzáféréshez (pl. környezeti változók)
import smtplib  # SMTP protokoll kezelésére (email küldéshez)
from email.mime.multipart import MIMEMultipart  # Többrészes email üzenetek létrehozásához
from email.mime.text import MIMEText  # Szöveges email tartalom létrehozásához
import sys  # Rendszer-specifikus paraméterek és függvények (program leállításához)
from dotenv import load_dotenv  # .env fájlból környezeti változók betöltésére

# ============================================================================
# SZÜLETÉSNAPOK ELLENŐRZÉSE
# ============================================================================
# Beolvassa a születésnapokat tartalmazó CSV fájlt
# A CSV fájl formátuma: név, email, év, hónap, nap
birthdays_df = pd.read_csv("birthdays.csv")

# Aktuális dátum lekérése
now = dt.datetime.now()

# Szűrés: csak azokat a sorokat veszi, ahol a hónap ÉS a nap megegyezik a mai dátummal
# A & operátor a pandas logikai ÉS operátora
# Minden feltételt zárójelbe kell tenni!
birthdays = birthdays_df[(birthdays_df["hónap"] == now.month)
                         & (birthdays_df["nap"] == now.day)]

# Ha nincs ma születésnapos, akkor leállítja a programot
if len(birthdays) == 0:
    print("Nincs ma szülinap.")
    sys.exit()

print(f"{len(birthdays)} db mai születésnap van!")

# ============================================================================
# KÖRNYEZETI VÁLTOZÓK BETÖLTÉSE
# ============================================================================
# Betölti a .env fájlból a környezeti változókat
# A .env fájl tartalmazza az érzékeny adatokat (pl.: jelszavak), amelyeket
# nem akarunk a kódban tárolni biztonsági okokból
load_dotenv()

# Hozzáférés a környezeti változókhoz a .env fájlból
# Ezek az adatok az email szerver kapcsolathoz szükségesek
host = os.getenv("MAIL_SMTP")  # SMTP szerver címe (pl. smtp.gmail.com)
password = os.getenv("MAIL_PASSWORD")  # Email fiók jelszava vagy app-specifikus jelszó
username = os.getenv("MAIL_USERNAME")  # Email fiók felhasználóneve (általában az email cím)
port = os.getenv("MAIL_PORT", default=587)  # SMTP port (alapértelmezett: 587 TLS-hez)

# ============================================================================
# EMAIL BEÁLLÍTÁSOK
# ============================================================================
# Küldő email címe és neve
sender_email = os.getenv("SENDER_EMAIL")
sender_name = os.getenv("SENDER_NAME")

# Elérhető levél sablonok listája
# A program véletlenszerűen választ egyet ezek közül minden címzettnek
email_template_files = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# ============================================================================
# EMAIL KÜLDÉS MINDEN SZÜLETÉSNAPOSNAK
# ============================================================================
# Végigmegy a mai születésnaposokon (iterrows() visszaadja az index-et és a sort)
for (index, person) in birthdays.iterrows():
    # Címzett adatainak kinyerése a CSV sorból
    receiver_email = person["email"]
    receiver_name = person["név"]

    # ============================================================================
    # LEVÉL SABLON KIVÁLASZTÁSA ÉS BETÖLTÉSE
    # ============================================================================
    # Véletlenszerűen kiválaszt egy levél sablont a listából
    filename = random.choice(email_template_files)
    # Megnyitja a kiválasztott sablon fájlt UTF-8 kódolással (magyar ékezetek miatt)
    # A 'with' utasítás automatikusan bezárja a fájlt, amikor véget ér a blokk
    with open(f"letter_templates/{filename}", encoding='UTF8') as file:
        template = file.read()

    # A [NAME] placeholder-t kicseréli a címzett nevére
    body = template.replace("[NAME]", receiver_name)

    # ============================================================================
    # EMAIL ÜZENET LÉTREHOZÁSA
    # ============================================================================
    # MIME (Multipurpose Internet Mail Extensions) üzenet létrehozása
    # A MIMEMultipart lehetővé teszi, hogy több részt (szöveg, html, csatolmány) tartalmazzon az üzenet
    message = MIMEMultipart()

    # Email fejléc beállítások
    message["Subject"] = "Boldog szülinapot!"
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = f"{receiver_name} <{receiver_email}>"

    # Az email törzsét hozzáadja az üzenethez
    # "plain" = egyszerű szöveges formátum (nem HTML)
    # "utf-8" = karakterkódolás magyar ékezetes karakterekhez
    message.attach(MIMEText(body, "plain", "utf-8"))

    # ============================================================================
    # EMAIL KÜLDÉSE SMTP PROTOKOLLON KERESZTÜL
    # ============================================================================
    try:
        # SMTP kapcsolat létrehozása a szerverrel
        # A 'with' utasítás automatikusan lezárja a kapcsolatot, amikor véget ér a blokk
        with smtplib.SMTP(host, port) as connection:
            # TLS (Transport Layer Security) titkosítás indítása a biztonságos kommunikációhoz
            connection.starttls()

            # Bejelentkezés az email szerverre a felhasználónévvel és jelszóval
            connection.login(user=username, password=password)

            # Email üzenet elküldése
            # from_addr: feladó email címe
            # to_addrs: címzett email címe (vagy email címek listája)
            # msg: az üzenet string formátumban (MIME üzenet konvertálása)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=receiver_email,
                msg=message.as_string()
            )
            print(f"Email sikeresen elküldve: {receiver_name}")

    except Exception as e:
        # Ha hiba történik az email küldés során, kiírja a hibaüzenetet
        print(f"✗ Hiba az email küldése során ({receiver_name}): {e}")

print("\nKész! Minden email elküldve.")