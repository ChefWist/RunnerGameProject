# Imports
import pygame
from enemy import Enemy
from player import Player
from screen import Screen
from snail import Snail
from random import randint
from fly import Fly

# Class
class EnemyHandler:

    # Data
    enemys: Enemy = []
    enemyTimer: int

    # Constructor
    def __init__(self, pygame: pygame):
        self.enemyTimer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemyTimer,1500)

    # Generate Enemy
    def generateEnemy(self, pygame: pygame, screen: Screen):
        if randint(0,1): self.enemys.append(Snail(pygame, screen))
        else: self.enemys.append(Fly(pygame, screen))
    
    # Tick Animation
    def tickAnimation(self):
        for enemy in self.enemys:
            enemy.tickAnimation()
    
    # Update Enemys
    def update(self, player: Player) -> bool:
        for enemy in self.enemys:
            if not enemy.update():
                self.enemys.pop(self.enemys.index(enemy))
                continue
            if player.rect.colliderect(enemy.rect):
                return False # Death
        return True
    
    # Draw Enemys
    def draw(self):
        for enemy in self.enemys: enemy.draw()