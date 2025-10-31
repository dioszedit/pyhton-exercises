# Négyzet kirajzolás turtle grafikával
from turtle import Turtle, Screen

# Turtle objektum létrehozása és beállítása
turtle = Turtle()
turtle.color("brown4")

# Négyzet kirajzolása
for _ in range(4):
    turtle.right(90) # 90 fokkal fordul jobra
    turtle.forward(100) # Rajzol 10 egységet előre

# Képernyő objektum létrehozása és bezárásra várakozás
screen = Screen()
screen.exitonclick()