import pygame
from ciudadano import Ciudadano

pygame.init()
win = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


jugador = Ciudadano(100,100)
color_fondo_normal = (230, 230, 230)

tiendas = [
    pygame.Rect(50, 150, 60, 80),
    pygame.Rect(150, 150, 60, 80),
    pygame.Rect(250, 150, 60, 80),
    pygame.Rect(350, 150, 60, 80),
    pygame.Rect(450, 150, 60, 80)
]
fondos = [
    (200, 100, 100),
    (100, 200, 100),
    (100, 100, 200),
    (200, 200, 100),
    (200, 100, 200)
]

run = True
while run:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    quieto = jugador.mover(keys)

    tienda_actual = -1
    if quieto:
        for i,t in enumerate(tiendas):
            if t.collidepoint(jugador.x + jugador.size//2, jugador.y + jugador.size//2):
                tienda_actual = i

    if tienda_actual >= 0:
        win.fill(fondos[tienda_actual])
    else:
        win.fill(color_fondo_normal)
        for t in tiendas:
            pygame.draw.rect(win, (120,120,120), t)

    jugador.dibujar(win)
    pygame.display.update()

pygame.quit()
