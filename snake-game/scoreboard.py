from turtle import Turtle

# Konstansok a pontszám, játék vége feliratok megjelenítéséhez
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    """
    A Scoreboard osztály a játék pontszámát kezeli és jeleníti meg.

    A Turtle osztályból származik, így közvetlenül képes szöveget írni a képernyőre.

    Attributes:
        score (int): A jelenlegi pontszám
    """

    def __init__(self):
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
        self.goto(x=0, y=270)
        self.show_score()

    def increase_score(self):
        """
        Növeli a pontszámot eggyel és frissíti a kijelzést.

        Ezt a metódust akkor kell hívni, amikor a kígyó ételt eszik.
        """
        self.score += 1
        self.show_score()

    def show_score(self):
        """
        Megjeleníti a jelenlegi pontszámot a képernyőn.

        Törli az előző pontszámot és kiírja az aktuális értéket.
        """
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Megjeleníti a "GAME OVER" üzenetet a képernyő közepén.

        Ezt a metódust akkor kell hívni, amikor a játék véget ér.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
