# Imports
import pygame
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

# Enemys
enemys: Enemy = []
enemyTimer: int = pygame.USEREVENT + 1
pygame.time.set_timer(enemyTimer,1500)


# Game Loop
while True:

    # Events
    enemys = eventH.handleEvents(pygame, screen, player, enemyTimer, enemys)
    
    # Clears Screen
    screen.screen.fill("Black")

    # Update
    player.update()
    for enemy in enemys:
        if not enemy.update():
            enemys.pop(enemys.index(enemy))
            continue
        if player.rect.colliderect(enemy.rect):
            eventH.quit(pygame)
    
    # Draw
    background.draw()
    player.draw()
    for enemy in enemys: enemy.draw()

    # Updates Display and Ticks
    pygame.display.update()
    clock.tick(MAX_FPS)


