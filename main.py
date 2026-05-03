# Imports
import pygame
from screen import Screen
from eventHandler import EventHandler
from background import Background
from player import Player
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

# Game Loop
while True:

    # Events
    eventH.handleEvents(pygame, player)
    
    # Clears Screen
    screen.screen.fill("Black")

    # Update
    player.update()

    # Draw
    background.draw()
    player.draw()

    # Updates Display and Ticks
    pygame.display.update()
    clock.tick(MAX_FPS)


