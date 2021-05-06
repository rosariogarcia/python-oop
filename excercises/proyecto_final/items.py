import sys
import inspect
from random import randint

"""
    Game items.
"""


class Item:

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"{self.name}\n-----\n{self.description}\nValue: {self.value}"


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return f"{self.name}\n-----\n{self.description}\nValue: {self.value}\nDamage: {self.damage}"


class Gold(Item):

    def __init__(self, amount=randint(1, 15)):
        self.amount = amount
        super().__init__(name="Gold",
                         description="A coin of ${}".format(str(self.amount)),
                         value=self.amount)


class Stone(Weapon):
    def __init__(self):
        super().__init__(name="Stone",
                         description="A Stone.",
                         value=0,
                         damage=5)


class Daga(Weapon):
    def __init__(self):
        super().__init__(name="Daga",
                         description="Una daga de un tamaño no muy grande",
                         value=10,
                         damage=10)


class StoneSword(Weapon):
    def __init__(self):
        super().__init__(name="Stone Sword",
                         description="A Stone Sword, looks good",
                         value=20,
                         damage=25)


def get_items():
    """
        Return items list
    """
    item_list = []

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and name not in ["Item", "Weapon"]:
            item_list.append(obj)

    return item_list
