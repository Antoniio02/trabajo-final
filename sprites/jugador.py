import pygame
from config import VELOCIDAD_JUGADOR

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

    def update(self, plataformas):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= VELOCIDAD_JUGADOR
        if teclas[pygame.K_RIGHT]:
            self.rect.x += VELOCIDAD_JUGADOR
        if teclas[pygame.K_UP]:
            self.rect.y -= VELOCIDAD_JUGADOR
        if teclas[pygame.K_DOWN]:
            self.rect.y += VELOCIDAD_JUGADOR

        colisiones = pygame.sprite.spritecollide(self, plataformas, False)
        for plataforma in colisiones:
            if self.rect.bottom <= plataforma.rect.top + 10:
                self.rect.bottom = plataforma.rect.top
