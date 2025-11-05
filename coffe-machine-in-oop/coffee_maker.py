from menu import MenuItem


class CoffeeMaker:
    """
    Kávéfőző gép modellje
    """

    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self) -> None:
        """
        Kinyomtatja az összes erőforrást.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink: MenuItem) -> bool:
        """
        True értéket ad vissza, ha a rendelés teljesíthető, False értéket, ha az alapanyagok nem elegendőek.
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order: MenuItem) -> None:
        """
        Levonja a szükséges összetevőket az erőforrásokból.
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
