# Imports
import pygame
from scoreHandler import ScoreHandler
from screen import Screen

# Class
class Menu:

    playerSurface: pygame.Surface
    playerRect: pygame.Rect

    font: pygame.font.Font

    def __init__(self, font: pygame.font.Font):
        self.playerSurface = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
        self.playerSurface = pygame.transform.rotozoom(self.playerSurface, 0, 3)
        self.playerRect = self.playerSurface.get_rect(center = (400,200))
        self.font = font

    def draw(self, screen: Screen, scoreH: ScoreHandler):
        screen.screen.fill("#0048785F")
        screen.screen.blit(self.playerSurface, self.playerRect)

        title_text = self.font.render("Runner Game",False,"Black")
        title_textRect = title_text.get_rect(center = (400,30))
        screen.screen.blit(title_text,title_textRect)

        if scoreH.score > 0:
            infoText = f"You Have {scoreH.score} Score!"
        else:
            infoText = "Press Space To Begin"
        info_text = self.font.render(infoText,False,"Black")
        info_textRect = info_text.get_rect(center = (400,375))
        screen.screen.blit(info_text,info_textRect)