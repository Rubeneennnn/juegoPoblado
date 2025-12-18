import pygame
from ciudadano import Ciudadano

pygame.init()
win = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.font.init()
fuente = pygame.font.SysFont(None, 32)

# -------- FONDOS --------
fondo_pueblo = pygame.transform.scale(
    pygame.image.load("media/fondo.png").convert(), (800, 800)
)

fondos_tiendas = [
    pygame.transform.scale(pygame.image.load("media/tiendaRopa.png").convert(), (800, 800)),
    pygame.transform.scale(pygame.image.load("media/tiendaAnimales.png").convert(), (800, 800)),
    pygame.transform.scale(pygame.image.load("media/tiendaInformatica.png").convert(), (800, 800)),
    pygame.transform.scale(pygame.image.load("media/tiendaSupermercado.png").convert(), (800, 800))
]

# -------- JUGADOR Y DINERO--------
jugador = Ciudadano(100, 100, 800, 800)
dinero = 200

carrito = []
comprados = []

mostrar_carrito = False
mostrar_comprados = False

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

icono_carrito = pygame.image.load("media/").convert_alpha()
icono_carrito = pygame.transform.scale(icono_carrito, (40, 40))
rect_carrito = pygame.Rect(700, 10, 40, 40)

icono_comprados = pygame.image.load("media/").convert_alpha()
icono_comprados = pygame.transform.scale(icono_comprados, (40, 40))
rect_comprados = pygame.Rect(650, 10, 40, 40)


# -------- SALIDA --------
img_salida = pygame.transform.scale(
    pygame.image.load("media/salida.png").convert_alpha(), (140, 60)
)
rect_salida = pygame.Rect(660, 740, 140, 60)

# -------- ESTADO --------
en_tienda = -1  # -1 = pueblo

# -------- LOOP --------
run = True
while run:
    clock.tick(60)
    texto_dinero = fuente.render(f"{dinero} €", True, (255, 255, 255))
    win.blit(texto_dinero, (20, 15))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            if rect_carrito.collidepoint(e.pos):
                mostrar_carrito = not mostrar_carrito
                mostrar_comprados = False

            if rect_comprados.collidepoint(e.pos):
                mostrar_comprados = not mostrar_comprados
                mostrar_carrito = False

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
        win.blit(icono_carrito, rect_carrito.topleft)
        win.blit(icono_comprados, rect_comprados.topleft)

        for i in range(4):
            win.blit(imagenes_tiendas[i], tiendas[i].topleft)
    else:
        win.blit(fondos_tiendas[en_tienda], (0, 0))
        win.blit(img_salida, rect_salida.topleft)

    if mostrar_carrito:
        pygame.draw.rect(win, (30, 30, 30), (200, 100, 400, 400))
        y = 120
        for item in carrito:
            texto = fuente.render(f"- {item}", True, (255, 255, 255))
            win.blit(texto, (220, y))
            y += 30

    if mostrar_comprados:
        pygame.draw.rect(win, (20, 20, 60), (200, 100, 400, 400))
        y = 120
        for item in comprados:
            texto = fuente.render(f"- {item}", True, (255, 255, 255))
            win.blit(texto, (220, y))
            y += 30

    jugador.dibujar(win)
    pygame.display.update()

pygame.quit()