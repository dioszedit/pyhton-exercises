# Esőriasztó Alkalmazás (Rain Alert)

Ez a projekt egy automatizált esőriasztó rendszer, amely az OpenWeatherMap API-t használja az időjárás előrejelzés lekérésére, és értesítést küld, ha csapadék várható a következő 12 órában.

## Funkciók

- Aktuális időjárási adatok lekérése földrajzi koordináták alapján.
- A következő 12 óra előrejelzésének elemzése.
- Automatikus értesítés (SMS), ha eső várható.
- Biztonságos API kulcs kezelés környezeti változókkal.

## Előfeltételek

A projekt futtatásához szükséged lesz egy ingyenes API kulcsra az [OpenWeatherMap](https://openweathermap.org/api) oldaláról (One Call API 3.0 vagy Hourly Forecast).

## Telepítés és Beállítás

1. Másold le a `.env.example` fájlt `.env` néven:
   ```bash
   cp .env.example .env
   ```
2. Nyisd meg a `.env` fájlt és add meg az adataidat:
   - `OWM_API_KEY`: Az OpenWeatherMap API kulcsod.
   - `MY_LAT` / `MY_LONG`: A tartózkodási helyed koordinátái.
   -  Twilio beállítások az SMS értesítéshez.

3. Telepítsd a szükséges csomagokat:
   ```bash
   pip install requests python-dotenv
   ```

## Használat

Futtasd a központi szkriptet:

```bash
python main.py
```

A program ellenőrzi az előrejelzést, és ha az időjárási kód 700 alatti (ami esőt, havat vagy vihart jelez), küldi az értesítést.