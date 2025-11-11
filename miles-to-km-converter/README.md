# Mérföld - Kilométer Átváltó

Egy egyszerű asztali alkalmazás mérföld kilométerre való átváltásához, Tkinter GUI-val készítve.

## Leírás

Ez a program lehetővé teszi a mérföldet kilométerre való gyors átváltását egy felhasználóbarát grafikus felületen keresztül. A projekt oktatási célokra készült, hogy bemutassa a Tkinter alapvető használatát Python-ban.

## 🎯 Funkciók

- ✅ Mérföld -> Kilométer átváltás (1 mérföld = 1.60934 km)
- ✅ Input validáció (csak számokat fogad el)
- ✅ Tizedesjegyek támogatása (pont és vessző is használható)
- ✅ Nullázás / Mégse funkció
- ✅ Modern, kétszínű UI design
- ✅ Automatikus kerekítés 2 tizedesjegyre

## Használat

### Követelmények

- Python 3.x telepítve
- Tkinter (általában a Python-nal együtt települ)

### Futtatás
```bash
python main.py
```

### Használati útmutató

1. Írd be a mérföld értéket az input mezőbe
2. Kattints a **"Számold ki!"** gombra
3. Az eredmény megjelenik az alsó sötét panelban
4. A **"Mégse"** gombbal nullázhatod az értékeket

## Tkinter GUI Elemek

### Használt widgetek:

- **Label** - Szöveg megjelenítésére (címkék, eredmény)
- **Entry** - Szöveg bevitelére (mérföld érték)
- **Button** - Gombok (Számold ki!, Mégse)
- **Frame** - Elemek csoportosítására (eredmény panel)

### Layout Manager:

- **grid()** - Rácsos elrendezés a fő ablakban
- **pack()** - Egymás alatti elrendezés a Frame-en belül

### Grid Paraméterek:
```python
# Pozícionálás
row=0, column=0        # Sor és oszlop index
columnspan=2           # Több oszlopon átnyúlik
sticky="ew"            # Vízszintes kitöltés (east-west)
sticky="nsew"          # Teljes cella kitöltése

# Távolságok
padx=(0, 10)          # Vízszintes margó (bal, jobb)
pady=(0, 10)          # Függőleges margó (fent, lent)
```

## Design Elemek

### Színséma:

- **Felső rész**: Világos (#f0f0f0 alapértelmezett)
- **Alsó rész**: Sötét szürke (#3a3f47)
- **Kiemelés**: Narancs-piros (#ff6b4a)
- **Eredmény szöveg**: Fehér (#ffffff)

## Tanulási Célok

Ez a projekt a következő Python és Tkinter koncepciókat demonstrálja:

1. **GUI létrehozás** - Tkinter ablak és widgetek
2. **Layout management** - grid() és pack() használata
3. **Event handling** - Gomb kattintás kezelése (command paraméter)
4. **Input validáció** - Csak számok elfogadása
5. **Függvények** - Kód újrafelhasználás és szervezés
6. **String műveletek** - replace(), float() konverziók
7. **Widget konfigurálás** - config() metódus használata

## 🔧 Kód Struktúra
```
main.py
│
├── validate_number()      # Input validáció
├── calculate()            # Átváltás logika
├── cancel_or_reset()      # Nullázás
│
├── Window setup           # Ablak konfigurálás
├── Input section          # Label + Entry + Buttons
└── Result section         # Frame + Result labels
```

## 💡 Továbbfejlesztési Lehetőségek

- [ ] Kilométer -> Mérföld irányú átváltás hozzáadása
- [ ] További mértékegységek (km/h, mph, stb.)
- [ ] Előzmények mentése
- [ ] Téma váltás (világos/sötét mód)
- [ ] Billentyűparancsok (Enter = számolás, Esc = mégse)
- [ ] Input validáció vizuális feedback-del

## Megjegyzések

- Tizedesjel lehet pont (.) vagy vessző (,)
- Az eredmény automatikusan 2 tizedesjegyre kerekít
- Üres vagy "0" értéknél a program nullázza az eredményt

## Licenc

Szabad felhasználás oktatási célokra.