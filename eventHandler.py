# Imports
import pygame
from player import Player
from enemy import Enemy
from screen import Screen
from enemyHandler import EnemyHandler
from sys import exit

# Event Handler
class EventHandler:

    # Handle Events
    def handleEvents(self, pygame: pygame, screen: Screen, player: Player, enemyH: EnemyHandler): 
        # Loops through all Events
        for event in pygame.event.get():
            # Quit Button
            if event.type == pygame.QUIT:
                self.quit(pygame)
            # Jump
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
            # Enemy
            if event.type == enemyH.enemyTimer:
                enemyH.generateEnemy(pygame, screen)
    
    # Quit
    def quit(self, pygame: pygame):
        pygame.quit()
        exit()