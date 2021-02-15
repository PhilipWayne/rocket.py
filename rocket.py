import pygame
import sys




class Settings():
    """A class to store all settings for Rocket."""
    def __init__(self):
        """Initialize the game screen settings."""
        # Screen settings.
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
        self.rotate_left = False
        self.rotate_right = False
        self.rocket_angle = 0


    def update(self):
        """Update the rocket position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 2
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 2
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 2 

    def rotated_center(self, image, rocket_angle):
        """Rotating rocket around its axis."""
        self.rotated_image = pygame.transform.rotate(self.image, self.rocket_angle)
        self.new_rect = self.rotated_image.get_rect(center = self.rect.center)
        return self.rotated_image, self.new_rect 

    def blit_rocket(self, rect, rocket_angle):
        """Draw the rocket at its current location."""       
        if self.rotate_left:
            self.rocket_angle = (self.rocket_angle + 1) % 360 
            self.screen.blit(self.rotated_image, self.new_rect) 
        else:
            self.rocket_angle = (self.rocket_angle + 0) % 360
            self.screen.blit(self.rotated_image, self.new_rect)    
           #01.02.2021
        if self.rotate_right:
            self.rocket_angle = (self.rocket_angle - 1) % 360 
            self.screen.blit(self.rotated_image, self.new_rect) 
        else:
            self.rocket_angle = (self.rocket_angle + 0) % 360
            self.screen.blit(self.rotated_image, self.new_rect)  

    def check_events(self, event):
        """Respond to a key events."""
        # Responses to the keydown events.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.moving_right = True
            if event.key == pygame.K_LEFT:
                self.moving_left = True
            if event.key == pygame.K_DOWN:
                self.moving_down = True 
            if event.key == pygame.K_UP:
                self.moving_up = True 
            if event.key == pygame.K_LSHIFT:
                self.rotate_left = True    
            if event.key == pygame.K_RSHIFT:
                self.rotate_right = True

        # Responses to the keyup events.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.moving_right = False
            if event.key == pygame.K_LEFT:
                self.moving_left = False
            if event.key == pygame.K_DOWN:
                self.moving_down = False 
            if event.key == pygame.K_UP:
                self.moving_up = False  
            if event.key == pygame.K_LSHIFT:
                self.rotate_left = False  
            if event.key == pygame.K_RSHIFT:
                self.rotate_right = False          

       



pygame.init()
rocket_settings = Settings()
icon = pygame.image.load('/media/philip/9074-45DF/Python/rocket/images/rocket_icon.png')


pygame.display.set_icon(icon)
screen = pygame.display.set_mode((rocket_settings.screen_width, rocket_settings.screen_height))
pygame.display.set_caption("Rocket")
rocket = Rocket(screen)

"""The main game loop."""
while True:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()    
        
        rocket.check_events(event)    

    screen.fill((rocket_settings.bg_color))
    rocket.update()
    rocket.rotated_center(rocket.image, rocket.rocket_angle)
    rocket.blit_rocket(rocket.rect,rocket.rocket_angle)  
    pygame.display.flip()
   