import pygame
from time import sleep
from Neutreeko.constants import *
from Neutreeko.piece import *
from Neutreeko.board import *
from Neutreeko.wincon import *
from Neutreeko.messages import *
from Neutreeko.menu import *
from Neutreeko.ai import *


#Main Function, code should be ran trought here. Executes game.

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Neutreeko AI")
    
    # Removed background image loading
    
    # Icon handling - standard or removed if asset is gone. 
    # For now, let's comment out icon setting to avoid crash if file is gone, 
    # or just use default pygame icon.
    # pygame.display.set_icon(icon) 

    clock = pygame.time.Clock()
    FPS = 30 # Increased FPS for smoother feel

    while True:
        draw_menu(screen)
        pygame.display.update()

        clock.tick(FPS)
        selected_mode = None

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if BUTTON_X <= mouseX <= BUTTON_X + BUTTON_WIDTH:
                    for i, mode in enumerate(["Player x Player", "Player x AI", "AI x AI"]):
                        button_y = BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_GAP)
                        if button_y <= mouseY <= button_y + BUTTON_HEIGHT:
                            selected_mode = mode
                            break

                    #Checks for selected mode then runs the game   
                    while selected_mode == "Player x Player":
                        board = create_board() 
                        draw_board(screen, board)
                        previous_states = [] #Checks for repetition
                        current_player = 2
                        game_over = False
                        selected_piece = None

                        while not game_over:
                            clock.tick(FPS)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    return 
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    mouseX, mouseY = pygame.mouse.get_pos()
                                    
                                    # Back button logic
                                    # Updated coordinates based on constants
                                    back_btn_x = BUTTON_X // 1.7
                                    back_btn_y = BUTTON_Y_START + 430
                                    back_btn_w = BUTTON_WIDTH // 3.2
                                    back_btn_h = BUTTON_HEIGHT 
                                    
                                    if back_btn_x <= mouseX <= back_btn_x + back_btn_w:
                                        if back_btn_y <= mouseY <= back_btn_y + back_btn_h:
                                            game_over = True
                                            selected_mode = None
                                            break

                                    col = int((mouseX - board_x) // square_size)
                                    row = int((mouseY - board_y) // square_size)

                                    if selected_piece is not None:
                                        if is_valid_move(board, selected_piece, (row, col)):
                                            move_piece(board, current_player, selected_piece, (row, col))
                                            draw_board(screen, board)
                                            selected_piece = None
                                            previous_states.append(tuple(map(tuple, board)))
                                            if previous_states.count(tuple(map(tuple, board))) == 3:
                                                display_message(screen, "DRAW!")
                                                game_over = True
                                            if check_win(board, current_player):
                                                display_message(screen, f'{"Black" if current_player == 2 else "White"} wins!')
                                                game_over = True
                                            current_player = 2 if current_player == 1 else 1
                                        else:
                                            if 0 <= row < rows and 0 <= col < cols and board[row][col] == current_player:
                                                draw_board(screen, board)
                                                selected_piece = (row, col)
                                                draw_possible_moves(screen, board, selected_piece)  
                                    else:
                                        #Select a piece
                                        if 0 <= row < rows and 0 <= col < cols and board[row][col] == current_player:
                                            draw_board(screen, board)
                                            selected_piece = (row, col)
                                            draw_possible_moves(screen, board, selected_piece)

                            draw_board(screen, board)
                            draw_possible_moves(screen, board, selected_piece)
                            pygame.display.update()              

                    while selected_mode == "Player x AI":
                        draw_difficulty_menu(screen)
                        pygame.display.update()

                        clock.tick(FPS)
                        selected_difficulty = None

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                return
                            elif event. type == MOUSEBUTTONDOWN:
                                mouseX, mouseY = pygame.mouse.get_pos()
                                if BUTTON_X <= mouseX <= BUTTON_X + BUTTON_WIDTH:
                                    for i, difficulty in enumerate(["Easy", "Medium", "Hard"]):
                                        button_y = BUTTON_Y_START + i * (BUTTON_HEIGHT + BUTTON_GAP)
                                        if button_y <= mouseY <= button_y + BUTTON_HEIGHT:
                                            selected_difficulty = difficulty
                                            break
                                    while selected_difficulty == difficulty:
                                        board = create_board() 
                                        draw_board(screen, board)
                                        previous_states = [] #Checks for repetition
                                        current_player = 2
                                        game_over = False
                                        selected_piece = None

                                        depth = 1 if difficulty == "Easy" else (3 if difficulty == "Medium" else 5)
                                        evaluation_function = get_evaluation_function(difficulty)
                                        
                                        while not game_over:
                                            clock.tick(FPS)
                                            if current_player == 2:
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        pygame.quit()
                                                        return 
                                                    elif event.type == pygame.MOUSEBUTTONDOWN:
                                                        mouseX, mouseY = pygame.mouse.get_pos()
                                                        
                                                        # Back button logic
                                                        back_btn_x = BUTTON_X // 1.7
                                                        back_btn_y = BUTTON_Y_START + 430
                                                        back_btn_w = BUTTON_WIDTH // 3.2
                                                        back_btn_h = BUTTON_HEIGHT 

                                                        if back_btn_x <= mouseX <= back_btn_x + back_btn_w:
                                                            if back_btn_y <= mouseY <= back_btn_y + back_btn_h:
                                                                game_over = True
                                                                selected_difficulty = None
                                                                selected_mode = None
                                                                break

                                                        col = int((mouseX - board_x) // square_size)
                                                        row = int((mouseY - board_y) // square_size)

                                                        if selected_piece is not None:
                                                            if is_valid_move(board, selected_piece, (row, col)):
                                                                move_piece(board, current_player, selected_piece, (row, col))
                                                                draw_board(screen, board)
                                                                selected_piece = None
                                                                previous_states.append(tuple(map(tuple, board)))
                                                                if previous_states.count(tuple(map(tuple, board))) == 3:
                                                                    display_message(screen, "DRAW!")
                                                                    game_over = True
                                                                if check_win(board, current_player):
                                                                    display_message(screen, ("Player Wins!"))
                                                                    game_over = True
                                                                current_player = 1
                                                            else:
                                                                if 0 <= row < rows and 0 <= col < cols and board[row][col] == current_player:
                                                                    draw_board(screen, board)
                                                                    selected_piece = (row, col)
                                                                    draw_possible_moves(screen, board, selected_piece)  
                                                        else:
                                                            #Select a piece
                                                            if 0 <= row < rows and 0 <= col < cols and board[row][col] == current_player:
                                                                draw_board(screen, board)
                                                                selected_piece = (row, col)
                                                                draw_possible_moves(screen, board, selected_piece)
                                            else:
                                                score, move = minimax(board, depth, current_player, True, evaluation_function)
                                                move_piece(board, current_player, move[0], move[1])
                                                draw_board(screen, board)
                                                if check_win(board, current_player):
                                                    display_message(screen, "AI wins!")
                                                    game_over = True
                                                current_player = 2  

                                            draw_board(screen, board)
                                            draw_possible_moves(screen, board, selected_piece)
                                            pygame.display.update()              

                    while selected_mode == "AI x AI":
                        difficulty1 = draw_AI_difficulty_menu(screen, "Blacks")
                        difficulty2 = draw_AI_difficulty_menu(screen, "Whites")
                        pygame.display.update()
                        clock.tick(FPS)

                        if difficulty1 and difficulty2:
                            evaluation_function1 = get_evaluation_function(difficulty1)
                            evaluation_function2 = get_evaluation_function(difficulty2)
                            depth1 = 1 if difficulty1 == "Easy" else (3 if difficulty1 == "Medium" else 5)
                            depth2 = 1 if difficulty2 == "Easy" else (3 if difficulty2 == "Medium" else 5)

                        board = create_board() 
                        draw_board(screen, board)
                        previous_states = [] #Checks for repetition
                        current_player = 2
                        game_over = False
                        selected_piece = None

                        while not game_over:
                            clock.tick(FPS)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    return 
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    mouseX, mouseY = pygame.mouse.get_pos()
                                    
                                    # Back button logic
                                    back_btn_x = BUTTON_X // 1.7
                                    back_btn_y = BUTTON_Y_START + 430
                                    back_btn_w = BUTTON_WIDTH // 3.2
                                    back_btn_h = BUTTON_HEIGHT 

                                    if back_btn_x <= mouseX <= back_btn_x + back_btn_w:
                                        if back_btn_y <= mouseY <= back_btn_y + back_btn_h:
                                            game_over = True
                                            selected_mode = None
                                            break
            
                            if current_player == 2:  # IA 1's turn
                                score, move = minimax(board, depth1, current_player, True, evaluation_function1)
                                move_piece(board, current_player, move[0], move[1])
                                draw_board(screen, board)
                                previous_states.append(tuple(map(tuple, board)))
                                if previous_states.count(tuple(map(tuple, board))) == 3:
                                    display_message(screen, "DRAW!")
                                    game_over = True
                                if check_win(board, current_player):
                                    display_message(screen, "Black (AI 1) wins!")
                                    game_over = True
                                    selected_mode = None
                                pygame.time.wait(250)
                                current_player = 1  # Switch to AI 2
                            else:  # IA 2's turn
                                score, move = minimax(board, depth2, current_player, True, evaluation_function2)
                                move_piece(board, current_player, move[0], move[1])
                                draw_board(screen, board)
                                if check_win(board, current_player):
                                    display_message(screen, "White (AI 2) wins!")
                                    game_over = True
                                    selected_mode = None
                                pygame.time.wait(250)
                                current_player = 2  # Switch to AI 1

                            draw_board(screen, board)
                            pygame.display.update() 
                   
        pygame.display.update()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()