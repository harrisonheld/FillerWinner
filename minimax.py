from gamestate import *


MAX_DEPTH = 6


def __utility(state: GameState, player: int):

    opposing_player = 1
    if player == 1:
        opposing_player = 0

    return state.player_score(player) - state.player_score(opposing_player)


def minimax(state: GameState, depth: int, maximizing_player: bool, player_to_win):
    if depth == 0:
        return __utility(state, player_to_win)

    if maximizing_player == state.player_current():
        max_eva = float('-inf')
        for c in range(GameState.COLORS):

            if not state.is_legal_move(c):
                continue

            next_board = state.next_state(c)
            eva = minimax(next_board, depth-1, False, player_to_win)
            if eva > max_eva:
                max_eva = eva

        return max_eva

    else:  # maximizing_player == state.other_player()
        min_eva = float('inf')
        for c in range(GameState.COLORS):

            if not state.is_legal_move(c):
                continue

            next_board = state.next_state(c)
            eva = minimax(next_board, depth-1, True, player_to_win)
            if eva < min_eva:
                min_eva = eva
        return min_eva


def choose_color(state: GameState):
    best_choice = float('-inf')
    best_rating = float('-inf')

    for c in range(GameState.COLORS):
        if not state.is_legal_move(c):
            continue

        resultant_state = state.next_state(c)
        choice_rating = minimax(resultant_state, MAX_DEPTH, True, state.player_current())
        if choice_rating > best_rating:
            best_rating = choice_rating
            best_choice = c

    return best_choice