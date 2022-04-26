'''
Tic Tac Toe: Game
Author: Austin Donovan
'''

import random

board = []
board_size = int(input("What board size? "))


def create_board():
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append('_')
        board.append(row)


def is_game_draw():
    for row in board:
        for item in row:
            if item == '_':
                return False
    return True


def display_board():
    for row in board:
        for item in row:
            print("|" + item, end="|")
        print()


def get_random_first_player():
    return random.randint(0, 1)


def player_winner(player):
    value = len(board)

    # check rows for winner
    for i in range(value):
        win = True
        for j in range(value):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    # check columns for winner
    for i in range(value):
        win = True
        for j in range(value):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    # check diagonals for winner
    win = True
    for i in range(value):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    # check for reverse winner
    win = True
    for i in range(value):
        if board[i][value - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False


# change player
def flip_player(player):
    return 'X' if player == 'O' else 'O'


# assign X or O location
def assign_location(row, col, player):
    board[row][col] = player


def start_game():
    create_board()

    # set random player at start
    player = 'X' if get_random_first_player() == 1 else 'O'
    while True:
        print(f"Player {player} turn")
        display_board()

        # take row and col from user input
        row, col = list(
            map(int, input("Enter row and column numbers to fix spot (example: 1 1): ").split()))
        print()

        # assign the spot on board
        assign_location(row - 1, col - 1, player)

        # checking whether current player is won or not
        if player_winner(player):
            print(f"Player {player} has won the game!")
            break

        # checking whether the game is draw or not
        if is_game_draw():
            print("It is a Draw, Game Over!")
            break

        # swapping the turn
        player = flip_player(player)

    # showing the final view of board
    print()
    display_board()


# starting the game
start_game()
