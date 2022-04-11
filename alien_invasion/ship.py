import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        """Initialize the ship and set its starting position."""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings


        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom


        # Store a decimal value of the ship's center.
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False


    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right: #checks the end window conrdinates
            self.centerX += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >  0 : # the start of the screen aka left
            self.centerX -= self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:
            self.centerY -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom <= self.screen_rect.bottom:
            self.centerY += self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerX 
        self.rect.centery = self.centerY


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx