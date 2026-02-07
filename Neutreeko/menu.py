from pygame import *
from .constants import *

def draw_menu(screen):
    screen.fill(BG_COLOR)

    # Draw Title
    try:
        title_font = pygame.font.SysFont("Arial", 60, bold=True)
    except:
        title_font = pygame.font.Font(None, 60)
    
    title_text = title_font.render("Neutreeko", True, TEXT_COLOR)
    title_rect = title_text.get_rect(center=(window_width // 2, 100))
    screen.blit(title_text, title_rect)

    # Draw buttons
    button_y = BUTTON_Y_START
    for mode in ["Player x Player", "Player x AI", "AI x AI"]:
        button_rect = pygame.Rect(BUTTON_X, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_x, mouse_y) else BUTTON_COLOR
        
        pygame.draw.rect(screen, color, button_rect, border_radius=15)

        # Render button text
        try:
            font = pygame.font.SysFont("Arial", 40)
        except:
            font = pygame.font.Font(None, 40)
            
        text = font.render(mode, True, TEXT_COLOR)
        text_rect = text.get_rect(center=button_rect.center) 
        screen.blit(text, text_rect)

        button_y += BUTTON_HEIGHT + BUTTON_GAP
    
    pygame.time.wait(10)
    pygame.display.flip()

def draw_difficulty_menu(screen):
    screen.fill(BG_COLOR)

    # Draw Title
    try:
        title_font = pygame.font.SysFont("Arial", 50, bold=True)
    except:
        title_font = pygame.font.Font(None, 50)
        
    title_text = title_font.render("Select Difficulty", True, TEXT_COLOR)
    title_rect = title_text.get_rect(center=(window_width // 2, 100))
    screen.blit(title_text, title_rect)

    # Draw difficulty buttons
    button_y = BUTTON_Y_START
    for mode in ["Easy", "Medium", "Hard"]:
        button_rect = pygame.Rect(BUTTON_X, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_x, mouse_y) else BUTTON_COLOR
        
        pygame.draw.rect(screen, color, button_rect, border_radius=15)

        # Render button text
        try:
            font = pygame.font.SysFont("Arial", 40)
        except:
            font = pygame.font.Font(None, 40)

        text = font.render(mode, True, TEXT_COLOR)
        text_rect = text.get_rect(center=button_rect.center) 
        screen.blit(text, text_rect)

        button_y += BUTTON_HEIGHT + BUTTON_GAP
    
    pygame.time.wait(10)
    pygame.display.flip()

def draw_AI_difficulty_menu(screen, ai_label):
    running = True
    selected_difficulty = None
    
    # Pre-load font
    try:
        font = pygame.font.SysFont("Arial", 40)
        title_font = pygame.font.SysFont("Arial", 50, bold=True)
    except:
        font = pygame.font.Font(None, 40)
        title_font = pygame.font.Font(None, 50)

    while running:
        screen.fill(BG_COLOR)
        
        title_text = title_font.render(f"Difficulty for {ai_label}", True, TEXT_COLOR)
        title_rect = title_text.get_rect(center=(window_width // 2, 100))
        screen.blit(title_text, title_rect)

        # Draw difficulty buttons
        button_y = BUTTON_Y_START
        for diff in ["Easy", "Medium", "Hard"]:
            button_rect = pygame.Rect(BUTTON_X, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_x, mouse_y) else BUTTON_COLOR
            
            pygame.draw.rect(screen, color, button_rect, border_radius=15)

            text = font.render(diff, True, TEXT_COLOR)
            text_rect = text.get_rect(center=button_rect.center) 
            screen.blit(text, text_rect)

            button_y += BUTTON_HEIGHT + BUTTON_GAP
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return None
            elif event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if BUTTON_X <= mouseX <= BUTTON_X + BUTTON_WIDTH:
                    for i, difficulty in enumerate(["Easy", "Medium", "Hard"]):
                        button_y = BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_GAP)
                        if button_y <= mouseY <= button_y + BUTTON_HEIGHT:
                            selected_difficulty = difficulty
                            running = False
                            break
        
        pygame.time.wait(10)
        pygame.display.flip()

    return selected_difficulty