import pygame
from ciudadano import Ciudadano

pygame.init()
win = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.font.init()

# Fuentes
fuente_peque = pygame.font.SysFont("Verdana", 18)
fuente_normal = pygame.font.SysFont("Verdana", 26, bold=True)
fuente_grande = pygame.font.SysFont("Verdana", 36, bold=True)

# -------- FONDOS --------
fondo_pueblo = pygame.transform.scale(pygame.image.load("media/fondo.png").convert(), (800, 800))
fondos_tiendas = [
    pygame.transform.scale(pygame.image.load("media/tiendaRopa.png").convert(), (800, 800)),
    pygame.transform.scale(pygame.image.load("media/tiendaAnimales.png").convert(), (800, 800)),
    pygame.transform.scale(pygame.image.load("media/tiendaInformatica.png").convert(), (800, 800)),
    pygame.transform.scale(pygame.image.load("media/tiendaSupermercado.png").convert(), (800, 800))
]

# -------- MONEDA PERSONALIZADA --------
# Sustituye "media/moneda.png" por el nombre de tu archivo de imagen
try:
    img_moneda = pygame.transform.scale(pygame.image.load("media/moneda.png").convert_alpha(), (30, 30))
except:
    # Si no tienes la imagen aún, creamos un círculo dorado temporal
    img_moneda = pygame.Surface((30, 30), pygame.SRCALPHA)
    pygame.draw.circle(img_moneda, (255, 215, 0), (15, 15), 15)

# -------- JUGADOR Y DINERO --------
jugador = Ciudadano(100, 100, 800, 800)
dinero = 2000
carrito = []
comprados = []
mostrar_carrito = False
mostrar_comprados = False

# -------- NOTIFICACIONES --------
mensaje_pantalla = ""
timer_mensaje = 0


def mostrar_notificacion(texto):
    global mensaje_pantalla, timer_mensaje
    mensaje_pantalla = texto
    timer_mensaje = 90


def realizar_compra():
    global dinero
    if not mostrar_carrito:
        mostrar_notificacion("¡Abre el carrito (V) para comprar!")
        return

    if len(carrito) > 0:
        coste = sum(i[1] for i in carrito)
        if dinero >= coste:
            dinero -= coste
            for item in carrito: comprados.append(item[0])
            carrito.clear()
            mostrar_notificacion("¡Compra realizada!")
        else:
            mostrar_notificacion("Dinero insuficiente")
    else:
        mostrar_notificacion("El carrito está vacío")


# -------- PRODUCTOS TIENDA ROPA (Nuevos Precios) --------
# Chaquetas: 250€ | Camisetas: 45€ | Sudaderas: 80€ | Pantalones: 50€
productos_ropa = {
    "Chaqueta Azul": [pygame.Rect(275, 250, 60, 60), 250, "media/chaquetaAzul.png"],
    "Chaqueta Blanca": [pygame.Rect(125, 250, 60, 60), 250, "media/chaquetaBlanca.png"],
    "Chaqueta Negra": [pygame.Rect(125, 350, 60, 60), 250, "media/chaquetaNegra.png"],
    "Chaqueta Rosa": [pygame.Rect(275, 350, 60, 60), 250, "media/chaquetaRosa.png"],

    "Camiseta Azul": [pygame.Rect(475, 250, 60, 60), 45, "media/camisetaAzul.png"],
    "Camiseta Blanca": [pygame.Rect(625, 250, 60, 60), 45, "media/camisetaBlanca.png"],
    "Camiseta Negra": [pygame.Rect(475, 350, 60, 60), 45, "media/camisetaNegra.png"],
    "Camiseta Rosa": [pygame.Rect(625, 350, 60, 60), 45, "media/camisetaRosa.png"],

    "Sudadera Azul": [pygame.Rect(275, 525, 60, 60), 80, "media/sudaderaAzul.png"],
    "Sudadera Blanca": [pygame.Rect(125, 525, 60, 60), 80, "media/sudaderaBlanca.png"],
    "Sudadera Negra": [pygame.Rect(310, 600, 60, 60), 80, "media/sudaderaNegra.png"],
    "Sudadera Rosa": [pygame.Rect(310, 700, 60, 60), 80, "media/sudaderaRosa.png"],

    "Pantalon Azul": [pygame.Rect(475, 525, 60, 60), 50, "media/pantalonAzul.png"],
    "Pantalon Blanco": [pygame.Rect(625, 525, 60, 60), 50, "media/pantalonBlanco.png"],
    "Pantalon Gris": [pygame.Rect(475, 655, 60, 60), 50, "media/pantalonGris.png"],
    "Pantalon Negro": [pygame.Rect(625, 655, 60, 60), 50, "media/pantalonNegro.png"]
}

for nombre, datos in productos_ropa.items():
    img = pygame.image.load(datos[2]).convert_alpha()
    datos.append(pygame.transform.scale(img, (60, 60)))

# -------- INTERFAZ --------
tiendas = [pygame.Rect(60, 120, 90, 120), pygame.Rect(140, 220, 90, 120), pygame.Rect(60, 340, 90, 120),
           pygame.Rect(140, 460, 90, 120)]
imagenes_tiendas = [pygame.transform.scale(pygame.image.load(f"media/tienda{i + 1}.png").convert_alpha(), (90, 120)) for
                    i in range(4)]
icono_carrito = pygame.transform.scale(pygame.image.load("media/carro.png").convert_alpha(), (60, 60))
rect_carrito = pygame.Rect(720, 10, 60, 60)
icono_comprados = pygame.transform.scale(pygame.image.load("media/compra.png").convert_alpha(), (60, 60))
rect_comprados = pygame.Rect(650, 10, 60, 60)
img_salida = pygame.transform.scale(pygame.image.load("media/salida.png").convert_alpha(), (140, 60))
rect_salida = pygame.Rect(660, 740, 140, 60)

en_tienda = -1
run = True

while run:
    clock.tick(60)
    win.fill((30, 30, 30))
    keys = pygame.key.get_pressed()
    jugador_rect = pygame.Rect(jugador.x, jugador.y, jugador.size, jugador.size)

    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if rect_carrito.collidepoint(e.pos):
                    mostrar_carrito = not mostrar_carrito
                    mostrar_comprados = False
                if rect_comprados.collidepoint(e.pos):
                    mostrar_comprados = not mostrar_comprados
                    mostrar_carrito = False

            if e.button == 3 and mostrar_carrito:
                for i, item in enumerate(carrito):
                    rect_item_lista = pygame.Rect(145, 200 + (i * 35), 510, 32)
                    if rect_item_lista.collidepoint(e.pos):
                        removido = carrito.pop(i)
                        mostrar_notificacion(f"Eliminado: {removido[0]}")
                        break

        if e.type == pygame.KEYDOWN:
            # Atajos de menú
            if e.key == pygame.K_v:  # Abrir Carrito
                mostrar_carrito = not mostrar_carrito
                mostrar_comprados = False
            if e.key == pygame.K_c:  # Abrir Compras
                mostrar_comprados = not mostrar_comprados
                mostrar_carrito = False

            # Acciones de tienda
            if e.key == pygame.K_e and en_tienda == 0:
                for nombre, datos in productos_ropa.items():
                    if jugador_rect.colliderect(datos[0]):
                        carrito.append((nombre, datos[1]))
                        mostrar_notificacion(f"Añadido: {nombre}")
                        break
            if e.key == pygame.K_r:
                realizar_compra()
            if e.key == pygame.K_g and mostrar_carrito and len(carrito) > 0:
                removido = carrito.pop()
                mostrar_notificacion(f"Quitado: {removido[0]}")

    if not mostrar_carrito and not mostrar_comprados:
        jugador.mover(keys)

    # Dibujo de Escenas
    if en_tienda == -1:
        win.blit(fondo_pueblo, (0, 0))
        for i, t in enumerate(tiendas):
            win.blit(imagenes_tiendas[i], t.topleft)
            if jugador_rect.colliderect(t):
                en_tienda = i
                jugador.x, jugador.y = 400, 650
    else:
        win.blit(fondos_tiendas[en_tienda], (0, 0))
        win.blit(img_salida, rect_salida.topleft)
        if jugador_rect.colliderect(rect_salida):
            en_tienda = -1
            jugador.x, jugador.y = 300, 300

        if en_tienda == 0:
            for nombre, datos in productos_ropa.items():
                rect_base, precio, _, img_base = datos
                if jugador_rect.colliderect(rect_base):
                    img_zoom = pygame.transform.scale(img_base, (95, 95))
                    win.blit(img_zoom, (rect_base.x - 17, rect_base.y - 17))
                    txt_info = fuente_peque.render(f"{precio}€ - [E] Añadir", True, (255, 255, 255))
                    win.blit(txt_info, (rect_base.x - 20, rect_base.y - 45))
                else:
                    win.blit(img_base, rect_base.topleft)

    # UI DINERO Y CONTROLES
    pygame.draw.rect(win, (50, 50, 50), (10, 10, 240, 50), border_radius=10)
    win.blit(img_moneda, (20, 20))  # Imagen de moneda personalizada
    win.blit(fuente_normal.render(f"{dinero}", True, (255, 215, 0)), (60, 18))

    # Indicadores de Teclas para el jugador
    win.blit(fuente_peque.render("[V]", True, (200, 200, 200)), (735, 75))
    win.blit(fuente_peque.render("[C]", True, (200, 200, 200)), (660, 75))

    win.blit(icono_carrito, rect_carrito.topleft)
    win.blit(icono_comprados, rect_comprados.topleft)

    # VENTANA CARRITO
    if mostrar_carrito:
        overlay = pygame.Surface((550, 520), pygame.SRCALPHA)
        pygame.draw.rect(overlay, (40, 40, 40, 240), (0, 0, 550, 520), border_radius=20)
        win.blit(overlay, (125, 90))
        pygame.draw.rect(win, (255, 255, 255), (125, 90, 550, 520), 2, border_radius=20)
        win.blit(fuente_grande.render("Carrito", True, (200, 200, 255)), (150, 105))
        win.blit(fuente_peque.render("[R] Comprar  |  [G] Quitar último", True, (100, 255, 100)), (150, 150))
        total_actual = sum(i[1] for i in carrito)
        win.blit(fuente_normal.render(f"Total: {total_actual}€", True, (255, 255, 255)), (480, 105))
        for i, item in enumerate(carrito):
            y_pos = 200 + (i * 35)
            if y_pos < 560:
                pygame.draw.rect(win, (60, 60, 60), (145, y_pos - 5, 510, 32), border_radius=5)
                win.blit(fuente_peque.render(f"🛒 {item[0]}", True, (250, 250, 250)), (160, y_pos))
                win.blit(fuente_peque.render(f"{item[1]}€", True, (150, 255, 150)), (580, y_pos))

    # VENTANA COMPRADOS
    if mostrar_comprados:
        overlay = pygame.Surface((550, 500), pygame.SRCALPHA)
        pygame.draw.rect(overlay, (30, 50, 30, 240), (0, 0, 550, 500), border_radius=20)
        win.blit(overlay, (125, 100))
        pygame.draw.rect(win, (100, 255, 100), (125, 100, 550, 500), 2, border_radius=20)
        win.blit(fuente_grande.render("Armario", True, (150, 255, 150)), (150, 120))
        for i, item in enumerate(comprados):
            y_pos = 180 + (i * 35)
            if y_pos < 560:
                win.blit(fuente_peque.render(f"✨ {item}", True, (255, 255, 255)), (170, y_pos))

    # NOTIFICACIONES
    if timer_mensaje > 0:
        s = pygame.Surface((450, 60), pygame.SRCALPHA)
        pygame.draw.rect(s, (0, 0, 0, 200), (0, 0, 450, 60), border_radius=15)
        win.blit(s, (175, 370))
        txt = fuente_normal.render(mensaje_pantalla, True, (255, 255, 100))
        win.blit(txt, txt.get_rect(center=(400, 400)))
        timer_mensaje -= 1

    jugador.dibujar(win)
    pygame.display.update()

pygame.quit()