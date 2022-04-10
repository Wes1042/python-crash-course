from turtle import update
import pygame 
from pygame.sprite import Group
from settings import Settings
import game_functions as gf

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width,settings.screen_height))
    pygame.display.set_caption("STARS")

    # Make a group of stars
    stars = Group()

    # Create a fleet of stars
    #gf.create_fleet(settings,screen,stars)

    while True:
        gf.update_screen(settings,screen,stars)

run_game()