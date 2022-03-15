import pygame 
from pygame.sprite import Group 
from settings import Settings

def run_game():
    # Initialize game and create screen
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_width,settings.screen_height)
    pygame.display.set_caption("Side shooter")

    # Make a ship.


    # Make a group to store bullets in


    #start the main loop of the game
    while True:
        