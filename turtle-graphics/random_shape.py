# Véletlenszerű színű geometriai alakzatok rajzolása turtle grafikával
import random
from turtle import Turtle, Screen

# Elérhető színek listája az alakzatokhoz
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def draw_shape(num_sides: int, s_turtle: Turtle) -> None:
    """
    Szabályos sokszöget rajzol a megadott oldalszámmal.

    Args:
        num_sides: Az alakzat oldalainak száma
        s_turtle: A turtle objektum, amely rajzol
    """
    # Kiszámítja a fordulási szöget az oldalszám alapján
    angle = 360 / num_sides
    # Minden oldalért
    for _ in range(num_sides):
        s_turtle.forward(100) # Előre megy 100 egységet
        s_turtle.right(angle) # Jobbra fordul a kiszámított szöggel

# Turtle objektum létrehozása és beállítása
turtle = Turtle()
turtle.shape("turtle")

# Háromszögtől kilencszögig rajzol alakzatokat
for i in range(3, 10):
    turtle.color(random.choice(colors)) # Véletlenszerű szín választása
    draw_shape(i, turtle) # Alakzat rajzolása i oldalszámmal

# A képernyő bezárása kattintásra vár
Screen().exitonclick()
