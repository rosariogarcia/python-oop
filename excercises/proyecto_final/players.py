import items
import world
from random import randint

class Players(object):
    def __init__(self):
        self.inventory = [items.Gold(15), items.StoneSword()]
        self.hp = 100
        self.location_x, self.location_y = world.start_pos
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("\n======================\nInventory:\n")
        for item in self.inventory:
            print(item, '\n')
        print("======================")

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)
    
    def attack(self, enemy):
        """
        Select the best weapon on inventory and discount from enemy live

        Args:
            enemy: Enemy
        """
        best_weapon = None
        max_damage = 0
        for item in self.inventory:
            if isinstance(item, items.Weapon):
                if item.damage > max_damage:
                    max_damage = item.damage
                    best_weapon = item

        enemy.hp -= best_weapon.damage
        print(f"You used {best_weapon.name} against {enemy.name}")
        if not enemy.is_alive():
            print(f"You kill to {enemy.name}!")
            cut = randint(10, 30) * enemy.max_hp / 100
            cure = randint(round(enemy.max_hp - cut), round(enemy.max_hp + cut))
            self.hp += cure
            print(f"You cure {cure} life ")
        else:
            print(f"{enemy.name} have {enemy.hp} HP")

    def win(self):
        self.victory = True

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)