# Coffee Machine Simulator (OOP verzió)

## Leírás

Ez egy objektum-orientált programozási (OOP) elvek szerint megírt kávégép szimulátor program Python nyelven. A program egy virtuális kávégépet szimulál, amely különböző italokat képes készíteni, kezeli a hozzávalókat, és pénzügyileg is nyilvántartja a tranzakciókat.

## Funkciók

### Főbb képességek:
- **Italválasztás**: Különböző kávéitalok közül választhat a felhasználó
- **Erőforrás-kezelés**: A gép ellenőrzi, hogy elegendő hozzávaló áll-e rendelkezésre az ital elkészítéséhez
- **Pénzkezelés**: Érmék fogadása és visszajáró kiszámítása
- **Riportok**: Aktuális készlet és pénzügyi adatok lekérdezése
- **Gép kikapcsolása**: Munkamenet befejezése

### Parancsok:
- **Italnevek** (pl. "espresso", "latte", "cappuccino"): Ital rendelése
- **"report"**: Aktuális erőforrások (víz, tej, kávé) és pénzügyi összesítő megjelenítése
- **"off"**: Kávégép kikapcsolása és program leállítása

## Használat

1. Futtassa a `main.py` fájlt:
   ```bash
   python main.py
   ```

2. Válasszon a menüből egy italt vagy adjon meg egy parancsot

3. Pénz bedobása esetén követi a program utasításait (érmék száma)

4. Ha minden rendben van, a gép elkészíti az italt és kiadja a visszajárót (ha van)

## Projekt struktúra
```
coffe-machine-in-oop/ 
├── main.py # Főprogram, felhasználói interfész 
├── menu.py # Menu osztály - elérhető italok kezelése 
├── coffee_maker.py # CoffeeMaker osztály - hozzávalók és italok készítése 
└── money_machine.py # MoneyMachine osztály - pénzügyi tranzakciók kezelése
```

## OOP Elvek

A program három fő osztályt használ:
- **Menu**: Kezeli az elérhető italokat és recepteket
- **CoffeeMaker**: Nyilvántartja az erőforrásokat és elkészíti az italokat
- **MoneyMachine**: Kezeli a pénzügyeket (fizetés, visszajáró, profit)

## Követelmények

- Python 3.x

## Megjegyzések

A program egy egyszerű parancssori alkalmazás, amely oktatási célokra készült az OOP koncepciók bemutatására.