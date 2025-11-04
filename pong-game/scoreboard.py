from turtle import Turtle
from constans import ALIGNMENT, FONT


class Scoreboard(Turtle):
    """
    A Scoreboard osztály a játék pontszámát kezeli és jeleníti meg.

    A Turtle osztályból származik, így közvetlenül képes szöveget írni a képernyőre.

    Attributes:
        score (int): A jelenlegi pontszám
    """

    def __init__(self, position: tuple[int, int]) -> None:
        """
        Inicializálja a Scoreboard objektumot.

        Beállítja a kezdeti pontszámot 0-ra, elrejti a turtle kurzort,
        és megjeleníti a pontszámot a képernyő tetején.
        """
        super().__init__()

        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.show_score()

    def increase_score(self) -> None:
        """
        Növeli a pontszámot eggyel és frissíti a kijelzést.
        """
        self.score += 1
        self.show_score()

    def show_score(self) -> None:
        """
        Megjeleníti a jelenlegi pontszámot a képernyőn.

        Törli az előző pontszámot és kiírja az aktuális értéket.
        """
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
