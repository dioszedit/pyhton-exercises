import os  # Operációs rendszer funkcióihoz való hozzáféréshez (pl. környezeti változók)
import smtplib  # SMTP protokoll kezelésére (email küldéshez)
from datetime import datetime  # Dátum és idő kezeléséhez szükséges osztály
from email.mime.multipart import MIMEMultipart  # Többrészes email üzenetek létrehozásához
from email.mime.text import MIMEText  # Szöveges email tartalom létrehozásához
import sys  # Rendszer-specifikus paraméterek és függvények (program leállításához)
from dotenv import load_dotenv  # .env fájlból környezeti változók betöltésére
from zoneinfo import ZoneInfo  # Időzóna kezeléshez (pl. Europe/Budapest)

import requests  # HTTP kérések küldéséhez API-k eléréséhez

# ============================================================================
# KÖRNYEZETI VÁLTOZÓK BETÖLTÉSE
# ============================================================================
# Betölti a .env fájlból a környezeti változókat
# A .env fájl tartalmazza az érzékeny adatokat (pl.: jelszavak), amelyeket
# nem akarunk a kódban tárolni biztonsági okokból
load_dotenv()

# ============================================================================
# SAJÁT POZÍCIÓ ÉS IDŐZÓNA BEÁLLÍTÁSA
# ============================================================================
# Ha nincs .env-ben beállítva megadva, akkor London koordinátái és időzónája lesz az alapértelmezett
# A pozíció szótárba (dictionary) kerül tárolásra, két kulccsal:
# - "lng": longitude (földrajzi hosszúság) - kelet-nyugat irány (-180 és +180 között)
# - "lat": latitude (földrajzi szélesség) - észak-dél irány (-90 és +90 között)
# Az os.getenv() második paramétere az alapértelmezett érték, ha a környezeti változó nincs beállítva
my_position = {
    "lng": float(os.getenv("MY_POSITION_LONGITUDE", 51.5072)),
    "lat": float(os.getenv("MY_POSITION_LATITUDE", -0.1276))
}
# Időzóna beállítása az időpontok helyes megjelenítéséhez a saját helyünk szerint
my_timezone = os.getenv("MY_TIMEZONE", "Europe/London")


def is_night() -> bool:
    """
    Ellenőrzi, hogy jelenleg éjszaka van-e a megadott koordinátákon.

    Returns:
        bool: True, ha éjszaka van, különben False
    """

    # ============================================================================
    # NAPKELTE ÉS NAPNYUGTA IDŐ LEKÉRDEZÉSE API-BÓL
    # ============================================================================
    # API hívás a napkelte és napnyugta időpontok lekérdezéséhez
    # A requests.get() egy HTTP GET kérést küld a megadott URL-re
    response = requests.get(
        url=os.getenv("SUNRISE_SUNSET_API_URL"),  # Az API URL-je a .env fájlból
        params={  # URL paraméterek (query string) - ezek az URL végéhez fűződnek ?lat=...&lng=... formában
            "lat": my_position["lat"],  # Földrajzi szélesség paraméter
            "lng": my_position["lng"],  # Földrajzi hosszúság paraméter
            "formatted": 0,  # Idő formázás nélkül kérjük le, alapértelmezetten 1, ilyenkor 12 órás formázás van
            "tzid ": my_timezone,  # Időzóna beállítása, hogy a helyi időt kapjuk vissza
        }
    )

    # Ellenőrizzük, hogy a HTTP kérés sikeres volt-e (200-as státusz kód)
    # Ha nem sikeres (pl. 404, 500), akkor hibát dob (HTTPError exception)
    response.raise_for_status()

    # A JSON formátumú választ Python szótárrá (dictionary) alakítjuk
    data = response.json()

    # Kinyerjük a napkelte és napnyugta időpontokat a válaszból
    # Ezek ISO 8601 formátumú stringek (pl.: "2025-11-20T05:46:09+00:00")
    # ahol a 'T' elválasztja a dátumot az időtől, a '+00:00' pedig a timezone offsetet jelöli
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    # ============================================================================
    # DATETIME OBJEKTUMOK LÉTREHOZÁSA
    # ============================================================================
    # A következő komment csak magyarázza a string szeletelést, de már nem használjuk
    # sunrise.split("T") - szeletelnénk a stringet a 'T' karakter mentén
    # Egy listát kapnánk a stringből,
    # pl.: ['2025-11-20', '05:46:09+00:00'] - eredeti string: '2025-11-20T05:46:09+00:00'

    # Az ISO 8601 formátumú string-eket átalakítjuk datetime objektummá
    # A datetime.fromisoformat() metódus automatikusan felismeri az ISO formátumot
    # Ezek a datetime objektumok lehetővé teszik az időpontok összehasonlítását
    sunrise_dt = datetime.fromisoformat(sunrise)
    sunset_dt = datetime.fromisoformat(sunset)

    # Jelenlegi időpont lekérése a beállított időzóna szerint
    # A ZoneInfo segítségével megadjuk, hogy melyik időzónában akarjuk az aktuális időt
    time_now_dt = datetime.now(ZoneInfo(my_timezone))

    if sunrise_dt <= time_now_dt <= sunset_dt:
        # Nappal van
        return False

    # Éjszaka van
    return True


def is_iss_overhead() -> bool:
    """
    Ellenőrzi, hogy ISS felettünk(közrlünkben) van-e

    Returns:
        bool: True, haigen
    """

    # ============================================================================
    # ISS (INTERNATIONAL SPACE STATION) POZÍCIÓ LEKÉRDEZÉSE
    # ============================================================================
    # API hívás az ISS (Nemzetközi Űrállomás) aktuális pozíciójának lekérdezéséhez
    # Ez az API nem igényel paramétereket, csak a végpontot hívjuk meg
    response = requests.get(url=os.getenv("ISS_POSITION_API_URL"))
    # Ellenőrizzük, hogy a kérés sikeres volt-e
    response.raise_for_status()

    data = response.json()
    # Az ISS koordinátáinak kinyerése a válaszból és float-tá konvertálása
    # A float() biztosítja, hogy számokként kezeljük az értékeket, nem stringként
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # ============================================================================
    # ISS LÁTHATÓSÁG ELLENŐRZÉS
    # ============================================================================
    # Ellenőrizzük, hogy az ISS a közelünkben van-e (±5 fok pontossággal)
    # Az 5 fokos "ablak" körülbelül 550 km-es távolságot jelent az egyenlítőnél
    # Mindkét feltételnek teljesülnie kell (logikai ÉS kapcsolat):
    # 1. A longitude (földrajzi hosszúság) különbsége legfeljebb 5 fok
    # 2. A latitude (földrajzi szélesség) különbsége legfeljebb 5 fok
    if (my_position["lng"] - 5 <= longitude <= my_position["lng"] + 5) and (
            my_position["lat"] - 5 <= latitude <= my_position["lat"] + 5):
        return True

    return False

# ============================================================================
# PROGRAM FŐ LOGIKÁJA
# ============================================================================
if is_night() and is_iss_overhead():
    # Éjszaka van és felettünk (közelünkben) halad át az űrállomás
    # Ilyenkor email értesítést küldünk ki

    # Ezek az adatok az email szerver kapcsolathoz szükségesek
    host = os.getenv("MAIL_SMTP")  # SMTP szerver címe (pl. smtp.gmail.com)
    password = os.getenv("MAIL_PASSWORD")  # Email fiók jelszava vagy app-specifikus jelszó
    username = os.getenv("MAIL_USERNAME")  # Email fiók felhasználóneve (általában az email cím)
    port = os.getenv("MAIL_PORT", default=587)  # SMTP port (alapértelmezett: 587 TLS-hez)

    # ============================================================================
    # EMAIL BEÁLLÍTÁSOK
    # ============================================================================
    # Küldő és fogadó email címe és neve
    sender_email = os.getenv("SENDER_EMAIL")
    sender_name = os.getenv("SENDER_NAME")
    receiver_email = "fogado@mailproba.com"
    receiver_name = "Fogadó Neve"

    body = "Az űrállomás feletünk halad át"

    # ============================================================================
    # EMAIL ÜZENET LÉTREHOZÁSA
    # ============================================================================
    # MIME (Multipurpose Internet Mail Extensions) üzenet létrehozása
    # A MIMEMultipart lehetővé teszi, hogy több részt (szöveg, html, csatolmány) tartalmazzon az üzenet
    message = MIMEMultipart()

    # Email fejléc beállítások
    message["Subject"] = "ISS értesítés"
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
            print(f"Email sikeresen elküldve")

    except Exception as e:
        # Ha hiba történik az email küldés során, kiírja a hibaüzenetet
        print(f"Hiba az email küldése során: {e}")
