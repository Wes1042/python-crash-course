
import pygame

class Ship():
    """Creates the motion of the ship object"""
    def __init__(self,settings,screen):
        self.screen = screen
        self.settings = settings

    # Load the ship image and ger its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    # Start ship at the left side of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.left = self.screen_rect.left

    # Store a decimal value of the ship's center
        self.centerx = float(self.rect.centerx)
    # Flags movement
        self.moving_up = False
        self.moving_down = False

        