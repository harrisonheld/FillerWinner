import random


class GameState:
    BOARD_WIDTH = 8
    BOARD_HEIGHT = 8
    COLORS = 6

    def __init__(self):
        self.board = []
        self.turn = 0

    def __str__(self):

        string_rep = ""

        for y in range(0, self.BOARD_HEIGHT):
            for x in range(0, self.BOARD_WIDTH):
                string_rep += str(self.board[x][y])
                string_rep += "  "
            string_rep += '\n'

        return string_rep

    @staticmethod
    def new_game():
        state = GameState()
        state.board = [[random.randint(0, GameState.COLORS) for _ in range(GameState.BOARD_WIDTH)] for _ in range(GameState.BOARD_HEIGHT)]
        return state
