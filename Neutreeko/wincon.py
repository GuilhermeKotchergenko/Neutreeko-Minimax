
from .constants import *

#Checks for the win condition after each move.

def check_win(board, player):

    # Check rows and columns
    for i in range(rows):
        for j in range(cols - 2):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == player:
                return True
        for j in range(rows - 2):
            if board[j][i] == board[j + 1][i] == board[j + 2][i] == player:
                return True
    # Check \ diagonals
    for i in range(rows - 2):
        for j in range(cols - 2):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == player:
                return True
    # Check / diagonals
    for i in range(2, rows):
        for j in range(cols - 2):
            if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2] == player:
                return True
    return False