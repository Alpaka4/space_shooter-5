from settings import *
import pygame
class Shield(pygame.sprite.Sprite):
    def __init__(self,player,screen):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.screen = screen
        self.image = pygame.image.load(SHIELD_NAME).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.player.rect.center
        self.last_update = pygame.time.get_ticks()
        self.count = 0
    def update(self):
        self.rect.center = self.player.rect.center
        now = pygame.time.get_ticks()
        if now - self.last_update > 5000:
            self.kill()
    def draw(self):
        self.screen.blit(self.image, self.rect)
