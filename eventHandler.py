# Imports
import pygame
from player import Player
from sys import exit

# Event Handler
class EventHandler:

    # Handle Events
    def handleEvents(self, pygame: pygame, player: Player): 
        # Loops through all Events
        for event in pygame.event.get():
            # Quit Button
            if event.type == pygame.QUIT:
                self.quit(pygame)
            # Jump
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
    
    # Quit
    def quit(self, pygame: pygame):
        pygame.quit()
        exit()