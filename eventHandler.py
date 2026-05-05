# Imports
import pygame
from sceneManager import SceneManager
from player import Player
from enemy import Enemy
from scoreHandler import ScoreHandler
from screen import Screen
from enemyHandler import EnemyHandler
from sys import exit

# Event Handler
class EventHandler:

    # Handle Events
    def handleEvents(self, pygame: pygame, screen: Screen, sceneM: SceneManager, scoreH: ScoreHandler, player: Player, enemyH: EnemyHandler): 
        # Loops through all Events
        for event in pygame.event.get():
            # Quit Button
            if event.type == pygame.QUIT:
                self.quit(pygame)
            match sceneM.get_scene():
                # Playing
                case sceneM.PLAYING:
                    # Jump
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            player.jump()
                    # Enemy
                    if event.type == enemyH.enemyTimer:
                        enemyH.generateEnemy(pygame, screen)
                # Menu
                case sceneM.MENU:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            scoreH.lastTime = pygame.time.get_ticks()
                            sceneM.set_scene(sceneM.PLAYING)
    
    # Quit
    def quit(self, pygame: pygame):
        pygame.quit()
        exit()