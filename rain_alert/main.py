import os  # Operációs rendszer funkcióihoz való hozzáféréshez (pl. környezeti változók)
from dotenv import load_dotenv  # .env fájlból környezeti változók betöltésére
import requests  # HTTP kérések küldéséhez API-k eléréséhez
from twilio.rest import Client

# ============================================================================
# KÖRNYEZETI VÁLTOZÓK BETÖLTÉSE
# ============================================================================
# Betölti a .env fájlból a környezeti változókat
# A .env fájl tartalmazza az érzékeny adatokat (pl.: jelszavak), amelyeket
# nem akarunk a kódban tárolni biztonsági okokból
load_dotenv()

# Alapértelmezett pozició London
latitude = os.getenv("POSITION_LATITUDE", 51.5072)
longitude = os.getenv("POSITION_LONGITUDE", -0.1276)

api_url = os.getenv("OPENWEATHER_API_URL")
api_key = os.getenv("OPENWEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
to_phone_number = os.getenv("TO_PHONE_NUMBER")

params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4,  # Csak a következő 12 óra előrejelzése érdekel
}
response = requests.get(api_url + "forecast", params=params)
response.raise_for_status()

weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    # item["weather"] - időjárási viszonyok listáját írja le
    for weather in hour_data["weather"]:
        condition_code = weather["id"]
        # OpenWeatherMap API időjárási viszony kódok
        # < 700: Eső, hó, vagy más csapadék(200 - 600 tartomány)
        # 700 - 799: Köd, pára, stb.
        # 800: Tiszta égbolt
        # > 800: Felhős
        if int(condition_code) < 700:
            will_rain = True
            break  # kilépünk a ciklusból

    if will_rain:
        break  # Ha megtaláltuk az első ilyen esetet, kilépünk

# vagy Pythonic megoldás:
# will_rain = any(item["weather"][0]["id"] < 700 for item in weather_data["list"])

if will_rain:
    if account_sid and auth_token and from_phone_number and to_phone_number:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Csapadékos időjárás lesz, ezért vigyél ernyőt!",
            from_=from_phone_number,
            to=to_phone_number,
        )

        print(f"Sent to {to_phone_number}: {message.body}")
    else:
        # Ha nem állítunk be SMS kiküldést, akkor csak a console-os kiírás lesz.
        print("Vigyél ernyőt! ☔")
else:
    print("Nem kell ernyő! ☀️")
