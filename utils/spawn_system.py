import random
from sprites.plataforma import Plataforma
from sprites.moneda import Moneda
from sprites.enemigo import Enemigo
from config import ANCHO, ALTO

def spawn_plataforma(velocidad_scroll, todos_los_sprites, plataformas):
    ancho_plataforma = random.randint(50, 150)
    x = ANCHO
    y = random.randint(100, ALTO - 50)
    nueva_plataforma = Plataforma(x, y, ancho_plataforma, 20)
    plataformas.add(nueva_plataforma)
    todos_los_sprites.add(nueva_plataforma)

def spawn_item(velocidad_scroll, todos_los_sprites, items):
    x = ANCHO
    y = random.randint(100, ALTO - 50)
    nueva_moneda = Moneda()
    nueva_moneda.rect.x = x
    nueva_moneda.rect.y = y
    items.add(nueva_moneda)
    todos_los_sprites.add(nueva_moneda)

def spawn_enemigo(velocidad_scroll, todos_los_sprites, enemigos):
    x = ANCHO
    y = random.randint(100, ALTO - 50)
    enemigo = Enemigo()
    enemigo.rect.x = x
    enemigo.rect.y = y
    enemigos.add(enemigo)
    todos_los_sprites.add(enemigo)
