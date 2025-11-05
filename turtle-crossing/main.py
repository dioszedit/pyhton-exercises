"""
Turtle Crossing - Főprogram

Egy egyszerű ügyességi játék, ahol a játékos egy teknőst irányít,
és el kell kerülnie az autókat, miközben megpróbál átjutni az úton.

Irányítás:
    - Fel nyíl: mozgatás felfelé
    - Le nyíl: mozgatás lefelé

Játékmenet:
    - Minden sikeres átkelésnél a szint nő és az autók gyorsulnak
    - Ha a játékos nekimegy egy autónak, vége a játéknak
    - Az autók véletlenszerűen jelennek meg és mozognak balra

Oktatási projekt - szabadon felhasználható
"""

import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Képernyő beállítása
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Kikapcsolja az automatikus képernyőfrissítést

# Játékobjektumok létrehozása
level = Scoreboard()  # Szint megjelenítő
player = Player()  # Játékos teknős
car_manager = CarManager()  # Autók kezelője

# Billentyűzet figyelés beállítása
screen.listen()
screen.onkey(fun=player.move_up, key="Up")  # Fel nyíl: mozgatás felfelé
screen.onkey(fun=player.move_down, key="Down")  # Le nyíl: mozgatás lefelé

# Fő játék ciklus
game_is_on = True
while game_is_on:
    # Képernyő frissítési idő (FPS szabályozás)
    # A car_speed változó értéke csökken minden szintlépéskor, így gyorsul a játék
    # A rendszer időzítési felbontása platformfüggő:
    # - Windows: ~15-16 ms
    # - Linux/Unix: ~1 ms vagy jobb
    time.sleep(car_manager.car_speed)

    # Ellenőrzi, hogy a játékos elérte-e a célvonalat
    if player.is_at_finish_line():
        player.reset_position()  # Visszahelyezi a kezdőpozícióba
        level.increase_level()  # Növeli a szintet
        car_manager.increase_speed()  # Gyorsítja az autókat

    # Autók mozgatása
    car_manager.move_cars()

    # Véletlenszerűen új autót hoz létre
    # 33% esély (0, 1, 2 közül ha 1-et dob)
    if random.randint(0, 2) == 1:
        car_manager.create_car()

    # Ütközés ellenőrzése minden autóval
    for car in car_manager.cars:
        # Ha a játékos 20 pixelnél közelebb van egy autóhoz, vége a játéknak
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()

    # Képernyő frissítése (manuális frissítés, mert a tracer ki van kapcsolva)
    screen.update()

# Játék befejezése - a képernyő kattintásra bezárul - Game Over esetén
screen.exitonclick()
