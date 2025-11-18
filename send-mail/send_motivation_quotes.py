# Motivációs idézetek küldése email-ben
# Ez a script hétfőnként automatikusan küld egy véletlenszerű motivációs idézetet email-ben

# Szükséges könyvtárak importálása
import datetime as dt # Dátum és idő kezelésére
import os # Operációs rendszer funkcióihoz való hozzáféréshez (pl. környezeti változók)
import random  # Véletlenszerű választáshoz
import smtplib # SMTP protokoll kezelésére (email küldéshez)
from email.mime.multipart import MIMEMultipart # Többrészes email üzenetek létrehozásához
from email.mime.text import MIMEText  # Szöveges email tartalom létrehozásához

from dotenv import load_dotenv # .env fájlból környezeti változók betöltésére

# ============================================================================
# KÖRNYEZETI VÁLTOZÓK BETÖLTÉSE
# ============================================================================
# Betölti a .env fájlból a környezeti változókat
# A .env fájl tartalmazza az érzékeny adatokat (pl.: jelszavak), amelyeket
# nem akarunk a kódban tárolni biztonsági okokból
load_dotenv()

# Hozzáférés a környezeti változókhoz a .env fájlból
# Ezek az adatok az email szerver kapcsolathoz szükségesek
host = os.getenv("MAIL_SMTP") # SMTP szerver címe (pl. smtp.gmail.com)
password = os.getenv("MAIL_PASSWORD") # Email fiók jelszava vagy app-specifikus jelszó
username = os.getenv("MAIL_USERNAME")  # Email fiók felhasználóneve (általában az email cím)
port = os.getenv("MAIL_PORT", default=587)  # SMTP port (alapértelmezett: 587 TLS-hez)

# ============================================================================
# EMAIL BEÁLLÍTÁSOK
# ============================================================================
# Küldő email címe és neve
sender_email = "kuldo@mailproba.com"
sender_name = "Küldő Neve"

# Fogadó email címe és neve
receiver_email = "fogado@mailproba.com"
receiver_name = "Fogadó Neve"

# ============================================================================
# EMAIL ÜZENET LÉTREHOZÁSA
# ============================================================================
# MIME (Multipurpose Internet Mail Extensions) üzenet létrehozása
# A MIMEMultipart lehetővé teszi, hogy több részt (szöveg, html, csatolmány) tartalmazzon az üzenet
message = MIMEMultipart()

# Email fejléc beállítások
message["Subject"] = "Heti motiváció"
message["From"] = f"{sender_name} <{sender_email}>"
message["To"] = f"{receiver_name} <{receiver_email}>"

# ============================================================================
# DÁTUM ELLENŐRZÉS - CSAK HÉTFŐN KÜLDJÖN EMAILT
# ============================================================================
# Aktuális dátum és idő lekérése
now = dt.datetime.now()
# A hét napjának lekérése (0=hétfő, 1=kedd, ..., 6=vasárnap)
day_of_week = now.weekday()

# Ellenőrzi, hogy hétfő van-e
if day_of_week == 0:
    # ============================================================================
    # IDÉZET FÁJL BEOLVASÁSA ÉS VÉLETLENSZERŰ VÁLASZTÁS
    # ============================================================================
    # Megnyitja az idézetek fájlját olvasási módban UTF-8 kódolással
    # Az UTF-8 kódolás biztosítja, hogy a magyar ékezetes karakterek helyesen jelenjenek meg
    with open("idezetek_magyarul.txt", mode="r", encoding="utf-8") as file:
        # Beolvassa az összes sort egy listába
        # Minden sor egy idézetet tartalmaz
        quotes = file.readlines()

    # Véletlenszerűen kiválaszt egy idézetet a listából
    body = random.choice(quotes)

    # Az email törzsét hozzáadja az üzenethez
    # "plain" = egyszerű szöveges formátum (nem HTML)
    # "utf-8" = karakterkódolás magyar ékezetes karakterekhez
    message.attach(MIMEText(body, "plain", "utf-8"))

    # ============================================================================
    # EMAIL KÜLDÉSE SMTP PROTOKOLLON KERESZTÜL
    # ============================================================================
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

    print("Email sikeresen elküldve!")