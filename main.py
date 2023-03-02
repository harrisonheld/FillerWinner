from gamestate import *
from minimax import *

game = GameState.new_game()
print(game)

while not game.finished():
    # smart choice
    assert(game.player_current() == 0)
    p1_choice = choose_color(game)
    game = game.next_state(p1_choice)
    print("Player 1 chooses " + str(p1_choice))
    print("Player 1 score " + str(game.player_score(0)))
    print("Player 2 score " + str(game.player_score(1)))
    print(str(game) + "\n\n")

    if game.finished():
        break

    # stupid choice
    assert(game.player_current() == 1)
    p2_choice = 0
    while not game.is_legal_move(p2_choice):
        p2_choice = random.randint(0, 5)
    game = game.next_state(p2_choice)
    print("Player 2 chooses " + str(p2_choice))
    print("Player 1 score " + str(game.player_score(0)))
    print("Player 2 score " + str(game.player_score(1)))
    print(str(game) + "\n\n")

print("game finished in " + str(game.turn) + " turns")