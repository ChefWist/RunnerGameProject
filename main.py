# Imports
import pygame
from enemyHandler import EnemyHandler
from screen import Screen
from eventHandler import EventHandler
from background import Background
from player import Player
from enemy import Enemy
pygame.init()

# System
MAX_FPS = 60
clock = pygame.time.Clock()
eventH = EventHandler()

# Screen
screen = Screen(pygame)

# Sprites
background = Background(pygame, screen)
player = Player(pygame, screen)
enemyH = EnemyHandler(pygame)

# Game Loop
while True:

    # Events
    eventH.handleEvents(pygame, screen, player, enemyH)
    
    # Clears Screen
    screen.screen.fill("Black")

    # Update
    player.update()
    if not enemyH.update(player): eventH.quit(pygame)

    # Draw
    background.draw()
    player.draw()
    enemyH.draw()

    # Updates Display and Ticks
    pygame.display.update()
    clock.tick(MAX_FPS)


