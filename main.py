# Imports
import pygame
from enemyHandler import EnemyHandler
from scoreHandler import ScoreHandler
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
font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Screen
screen = Screen(pygame)

# Sprites
background = Background(pygame, screen)
scoreH = ScoreHandler(font)
player = Player(pygame, screen)
enemyH = EnemyHandler(pygame)

# Game Loop
while True:

    # Events
    eventH.handleEvents(pygame, screen, player, enemyH)
    
    # Clears Screen
    screen.screen.fill("Black")

    # Update
    scoreH.update(pygame)
    player.update()
    if not enemyH.update(player): eventH.quit(pygame)

    # Draw
    background.draw()
    scoreH.draw(screen)
    player.draw()
    enemyH.draw()

    # Updates Display and Ticks
    pygame.display.update()
    clock.tick(MAX_FPS)


