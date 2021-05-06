import sys
import inspect

"""
    Game enemies.
"""

class Enemy:

    is_boss = False

    def __init__(self, name, hp, damage):

        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Soldier(Enemy):
    lvl = 0

    def __init__(self):
        super().__init__(name="Soldier",
                         hp=10,
                         damage=10)


class Guerrero(Enemy):
    lvl = 0
    
    def __init__(self):
        super().__init__(name="Guerrero",
                         hp=20,
                         damage=9)


class Archer(Enemy):
    lvl = 0

    def __init__(self):
        super().__init__(name="Archer",
                         hp=7,
                         damage=10)


""" class Lancero(Enemy):
    lvl = 0

    def __init__(self):
        super().__init__(name="Lancero",
                         hp=15,
                         damage=10) """

""" 
class Araña(Enemy):
    lvl = 0
    def __init__(self):
        super().__init__(name="Araña",
                         hp=15,
                         damage=15) """


class ArmyMaster(Enemy):
    lvl = 0
    is_boss = True
    def __init__(self):
        super().__init__(name="Army Master",
                         hp=35,
                         damage=35)


class Dragon(Enemy):
    lvl = 0

    def __init__(self):
        super().__init__(name="Dragon",
                         hp=50,
                         damage=25)


def get_enemies_level(level):
    """
    Returns enemies of game.

    Args:
        level: Game level
    """
    enemy_list = []

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and name != "Enemy":
            if obj.lvl == level and not obj.is_boss:
                enemy_list.append(obj)

    return enemy_list


def get_bosses_level(level):
    """
    Return boss of game.

    Args:
        level: Game level
    """
    boss_list = []

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and name != "Enemy":
            if obj.lvl == level and obj.is_boss:
                boss_list.append(obj)

    return boss_list
