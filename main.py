#Arreglar el historial y arreglar el carrito cuando se vaya de la tienda.

import pygame
from ciudadano import Ciudadano

pygame.init()
pygame.font.init()

ANCHO, ALTO = 800, 800
win = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulador de Tiendas - OOP Completo")
clock = pygame.time.Clock()


# IMÁGENES

IMAGENES = {}

def cargar_img(ruta, size=None):
    clave = (ruta, size)
    if clave in IMAGENES:
        return IMAGENES[clave]
    try:
        img = pygame.image.load(ruta).convert_alpha()
        if size:
            img = pygame.transform.smoothscale(img, size)
    except:
        img = pygame.Surface(size if size else (60, 60), pygame.SRCALPHA)
        img.fill((255, 0, 255))
    IMAGENES[clave] = img
    return img


# FUENTES

fuente_peque = pygame.font.SysFont("Verdana", 16)
fuente_normal = pygame.font.SysFont("Verdana", 26, bold=True)
fuente_grande = pygame.font.SysFont("Verdana", 36, bold=True)


# CLASES


class Producto:
    """ Clase Padre """
    def __init__(self, nombre, precio, rect, ruta_img):
        self.nombre = nombre
        self.precio = precio
        self.rect = rect
        self.img = cargar_img(ruta_img, (60, 60))

    def dibujar(self, win, hover=False):
        if hover:
            img = pygame.transform.smoothscale(self.img, (95, 95))
            win.blit(img, (self.rect.x - 17, self.rect.y - 17))
        else:
            win.blit(self.img, self.rect.topleft)

    def obtener_info(self):
        #""" Método polimórfico base """
        return f"{self.nombre} - {self.precio}€"

# --- CLASES HIJAS ---

class Ropa(Producto):
    def obtener_info(self):
        return f"👕 {self.nombre} | {self.precio}€"

class Mascota(Producto):
    def obtener_info(self):
        return f"🐾 {self.nombre} | {self.precio}€"

class Electronica(Producto):
    def obtener_info(self):
        return f"💾 {self.nombre} | {self.precio}€"

class Alimento(Producto):
    def obtener_info(self):
        return f"🍎 {self.nombre} | {self.precio}€"

class Tienda:
    def __init__(self, fondo_path, items):
        self.fondo = cargar_img(fondo_path, (ANCHO, ALTO))
        self.items = items


# LISTAS COMPLETAS DE PRODUCTOS

# TIENDA 0: ROPA
items_ropa = [
    Ropa("Chaqueta Azul", 250, pygame.Rect(125, 250, 60, 60), "media/chaquetaAzul.png"),
    Ropa("Chaqueta Blanca", 250, pygame.Rect(275, 250, 60, 60), "media/chaquetaBlanca.png"),
    Ropa("Chaqueta Negra", 250, pygame.Rect(125, 375, 60, 60), "media/chaquetaNegra.png"),
    Ropa("Chaqueta Rosa", 250, pygame.Rect(275, 375, 60, 60), "media/chaquetaRosa.png"),

    Ropa("Camiseta Azul", 45, pygame.Rect(475, 250, 60, 60), "media/camisetaAzul.png"),
    Ropa("Camiseta Blanca", 45, pygame.Rect(625, 250, 60, 60), "media/camisetaBlanca.png"),
    Ropa("Camiseta Negra", 45, pygame.Rect(475, 375, 60, 60), "media/camisetaNegra.png"),
    Ropa("Camiseta Rosa", 45, pygame.Rect(625, 375, 60, 60), "media/camisetaRosa.png"),

    Ropa("Sudadera Azul", 80, pygame.Rect(125, 550, 60, 60), "media/sudaderaAzul.png"),
    Ropa("Sudadera Blanca", 80, pygame.Rect(275, 550, 60, 60), "media/sudaderaBlanca.png"),
    Ropa("Sudadera Negra", 80, pygame.Rect(125, 675, 60, 60), "media/sudaderaNegra.png"),
    Ropa("Sudadera Rosa", 80, pygame.Rect(275, 675, 60, 60), "media/sudaderaRosa.png"),

    Ropa("Pantalón Azul", 50, pygame.Rect(475, 550, 60, 60), "media/pantalonAzul.png"),
    Ropa("Pantalón Blanco", 50, pygame.Rect(625, 550, 60, 60), "media/pantalonBlanco.png"),
    Ropa("Pantalón Gris", 50, pygame.Rect(475, 675, 60, 60), "media/pantalonGris.png"),
    Ropa("Pantalón Negro", 50, pygame.Rect(625, 675, 60, 60), "media/pantalonNegro.png"),
]

# TIENDA 1: ANIMALES
items_animales = [
    Mascota("Perro", 500, pygame.Rect(125, 250, 60, 60), "media/animalPerro.png"),
    Mascota("Gato", 400, pygame.Rect(275, 250, 60, 60), "media/animalGato.png"),
    Mascota("Hamster", 50, pygame.Rect(125, 375, 60, 60), "media/animalHamster.png"),
    Mascota("Pez", 20, pygame.Rect(275, 375, 60, 60), "media/animalPez.png"),

    Mascota("Comida Perros", 30, pygame.Rect(125, 550, 60, 60), "media/comidaPerros.png"),
    Mascota("Comida Gatos", 25, pygame.Rect(275, 550, 60, 60), "media/comidaGatos.png"),
    Mascota("Comida Hamster", 10, pygame.Rect(125, 675, 60, 60), "media/comidaHamster.png"),
    Mascota("Comida Peces", 8, pygame.Rect(275, 675, 60, 60), "media/comidaPeces.png"),

    Mascota("Juguete Perro", 20, pygame.Rect(475, 550, 60, 60), "media/jueguetesPerro.png"),
    Mascota("Juguete Gato", 15, pygame.Rect(625, 550, 60, 60), "media/juguetesGato.png"),
    Mascota("Juguete Hamster", 12, pygame.Rect(475, 675, 60, 60), "media/jueguetesHamster.png"),
    Mascota("Juguete Peces", 10, pygame.Rect(625, 675, 60, 60), "media/juguetesPeces.png"),

    Mascota("Spray Limpieza", 15, pygame.Rect(475, 250, 60, 60), "media/limpiezaSpray.png"),
    Mascota("Bolsas Basura", 5, pygame.Rect(625, 250, 60, 60), "media/limpiezaBolsas.png"),
    Mascota("Aspiradora", 120, pygame.Rect(475, 375, 60, 60), "media/limpiezaAspiradora.png"),
]

# TIENDA 2: INFORMÁTICA
items_informatica = [
    Electronica("PC Azul", 900, pygame.Rect(125, 250, 60, 60), "media/ordenadorAzul.png"),
    Electronica("PC Blanco", 900, pygame.Rect(275, 250, 60, 60), "media/ordenadorBlanco.png"),
    Electronica("PC Negro", 900, pygame.Rect(125, 375, 60, 60), "media/ordenadorNegro.png"),
    Electronica("PC Verde", 900, pygame.Rect(275, 375, 60, 60), "media/ordenadorVerde.png"),

    Electronica("Teclado Blanco", 60, pygame.Rect(125, 550, 60, 60), "media/tecladoBlanco.png"),
    Electronica("Teclado Negro", 60, pygame.Rect(275, 550, 60, 60), "media/tecladoNegro.png"),
    Electronica("Ratón Blanco", 35, pygame.Rect(125, 675, 60, 60), "media/ratonBlanco.png"),
    Electronica("Ratón Negro", 35, pygame.Rect(275, 675, 60, 60), "media/ratonNegro.png"),

    Electronica("Cascos Blancos A.", 150, pygame.Rect(475, 550, 60, 60), "media/cascosBlancosAirPods.png"),
    Electronica("Cascos Blancos D.", 120, pygame.Rect(625, 550, 60, 60), "media/cascosBlancosDiadema.png"),
    Electronica("Cascos Negros A.", 150, pygame.Rect(475, 675, 60, 60), "media/cascosNegrosAirPods.png"),
    Electronica("Cascos Negros D.", 120, pygame.Rect(625, 675, 60, 60), "media/cascosNegrosDiadema.png"),

    Electronica("PlayStation", 500, pygame.Rect(475, 250, 60, 60), "media/consolaPlay.png"),
    Electronica("Xbox", 500, pygame.Rect(625, 250, 60, 60), "media/consolaXbox.png"),
    Electronica("Nintendo Switch", 450, pygame.Rect(475, 375, 60, 60), "media/consolaSwitch.png"),
]

# TIENDA 3: SUPERMERCADO
items_supermercado = [
    Alimento("Manzana", 2, pygame.Rect(125, 250, 60, 60), "media/frutaManzana.png"),
    Alimento("Plátano", 2, pygame.Rect(275, 250, 60, 60), "media/frutaPlatano.png"),
    Alimento("Brócoli", 3, pygame.Rect(125, 375, 60, 60), "media/frutaBrocoli.png"),
    Alimento("Judías", 3, pygame.Rect(275, 375, 60, 60), "media/frutaJudias.png"),

    Alimento("Agua", 1, pygame.Rect(125, 550, 60, 60), "media/frescosAgua.png"),
    Alimento("Leche", 1.5, pygame.Rect(275, 550, 60, 60), "media/frescosLeche.png"),
    Alimento("Huevos", 3, pygame.Rect(125, 675, 60, 60), "media/fresosHuevos.png"),
    Alimento("Sushi", 6, pygame.Rect(275, 675, 60, 60), "media/frescosSushi.png"),

    Alimento("Croissants", 2.5, pygame.Rect(475, 250, 60, 60), "media/bolleriaCroisants.png"),
    Alimento("Napolitanas", 2.5, pygame.Rect(625, 250, 60, 60), "media/bolleriaNapolitanas.png"),
    Alimento("Crepes", 3, pygame.Rect(475, 375, 60, 60), "media/bolleriasCrepes.png"),
    Alimento("Tarta", 8, pygame.Rect(625, 375, 60, 60), "media/bolleriasTartas.png"),

    Alimento("Nuggets", 4, pygame.Rect(475, 550, 60, 60), "media/precocinadosNuggets.png"),
    Alimento("Patatas", 3, pygame.Rect(625, 550, 60, 60), "media/precocinadosPatatas.png"),
    Alimento("Canelones", 4, pygame.Rect(475, 675, 60, 60), "media/precocinadosCanelones.png"),
    Alimento("Migas", 3, pygame.Rect(625, 675, 60, 60), "media/precocinadosMigas.png"),
]

# Configuración de las tiendas
tiendas_data = {
    0: Tienda("media/tiendaRopa.png", items_ropa),
    1: Tienda("media/tiendaAnimales.png", items_animales),
    2: Tienda("media/tiendaInformatica.png", items_informatica),
    3: Tienda("media/tiendaSupermercado.png", items_supermercado),
}

entradas_rects = [
    pygame.Rect(20, 375, 90, 120),
    pygame.Rect(175, 375, 90, 120),
    pygame.Rect(20, 500, 90, 120),
    pygame.Rect(175, 500, 90, 120),
]
imgs_entradas = [
    cargar_img("media/tienda1.png", (90, 120)),
    cargar_img("media/tienda2.png", (90, 120)),
    cargar_img("media/tienda3.png", (90, 120)),
    cargar_img("media/tienda4.png", (90, 120)),
]

# ESTADO DEL JUEGO

jugador = Ciudadano(300, 300, ANCHO, ALTO)
dinero = 4000
carrito = []
comprados = []
en_tienda_id = -1

mostrar_carrito = False
mostrar_comprados = False

fondo_pueblo = cargar_img("media/fondo.png", (ANCHO, ALTO))
img_moneda = cargar_img("media/moneda.png", (30, 30))
icono_carrito = cargar_img("media/carro.png", (60, 60))
icono_comprados = cargar_img("media/compra.png", (60, 60))
icono_salida = cargar_img("media/salida.png", (60, 60))

mensaje = ""
timer_msg = 0

def notificar(txt):
    global mensaje, timer_msg
    mensaje = txt
    timer_msg = 90


# BUCLE PRINCIPAL

run = True
while run:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    jugador_rect = pygame.Rect(jugador.x, jugador.y, jugador.size, jugador.size)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_v:
                mostrar_carrito = not mostrar_carrito
                mostrar_comprados = False
            if e.key == pygame.K_c:
                mostrar_comprados = not mostrar_comprados
                mostrar_carrito = False

            if e.key == pygame.K_t and carrito:
                eliminado = carrito.pop()
                notificar(f"Eliminado: {eliminado.nombre}")

            if e.key == pygame.K_e and en_tienda_id != -1:
                tienda_actual = tiendas_data[en_tienda_id]
                for p in tienda_actual.items:
                    if jugador_rect.colliderect(p.rect):
                        carrito.append(p)
                        notificar(f"Añadido: {p.nombre}")

            if e.key == pygame.K_r and carrito:
                total = sum(p.precio for p in carrito)
                if dinero >= total:
                    dinero -= total
                    comprados.extend(carrito)
                    carrito.clear()
                    notificar(f"Compra total: {total}€")
                else:
                    notificar("Dinero insuficiente")

            if e.key == pygame.K_g and en_tienda_id != -1:
                en_tienda_id = -1
                jugador.x, jugador.y = 300, 300

    # ACTUALIZACIÓN
    if not mostrar_carrito and not mostrar_comprados:
        jugador.mover(keys)

    # DIBUJADO
    if en_tienda_id == -1:
        win.blit(fondo_pueblo, (0, 0))
        for i, rect_t in enumerate(entradas_rects):
            win.blit(imgs_entradas[i], rect_t.topleft)
            if jugador_rect.colliderect(rect_t):
                en_tienda_id = i
                jugador.x, jugador.y = 400, 650
    else:
        tienda_obj = tiendas_data[en_tienda_id]
        win.blit(tienda_obj.fondo, (0, 0))
        for p in tienda_obj.items:
            hover = jugador_rect.colliderect(p.rect)
            p.dibujar(win, hover)
            if hover:
                lbl = fuente_peque.render(f"{p.precio}€ [E]", True, (255, 255, 255))
                win.blit(lbl, (p.rect.x - 5, p.rect.y - 25))

    # CARRITOS
    win.blit(icono_salida, (580, 10))
    win.blit(icono_comprados, (650, 10))
    win.blit(icono_carrito, (720, 10))

    win.blit(fuente_peque.render("[G]", True, (200, 200, 200)), (595, 75))
    win.blit(fuente_peque.render("[C]", True, (200, 200, 200)), (665, 75))
    win.blit(fuente_peque.render("[V]", True, (200, 200, 200)), (735, 75))

    pygame.draw.rect(win, (40, 40, 40), (10, 10, 240, 50), border_radius=10)
    win.blit(img_moneda, (20, 20))
    win.blit(fuente_normal.render(str(round(dinero, 2)), True, (255, 215, 0)), (60, 18))

    # CARRITO
    if mostrar_carrito:
        s = pygame.Surface((550, 500), pygame.SRCALPHA)
        pygame.draw.rect(s, (40, 40, 40, 230), s.get_rect(), border_radius=20)
        win.blit(s, (125, 120))
        win.blit(fuente_grande.render("Carrito", True, (200, 200, 255)), (150, 140))
        win.blit(fuente_peque.render("[R] Pagar   [T] Quitar último", True, (150, 255, 150)), (150, 180))

        for i, p in enumerate(carrito):
            # Aquí se ejecuta el método específico de la clase hija
            win.blit(
                fuente_peque.render(p.obtener_info(), True, (255, 255, 255)),
                (150, 220 + i * 28)
            )

    # COMPRADOS
    if mostrar_comprados:
        s = pygame.Surface((550, 500), pygame.SRCALPHA)
        pygame.draw.rect(s, (30, 50, 30, 230), s.get_rect(), border_radius=20)
        win.blit(s, (125, 120))
        win.blit(fuente_grande.render("Historial", True, (150, 255, 150)), (150, 140))

        for i, p in enumerate(comprados):
            win.blit(
                fuente_peque.render(p.obtener_info(), True, (200, 200, 200)),
                (150, 200 + i * 28)
            )

    jugador.dibujar(win)

    if timer_msg > 0:
        s = pygame.Surface((450, 60), pygame.SRCALPHA)
        pygame.draw.rect(s, (0, 0, 0, 200), s.get_rect(), border_radius=15)
        win.blit(s, (175, 370))
        win.blit(fuente_normal.render(mensaje, True, (255, 255, 100)), (200, 385))
        timer_msg -= 1

    pygame.display.update()

pygame.quit()