import pygame
from ciudadano import Ciudadano

pygame.init()
pygame.font.init()

ANCHO, ALTO = 800, 800
win = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulador de Tiendas")
clock = pygame.time.Clock()

# =====================================================
# SISTEMA DE IMÁGENES (CACHE + ALPHA)
# =====================================================
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
    IMAGENES[clave] = img
    return img

# =====================================================
# FUENTES
# =====================================================
fuente_peque = pygame.font.SysFont("Verdana", 16)
fuente_normal = pygame.font.SysFont("Verdana", 26, bold=True)
fuente_grande = pygame.font.SysFont("Verdana", 36, bold=True)

# =====================================================
# CLASE PRODUCTO
# =====================================================
class Producto:
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

# =====================================================
# FONDOS E ICONOS
# =====================================================
fondo_pueblo = cargar_img("media/fondo.png", (ANCHO, ALTO))
fondos_tiendas = [
    cargar_img("media/tiendaRopa.png", (ANCHO, ALTO)),
    cargar_img("media/tiendaAnimales.png", (ANCHO, ALTO)),
    cargar_img("media/tiendaInformatica.png", (ANCHO, ALTO)),
    cargar_img("media/tiendaSupermercado.png", (ANCHO, ALTO)),
]

img_moneda = cargar_img("media/moneda.png", (30, 30))
icono_carrito = cargar_img("media/carro.png", (60, 60))
icono_comprados = cargar_img("media/compra.png", (60, 60))
icono_salida = cargar_img("media/salida.png", (60, 60))

rect_salida = pygame.Rect(580, 10, 60, 60)
rect_comprados = pygame.Rect(650, 10, 60, 60)
rect_carrito = pygame.Rect(720, 10, 60, 60)

# =====================================================
# JUGADOR
# =====================================================
jugador = Ciudadano(300, 300, ANCHO, ALTO)

# =====================================================
# ECONOMÍA
# =====================================================
dinero = 5000
carrito = []
comprados = []

mostrar_carrito = False
mostrar_comprados = False

# =====================================================
# NOTIFICACIONES
# =====================================================
mensaje = ""
timer_msg = 0

def notificar(txt):
    global mensaje, timer_msg
    mensaje = txt
    timer_msg = 90

# =====================================================
# TIENDAS (ENTRADAS)
# =====================================================
tiendas_rects = [
    pygame.Rect(20, 375, 90, 120),
    pygame.Rect(175, 375, 90, 120),
    pygame.Rect(20, 500, 90, 120),
    pygame.Rect(175, 500, 90, 120),
]

imagenes_tiendas = [
    cargar_img("media/tienda1.png", (90, 120)),
    cargar_img("media/tienda2.png", (90, 120)),
    cargar_img("media/tienda3.png", (90, 120)),
    cargar_img("media/tienda4.png", (90, 120)),
]

# =====================================================
# PRODUCTOS DE TODAS LAS TIENDAS
# =====================================================
tiendas_items = {

    # ================= ROPA =================
    0: [
        Producto("Chaqueta Azul", 250, pygame.Rect(125, 250, 60, 60), "media/chaquetaAzul.png"),
        Producto("Chaqueta Blanca", 250, pygame.Rect(275, 250, 60, 60), "media/chaquetaBlanca.png"),
        Producto("Chaqueta Negra", 250, pygame.Rect(125, 375, 60, 60), "media/chaquetaNegra.png"),
        Producto("Chaqueta Rosa", 250, pygame.Rect(275, 375, 60, 60), "media/chaquetaRosa.png"),

        Producto("Camiseta Azul", 45, pygame.Rect(475, 250, 60, 60), "media/camisetaAzul.png"),
        Producto("Camiseta Blanca", 45, pygame.Rect(625, 250, 60, 60), "media/camisetaBlanca.png"),
        Producto("Camiseta Negra", 45, pygame.Rect(475, 375, 60, 60), "media/camisetaNegra.png"),
        Producto("Camiseta Rosa", 45, pygame.Rect(625, 375, 60, 60), "media/camisetaRosa.png"),

        Producto("Sudadera Azul", 80, pygame.Rect(125, 550, 60, 60), "media/sudaderaAzul.png"),
        Producto("Sudadera Blanca", 80, pygame.Rect(275, 550, 60, 60), "media/sudaderaBlanca.png"),
        Producto("Sudadera Negra", 80, pygame.Rect(125, 675, 60, 60), "media/sudaderaNegra.png"),
        Producto("Sudadera Rosa", 80, pygame.Rect(275, 675, 60, 60), "media/sudaderaRosa.png"),

        Producto("Pantalón Azul", 50, pygame.Rect(475, 550, 60, 60), "media/pantalonAzul.png"),
        Producto("Pantalón Blanco", 50, pygame.Rect(625, 550, 60, 60), "media/pantalonBlanco.png"),
        Producto("Pantalón Gris", 50, pygame.Rect(475, 675, 60, 60), "media/pantalonGris.png"),
        Producto("Pantalón Negro", 50, pygame.Rect(625, 675, 60, 60), "media/pantalonNegro.png"),
    ],

    # ================= ANIMALES =================
    1: [
        Producto("Perro", 500, pygame.Rect(125, 250, 60, 60), "media/animalPerro.png"),
        Producto("Gato", 400, pygame.Rect(275, 250, 60, 60), "media/animalGato.png"),
        Producto("Hamster", 50, pygame.Rect(125, 375, 60, 60), "media/animalHamster.png"),
        Producto("Pez", 20, pygame.Rect(275, 375, 60, 60), "media/animalPez.png"),

        Producto("Comida Perros", 30, pygame.Rect(125, 550, 60, 60), "media/comidaPerros.png"),
        Producto("Comida Gatos", 25, pygame.Rect(275, 550, 60, 60), "media/comidaGatos.png"),
        Producto("Comida Hamster", 10, pygame.Rect(125, 675, 60, 60), "media/comidaHamster.png"),
        Producto("Comida Peces", 8, pygame.Rect(275, 675, 60, 60), "media/comidaPeces.png"),

        Producto("Juguete Perro", 20, pygame.Rect(475, 550, 60, 60), "media/jueguetesPerro.png"),
        Producto("Juguete Gato", 15, pygame.Rect(625, 550, 60, 60), "media/juguetesGato.png"),
        Producto("Juguete Hamster", 12, pygame.Rect(475, 675, 60, 60), "media/jueguetesHamster.png"),
        Producto("Juguete Peces", 10, pygame.Rect(625, 675, 60, 60), "media/juguetesPeces.png"),

        Producto("Spray Limpieza", 15, pygame.Rect(475, 250, 60, 60), "media/limpiezaSpray.png"),
        Producto("Bolsas Basura", 5, pygame.Rect(625, 250, 60, 60), "media/limpiezaBolsas.png"),
        Producto("Aspiradora", 120, pygame.Rect(475, 375, 60, 60), "media/limpiezaAspiradora.png"),
    ],

    # ================= INFORMÁTICA =================
    2: [
        Producto("PC Azul", 900, pygame.Rect(125, 250, 60, 60), "media/ordenadorAzul.png"),
        Producto("PC Blanco", 900, pygame.Rect(275, 250, 60, 60), "media/ordenadorBlanco.png"),
        Producto("PC Negro", 900, pygame.Rect(125, 375, 60, 60), "media/ordenadorNegro.png"),
        Producto("PC Verde", 900, pygame.Rect(275, 375, 60, 60), "media/ordenadorVerde.png"),

        Producto("Teclado Blanco", 60, pygame.Rect(125, 550, 60, 60), "media/tecladoBlanco.png"),
        Producto("Teclado Negro", 60, pygame.Rect(275, 550, 60, 60), "media/tecladoNegro.png"),
        Producto("Ratón Blanco", 35, pygame.Rect(125, 675, 60, 60), "media/ratonBlanco.png"),
        Producto("Ratón Negro", 35, pygame.Rect(275, 675, 60, 60), "media/ratonNegro.png"),

        Producto("Cascos Blancos AirPods", 150, pygame.Rect(475, 550, 60, 60), "media/cascosBlancosAirPods.png"),
        Producto("Cascos Blancos Diadema", 120, pygame.Rect(625, 550, 60, 60), "media/cascosBlancosDiadema.png"),
        Producto("Cascos Negros AirPods", 150, pygame.Rect(475, 675, 60, 60), "media/cascosNegrosAirPods.png"),
        Producto("Cascos Negros Diadema", 120, pygame.Rect(625, 675, 60, 60), "media/cascosNegrosDiadema.png"),

        Producto("PlayStation", 500, pygame.Rect(475, 250, 60, 60), "media/consolaPlay.png"),
        Producto("Xbox", 500, pygame.Rect(625, 250, 60, 60), "media/consolaXbox.png"),
        Producto("Nintendo Switch", 450, pygame.Rect(475, 375, 60, 60), "media/consolaSwitch.png"),
    ],

    # ================= SUPERMERCADO =================
    3: [
        Producto("Manzana", 2, pygame.Rect(125, 250, 60, 60), "media/frutaManzana.png"),
        Producto("Plátano", 2, pygame.Rect(275, 250, 60, 60), "media/frutaPlatano.png"),
        Producto("Brócoli", 3, pygame.Rect(125, 375, 60, 60), "media/frutaBrocoli.png"),
        Producto("Judías", 3, pygame.Rect(275, 375, 60, 60), "media/frutaJudias.png"),

        Producto("Agua", 1, pygame.Rect(125, 550, 60, 60), "media/frescosAgua.png"),
        Producto("Leche", 1.5, pygame.Rect(275, 550, 60, 60), "media/frescosLeche.png"),
        Producto("Huevos", 3, pygame.Rect(125, 675, 60, 60), "media/fresosHuevos.png"),
        Producto("Sushi", 6, pygame.Rect(275, 675, 60, 60), "media/frescosSushi.png"),

        Producto("Croissants", 2.5, pygame.Rect(475, 250, 60, 60), "media/bolleriaCroisants.png"),
        Producto("Napolitanas", 2.5, pygame.Rect(625, 250, 60, 60), "media/bolleriaNapolitanas.png"),
        Producto("Crepes", 3, pygame.Rect(475, 375, 60, 60), "media/bolleriasCrepes.png"),
        Producto("Tarta", 8, pygame.Rect(625, 375, 60, 60), "media/bolleriasTartas.png"),

        Producto("Nuggets", 4, pygame.Rect(475, 550, 60, 60), "media/precocinadosNuggets.png"),
        Producto("Patatas", 3, pygame.Rect(625, 550, 60, 60), "media/precocinadosPatatas.png"),
        Producto("Canelones", 4, pygame.Rect(475, 675, 60, 60), "media/precocinadosCanelones.png"),
        Producto("Migas", 3, pygame.Rect(625, 675, 60, 60), "media/precocinadosMigas.png"),
    ]
}

# =====================================================
# ESTADO
# =====================================================
en_tienda = -1
run = True

# =====================================================
# BUCLE PRINCIPAL
# =====================================================
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
                carrito.pop()
                notificar("Producto eliminado")

            if e.key == pygame.K_e and en_tienda in tiendas_items:
                for p in tiendas_items[en_tienda]:
                    if jugador_rect.colliderect(p.rect):
                        carrito.append(p)
                        notificar(f"Añadido: {p.nombre}")

            if e.key == pygame.K_r and carrito:
                total = sum(p.precio for p in carrito)
                if dinero >= total:
                    dinero -= total
                    comprados.extend(carrito)
                    carrito.clear()
                    notificar("Compra realizada")
                else:
                    notificar("Dinero insuficiente")

            if e.key == pygame.K_g and en_tienda != -1:
                carrito.clear()
                en_tienda = -1
                jugador.x, jugador.y = 300, 300

    if not mostrar_carrito and not mostrar_comprados:
        jugador.mover(keys)

    # =====================================================
    # DIBUJADO
    # =====================================================
    if en_tienda == -1:
        win.blit(fondo_pueblo, (0, 0))
        for i, t in enumerate(tiendas_rects):
            win.blit(imagenes_tiendas[i], t.topleft)
            if jugador_rect.colliderect(t):
                en_tienda = i
                jugador.x, jugador.y = 400, 650
    else:
        win.blit(fondos_tiendas[en_tienda], (0, 0))
        for p in tiendas_items[en_tienda]:
            hover = jugador_rect.colliderect(p.rect)
            p.dibujar(win, hover)
            if hover:
                win.blit(
                    fuente_peque.render(f"{p.precio}€  [E]", True, (255, 255, 255)),
                    (p.rect.x - 5, p.rect.y - 25)
                )

    # =====================================================
    # UI SUPERIOR
    # =====================================================
    win.blit(icono_salida, rect_salida)
    win.blit(icono_comprados, rect_comprados)
    win.blit(icono_carrito, rect_carrito)

    win.blit(fuente_peque.render("[G]", True, (200, 200, 200)), (595, 75))
    win.blit(fuente_peque.render("[C]", True, (200, 200, 200)), (665, 75))
    win.blit(fuente_peque.render("[V]", True, (200, 200, 200)), (735, 75))

    pygame.draw.rect(win, (40, 40, 40), (10, 10, 240, 50), border_radius=10)
    win.blit(img_moneda, (20, 20))
    win.blit(fuente_normal.render(str(dinero), True, (255, 215, 0)), (60, 18))

    # =====================================================
    # CARRITO
    # =====================================================
    if mostrar_carrito:
        s = pygame.Surface((550, 500), pygame.SRCALPHA)
        pygame.draw.rect(s, (40, 40, 40, 230), s.get_rect(), border_radius=20)
        win.blit(s, (125, 120))

        win.blit(fuente_grande.render("Carrito", True, (200, 200, 255)), (150, 140))
        win.blit(
            fuente_peque.render("[R] Comprar todo   [T] Quitar último", True, (180, 255, 180)),
            (150, 180)
        )

        for i, p in enumerate(carrito):
            win.blit(
                fuente_peque.render(f"{p.nombre} - {p.precio}€", True, (255, 255, 255)),
                (150, 220 + i * 28)
            )

    # =====================================================
    # COMPRADOS
    # =====================================================
    if mostrar_comprados:
        s = pygame.Surface((550, 500), pygame.SRCALPHA)
        pygame.draw.rect(s, (30, 50, 30, 230), s.get_rect(), border_radius=20)
        win.blit(s, (125, 120))

        win.blit(fuente_grande.render("Comprados", True, (150, 255, 150)), (150, 140))

        for i, p in enumerate(comprados):
            win.blit(
                fuente_peque.render(p.nombre, True, (255, 255, 255)),
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
