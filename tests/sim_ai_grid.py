
import sys
import os
import time

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Neutreeko.ai import minimax, get_evaluation_function, check_win
from Neutreeko.board import create_board
from Neutreeko.piece import move_piece
from Neutreeko.constants import *

def play_game(diff1, diff2):
    # Player 1: diff1 (Black)
    # Player 2: diff2 (White)
    
    board = create_board()
    current_player = 2 # Black starts (Player 2 in code based on board setup?)
    # Wait, in board.py:
    # board[0][1] = ... = 1 (White?)
    # board[4][1] = ... = 2 (Black?)
    # main.py says: 
    # if current_player == 2: # IA 1's turn (Blacks)
    # So P2 is Black, P1 is White.
    
    eval_func1 = get_evaluation_function(diff1)
    eval_func2 = get_evaluation_function(diff2)
    
    # Depths: Reduced Hard to 4 for simulation speed (5 is too slow for 100 games)
    depth1 = 1 if diff1 == "Easy" else (3 if diff1 == "Medium" else 4)
    depth2 = 1 if diff2 == "Easy" else (3 if diff2 == "Medium" else 4)
    
    moves_count = 0
    max_moves = 200 # Prevent infinite loops
    previous_states = []

    while moves_count < max_moves:
        # Check Draw by Repetition
        state = tuple(map(tuple, board))
        previous_states.append(state)
        if previous_states.count(state) >= 3:
            return "Draw"
            
        if current_player == 2: # P2 (Black)
            _, move = minimax(board, depth1, current_player, True, eval_func1)
        else: # P1 (White)
            _, move = minimax(board, depth2, current_player, True, eval_func2)
            
        if move is None:
            # No moves available? usually means loss or draw depending on rules.
            # In Neutreeko, if you can't move, you lose? Or just pass? 
            # Rules usually say you always can move unless blocked perfectly?
            # treating as Loss for current player
            return "White" if current_player == 2 else "Black"
            
        move_piece(board, current_player, move[0], move[1])
        moves_count += 1
        
        if check_win(board, current_player):
            return "Black" if current_player == 2 else "White"
            
        current_player = 1 if current_player == 2 else 2
        
    return "Draw" # Max moves reached

def run_simulation():
    difficulties = ["Easy", "Medium", "Hard"]
    results = {} # Key: (P1_Diff, P2_Diff), Value: {Black: 0, White: 0, Draw: 0}
    
    total_games_per_matchup = 20
    
    print(f"{'P1 (Black)':<10} vs {'P2 (White)':<10} | {'Black Win':<10} | {'White Win':<10} | {'Draws':<10}")
    print("-" * 60)
    
    for d1 in difficulties:
        for d2 in difficulties:
            stats = {"Black": 0, "White": 0, "Draw": 0}
            print(f"Simulating {d1} vs {d2}...", end="", flush=True)
            
            for _ in range(total_games_per_matchup):
                winner = play_game(d1, d2)
                stats[winner] += 1
            
            print(f"\r{d1:<10} vs {d2:<10} | {stats['Black']:<10} | {stats['White']:<10} | {stats['Draw']:<10}")
            results[(d1, d2)] = stats

    return results

if __name__ == "__main__":
    run_simulation()
