# Imports
import pygame
from screen import Screen

# Class
class Sprite:

    # Info
    surfs: pygame.Surface
    surf: pygame.Surface
    rect: pygame.Rect

    # Animation
    frame: float

    # Screen
    screen: Screen 

    # Constructor
    def __init__(self, pygame: pygame, screen: Screen, imagePaths: str):
        self.screen = screen
        self.frame = 0.0
        # Info
        self.surfs = []
        for path in imagePaths:
            self.surfs.append(pygame.image.load(path).convert_alpha())
        self.surf = self.surfs[0]
        self.rect = self.surfs[0].get_rect(center = (0,0))
    
    # Draw
    def draw(self):
        self.screen.screen.blit(self.surf,self.rect)
    
    # Tick Animation
    def tickAnimation(self):
        self.frame += 1
        if self.frame >= len(self.surfs): self.frame = 0.0
        self.surf = self.surfs[int(self.frame)]


