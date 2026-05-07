# Imports
import pygame

# Class
class SoundHandler:

    music: pygame.mixer.Sound
    jumpSFX: pygame.mixer.Sound

    # Constructor
    def __init__(self, pygame: pygame):
        pygame.mixer.init()
        self.music = pygame.mixer.Sound("audio/music.wav")
        self.jumpSFX = pygame.mixer.Sound("audio/jump.mp3")
        self.music.set_volume(0.8)
        self.music.play(-1)
    
    # Jump
    def playJumpSFX(self): self.jumpSFX.play()