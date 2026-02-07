from Neutreeko.piece import *
from Neutreeko.wincon import *

def evaluate_easy(board, player):
    # Random evaluation to simulate easier games
    import random
    return random.randint(-10, 10)

# Hard and Medium difficulties
# Hard and Medium difficulties
# Precompute segments for 5x5 board (Length 3)
SEGMENTS = []
# Horizontal segments
for r in range(5):
    for c in range(3):
        SEGMENTS.append([(r,c), (r,c+1), (r,c+2)])
# Vertical segments
for c in range(5):
    for r in range(3):
        SEGMENTS.append([(r,c), (r+1,c), (r+2,c)])
# Diagonal (Down-Right)
for r in range(3):
    for c in range(3):
        SEGMENTS.append([(r,c), (r+1,c+1), (r+2,c+2)])
# Diagonal (Up-Right) / Anti-Diagonal
for r in range(2, 5):
    for c in range(3):
        SEGMENTS.append([(r,c), (r-1,c+1), (r-2,c+2)])

def evaluate_medium(board, player):
    score = 0
    opponent = 3 - player
    
    # Heuristic Weights
    WEIGHT_2_UNBLOCKED = 200    # 2 pieces connected with empty space to complete 3
    WEIGHT_CENTER = 5           # Control of center squares

    # 1. Analyze all precomputed segments
    for seg in SEGMENTS:
        # Get piece values directly
        p1 = board[seg[0][0]][seg[0][1]]
        p2 = board[seg[1][0]][seg[1][1]]
        p3 = board[seg[2][0]][seg[2][1]]
        
        # Count occurrences manually for speed
        p_count = 0
        o_count = 0
        e_count = 0
        
        if p1 == player: p_count += 1
        elif p1 == opponent: o_count += 1
        else: e_count += 1
            
        if p2 == player: p_count += 1
        elif p2 == opponent: o_count += 1
        else: e_count += 1
            
        if p3 == player: p_count += 1
        elif p3 == opponent: o_count += 1
        else: e_count += 1

        # If segment has both player and opponent, it's useless
        if p_count > 0 and o_count > 0:
            continue
        
        # Player potential
        if p_count == 3:
            return 10000 
        elif p_count == 2: # and e_count == 1 implicit
            score += WEIGHT_2_UNBLOCKED
        elif p_count == 1: # and e_count == 2 implicit
            score += 10 
            
        # Opponent threats (Negative score)
        if o_count == 3:
            return -10000
        elif o_count == 2:
            score -= WEIGHT_2_UNBLOCKED * 1.5 
        elif o_count == 1:
            score -= 10

    # 2. Center Control
    # Center 3x3 area is valuable for mobility
    # Manually check center positions ((1,1) to (3,3))
    for r in range(1, 4):
        for c in range(1, 4):
            val = board[r][c]
            if val == player:
                score += WEIGHT_CENTER
            elif val == opponent:
                score -= WEIGHT_CENTER

    return score

def minimax(board, depth, player, is_maximizing_player, evaluate_function, alpha=float('-inf'), beta=float('inf')):
    # Determine who is the maximizing player relative to this recursion
    # If is_maximizing_player is True, 'player' is Max.
    # If is_maximizing_player is False, 'player' is Min.
    
    # We want to return +Score if Max wins, -Score if Min wins.
    # Note: 'player' is the player whose turn it is currently.
    
    max_player = player if is_maximizing_player else (3 - player) 
    min_player = (3 - player) if is_maximizing_player else player
    
    # If Max Player won (or Min Player lost previous turn), return +Inf
    if check_win(board, max_player):
        return 100000 + depth, None 
        
    # If Min Player won (or Max Player lost previous turn), return -Inf
    if check_win(board, min_player):
        return -100000 - depth, None 

    if depth == 0:
        # Evaluate from the perspective of the maximizing player
        # evaluate_function(board, p) returns +Score if p is winning.
        
        # We always want the score relative to max_player.
        # But evaluate_function takes 'player' argument.
        # If we are maximizing, current 'player' is max_player.
        # If we are minimizing, current 'player' is min_player.
        
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