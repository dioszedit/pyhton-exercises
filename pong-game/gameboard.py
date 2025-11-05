from turtle import Screen, Turtle
from scoreboard import Scoreboard
from racket import Racket
from ball import Ball
from constants import UP, MIN_X, MAX_X, MIN_Y, MAX_Y, MOVE_DISTANCE, FONT, ALIGNMENT
import time


def show_game_over() -> None:
    """
    GAME OVER feliratot jeleníti meg
    """
    text = Turtle()
    text.hideturtle()
    text.color("white")
    text.write("GAME OVER", align=ALIGNMENT, font=FONT)


class Gameboard:
    def __init__(self) -> None:
        """
        Inicializálja a Gameboard objektumot.

        Beállítja a képernyőt, létrehozza a játékosok pontszámtábláit és ütőit,
        rajzolja meg a háló vonalat, beállítja a billentyűzet kezelést.
        """
        # Képernyő beállítása
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)  # Kikapcsolja az automatikus képernyő frissítést

        # Bal oldali játékos inicializálása
        self.person_left = Scoreboard((-80, 220))
        self.racket_left = Racket((MIN_X, 0))

        # Jobb oldali játékos inicializálása
        self.person_right = Scoreboard((80, 220))
        self.racket_right = Racket((MAX_X, 0))

        # Játéktér előkészítése
        self.create_net()
        self.ball = Ball()
        self.racket_listener()

    def create_net(self) -> None:
        """
        Létrehozza a játéktér közepén lévő szaggatott hálóvonalat.

        A háló vizuálisan elválasztja a két játékos területét.
        """
        net = Turtle()
        net.hideturtle()
        net.pensize(5)
        net.penup()
        net.color("white")
        # A háló a tábla alsó pontjától indul
        net.goto(x=0, y=MIN_Y)
        net.setheading(UP)

        # Szaggatott vonal rajzolása
        for _ in range(15):
            net.pendown()
            net.fd(MOVE_DISTANCE)
            net.penup()
            net.fd(MOVE_DISTANCE)

        self.screen.update()

    def racket_listener(self) -> None:
        """
        Beállítja a billentyűzet eseménykezelőket az ütők mozgatásához.

        Bal oldali játékos: W/S billentyűk (fel/le)
        Jobb oldali játékos: Nyíl billentyűk (fel/le)
        """
        self.screen.listen()
        self.screen.onkey(self.racket_left.up, "w")
        self.screen.onkey(self.racket_left.down, "s")
        self.screen.onkey(self.racket_right.up, "Up")
        self.screen.onkey(self.racket_right.down, "Down")

    def run(self) -> None:
        """
        A játék fő ciklusa.
        """
        is_on_game = True
        while is_on_game:
            self.ball.move()
            time.sleep(0.1)
            self.screen.update()

            if self.person_left.score == 10 or self.person_right.score == 10:
                is_on_game = False
            else:
                # Vízszintesen falnak ütközik a labda
                if self.ball.xcor() > MAX_X:
                    self.person_left.increase_score()
                    self.ball.reset_position()

                if self.ball.xcor() < MIN_X:
                    self.person_right.increase_score()
                    self.ball.reset_position()

                # Fent vagy lent falnak ütjözik a labda, akkor visszapattan
                if self.ball.ycor() > MAX_Y or self.ball.ycor() < MIN_Y:
                    self.ball.bounce_y()

                # Bal ütőnek ütközik a labda
                if self.ball.distance(self.racket_left) < 50 and self.ball.xcor() < (MIN_X + 30):
                    self.ball.bounce_x()

                # Jobb ütőnek ütközik a labda
                if self.ball.distance(self.racket_right) < 50 and self.ball.xcor() > (MAX_X - 30):
                    self.ball.bounce_x()

        show_game_over()
        self.screen.exitonclick()
