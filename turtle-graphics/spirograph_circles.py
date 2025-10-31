# Spirográf minta - Színes körök rajzolása turtle grafikával
# A program egy spirográf-szerű mintát hoz létre úgy, hogy körök sorozatát rajzolja,
# minden körrajzolás után kis szöggel elfordulva
import random
from turtle import Turtle, Screen


def random_color() -> tuple[float, float, float]:
    """Véletlen RGB színt generál (0-255 tartományban)"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# Rajzolási képernyő létrehozása és beállítása
screen = Screen()
screen.colormode(255)  # RGB színmód beállítása (0-255 tartomány)

# Turtle objektum létrehozása és konfigurálása
turtle = Turtle()
turtle.speed("fastest")  # Felyorsítja a kirajzolása


def draw_spirograph(size_of_gap: int) -> None:
    """
    Spirográf mintát rajzol körök sorozatával.

    Args:
        size_of_gap: A körök közötti szögeltérés fokban (1-360 közötti érték)
                     Minél kisebb az érték, annál sűrűbb lesz a minta
    """

    for i in range(int(360 / size_of_gap)):
        turtle.color(random_color())  # Véletlen szín beállítása minden lépéshez
        turtle.setheading(i * size_of_gap)  # Elfordul angle értékkel balra
        turtle.circle(80)  # Rajzol egy kört 80 egység sugarú


# Spirográf rajzolása
draw_spirograph(12)
# A képernyő bezárása kattintásra vár
screen.exitonclick()
