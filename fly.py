# Import
import pygame
from enemy import Enemy

# Class
class Fly(Enemy):

    # Constructor
    def __init__(self, pygame, screen):
        super().__init__(pygame, screen, "graphics/Fly/Fly1.png")
        self.rect.bottom = 200
