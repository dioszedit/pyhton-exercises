"""
Konstansok a Pong játékhoz.

Ez a modul tartalmazza az összes fontos konstans értéket, amelyeket
a játék különböző részei használnak (pozíciók, méretek, irányok, stb.).
"""

# Szöveg formázásokhoz: pl.: pontszám megjelenítéséhez
ALIGNMENT: str = "center"
FONT: tuple[str, int, str] = ("Courier", 40, "normal")

# Irányok fokban megdava
UP: int = 90
DOWN: int = 270
LEFT: int = 180
RIGHT: int = 0

# Lépésköz - háló rajzoláshoz és ütő mozgatáshoz
MOVE_DISTANCE: int = 20
BALL_STEP: int = 10

# Koordináta keretek
MAX_Y: int = 280
MIN_Y: int = -280
MAX_X: int = 360
MIN_X: int = -360
