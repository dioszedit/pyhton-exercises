# Szaggatott vonal rajzolása turtle grafikával
from turtle import Turtle, Screen

# Turtle objektum létrehozása
turtle = Turtle()
# turtle.shape("circle") # Alternatív alakzat
turtle.color("brown4") # Barna szín beállítása

# 15 szaggatott szakasz rajzolása
for _ in range(15):
    turtle.forward(10) # Látható vonal rajzolása (10 egység)
    turtle.penup() # Toll felemelése (nem rajzol)
    turtle.forward(10)  # Láthatatlan rész (10 egység)
    turtle.pendown() # Toll leengedése (újra rajzol)

# Képernyő objektum létrehozása és bezárásra várakozás
screen = Screen()
screen.exitonclick()