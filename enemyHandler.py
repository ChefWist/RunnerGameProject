# Imports
import pygame
from enemy import Enemy
from player import Player
from screen import Screen

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
        self.enemys.append(Enemy(pygame, screen, "graphics/snail/snail1.png"))
    
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