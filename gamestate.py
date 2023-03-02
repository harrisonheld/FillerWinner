import copy
import random


class GameState:
    BOARD_WIDTH = 8
    BOARD_HEIGHT = 7
    COLORS = 6
    PLAYER_POSITIONS = ((0, BOARD_HEIGHT-1), (BOARD_WIDTH-1, 0))

    def __init__(self):
        self.board = []
        self.turn = 0

    def __str__(self):

        string_rep = ""
        COLORS = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m']

        for y in range(0, self.BOARD_HEIGHT):
            for x in range(0, self.BOARD_WIDTH):
                color = self.board[x][y]
                string_rep += COLORS[color] + str(color)
                string_rep += "  "
            string_rep += '\n'

        string_rep += '\033[0m'
        return string_rep

    def player_current(self):
        return self.turn % 2

    def player_other(self):
        return (self.turn + 1) % 2

    def player_color(self, player: int):
        pos = GameState.PLAYER_POSITIONS[player]
        x = pos[0]
        y = pos[1]
        return self.board[x][y]

    def is_legal_move(self, c):
        return c != self.player_color(0) and c != self.player_color(1)

    def player_score(self, player: int):
        return self.flood_count(GameState.PLAYER_POSITIONS[player])

    def finished(self):
        colors_present = set()
        for y in range(GameState.BOARD_HEIGHT):
            for x in range(GameState.BOARD_WIDTH):
                colors_present.add(self.board[x][y])

        return len(colors_present) <= 2

    def next_state(self, color_chosen: int):

        if color_chosen in [self.player_color(0), self.player_color(1)]:
            raise Exception('You cannot play a color that is already belonged to a player.')

        subsequent_state = GameState()
        subsequent_state.board = copy.deepcopy(self.board)
        player_pos = GameState.PLAYER_POSITIONS[self.player_current()]
        subsequent_state.__flood_fill(player_pos, color_chosen)
        subsequent_state.turn = self.turn + 1

        return subsequent_state

    def flood_count(self, start_coords: (int, int)):
        start_x = start_coords[0]
        start_y = start_coords[1]
        color_to_search_for = self.board[start_x][start_y]

        count = 0

        to_examine = set()
        examined = set()

        to_examine.add(start_coords)
        while len(to_examine) > 0:
            (x, y) = to_examine.pop()
            examined.add((x, y))
            c = self.board[x][y]
            if not c == color_to_search_for:
                continue
            count += 1
            if x > 0 and (x-1, y) not in examined:
                to_examine.add((x-1, y))
            if x < GameState.BOARD_WIDTH - 1 and (x+1, y) not in examined:
                to_examine.add((x+1, y))
            if y > 0 and (x, y-1) not in examined:
                to_examine.add((x, y - 1))
            if y < GameState.BOARD_HEIGHT - 1 and (x, y+1) not in examined:
                to_examine.add((x, y + 1))

        return count

    def __flood_fill(self, start_coords: (int, int), color_to_fill_with):


        start_x = start_coords[0]
        start_y = start_coords[1]
        color_to_replace = self.board[start_x][start_y]

        if color_to_fill_with == color_to_replace:
            raise Exception('You should not be flood filling a with color that is already in this start position.')

        to_fill = set()
        to_fill.add(start_coords)
        
        while len(to_fill) > 0:
            (x, y) = to_fill.pop()
            c = self.board[x][y]
            if not c == color_to_replace:
                continue
            self.board[x][y] = color_to_fill_with
            if x > 0:
                to_fill.add((x-1, y))
            if x < GameState.BOARD_WIDTH - 1:
                to_fill.add((x+1, y))
            if y > 0 and (x, y-1):
                to_fill.add((x, y - 1))
            if y < GameState.BOARD_HEIGHT - 1:
                to_fill.add((x, y + 1))

        return

    @staticmethod
    def new_game(seed=None):

        if seed is not None:
            random.seed(seed)

        state = GameState()
        state.board = [[random.randint(0, GameState.COLORS-1) for _ in range(GameState.BOARD_HEIGHT)] for _ in range(GameState.BOARD_WIDTH)]
        return state
