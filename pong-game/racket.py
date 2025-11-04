from turtle import Turtle
import constans


class Racket(Turtle):
    """
    A Racket osztály az ütőt reprezentálja a Pong játékban.

    A Turtle osztályból származik, így közvetlenül képes grafikus elemeket
    megjeleníteni és mozgatni a képernyőn.

    Attributes:
        Örökli a Turtle osztály összes attribútumát
    """

    def __init__(self, position: tuple[float, float]) -> None:
        """
       Inicializálja a Racket objektumot.

       Beállítja az ütő megjelenését (fehér téglalap), pozícióját és irányát.

       Args:
           position: Az ütő kezdeti pozíciója (x, y) koordináták formájában
       """
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(constans.UP)
        self.goto(position)
        self.speed("fastest")

    def up(self) -> None:
        """
        Felfelé mozgatjuk az ütőt

        Ellenőrzi, hogy az ütő nem lépné-e túl a felső határt,
        majd ha nem, akkor elmozgatja felfelé a megadott távolsággal.
        """
        if self.ycor() < constans.MAX_Y - constans.MOVE_DISTANCE:
            new_y = self.ycor() + constans.MOVE_DISTANCE
            self.goto(x=self.xcor(), y=new_y)

    def down(self) -> None:
        """
        Lefelé mozgatjuk az ütőt

        Ellenőrzi, hogy az ütő nem lépné-e túl az alsó határt,
        majd ha nem, akkor elmozgatja lefelé a megadott távolsággal.
        """
        if self.ycor() > (constans.MIN_Y + constans.MOVE_DISTANCE):
            new_y = self.ycor() - constans.MOVE_DISTANCE
            self.goto(x=self.xcor(), y=new_y)
