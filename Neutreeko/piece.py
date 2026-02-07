
from .constants import *

#Function to allow for piece movement

def move_piece(board, player, start, end):
    start_row, start_col = start
    end_row, end_col = end
    
    # Check if the start position contains the player's piece
    if board[start_row][start_col] != player:
        return False

    # Check if the end position is empty
    if board[end_row][end_col] != 0:
        return False
    
    # Check if the move is valid
    if not is_valid_move(board, start, end):
        return False

    # Make the move
    board[start_row][start_col] = 0
    board[end_row][end_col] = player

    return True

#Check valid moves
def is_valid_move(board, start, end):
    start_row, start_col = start
    end_row, end_col = end

    # Check if the start and end positions are within the board bounds
    if not (0 <= start_row < rows and 0 <= start_col < cols and 0 <= end_row < rows and 0 <= end_col < cols):
        return False

    # Check if the start position contains the player's piece
    if board[start_row][start_col] == 0:
        return False

    # Check if the end position is empty
    if board[end_row][end_col] != 0:
        return False

    # Check if the move is in a straight line or diagonal
    if start_row != end_row and start_col != end_col and abs(start_row - end_row) != abs(start_col - end_col):
        return False

    # Check for obstruction along the path and if the end position is the farthest empty square
    delta_row = 1 if end_row > start_row else -1
    delta_col = 1 if end_col > start_col else -1

    if start_row == end_row:  # Horizontal move
        for col in range(start_col + delta_col, cols if delta_col == 1 else -1, delta_col):
            if board[start_row][col] != 0:
                return col - delta_col == end_col
        return end_col == (cols - 1 if delta_col == 1 else 0)
    elif start_col == end_col:  # Vertical move
        for row in range(start_row + delta_row, rows if delta_row == 1 else -1, delta_row):
            if board[row][start_col] != 0:
                return row - delta_row == end_row
        return end_row == (rows - 1 if delta_row == 1 else 0)
    else:  # Diagonal move
        for delta in range(1, min(rows, cols)):
            row = start_row + delta_row * delta
            col = start_col + delta_col * delta
            if not (0 <= row < rows and 0 <= col < cols) or board[row][col] != 0:
                return row - delta_row == end_row and col - delta_col == end_col
        return end_row == (rows - 1 if delta_row == 1 else 0) and end_col == (cols - 1 if delta_col == 1 else 0)

def get_possible_moves(board, player):
    moves = []
    rows, cols = len(board), len(board[0])

    for start_row in range(rows):
        for start_col in range(cols):
            if board[start_row][start_col] == player:
                # Tente mover para todas as outras células
                for end_row in range(rows):
                    for end_col in range(cols):
                        if is_valid_move(board, (start_row, start_col), (end_row, end_col)):
                            moves.append(((start_row, start_col), (end_row, end_col)))
    return moves

