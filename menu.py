# Imports
import pygame
from screen import Screen

# Class
class Menu:

    playerSurface: pygame.Surface
    playerRect: pygame.Rect

    def __init__(self):
        self.playerSurface = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
        self.playerSurface = pygame.transform.rotozoom(self.playerSurface, 0, 3)
        self.playerRect = self.playerSurface.get_rect(center = (400,200))

    def draw(self, screen: Screen):
        screen.screen.fill("#0048785F")
        screen.screen.blit(self.playerSurface, self.playerRect)