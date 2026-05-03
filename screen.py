import pygame

# Screen Class
class Screen:

    # Dimensions    
    SCREEN_DIMENSIONS: tuple = (800,400)
    # Info
    title: str = "Runner"
    # Screen
    screen: pygame.Surface

    # Constructor
    def __init__(self, pygame: pygame):
        self.screen = pygame.display.set_mode(self.SCREEN_DIMENSIONS) # Creates Window
        pygame.display.set_caption(self.title) # Title
