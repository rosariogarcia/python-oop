import items, enemies, actions, world
import world
from random import choice

"""
    Game's Rooms
"""

DIALOG_INTROS_ALIVE = [
    "Oh no! A {} savage appeared",
    "You find a {}!",
    "Careful! An {} enemY!"
]

DIALOG_INTROS_DEAD = [
    "The body of a dead enemy {} lies on the ground.",
    "You see the body of a {} dead."
]

DIALOG_EMPTY_ROOM = [
    "An empty hall",
    "Seems to be nothing",
    "There is nothing"
]

DIALOG_BOSS_ALIVE = [
    "BOSS_INTRO_ALIVE"
]

DIALOG_BOSS_DEAD = [
    "BOSS_INTRO_DEAD"
]


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """ Returns adjacent movements to player."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """ Returns available actions on room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """You are in front of the castle gate.\nInside you know that you should go forward to enter the castle and look for the princess,\nbut inside you feel a fear that wants you to go backwards."""
    
    def modify_player(self, player):
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, *args):
        item = choice(items.get_items())()

        self.item = item
        super().__init__(x, y)

    def modify_player(self, player):
        self.add_loot(player)

    def intro_text(self):
        return f"¡You found: {self.item.name}!\nYou catch it"

    def add_loot(self, player):
        """ Add the item to player

        Args:
            player: Player
        """
        player.inventory.append(self.item)


class EmptyRoom(MapTile):

    def __init__(self, x, y, *args):
        self.intro = choice(DIALOG_EMPTY_ROOM)
        super().__init__(x, y)

    def intro_text(self):
        return self.intro

    def modify_player(self, player):
        pass


class EnemyRoom(MapTile):

    def __init__(self, x, y, level):
        enemy = choice(enemies.get_enemies_level(level))()

        self.enemy = enemy
        self.intro_alive = choice(DIALOG_INTROS_ALIVE)
        self.intro_dead = choice(DIALOG_INTROS_DEAD)
        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            text = self.intro_alive
        else:
            text = self.intro_dead
        return text.format(self.enemy.name)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(f"The enemy did {self.enemy.damage} damage to you. You have {player.hp} HP.")

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy=self.enemy)]
        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            return moves


class BossRoom(MapTile):
    def __init__(self, x, y, level):
        boss = choice(enemies.get_bosses_level(level))()

        self.enemy = boss
        self.intro_alive = choice(DIALOG_BOSS_ALIVE)
        self.intro_dead = choice(DIALOG_BOSS_DEAD)
        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            text = self.intro_alive
        else:
            text = self.intro_dead

        return text.format(self.enemy.name)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(f"The enemy did {self.enemy.damage} damage to you. You have {player.hp} HP.")

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy=self.enemy)]
        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            moves.append(actions.Win())
            return moves
