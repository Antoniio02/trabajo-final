import pygame
from config import ANCHO, ALTO, COLOR_FONDO
from sprites.jugador import Jugador
from utils.spawn_system import spawn_item, spawn_plataforma, spawn_enemigo
from utils.game_over import pantalla_game_over
from sprites.plataforma import Plataforma

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Corre, Corre, Corre!")
reloj = pygame.time.Clock()

def main():
    global plataformas, velocidad_scroll

    jugador = Jugador()
    todos_los_sprites = pygame.sprite.Group()
    monedas = pygame.sprite.Group()
    items = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    plataformas = pygame.sprite.Group()

    todos_los_sprites.add(jugador)

    corriendo = True
    spawn_timer = 0
    spawn_enemigo_timer = 0
    spawn_plataforma_timer = 0
    velocidad_scroll = 5

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        todos_los_sprites.update(velocidad_scroll)

        spawn_timer += 1
        if spawn_timer > 60:
            spawn_item(velocidad_scroll, todos_los_sprites, items)
            spawn_timer = 0

        spawn_enemigo_timer += 1
        if spawn_enemigo_timer > 120:
            spawn_enemigo(velocidad_scroll, todos_los_sprites, enemigos)
            spawn_enemigo_timer = 0

        spawn_plataforma_timer += 1
        if spawn_plataforma_timer > 90:
            spawn_plataforma(velocidad_scroll, todos_los_sprites, plataformas)
            spawn_plataforma_timer = 0

        pantalla.fill(COLOR_FONDO)
        todos_los_sprites.draw(pantalla)

        pygame.display.update()

        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
