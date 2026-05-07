# Imports
import pygame
from sprite import Sprite
from random import randint

# Class
class Enemy(Sprite):

    # Speed
    SPEED = 5

    # Construtor
    def __init__(self, pygame, screen, imagePaths):
        super().__init__(pygame, screen, imagePaths)
        self.rect.bottomleft = (randint(900,1100), 300)
    
    # Update
    def update(self) -> bool:
        # Moves Enemy
        self.rect.x -= self.SPEED
        if self.rect.left <= -100:
            return False
        return True