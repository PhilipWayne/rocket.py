class Settings():
    """A class to store all settings for Rocket."""
    def __init__(self):
        """Initialize the game screen settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 700
        self.bg_color = (21, 36, 110)

class Rocket():
    """A class that describes rocket."""
    def __init__(self, screen):
        """Initialize rocket and its starting position."""
        self.screen = screen
        #Load the rocket image and get its rect.
        self.image = pygame.image.load('/media/philip/9074-45DF/Python/rocket/images/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #set starting position of a rocket.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        #movement flag.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False