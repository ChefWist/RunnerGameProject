# Imports
import pygame
from screen import Screen

# Class
class Sprite:

    # Info
    surf: pygame.Surface
    rect: pygame.Rect

    # Screen
    screen: Screen 

    # Constructor
    def __init__(self, pygame: pygame, screen: Screen, imagePath: str):
        self.screen = screen
        # Info
        self.surf = pygame.image.load(imagePath).convert_alpha()
        self.rect = self.surf.get_rect(center = (0,0))
    
    # Draw
    def draw(self):
        self.screen.screen.blit(self.surf,self.rect)
