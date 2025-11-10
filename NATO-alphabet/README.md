# NATO Fonetikus Ábécé

## A feladat

Készíts egy programot, amely egy megadott szót átalakít NATO fonetikus ábécé kódokká!

**Példa:**
- Bemenet: `HELLO`
- Kimenet: `['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']`

A program:
1. Beolvassa a NATO fonetikus ábécé CSV fájlt
2. Bekér egy szót a felhasználótól
3. Minden betűt átalakít a megfelelő NATO kódra
4. Kiírja az eredményt lista formában

## Mit gyakoroltat ez a feladat?

### 1. **Dictionary Comprehension** (Szótár létrehozás)

A pandas DataFrame-ből egyetlen sorban készítünk szótárt:

```python
letter_dict = {row.letter: row.code for (index, row) in read_data.iterrows()}
```

**Hagyományos megoldás (for ciklus):**
```python
letter_dict = {}
for index, row in read_data.iterrows():
    letter_dict[row.letter] = row.code
```

**Eredmény:**
```python
{
    'A': 'Alfa',
    'B': 'Bravo',
    'C': 'Charlie',
    ...
}
```

**Mit tanul belőle?**
- Kompakt, olvasható kód írása
- Adatok transzformálása egyik struktúrából másikba
- Kulcs-érték párok létrehozása

---

### 2. **List Comprehension** (Lista létrehozás)

A szóból egyetlen sorban készítünk listát:

```python
phonetic_list = [letter_dict[letter] for letter in word]
```

**Hagyományos megoldás (for ciklus):**
```python
phonetic_list = []
for letter in word:
    phonetic_list.append(letter_dict[letter])
```

**Mit tanul belőle?**
- Tömör kód írása
- Iterálás stringeken
- Lista elemek transzformálása

---

### 3. **List Comprehension feltétellel** (Szűrés)

Ha csak az érvényes betűket akarjuk:

```python
phonetic_list = [letter_dict[letter] for letter in word if letter in letter_dict]
```

**Struktúra:**
```
[KIFEJEZÉS for ELEM in ITERÁLHATÓ if FELTÉTEL]
```

**Hagyományos megoldás:**
```python
phonetic_list = []
for letter in word:
    if letter in letter_dict:
        phonetic_list.append(letter_dict[letter])
```

**Mit tanul belőle?**
- Szűrés és transzformálás egyben
- Tiszta, pythonos kódstílus
- Hatékony adatfeldolgozás

---

## Comprehension példák lépésről lépésre

### Dictionary Comprehension

```python
# 1. lépés: Megértjük a DataFrame-et
print(read_data)
#   letter    code
# 0      A    Alfa
# 1      B   Bravo
# 2      C Charlie

# 2. lépés: Iterálás soronként
for index, row in read_data.iterrows():
    print(f"{row.letter} -> {row.code}")

# 3. lépés: Szótár készítése comprehension-nel
letter_dict = {row.letter: row.code for (index, row) in read_data.iterrows()}
```

### List Comprehension

```python
# 1. lépés: Megértjük a feladatot
word = "ABC"
# Minden betűt át kell alakítani

# 2. lépés: Hagyományos for ciklus
result = []
for letter in word:
    result.append(letter_dict[letter])

# 3. lépés: Ugyanaz comprehension-nel
result = [letter_dict[letter] for letter in word]
```

### List Comprehension feltétellel

```python
# 1. lépés: Problém - mi van, ha érvénytelen karakter van?
word = "A1B"  # Az '1' nincs a szótárban!

# 2. lépés: Szűrés hagyományosan
result = []
for letter in word:
    if letter in letter_dict:  # Ellenőrizzük!
        result.append(letter_dict[letter])

# 3. lépés: Ugyanaz comprehension-nel
result = [letter_dict[letter] for letter in word if letter in letter_dict]
```

---

## További gyakorlási lehetőségek

1. **Számok szűrése listából:**
   ```python
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   even = [n for n in numbers if n % 2 == 0]
   # [2, 4, 6, 8, 10]
   ```

2. **Stringek nagybetűssé alakítása:**
   ```python
   words = ['apple', 'banana', 'cherry']
   upper = [word.upper() for word in words]
   # ['APPLE', 'BANANA', 'CHERRY']
   ```

3. **Szótár invertálása:**
   ```python
   original = {'a': 1, 'b': 2, 'c': 3}
   inverted = {value: key for key, value in original.items()}
   # {1: 'a', 2: 'b', 3: 'c'}
   ```

---

## Tanulási célok

- ✅ Pandas DataFrame iterálás megértése
- ✅ Dictionary Comprehension elsajátítása
- ✅ List Comprehension elsajátítása
- ✅ Feltételes szűrés comprehension-ben