import pygame
from .constants import *
from .piece import *

# Draw the board
def create_board():
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    board[0][1] = board[3][2] = board[0][3] = 1
    board[4][1] = board[1][2] = board[4][3] = 2
    return board

def draw_board(screen, board):
    # Fill background
    screen.fill(BG_COLOR)

    # Draw Board Background (The square container)
    pygame.draw.rect(screen, BOARD_COLOR, (board_x - 10, board_y - 10, 20 + cols * square_size, 20 + rows * square_size))
    
    # Draw Grid and Pieces
    for row in range(rows):
        for col in range(cols):
            # Draw square outline / grid
            rect = (board_x + col * square_size, board_y + row * square_size, square_size, square_size)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1) # 1px border

            piece = board[row][col]
            center = (board_x + col * square_size + square_size // 2, board_y + row * square_size + square_size // 2)
            radius = square_size // 2 - 10

            if piece == 1:
                # Player 1 (White)
                pygame.draw.circle(screen, PIECE_WHITE, center, radius)
                pygame.draw.circle(screen, (200, 200, 200), center, radius, 2) # Border
            elif piece == 2:
                # Player 2 (Black)
                pygame.draw.circle(screen, PIECE_BLACK, center, radius)
                pygame.draw.circle(screen, (20, 20, 20), center, radius, 2) # Border

    # Draw Back Button
    button_y = BUTTON_Y_START + 430 # Approximate position relative to old layout
    # Adjusting button position to be more standard if needed, but keeping logic similar for now
    
    button_rect = pygame.Rect(50, 50, 100, 50) # Moving back button to top-left for cleaner UI
    
    # Original logic had it below the menu buttons area? Let's check original code.
    # Original: button_rect = pygame.Rect(BUTTON_X // 1.7, button_y + 430, BUTTON_WIDTH // 3.2, BUTTON_HEIGHT)
    # The original placement was a bit odd, relative to the menu buttons.
    # Let's align it nicely.
    
    # Actually, main.py logic depends on the specific click area. 
    # To avoid breaking main.py's event handling too much right now, I should keep the position somewhat similar 
    # OR I have to update main.py's click detection logic simultaneously.
    # I will stick to the visual refactor first, but I'll make the button look standard.
    
    # NOTE: main.py hardcodes click detection regions. I MUST be careful.
    # main.py: if (BUTTON_X // 1.7) <= mouseX <= ...
    # So I should use the same coordinates for drawing to match the click logic, 
    # until I refactor the click logic in main.py.
    
    back_btn_x = BUTTON_X // 1.7
    back_btn_y = BUTTON_Y_START + 430
    back_btn_w = BUTTON_WIDTH // 3.2
    back_btn_h = BUTTON_HEIGHT # BUTTON_HEIGHT is now 80 (was 100). 
    
    # I need to verify if changing BUTTON_HEIGHT in constants.py breaks the hardcoded math in main.py.
    # main.py uses BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_GAP) for clicks.
    # So if I changed BUTTON_HEIGHT in constants, main.py's math will calculate NEW positions.
    # So as long as I draw where the math says, it's fine.
    
    button_rect = pygame.Rect(back_btn_x, back_btn_y, back_btn_w, back_btn_h)
    
    mouse_pos = pygame.mouse.get_pos()
    color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
    
    pygame.draw.rect(screen, color, button_rect, border_radius=10)
    
    # Font
    # Loading default system font or bundled font if available. Only Starborn was there.
    # I'll try to use a system font for neutrality.
    try:
        font = pygame.font.SysFont("Arial", 30, bold=True)
    except:
        font = pygame.font.Font(None, 30)
        
    text = font.render("<--", True, TEXT_COLOR)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

# Draw possible moves hints
def draw_possible_moves(screen, board, selected_piece):
    if selected_piece is not None:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            row, col = selected_piece
            while 0 <= row+dx < rows and 0 <= col+dy < cols and board[row+dx][col+dy] == 0:
                row += dx
                col += dy
                if is_valid_move(board, selected_piece, (row, col)):
                    center = (board_x + col * square_size + square_size // 2, board_y + row * square_size + square_size // 2)
                    pygame.draw.circle(screen, HIGHLIGHT_COLOR, center, 15)

