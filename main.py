# Imports
import pygame
from enemyHandler import EnemyHandler
from scoreHandler import ScoreHandler
from screen import Screen
from eventHandler import EventHandler
from background import Background
from player import Player
from sceneManager import SceneManager
from enemy import Enemy
from menu import Menu
pygame.init()

# System
MAX_FPS = 60
clock = pygame.time.Clock()
eventH = EventHandler()
font = pygame.font.Font("font/Pixeltype.ttf", 50)
sceneM = SceneManager()

# Screen
screen = Screen(pygame)
menu = Menu()

# Sprites
background = Background(pygame, screen)
scoreH = ScoreHandler(font)
player = Player(pygame, screen)
enemyH = EnemyHandler(pygame)

# Game Loop
while True:

    # Events
    eventH.handleEvents(pygame, screen, sceneM, scoreH, player, enemyH)
    
    # Clears Screen
    screen.screen.fill("Black")

    # Check Scene
    match sceneM.get_scene():
        # Playing Scene
        case sceneM.PLAYING:

            # Update
            scoreH.update(pygame)
            player.update()
            playerAlive: bool = enemyH.update(player)
            if not playerAlive:
                # Death
                player.rect.midbottom = (120,300)
                player.yVel = 0
                enemyH.enemys = []
                sceneM.set_scene(sceneM.MENU)

            # Draw
            background.draw()
            scoreH.draw(screen)
            player.draw()
            enemyH.draw()
        # Menu Scene
        case sceneM.MENU:
            # Draw
            menu.draw(screen)


    # Updates Display and Ticks
    pygame.display.update()
    clock.tick(MAX_FPS)


