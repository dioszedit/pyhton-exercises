import random
from turtle import Turtle, Screen

# Létrehozzuk a képernyőt és beállítjuk a méretét
screen = Screen()
screen.setup(width=500, height=400)

# Bekérjük a felhasználó tippjét egy popup ablakban
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# A teknőcök színeinek listája
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

# Verseny állapot jelző változó
is_race_on = False

# Létrehozunk 6 teknőcöt és elhelyezzük őket a kezdőpozícióban
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-125 + (i * 50)))
    turtles.append(new_turtle)

# Elindítjuk a versenyt
is_race_on = True
while is_race_on:
    for turtle in turtles:
        # Minden teknőc véletlenszerű távolságot halad előre (0-10 pixel között)
        turtle.forward(random.randint(0, 10))

        # Ellenőrizzük, hogy elérte-e valamelyik teknőc a célvonalat (x = 230)
        if turtle.xcor() > 230:
            is_race_on = False  # Verseny vége
            winning_color = turtle.pencolor() # Győztes teknőc színe

            # Kiírjuk az eredményt
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
