import pygame

# Window & Board Dimensions
window_width, window_height = 1280, 800
board_width, board_height = 680, 680
rows, cols = 5, 5
square_size = board_width // cols
board_x = (window_width - board_width) // 2
board_y = (window_height - board_height) // 2

# Neutral Color Palette
BG_COLOR = (44, 62, 80)          # Dark Blue-Grey
BOARD_COLOR = (236, 240, 241)    # Off-White / Light Grey
GRID_COLOR = (149, 165, 166)     # Grey for grid lines
BUTTON_COLOR = (52, 152, 219)    # Blue
BUTTON_HOVER_COLOR = (41, 128, 185) # Darker Blue
TEXT_COLOR = (255, 255, 255)     # White
PIECE_WHITE = (236, 240, 241)    # White pieces
PIECE_BLACK = (44, 62, 80)       # Black pieces (matching BG for contrast on board)
HIGHLIGHT_COLOR = (46, 204, 113) # Green for valid moves

# Button Dimensions
BUTTON_WIDTH = 400
BUTTON_HEIGHT = 80
BUTTON_GAP = 30
BUTTON_X = (window_width - BUTTON_WIDTH) // 2
BUTTON_Y_START = 200



