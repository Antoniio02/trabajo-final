import pygame

class Moneda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)

    def update(self, velocidad_scroll):
        self.rect.x -= velocidad_scroll
        if self.rect.right < 0:
            self.kill()
