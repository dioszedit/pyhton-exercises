"""
Konstansok a Pong játékhoz.

Ez a modul tartalmazza az összes fontos konstans értéket, amelyeket
a játék különböző részei használnak (pozíciók, méretek, irányok, stb.).
"""

# Szöveg formázásokhoz: pl.: pontszám megjelenítéséhez
ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

# Irányok fokban megdava
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Lépésköz - háló rajzoláshoz és ütő mozgatáshoz
MOVE_DISTANCE = 20
BALL_STEP = 10

# Koordináta keretek
MAX_Y = 280
MIN_Y = -280
MAX_X = 360
MIN_X = -360
