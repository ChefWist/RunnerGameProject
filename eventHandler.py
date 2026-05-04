# Imports
import pygame
from player import Player
from enemy import Enemy
from screen import Screen
from sys import exit

# Event Handler
class EventHandler:

    # Handle Events
    def handleEvents(self, pygame: pygame, screen: Screen, player: Player, enemyTimer: int, enemyList: Enemy) -> Enemy: 
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
            if event.type == enemyTimer:
                enemyList.append(Enemy(pygame, screen, "graphics/snail/snail1.png"))
        return enemyList
    
    # Quit
    def quit(self, pygame: pygame):
        pygame.quit()
        exit()