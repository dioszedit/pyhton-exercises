"""
Snake Game - Kígyó játék Turtle grafikával

Ez a program egy klasszikus Snake játékot valósít meg, ahol a játékos
a nyilakkal irányítja a kígyót a képernyőn.
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Képernyő inicializálása és beállítása
screen = Screen()
screen.setup(width=600, height=600)  # 600x600 pixeles ablak
screen.bgcolor("black")  # Fekete háttér
screen.title("Snake Game")  # Ablak címe
screen.tracer(0)  # Animáció kikapcsolása (manuális frissítéshez)

# Kígyó és étel objektumok létrehozása
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Billentyűzet események figyelése
screen.listen()
screen.onkey(fun=snake.left, key="Left")  # Bal nyíl - balra fordulás
screen.onkey(fun=snake.right, key="Right")  # Jobb nyíl - jobbra fordulás
screen.onkey(fun=snake.up, key="Up")  # Fel nyíl - felfelé fordulás
screen.onkey(fun=snake.down, key="Down")  # Le nyíl - lefelé fordulás

# Játék fő ciklusa
game_is_on = True
while game_is_on:
    screen.update()  # Képernyő frissítése (animáció megjelenítése)
    time.sleep(0.1)  # 0.1 másodperc várakozás (játék sebessége)

    snake.move()  # Kígyó mozgatása előre

    if food.distance(snake.head()) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    #  ütközés vizsgálat a fallal
    if snake.head().xcor() > 280 or snake.head().xcor() < -280 or snake.head().ycor() > 280 or snake.head().ycor() < -280:
        scoreboard.show_game_over()
        game_is_on = False

    # ütközés vizsgálat a kígyó saját farkával
    # listák szeletelése (list slicing - list[start:end]) - az 1. indextől az utolsóig adja vissza a listát
    for segment in snake.body[1:]:  # minden szegmenst vizsgálunk kivéve a kígyó fejét
        if snake.head().distance(segment) < 10:
            scoreboard.show_game_over()
            game_is_on = False

screen.exitonclick()  # Ablak bezárása kattintásra
