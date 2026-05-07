# Import
import pygame
from enemy import Enemy

# Class
class Snail(Enemy):

    # Constructor
    def __init__(self, pygame, screen):
        super().__init__(pygame, screen, ["graphics/snail/snail1.png", "graphics/snail/snail2.png"])
        self.rect.bottom = 300
