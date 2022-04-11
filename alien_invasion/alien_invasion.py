import pygame 
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button 
from ship import Ship
import game_functions as gf
from scoreboard import Scoreboard




def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button.
    play_button = Button(ai_settings,screen,"Play")

    # Create an instance to store game statistics and create a scoreboard .
    stats = GameStats(ai_settings)
    # Make a ship,a group of bullets , and a group of aliens.
    ship = Ship(ai_settings,screen)
    sb = Scoreboard(ai_settings,screen,stats)
    aliens = Group()

    #Create a fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # Make a group to store bullets in.
    bullets = Group()

    #start the main loop for the game
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets) #listener
        if stats.game_active:
            ship.update() # update ship
            gf.update_bullets(ai_settings, screen, stats,sb,ship, aliens, bullets)  # update amount of bullets stored and hit
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,bullets)
        
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) # display in screen 
    
 
run_game()
 