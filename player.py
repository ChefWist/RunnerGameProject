# Imports
import pygame
from soundHandler import SoundHandler
from sprite import Sprite

# Class
class Player(Sprite):

    # Gravity
    GRAVITY = 1
    JUMP_VELOCITY = 20
    yVel = 0

    # Constructor
    def __init__(self, pygame, screen):
        super().__init__(pygame, screen, "graphics/Player/player_walk_1.png")
        self.rect.midbottom = (120, 300)

    # Update
    def update(self):

        # Gravity
        self.yVel += self.GRAVITY
        self.rect.bottom += self.yVel
        if self.onFloor(): self.rect.bottom = 300

    # Jump
    def jump(self, soundH: SoundHandler):
        if self.onFloor():
            self.yVel = -self.JUMP_VELOCITY
            soundH.playJumpSFX()

    # Function
    def onFloor(self) -> bool:
        return self.rect.bottom >= 300