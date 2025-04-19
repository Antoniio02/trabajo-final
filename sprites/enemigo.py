import pygame
import random
from config import ALTO
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, volador=False):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Color rojo
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.volador = volador
        self.direccion = random.choice([-1, 1])

    def update(self, velocidad_scroll):
        self.rect.x -= velocidad_scroll + 2
        if self.volador:
            self.rect.y += self.direccion * 2
            if self.rect.top < 50 or self.rect.bottom > ALTO - 200:
                self.direccion *= -1

        if self.rect.right < 0:
            self.kill()
