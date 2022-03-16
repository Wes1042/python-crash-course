import sys
from turtle import Screen
import pygame

def check_events():
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen):
    """Updates the screen """
    
    screen.fill(ai_settings.bg_color)

    pygame.display.flip()