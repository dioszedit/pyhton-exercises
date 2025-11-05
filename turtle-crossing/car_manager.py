"""
Autók kezelése a Turtle Crossing játékban.

Ez a modul felelős az autók létrehozásáért, mozgatásáért és
sebességük növeléséért a játék során.
"""

import random
from turtle import Turtle

# Konstansok az autók megjelenéséhez és mozgásához
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    """
    Az autók kezelését végző osztály.

    Attributes:
        cars (list): A pályán lévő autók listája
        car_speed (float): A játék sebességét szabályozó várakozási idő (másodperc)
    """

    def __init__(self) -> None:
        self.cars = []
        self.car_speed = 0.2

    def create_car(self) -> None:
        """
        Új autót hoz létre véletlenszerű színnel és pozícióval.

        Az autó a képernyő jobb szélén jelenik meg (-250 és 250 közötti
        véletlenszerű y koordinátán), és balra néz (180 fok).
        """
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.cars.append(new_car)

    def move_cars(self) -> None:
        """
        Mozgatja az összes autót balra, és törli azokat, amelyek elhagyták a képernyőt.

        Ha egy autó elhagyja a képernyő bal szélét, eltávolítja a listából,
        törli a rajzát, elrejti és felszabadítja a memóriát.
        """
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
            # A képernyőn kívül eső autót töröljük a memória optimalizálása érdekében
            if car.xcor() < (-300 - (car.width() / 2)):
                self.cars.remove(car)
                car.clear()
                car.hideturtle()
                del car

    def increase_speed(self) -> None:
        """
        Növeli a játék sebességét a car_speed csökkentésével.

        Minden szintlépésnél 10%-kal gyorsítja a játékot, de maximum
        0.016 mp-ig (60 FPS), ami a Windows rendszer időzítési felbontásának felel meg.
        A rendszer időzítési felbontása platformfüggő:
        - Windows: ~15-16 ms
        - Linux/Unix: ~1 ms vagy jobb
        """
        # Ha már elértük a maximális sebességet, nem gyorsítunk tovább
        if self.car_speed == 0.016:
            return

        self.car_speed *= 0.9 # 10%-os gyorsítás

        # Gyorsítás nem mehet a végtelenségig, ezért korlátozzuk
        # Windows környezetben 0.016 mp (16 ms) ≈ 60 FPS
        if self.car_speed < 0.016:
            self.car_speed = 0.016
