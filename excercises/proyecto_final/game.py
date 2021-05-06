import world
from players import Players


def play_game():
    """
        Play yhe game
    """
    print("\n====================================================================")
    world.create_world()
    player = Players()
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())

    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            print("\nSelect an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input("\nAction: ")
            print("====================================================================")
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    if action_input == 'i':
                        print(room.intro_text())
                    break

    if not player.is_alive():
        print("You Lost!")
    elif player.victory:
        print("The princess is in another castle!")

if __name__ == '__main__':
    play_game()