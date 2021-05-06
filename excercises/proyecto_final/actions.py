from players import Players


class Action:
    def __init__(self, name, hotkey, method, **kwargs):
        self.name = name
        self.hotkey = hotkey
        self.method = method
        self.kwargs = kwargs

    def __str__(self):
        return f"{self.hotkey}: {self.name}"


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Players.move_north,
                         name='Mover to North',
                         hotkey='n')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Players.move_south,
                         name='Move to South',
                         hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Players.move_east,
                         name='Move to East',
                         hotkey='e')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Players.move_west,
                         name='Move to West',
                         hotkey='w')


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=Players.print_inventory,
                         name='View Inventory',
                         hotkey='i')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Players.attack,
                         name='Attack',
                         hotkey='a',
                         enemy=enemy)


class Win(Action):
    def __init__(self):
        super().__init__(method=Players.win,
                         name='Rescue princess and leave the castle!',
                         hotkey='q')
