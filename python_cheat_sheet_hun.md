#  PYTHON SEGÉDLET
---

##  ALAPOK

###  Print (Kiírás)
Egy szöveget ír ki a konzolra.
```python
print("Hello World")
```

###  Input (Bemenet)
Kiír egy szöveget a konzolra, és bekér egy szöveges bemenetet a felhasználótól.
```python
input("Mi a neved?")
```

###  Megjegyzések
A `# ` szimbólum elé írva megjegyzéseket tehetsz a kódsorba. A számítógép figyelmen kívül hagyja a megjegyzéseket.
```python
# Ez egy megjegyzés
print("Ez kód")
```

###  Változók
A változó nevet ad egy adatdarabnak. Olyan, mint egy doboz címkével, amely megmondja, mi van a dobozban.
```python
my_name = "John"
my_age = 10
```

###  A += Operátor
Ez egy kényelmes módja annak, hogy azt mondjuk: "vedd az előző értéket és add hozzá".
```python
my_age = 12
my_age += 4
# my_age most 16
```

---

##  ADATTÍPUSOK

###  Egész számok (Integer)
Az egész számok kerek számok.
```python
my_number = 354
```

###  Lebegőpontos számok (Float)
A lebegőpontos számok tizedesjegyekkel rendelkező számok. Amikor olyan számítást végzel, amely törtszámot eredményez, például 4 ÷ 3, az eredmény mindig lebegőpontos szám lesz.
```python
my_float = 3.14159
```

###  Karakterláncok (String)
A karakterlánc karakterek sorozata. Dupla idézőjelekkel kell körülvenni.
```python
my_string = "Hello"
```

###  Karakterlánc-összefűzés
Karakterláncokat adhatsz össze új karakterlánc létrehozásához. Ezt összefűzésnek nevezzük. Új karakterláncot eredményez.
```python
"Szia" + "John"
# SziaJohn lesz belőle
```

###  Escape karakter a karakterláncban
Mivel a dupla idézőjel speciális karakter (karakterláncot jelöl), ha használni szeretnéd egy karakterláncban, akkor escape-elned kell egy "\" jellel.
```python
speech = "Azt mondta: \"Szia\""
print(speech)
# kiírja: Azt mondta: "Szia"
```

###  F-stringek
Változót illeszthetsz be egy karakterláncba f-stringek használatával. A szintaxis egyszerű, csak illeszd be a változót kapcsos zárójelek közé {}.
```python
days = 365
print(f"Egy évben {days} nap van")
```

###  Adattípusok konvertálása
Konvertálhatsz egy változót egyik adattípusból a másikba.

Konvertálás lebegőpontos számmá:
```python
float()
```

Konvertálás egész számmá:
```python
int()
```

Konvertálás karakterlánccá:
```python
str()
```

Példa:
```python
n = 354
new_n = float(n)
print(new_n) # eredmény: 354.0
```

###  Adattípusok ellenőrzése
A `type()` függvénnyel ellenőrizheted, hogy egy adott változó milyen adattípusú.
```python
n = 3.14159
type(n) # eredmény: float
```

---

##  MATEMATIKA

###  Aritmetikai operátorok
Matematikai számításokat végezhetsz Pythonban, ha ismered a megfelelő operátorokat.
```python
3+2   # Összeadás
4-1   # Kivonás
2*3   # Szorzás
5/2   # Osztás
5**2  # Hatványozás
```

###  A += Operátor
Ez egy kényelmes módja egy változó módosításának. Veszi a változó meglévő értékét és hozzáad.
Használhatod a többi matematikai operátort is, pl. -= vagy *=
```python
my_number = 4
my_number += 2
# eredmény 6
```

###  A Modulo Operátor
Gyakran szeretnéd tudni, mennyi a maradék egy osztás után.
pl. 4 ÷ 2 = 2 maradék nélkül
de 5 ÷ 2 = 2 maradék 1-gyel

A modulo nem az osztás eredményét adja, csak a maradékot.
Nagyon hasznos lehet bizonyos helyzetekben, pl. annak kiderítésére, hogy egy szám páros vagy páratlan.
```python
5 % 2
# eredmény 1
```

---

##  HIBÁK

###  Szintaxis hiba (Syntax Error)
A szintaxis hibák akkor történnek, amikor a kódod nem értelmes a számítógép számára. Ez történhet, mert elírtál valamit, túl sok zárójel van, vagy hiányzik egy vessző.
```python
print(12 + 4))
  File "<stdin>", line 1
    print(12 + 4))
                 ^
SyntaxError: unmatched ')'
```

###  Névhiba (Name Error)
Ez akkor történik, amikor olyan változó van egy névvel, amelyet a számítógép nem ismer fel. Általában azért van, mert elírtad egy korábban létrehozott változó nevét.
Megjegyzés: a változónevek érzékenyek a kis- és nagybetűkre!
```python
my_number = 4
my_Number + 2
Traceback (most recent call last): File "<stdin>", line 1,
NameError: name 'my_Number' is not defined
```

###  Nullával való osztás hibája (Zero Division Error)
Ez akkor történik, amikor megpróbálsz nullával osztani. Ez matematikailag lehetetlen, ezért a Python is panaszkodik.
```python
5 % 0
Traceback (most recent call last): File "<stdin>", line 1,
ZeroDivisionError: integer division or modulo by zero
```

---

##  FÜGGVÉNYEK

###  Függvények létrehozása
Ez az alapvető szintaxis egy függvényhez Pythonban. Lehetővé teszi, hogy nevet adj egy utasításkészletnek, így többször is aktiválhatod anélkül, hogy újra kellene írnod vagy másolnod-beillesztened. A függvény tartalmának behúzottnak kell lennie, jelezve, hogy a függvényen belül van.
```python
def my_function():
    print("Hello")
    name = input("A neved:")
    print("Hello")
```

###  Függvények meghívása
A függvényt úgy aktiválod, hogy meghívod. Ezt egyszerűen úgy teszed, hogy írod a függvény nevét, amit egy pár kerek zárójel követ. Ez lehetővé teszi, hogy meghatározd, mikor induljon el a függvény és hányszor.
```python
my_function()
my_function()
# A my_function függvény kétszer fog lefutni.
```

###  Függvények bemenetekkel
Az egyszerű függvényeken túl bemenetet is adhatsz a függvénynek. Így minden alkalommal a függvény valami mást csinálhat a bemenettől függően. Hasznossabbá és újrafelhasználhatóbbá teszi a függvényt.
```python
def add(n1, n2):
    print(n1 + n2)

add(2, 3)
```

###  Függvények kimenetekkel
A bemenetek mellett a függvénynek kimenete is lehet. A kimeneti értéket a "return" kulcsszó előzi meg. Ez lehetővé teszi a függvény eredményének tárolását.
```python
def add(n1, n2):
    return n1 + n2

result = add(2, 3)
```

###  Változók hatóköre (Scope)
A függvényen belül létrehozott változók megsemmisülnek, miután a függvény végrehajtódott. Az a hely (kódsor), ahol használsz egy változót, meghatározza annak értékét.
Itt n értéke 2, de a my_function()-ön belül n értéke 3.
Tehát n kiírása a függvényen belül és kívül meghatározza annak értékét.
```python
n = 2
def my_function():
    n = 3
    print(n)

print(n) # Kiírja: 2
my_function() # Kiírja: 3
```

###  Kulcsszavas argumentumok (Keyword Arguments)
Függvény hívásakor kulcsszavas argumentumot vagy csak az értéket adhatod meg.
Kulcsszavas argumentum használata azt jelenti, hogy nem kell követned a sorrendet a bemenetek megadásakor.
```python
def divide(n1, n2):
    result = n1 / n2

# 1. lehetőség:
divide(10, 5)
# 2. lehetőség:
divide(n2=5, n1=10)
```

---

##  FELTÉTELEK

###  If (Ha)
Ez az alapvető szintaxis annak tesztelésére, hogy egy feltétel igaz-e. Ha igen, a behúzott kód végrehajtásra kerül, ha nem, akkor kihagyásra.
```python
n = 5
if n > 2:
    print("Nagyobb mint 2")
```

###  Else (Különben)
Ezzel olyan kódot adhatsz meg, amely végrehajtásra kerül, ha a feltétel hamis.
```python
age = 18
if age > 16:
    print("Vezethetsz")
else:
    print("Ne vezess")
```

###  Elif (Különben ha)
A kezdeti If feltételen túl további feltételeket adhatsz meg, amelyeket akkor tesztel, ha az első feltétel hamis.
Amint egy elif feltétel igaz, a többi elif feltétel már nem kerül ellenőrzésre és átugorja őket.
```python
weather = "sunny"
if weather == "rain":
    print("vigyél esernyőt")
elif weather == "sunny":
    print("vigyél napszemüveget")
elif weather == "snow":
    print("vigyél kesztyűt")
```

###  Összehasonlító operátorok
Ezek a matematikai összehasonlító operátorok lehetővé teszik a feltételes ellenőrzések finomítását.
```python
> Nagyobb mint
< Kisebb mint
>= Nagyobb vagy egyenlő
<= Kisebb vagy egyenlő
== Egyenlő
!= Nem egyenlő
```

###  and (és)
Ez azt várja, hogy mindkét feltétel igaz legyen az and két oldalán.
```python
s = 58
if s < 60 and s > 50:
    print("Az osztályzatod C")
```

###  or (vagy)
Ez azt várja, hogy a feltételek egyike igaz legyen az or két oldalán. Alapvetően mindkét feltétel nem lehet hamis.
```python
age = 12
if age < 16 or age > 200:
    print("Nem vezethetsz")
```

###  not (nem)
Ez megfordítja a feltétel eredeti eredményét. pl. ha igaz volt, akkor most hamis.
```python
if not 3 > 1:
    print("valami")
# Nem lesz kiírva.
```

---

##  CIKLUSOK

###  While ciklus
Ez egy olyan ciklus, amely addig ismétli magát, amíg a while feltétel hamissá nem válik.
```python
n = 1
while n < 100:
    n += 1
```

###  For ciklus
A for ciklusok több kontrollt adnak, mint a while ciklusok. Bármilyen iterálható dolgon végigciklushatsz. pl. egy tartomány, egy lista, egy dictionary vagy tuple.
```python
all_fruits = ["apple", "banana", "orange"]
for fruit in all_fruits:
    print(fruit)
```

###  _ egy For ciklusban
Ha az érték, amelyen a for ciklus végigiterál, pl. a szám a tartományban vagy az elem a listában, nem szükséges, helyettesítheted egy aláhúzással.
```python
for _ in range(100):
    # Csinálj valamit 100-szor.
```

###  break (kilépés)
Ez a kulcsszó lehetővé teszi, hogy kitörj a ciklusból. For vagy while ciklusban is használhatod.
```python
scores = [34, 67, 99, 105]
for s in scores:
    if s > 100:
        print("Érvénytelen")
        break
    print(s)
```

###  continue (folytatás)
Ez a kulcsszó lehetővé teszi, hogy kihagyd a ciklus ezen iterációját és a következőre ugorj. A ciklus továbbra is folytatódik, de felülről kezdi.
```python
n = 0
while n < 100:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
# Kiírja az összes páratlan számot
```

###  Végtelen ciklusok
Néha az a feltétel, amelyet ellenőrzöl, hogy a ciklus folytatódjon-e, sosem válik hamissá. Ebben az esetben a ciklus örökké folytatódik (vagy amíg a számítógéped meg nem állítja). Ez gyakoribb while ciklusoknál.
```python
while 5 > 1:
    print("I'm a survivor")
```

---

##  LISTA METÓDUSOK

###  Listák összeadása
Kiterjeszthetsz egy listát egy másik listával az extend kulcsszó vagy a + szimbólum használatával.
```python
list1 = [1, 2, 3]
list2 = [9, 8, 7]
new_list = list1 + list2
list1 += list2
```

###  Elem hozzáadása listához
Ha csak egyetlen elemet szeretnél hozzáadni egy listához, az `.append()` metódust kell használnod.
```python
all_fruits = ["apple", "banana", "orange"]
all_fruits.append("pear")
```

###  Lista index
Egy adott elem kinyeréséhez egy listából használhatod az index számát.
Ez a szám lehet negatív is, ha a lista végéről szeretnél kezdeni számolni.
```python
letters = ["a", "b", "c"]
letters[0]
# Eredmény:"a"
letters[-1]
# Eredmény: "c"
```

###  Lista szeletelés (Slicing)
A lista index és a kettőspont szimbólum használatával szétvághatsz egy listát, hogy csak a kívánt részt kapd meg.
A kezdet benne van, de a vég nincs.
```python
# list[start:end]
letters = ["a","b","c","d","e","f"]
letters[1:3]
# Eredmény: ["b", "c"]
letters[2:5:2] # 2-től 5-ig nézzük, de csak minden 2.-at szeretnénk megkapni
# Eredmény: ["c", "e"]
letters[::2] # minden 2. elemet szeretnénk megkapni
# Erdemény: ["a", "c", "e"]
letters[::-1] # megfordítja a listát
# Eredmény ["f", "e", "d", "c", "b", "a"]
```

### Lista előállítása másik listából
Egy listának az előállítása egy másik listából a következő elvet követi
*new_list = [new_item for item in other_list]*
```python
# Hagyomásnyosan előállítva
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    new_item = n * 2
    new_list.append(new_item)
```
 
```python
# Egyszerűsítve a fenti for ciklus helyett
numbers = [1, 2, 3]
new_list = [ n * 2 for n in numbers]
```
### Feltételesen lista előállítása másik listából
Egy listának az előállítása egy másik listából feltétel teljesülése esetén a következő elvet követi
*new_list = [new_item for item in other_list if test]*

```python
# Rövid nevekre vagyunk kiváncsiak, amik 5 karaternél kevesebből állnak
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "John", "Jane", "Jill", "Jenny"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
# Eredmény: ['Alex', 'Beth', 'Dave', 'John', 'Jane', 'Jill']
```
---

##  BEÉPÍTETT FÜGGVÉNYEK

###  Range (Tartomány)
Gyakran számok tartományát szeretnéd generálni. Megadhatod a kezdetet, végét és a lépést.
A kezdet benne van, de a vég nincs:
start <= range < end
```python
#  range(start, end, step)
for i in range(6, 0, -2):
    print(i)
#  eredmény: 6, 4, 2
#  0 nincs benne.
```

###  Randomizálás (Véletlenszerűség)
A random függvények a random modulból származnak, amelyet importálni kell.
Ebben az esetben a kezdet és a vég is benne van:
start <= randint <= end
```python
import random
#  randint(start, end)
n = random.randint(2, 5)
# n lehet 2, 3, 4 vagy 5.
```

###  Round (Kerekítés)
Ez matematikai kerekítést végez.
Tehát 3.1-ből 3 lesz, 4.5-ből 5 és 5.8-ból 6.
```python
round(4.6)
#  eredmény: 5
```

###  abs (Abszolút érték)
Ez az abszolút értéket adja vissza.
Alapvetően eltávolítja az összes negatív előjelet.
```python
abs(-4.6)
#  eredmény: 4.6
```

---

##  MODULOK

###  Importálás
Néhány modul előre telepítve van a pythonnal, pl. random/datetime
Más modulokat telepíteni kell a pypi.org-ról
```python
import random
n = random.randint(3, 10)
```

###  Álnevek (Aliasing)
Az `as` kulcsszó használatával más nevet adhatsz a modulodnak.
```python
import random as r
n = r.randint(1, 5)
```

###  Importálás modulokból
Importálhatsz egy specifikus dolgot egy modulból, pl. egy függvényt/osztályt/konstanst.
Ezt a `from` kulcsszóval teheted meg.
Ez megkímélhet attól, hogy sokszor ugyanazt kell gépelned.
```python
from random import randint
n = randint(1, 5)
```

###  Minden importálása
Használhatod a helyettesítő karaktert (*), hogy mindent importálj egy modulból. Vigyázat, ez általában csökkenti a kód olvashatóságát.
```python
from random import *
list = [1, 2, 3]
choice(list)
#  Olvashatóbb/érthetőbb
# random.choice(list)
```

---

##  OSZTÁLYOK ÉS OBJEKTUMOK

###  Python osztály létrehozása
Osztályt a `class` kulcsszó használatával hozol létre.
Megjegyzés: az osztálynevek Pythonban PascalCase formátumúak.
Tehát egy üres osztály létrehozásához:
```python
class MyClass:
    # osztály definiálása
```

###  Objektum létrehozása osztályból
Új objektumpéldányt az osztálynév + () használatával hozhatsz létre.
```python
class Car:
    pass

my_toyota = Car()
```

###  Osztály metódusok
Létrehozhatsz egy függvényt, amely egy osztályhoz tartozik, ezt metódusnak nevezzük.
```python
class Car:
    def drive(self):
        print("move")

my_honda = Car()
my_honda.drive()
```

###  Osztály változók
Létrehozhatsz egy változót egy osztályban.
A változó értéke elérhető lesz az osztályból létrehozott összes objektum számára.
```python
class Car:
    colour = "black"

car1 = Car()
print(car1.colour) # black
```

###  Osztály tulajdonságok (Properties)
Létrehozhatsz egy változót egy osztály init() metódusában, így az osztályból létrehozott összes objektumnak hozzáférése lesz ahhoz a változóhoz.
```python
class Car:
    def __init__(self, name):
        self.name = "Jimmy"
```

###  A __init__ metódus
Az init metódus minden alkalommal meghívódik, amikor új objektumot hozol létre az osztályból.
```python
class Car:
    def __init__(self):
        print("Building car")

my_toyota = Car()
# Látni fogod, hogy "building car" ki lett írva.
```

###  Osztály öröklődés (Inheritance)
Amikor új osztályt hozol létre, örökölheted egy másik osztály metódusait és tulajdonságait.
```python
class Animal:
    def breathe(self):
        print("breathing")

class Fish(Animal):
    def breathe(self):
        super().breathe()
        print("underwater")

nemo = Fish()
nemo.breathe()
# Eredmény:
# breathing
# underwater
```

---

Forrás: **www.appbrewery.com**