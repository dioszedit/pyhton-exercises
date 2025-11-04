import random
from turtle import Turtle
from constans import BALL_STEP, MAX_X, MAX_Y


class Ball(Turtle):
    """
    A Ball osztály a labdát reprezentálja a Pong játékban.

    A Turtle osztályból származik, és kezeli a labda mozgását és
    irányváltoztatását a játéktéren.

    Attributes:
        x_move (int): A labda vízszintes mozgásának mértéke
        y_move (int): A labda függőleges mozgásának mértéke
    """

    def __init__(self) -> None:
        """
        Inicializálja a Ball objektumot.

        Beállítja a labda megjelenését (fehér kör), és véletlenszerű
        kezdő irányt választ a labda mozgásához.
        """
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        # Véletlenszerű kezdő irány választása
        self.x_move = random.choice([-10, 10])  # Balra vagy jobbra
        self.y_move = random.choice([-10, 10])  # Fel vagy le

    def move(self) -> None:
        """
        Mozgatja a labdát az aktuális irányában.

        Kiszámítja a labda új pozícióját az x_move és y_move értékek alapján.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self) -> None:
        """
        Megfordítja a labda függőleges irányát.
        """
        self.y_move *= -1

    def bounce_x(self) -> None:
        """
        Megfordítja a labda vízszintes irányát.
        """
        self.x_move *= -1

    def reset_position(self) -> None:
        """
        A játéktér közepére helyezi a labdát és az ellenkező játékos felé irányítja a labdát
        """
        self.goto(0, 0)
        self.y_move = random.choice([-10, 10])
        self.bounce_x()
