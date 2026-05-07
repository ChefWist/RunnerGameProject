# Imports
import pygame
from screen import Screen

# Class
class Sprite:

    # Info
    surfs: pygame.Surface = []
    rect: pygame.Rect

    # Screen
    screen: Screen 

    # Constructor
    def __init__(self, pygame: pygame, screen: Screen, imagePaths: str):
        self.screen = screen
        # Info
        self.surfs = []
        for path in imagePaths:
            self.surfs.append(pygame.image.load(path).convert_alpha())
        self.rect = self.surfs[0].get_rect(center = (0,0))
    
    # Draw
    def draw(self):
        self.screen.screen.blit(self.surfs[0],self.rect)
