import pygame

def pantalla_game_over():
    fuente = pygame.font.Font(None, 74)
    texto = fuente.render('Game Over', True, (255, 0, 0))
    rect_texto = texto.get_rect(center=(400, 300))
    return texto, rect_texto
