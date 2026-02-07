import pygame
from .constants import *

#Display winning message.

surface = pygame.Surface((window_width, window_height), pygame.SRCALPHA)

#Winning message
def display_message(screen, msg):
    pygame.draw.rect(surface, (255, 255, 255, 100), [0, 0, 1280, 800])
    screen.blit(surface, (0, 0))
    font = pygame.font.Font(None, 56)
    text = font.render(msg, True, (0, 0, 0))
    screen.blit(text, ((window_width - text.get_width()) // 2, (window_height - text.get_height()) // 2))
    pygame.display.update()
    pygame.time.wait(2000)