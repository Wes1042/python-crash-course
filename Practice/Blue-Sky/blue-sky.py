import pygame
from settings import Settings
import screen_function as sf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height,ai_settings.bg_color))
    pygame.display.set_caption("Blue Sky")

    while True:
        sf.check_events()
        sf.update_screen(ai_settings,screen)


run_game()