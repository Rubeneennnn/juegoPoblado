import pygame
from ciudadano import Ciudadano

pygame.init()
win = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# -------- FONDOS --------
fondo_pueblo = pygame.transform.scale(
    pygame.image.load("media/fondo.png").convert(), (800, 800)
)

fondos_tiendas = [
    pygame.transform.scale(pygame.image.load("media/fondo1.png").convert(), (800, 800)),
    pygame.transform.scale(pygame.image.load("media/fondo2.png").convert(), (800, 800)),
    pygame.transform.scale(pygame.image.load("media/fondo3.png").convert(), (800, 800)),
    pygame.transform.scale(pygame.image.load("media/fondo4.png").convert(), (800, 800))
]

# -------- JUGADOR --------
jugador = Ciudadano(100, 100)

# -------- TIENDAS --------
imagenes_tiendas = [
    pygame.transform.scale(pygame.image.load(f"media/tienda{i+1}.png").convert_alpha(), (90, 120))
    for i in range(4)
]

# Posiciones dentro del triángulo izquierdo
tiendas = [
    pygame.Rect(60, 120, 90, 120),
    pygame.Rect(140, 220, 90, 120),
    pygame.Rect(60, 340, 90, 120),
    pygame.Rect(140, 460, 90, 120)
]

# -------- SALIDA --------
img_salida = pygame.transform.scale(
    pygame.image.load("media/salida.png").convert_alpha(), (140, 60)
)
rect_salida = pygame.Rect(640, 20, 140, 60)

# -------- ESTADO --------
en_tienda = -1  # -1 = pueblo

# -------- LOOP --------
run = True
while run:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    jugador.mover(keys)

    jugador_rect = pygame.Rect(jugador.x, jugador.y, jugador.size, jugador.size)

    # -------- LÓGICA --------
    if en_tienda == -1:
        for i, t in enumerate(tiendas):
            if jugador_rect.colliderect(t):
                en_tienda = i
                jugador.x, jugador.y = 100, 100
    else:
        if jugador_rect.colliderect(rect_salida):
            en_tienda = -1
            jugador.x, jugador.y = 300, 300

    # -------- DIBUJO --------
    if en_tienda == -1:
        win.blit(fondo_pueblo, (0, 0))
        for i in range(4):
            win.blit(imagenes_tiendas[i], tiendas[i].topleft)
    else:
        win.blit(fondos_tiendas[en_tienda], (0, 0))
        win.blit(img_salida, rect_salida.topleft)

    jugador.dibujar(win)
    pygame.display.update()

pygame.quit()