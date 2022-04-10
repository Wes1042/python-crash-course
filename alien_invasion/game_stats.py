class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self,ai_settings):
        """Initialize statisitcs."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start The game in an inactive state
        self.game_active = False


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.ai_settings.ship_limit 

    