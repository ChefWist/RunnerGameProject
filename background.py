# Imports
import pygame
from screen import Screen

# Class
class Background:
    
    # Images
    groundSurf: pygame.Surface
    skySurf: pygame.Surface
    # Screen
    screen: Screen

    # Constructor
    def __init__(self, pygame: pygame, screen: Screen):
        # Screen
        self.screen = screen
        # Images
        self.groundSurf = pygame.image.load("graphics/ground.png").convert_alpha()
        self.skySurf = pygame.image.load("graphics/Sky.png").convert_alpha()

    # Draw
    def draw(self):
        self.screen.screen.blit(self.groundSurf,(0,300))
        self.screen.screen.blit(self.skySurf,(0,0))