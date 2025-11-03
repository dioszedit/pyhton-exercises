from turtle import Turtle

# Konstansok a kígyó mozgásához és irányításához
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    A Snake osztály a kígyó játék kígyóját reprezentálja.

    Attributes:
        body (list): A kígyó testét alkotó Turtle objektumok listája
    """

    def __init__(self) -> None:
        """
        Inicializálja a Snake objektumot.

        Minden szegmens egy fehér négyzet (20px × 20px), amelyek vízszintesen
        egymás mellett helyezkednek el.
        """
        self.body = []
        self.create_snake()

    def create_snake(self) -> None:
        """
        A kígyó elkészítése
        """
        #  Minden szegmens egy fehér négyzet, amelyek vízszintesen
        #  egymás mellett helyezkednek el.
        for segment in range(3):
            self.add_segment((MOVE_DISTANCE * segment, 0))

    def head(self) -> Turtle:
        """
        Visszaadja a kígyó fejét (első szegmensét).

        Returns:
            Turtle: A kígyó fej szegmense (body lista első eleme)
        """
        return self.body[0]

    def add_segment(self, position: tuple[float, float]) -> None:
        """
        Hozzáad egy új szegmenst a kígyóhoz a megadott pozícióban.

        Args:
            position (tuple[float, float]): Az új szegmens pozíciója (x, y) koordinátákban
        """
        segment = Turtle("square")  # 20px * 20px nagyságú a négyzet
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.body.append(segment)

    def extend(self) -> None:
        """
        Meghosszabbítja a kígyót egy új szegmenssel.

        Az új szegmens a kígyó utolsó szegmensének pozíciójában jelenik meg,
        így a kígyó látszólag megnő, amikor ételt eszik.
        """
        self.add_segment(self.body[-1].position())

    def move(self) -> None:
        """
        Mozgatja a kígyót előre.

        A mozgás úgy történik, hogy minden szegmens az előtte lévő
        szegmens pozíciójára lép, míg a fej (első szegmens) MOVE_DISTANCE
        pixelt halad előre a jelenlegi irányába.
        """
        for segment_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment_num - 1].xcor()
            new_y = self.body[segment_num - 1].ycor()
            self.body[segment_num].goto(x=new_x, y=new_y)  # az előző pozicióra mozgatjuk
        self.head().forward(MOVE_DISTANCE)  # Fej mozgatása előre

    def left(self) -> None:
        """
        Elforgatja a kígyó fejét balra (180°).

        A metódus megakadályozza, hogy a kígyó visszaforduljon,
        ha épp jobbra (0°) néz, mert hátrafelé nem tud menni.
        """
        if self.head().heading() != RIGHT:
            self.head().setheading(LEFT)

    def right(self) -> None:
        """
        Elforgatja a kígyó fejét jobbra (0°).

        A metódus megakadályozza, hogy a kígyó visszaforduljon,
        ha épp balra (180°) néz, mert hátrafelé nem tud menni.
        """
        if self.head().heading() != LEFT:
            self.head().setheading(RIGHT)

    def up(self) -> None:
        """
         Elforgatja a kígyó fejét felfelé (90°).

        A metódus megakadályozza, hogy a kígyó visszaforduljon,
        ha épp lefelé (270°) néz, mert hátrafelé nem tud menni.
        """
        if self.head().heading() != DOWN:
            self.head().setheading(UP)

    def down(self) -> None:
        """
         Elforgatja a kígyó fejét lefelé (270°).

        A metódus megakadályozza, hogy a kígyó visszaforduljon,
        ha épp felfelé (90°) néz, mert hátrafelé nem tud menni.
        """
        if self.head().heading() != UP:
            self.head().setheading(DOWN)
