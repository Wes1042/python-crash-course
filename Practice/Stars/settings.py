from msilib.schema import Class


class Settings():
    """A class to store the settings for stars"""

    def __init__ (self):
        """Initialize the screen"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        