"""
Játékos teknős kezelése a Turtle Crossing játékban.

Ez a modul tartalmazza a Player osztályt, amely a játékos által
irányított teknőst reprezentálja.
"""

from turtle import Turtle

# Konstansok a játékos pozíciójához és mozgásához
STARTING_POSITION: tuple[int, int] = (0, -280)  # Kezdőpozíció a képernyő alján
MOVE_DISTANCE: int = 10  # Egy lépés távolsága pixelben
FINISH_LINE_Y: int = 280  # Célvonal y koordinátája
UP: int = 90  # Felfelé irány (fok)
DOWN: int = 270  # Lefelé irány (fok)


class Player(Turtle):
    """
    A játékos teknőst reprezentáló osztály.

    A Turtle osztályból öröklődik, így rendelkezik annak összes
    tulajdonságával és metódusával.
    """

    def __init__(self) -> None:
        """
        Inicializálja a Player objektumot.

        Beállítja a teknős megjelenését, sebességét és kezdőpozícióját.
        """
        super().__init__()
        self.shape("turtle")  # Teknős alakú kurzor
        self.speed("fastest")  # Animáció sebessége (nem a mozgási sebesség!)
        self.penup()
        self.setheading(UP)
        self.goto(STARTING_POSITION)

    def move_up(self) -> None:
        """
        Felfelé mozgatja a játékos a teknőst.
        """
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def move_down(self) -> None:
        """
         Lefelé mozgatja a játékos a teknőst.
        """
        self.setheading(DOWN)
        if self.ycor() > -280:
            self.forward(MOVE_DISTANCE)

    def reset_position(self) -> None:
        """
        Visszahelyezi a játékost a kezdőpozícióba.

        Ezt a metódust akkor hívjuk, amikor a játékos sikeresen átért
        a célvonalon és új szintre lép.
        """
        self.goto(STARTING_POSITION)
        self.setheading(UP)
