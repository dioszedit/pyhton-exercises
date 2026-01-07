import os  # Operációs rendszer funkcióihoz való hozzáféréshez (pl. környezeti változók)
from dotenv import load_dotenv  # .env fájlból környezeti változók betöltésére
import requests  # HTTP kérések küldéséhez API-k eléréséhez

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

params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4, # Csak a következő 12 óra előrejelzése érdekel
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
            break # kilépünk a ciklusból

    if will_rain:
        break  # Ha megtaláltuk az első ilyen esetet, kilépünk

# vagy Pythonic megoldás:
# will_rain = any(item["weather"][0]["id"] < 700 for item in weather_data["list"])

if will_rain:
    print("Vigyél ernyőt! ☔")
else:
    print("Nem kell ernyő! ☀️")