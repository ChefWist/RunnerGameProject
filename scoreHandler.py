# Imports
import pygame
from screen import Screen

# Class
class ScoreHandler:

    # Font
    font: pygame.font
    score = 0
    lastTime = 0

    # Constructor
    def __init__(self, font: pygame.font):
        self.font = font
    
    # Update
    def update(self, pygame: pygame):
        self.score = int((pygame.time.get_ticks()-self.lastTime)/1000)

    # Draw
    def draw(self, screen: Screen):
        text = self.font.render(f"Score: {self.score}", False, "Black")
        textRect = text.get_rect(center = (400,50))
        screen.screen.blit(text,textRect)