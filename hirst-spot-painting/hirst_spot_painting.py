# Hirst-stílusú pöttyös festmény - Damien Hirst spot painting reprodukció
# A program egy négyzetrács elrendezésben színes pöttyöket rajzol,
# a színeket egy képfájlból nyeri ki a colorgram könyvtár segítségével

import colorgram  # Csomag leírás: https://pypi.org/project/colorgram.py/
import random
from turtle import Turtle, Screen

# Konstansok
GRID_SIZE: int = 10  # A rács mérete (sorok és oszlopok száma)
DOT_SPACING: int = 50  # Pöttyök közötti távolság pixelben
DOT_SIZE: int = 20  # Egy pötty átmérője pixelben

turtle = Turtle()
turtle.speed("fastest")
turtle.hideturtle() # Elrejtjük a kurzort

screen = Screen()
screen.colormode(255)


def hirst_colors() -> list[tuple[int, int, int]]:
    """
    Színpalettát készít egy képfájlból a colorgram könyvtár segítségével.

    A függvény kinyeri a domináns színeket a 'hirst_colors.webp' fájlból
    és RGB tuple-ök listájaként adja vissza őket.

    Returns:
        list[tuple[int, int, int]]: RGB színek listája, ahol minden szín
                                     egy (r, g, b) tuple 0-255 értékekkel
    """

    # A képből 15 domináns szín kinyerése
    list_colors = colorgram.extract('hirst_colors.webp', 15)
    rgb_colors = []

    # Minden szín konvertálása RGB tuple-lé
    for color in list_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    return rgb_colors


def turtle_step(gap: int) -> None:
    """
    A teknőcöt előre mozgatja anélkül, hogy rajzolna.

    Args:
        gap: A megtett távolság pixelben
    """
    turtle.penup()
    turtle.forward(gap)
    turtle.pendown()


def draw_spots(colors, row_or_col_num) -> None:
    """
    Pöttyök négyzetrácsát rajzolja a megadott színekkel.

    A függvény row_or_col_num x row_or_col_num méretű rácsban helyezi el
    a pöttyöket, minden pötty véletlenszerűen választott színű.

    Args:
        colors: RGB színek listája, amelyekből véletlenszerűen választ
        row_or_col_num: A rács mérete (sorok és oszlopok száma)
    """
    # Sorok rajzolása
    for row in range(row_or_col_num):
        # Oszlopok rajzolása az aktuális sorban
        for col in range(row_or_col_num):
            turtle.dot(DOT_SIZE, random.choice(colors))
            turtle_step(DOT_SPACING)

        # Következő sor kezdőpozíciójára ugrás
        turtle.setheading(90)
        turtle_step(DOT_SPACING)
        turtle.setheading(180)
        turtle_step(DOT_SPACING * row_or_col_num)
        turtle.setheading(0)


# Kezdő pozíció beállítása (balra-le a középponthoz képest)
# Így a kész rajz körübelül a képernyő közepén lesz
turtle.setheading(225)
turtle_step(int((DOT_SPACING * GRID_SIZE) / 1.5))
turtle.setheading(0)

# "Hirst" pöttyös festmény rajzolása
draw_spots(hirst_colors(), GRID_SIZE)

# A képernyő bezárása kattintásra vár
screen.exitonclick()
