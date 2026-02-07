
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Neutreeko.ai import minimax, evaluate_medium, check_win
from Neutreeko.constants import *

def print_board(board):
    for row in board:
        print(row)
    print()

def test_minimax_basic():
    print("Testing Basic Minimax Logic...")
    
    # Standard Start Board
    board = [[0]*5 for _ in range(5)]
    # Example config (not standard, just random)
    board[0][1] = 2; board[0][3] = 2; board[3][2] = 2
    board[1][2] = 1; board[4][1] = 1; board[4][3] = 1
    
    print("Initial Board (Test Setup):")
    print_board(board)
    
    # Run Minimax Depth 2 for Player 1
    # Check for crashes
    try:
        score, move = minimax(board, 2, 1, True, evaluate_medium)
        print(f"Minimax Result (Depth 2, Player 1): Score={score}, Move={move}")
    except Exception as e:
        print(f"FAIL: Minimax crashed with error: {e}")
        return

    if move is None:
        # Move might be None if no moves available (unlikely here) or if win/loss detected immediately with depth 0?
        # But depth is 2.
        print("WARNING: Minimax returned No Move.")
    else:
        print("PASS: Minimax returned a candidate move.")

    # Test Win Detection
    # Create a board where P1 has WON on the board.
    board_win = [[0]*5 for _ in range(5)]
    board_win[0][0] = 1; board_win[0][1] = 1; board_win[0][2] = 1
    
    # If P1 has won, calling minimax (even if it thinks it's P1 turn) should return a high score immediately.
    # The check_win at the start of minimax handles this.
    score_win, _ = minimax(board_win, 1, 1, True, evaluate_medium)
    print(f"Win Board Score: {score_win}")
    if score_win > 100000:
        print("PASS: Detected Win State with correct high score logic.")
    else:
        print(f"FAIL: Did not return high score > 100000 for win state. Got {score_win}")

    # Test Loss Detection (Opponent P2 won)
    board_loss = [[0]*5 for _ in range(5)]
    board_loss[0][0] = 2; board_loss[0][1] = 2; board_loss[0][2] = 2
    
    # Run as P1. Opponent P2 has winning line.
    score_loss, _ = minimax(board_loss, 1, 1, True, evaluate_medium)
    print(f"Loss Board Score: {score_loss}")
    if score_loss < -100000:
        print("PASS: Detected Loss State with correct low score logic.")
    else:
        print(f"FAIL: Did not return low score < -100000 for loss state. Got {score_loss}")

if __name__ == "__main__":
    test_minimax_basic()
