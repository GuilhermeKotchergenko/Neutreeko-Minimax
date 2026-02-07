from Neutreeko.piece import *
from Neutreeko.wincon import *

def evaluate_easy(board, player):
    # Random evaluation to simulate easier games
    import random
    return random.randint(-10, 10)

# Hard and Medium difficulties
def evaluate_medium(board, player):
    score = 0
    opponent = 3 - player
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    max_score = 10000  

    # Immediate win check
    for x in range(5):
        for y in range(5):
            for dx, dy in directions:
                if x + 2*dx < 5 and y + 2*dy < 5 and x + 2*dx >= 0 and y + 2*dy >= 0:
                    if board[x][y] == player and board[x + dx][y + dy] == player and board[x + 2*dx][y + 2*dy] == player:
                        return max_score  # Immediate win for player
                    if board[x][y] == opponent and board[x + dx][y + dy] == opponent and board[x + 2*dx][y + 2*dy] == opponent:
                        return -max_score  # Block immediate win for opponent

    # Threat detection and blocking
    for x in range(5):
        for y in range(5):
            if board[x][y] == player or board[x][y] == opponent:
                current_player = board[x][y]
                for dx, dy in directions:
                    if x + 3*dx < 5 and y + 3*dy < 5 and x + 3*dx >= 0 and y + 3*dy >= 0:
                        if board[x + dx][y + dy] == current_player and board[x + 2*dx][y + 2*dy] == current_player and board[x + 3*dx][y + 3*dy] == 0:
                            if current_player == player:
                                score += 85
                            else:
                                score -= 100

    # Center control
    center_positions = [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)]
    for x, y in center_positions:
        if board[x][y] == player:
            score += 3
        elif board[x][y] == opponent:
            score -= 3

    return score

def minimax(board, depth, player, is_maximizing_player, evaluate_function, alpha=float('-inf'), beta=float('inf')):
    # Check for immediate wins for either player
    # If the previous player won, the game is over.
    # We prefer winning sooner (depth added) and delaying loss (depth subtracted)
    if check_win(board, 1):
        return 100000 + depth, None 
    if check_win(board, 2):
        return -100000 - depth, None 

    if depth == 0:
        # Evaluate from the perspective of the maximizing player (Player 1)
        # If is_maximizing_player is True, we want positive score for P1.
        # If is_maximizing_player is False, we want negative score for P1 (since P2 is minimizing).
        # Assuming evaluate_function returns +score if 'player' has advantage:
        score = evaluate_function(board, player)
        if not is_maximizing_player:
            score = -score
        return score, None

    if is_maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_possible_moves(board, player):
            new_board = [row[:] for row in board]
            move_piece(new_board, player, move[0], move[1])
            # Pass turn to opponent (false)
            eval, _ = minimax(new_board, depth - 1, 3 - player, False, evaluate_function, alpha, beta)
            
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        # Use 'player' argument, NOT '3 - player'.
        # 'player' is already the correct ID for the minimizing player here.
        for move in get_possible_moves(board, player):
            new_board = [row[:] for row in board]
            move_piece(new_board, player, move[0], move[1])
            # Pass turn back to main player (true)
            eval, _ = minimax(new_board, depth - 1, 3 - player, True, evaluate_function, alpha, beta)
            
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move
    
def get_evaluation_function(difficulty):
    if difficulty == "Easy":
        return evaluate_easy
    elif difficulty == "Medium":
        return evaluate_medium
    elif difficulty == "Hard":
        return evaluate_medium