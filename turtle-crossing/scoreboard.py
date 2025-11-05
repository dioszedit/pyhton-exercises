"""
Szint megjelenítése a Turtle Crossing játékban.

Ez a modul tartalmazza a Scoreboard osztályt, amely a játékos
aktuális szintjét jeleníti meg és kezeli a játék vége üzenetet.
"""

from turtle import Turtle

# Konstansok a szöveg megjelenítéséhez
FONT: tuple[str, int, str] = ("Courier", 24, "normal")
ALIGNMENT_CENTER: str = "center"
ALIGNMENT_LEFT: str = "left"


class Scoreboard(Turtle):
    """
    A pontszám (szint) megjelenítését kezelő osztály.

    A Turtle osztályból öröklődik, és a képernyő bal felső sarkában
    jeleníti meg az aktuális szintet.

    Attributes:
        level (int): A játékos aktuális szintje
    """

    def __init__(self) -> None:
        """
        Inicializálja a Scoreboard objektumot.

        Beállítja a kezdő szintet (1), elrejti a teknős kurzort,
        és megjeleníti a szintet a képernyő bal felső sarkában.
        """
        super().__init__()

        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=250)
        self.show_level()

    def increase_level(self) -> None:
        """
        Növeli a szintet eggyel és frissíti a kijelzést.
        """
        self.level += 1
        self.show_level()

    def show_level(self) -> None:
        """
        Megjeleníti a jelenlegi szintet a képernyőn.

        Törli az előző szövegét és kiírja az aktuális szint értékét.
        A szöveg balra igazított és a bal felső sarokban jelenik meg.
        """
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT_LEFT, font=FONT)

    def game_over(self) -> None:
        """
        Megjeleníti a "GAME OVER" üzenetet a képernyő közepén.

        Ezt a metódust akkor hívjuk, amikor a játékos nekimegy
        egy autónak és vége a játéknak.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT_CENTER, font=FONT)
