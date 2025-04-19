import pygame

class ItemEscudo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))  # Color verde
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, velocidad_scroll):
        self.rect.x -= velocidad_scroll
