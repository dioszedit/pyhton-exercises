# Vélet irányú séta megvalósítása turtle grafikával
import random
from turtle import Turtle, Screen

def random_color():
    """Véletlen RGB színt generál (0-255 tartományban)"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

# Fordulási szögek (0° = jobbra, 90° = fel, 180° = balra, 270° = le)
angles = [0, 90, 180, 270]

# Rajzolási képernyő létrehozása és beállítása
screen = Screen()
screen.colormode(255) # RGB színmód beállítása (0-255 tartomány)

# Turtle objektum létrehozása és konfigurálása
turtle = Turtle()
turtle.pensize(10) # Toll mérete/vastagsága
turtle.speed("fastest") # Felyorsítja a kirajzolása

# Véletlen lépésszámú séta (0 és 100 között)
for _ in range(random.randint(0, 100)):
    turtle.color(random_color()) # Véletlen szín beállítása minden lépéshez
    turtle.forward(20) # 20 pixel előre mozgás
    turtle.setheading(random.choice(angles)) # Véletlen új irány kiválasztása

# A képernyő bezárása kattintásra vár
screen.exitonclick()