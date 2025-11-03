import random
from turtle import Turtle


class Food(Turtle):
    """
    A Food osztály az ételt reprezentálja a kígyó játékban.

    A Turtle osztályból származik, és egy kék kör alakú objektumként
    jelenik meg a képernyőn véletlenszerű pozíciókban.

    Az étel mérete 10x10 pixel (az eredeti 20x20 pixel fele).
    """

    def __init__(self) -> None:
        """
        Inicializálja a Food objektumot.

        Beállítja az étel kinézetét (kék kör), méretét és véletlenszerű
        kezdő pozícióját a játéktéren belül.
        """
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:
        """
        Véletlenszerű új pozícióba helyezi az ételt.

        Az étel a játéktér határain belül (-280 és 280 pixel között)
        kerül véletlenszerűen elhelyezésre mind x, mind y koordinátában.

        Ezt a metódust akkor kell hívni, amikor a kígyó megeszi az ételt.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
