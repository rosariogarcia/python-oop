import tiles
import pprint
from random import choice, randint


_rooms = ["EnemyRoom", "EmptyRoom"]

# LAYOUT:
# ['S', 'L', 'E', 'V', 'L'],
# ['/', 'V', 'V', '/', '/'],
# ['/', '/', 'E', 'E', 'V'],
# ['/', '/', '/', 'V', '/'],
# ['/', '/', '/', 'E', '/']
_layout = [[tiles.StartingRoom(0, 0), tiles.LootRoom(1, 0, 0), tiles.EnemyRoom(2, 0, 0),
            tiles.EmptyRoom(3, 0, 0), tiles.LootRoom(4, 0, 0)],
           [None, tiles.EmptyRoom(1, 1), tiles.EmptyRoom(2, 1), None, None],
           [None, None, tiles.EnemyRoom(2, 2, 0), tiles.EnemyRoom(3, 2, 0), tiles.EmptyRoom(4, 2)],
           [None, None, None, tiles.EmptyRoom(3, 3), None],
           [None, None, None, tiles.BossRoom(3, 4, 0), None]]

lvl = 0
_world = {}
start_pos = (0, 0)


def create_layout(cols, rows):
    """
    Create a random layout.

    Args:
        rows: Rows quantity
        cols: Cols quantity
    """
    loot_count = 0
    layout = []
    for y in range(rows):
        tile = []
        for x in range(cols):
            n = randint(0, 10)
            if n == 0 and loot_count < 2:
                room = "LootRoom"
                loot_count += 1
            elif 0 < n < 6:
                room = choice(_rooms)
            else:
                room = None

            if room is not None:
                tile.append(getattr(__import__('tiles'), room)(x, y, lvl))
            else:
                tile.append(None)
        layout.append(tile)

    layout[0][0] = tiles.StartingRoom(0, 0)
    return layout


def create_world():
    for y in range(len(_layout)):
        for x in range(len(_layout[y])):
            _world[x, y] = _layout[y][x]



def tile_exists(x, y):
    return _world.get((x, y))
