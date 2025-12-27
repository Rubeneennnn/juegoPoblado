import flet as ft
import time
from ciudadano import Ciudadano


# =====================================================
# CLASES (HERENCIA Y POLIMORFISMO)
# =====================================================

class Producto:
    """ Clase Padre """

    def __init__(self, nombre, precio, x, y, ruta_img):
        self.nombre = nombre
        self.precio = precio
        self.x = x
        self.y = y
        self.ruta_img = ruta_img

        # Widget visual: Contenedor con Imagen interactiva
        self.widget = ft.Container(
            content=ft.Image(src=ruta_img, fit=ft.ImageFit.CONTAIN),
            width=60, height=60,
            left=x, top=y,
            on_click=self.al_clic,
            tooltip=f"{nombre} ({precio}€)"
        )
        self.app_callback = None

    def asignar_callback(self, callback):
        self.app_callback = callback

    def al_clic(self, e):
        if self.app_callback:
            self.app_callback(self)

    def obtener_info(self):
        """ Método base """
        return f"{self.nombre} - {self.precio}€"


# --- CLASES HIJAS (POLIMORFISMO) ---

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
        self.fondo_path = fondo_path
        self.items = items


# =====================================================
# LISTAS COMPLETAS DE PRODUCTOS (TODOS LOS ITEMS)
# =====================================================

# TIENDA 0: ROPA
items_ropa = [
    Ropa("Chaqueta Azul", 250, 125, 250, "media/chaquetaAzul.png"),
    Ropa("Chaqueta Blanca", 250, 275, 250, "media/chaquetaBlanca.png"),
    Ropa("Chaqueta Negra", 250, 125, 375, "media/chaquetaNegra.png"),
    Ropa("Chaqueta Rosa", 250, 275, 375, "media/chaquetaRosa.png"),

    Ropa("Camiseta Azul", 45, 475, 250, "media/camisetaAzul.png"),
    Ropa("Camiseta Blanca", 45, 625, 250, "media/camisetaBlanca.png"),
    Ropa("Camiseta Negra", 45, 475, 375, "media/camisetaNegra.png"),
    Ropa("Camiseta Rosa", 45, 625, 375, "media/camisetaRosa.png"),

    Ropa("Sudadera Azul", 80, 125, 550, "media/sudaderaAzul.png"),
    Ropa("Sudadera Blanca", 80, 275, 550, "media/sudaderaBlanca.png"),
    Ropa("Sudadera Negra", 80, 125, 675, "media/sudaderaNegra.png"),
    Ropa("Sudadera Rosa", 80, 275, 675, "media/sudaderaRosa.png"),

    Ropa("Pantalón Azul", 50, 475, 550, "media/pantalonAzul.png"),
    Ropa("Pantalón Blanco", 50, 625, 550, "media/pantalonBlanco.png"),
    Ropa("Pantalón Gris", 50, 475, 675, "media/pantalonGris.png"),
    Ropa("Pantalón Negro", 50, 625, 675, "media/pantalonNegro.png"),
]

# TIENDA 1: ANIMALES
items_animales = [
    Mascota("Perro", 500, 125, 250, "media/animalPerro.png"),
    Mascota("Gato", 400, 275, 250, "media/animalGato.png"),
    Mascota("Hamster", 50, 125, 375, "media/animalHamster.png"),
    Mascota("Pez", 20, 275, 375, "media/animalPez.png"),

    Mascota("Comida Perros", 30, 125, 550, "media/comidaPerros.png"),
    Mascota("Comida Gatos", 25, 275, 550, "media/comidaGatos.png"),
    Mascota("Comida Hamster", 10, 125, 675, "media/comidaHamster.png"),
    Mascota("Comida Peces", 8, 275, 675, "media/comidaPeces.png"),

    Mascota("Juguete Perro", 20, 475, 550, "media/jueguetesPerro.png"),
    Mascota("Juguete Gato", 15, 625, 550, "media/juguetesGato.png"),
    Mascota("Juguete Hamster", 12, 475, 675, "media/jueguetesHamster.png"),
    Mascota("Juguete Peces", 10, 625, 675, "media/juguetesPeces.png"),

    Mascota("Spray Limpieza", 15, 475, 250, "media/limpiezaSpray.png"),
    Mascota("Bolsas Basura", 5, 625, 250, "media/limpiezaBolsas.png"),
    Mascota("Aspiradora", 120, 475, 375, "media/limpiezaAspiradora.png"),
]

# TIENDA 2: INFORMÁTICA
items_informatica = [
    Electronica("PC Azul", 900, 125, 250, "media/ordenadorAzul.png"),
    Electronica("PC Blanco", 900, 275, 250, "media/ordenadorBlanco.png"),
    Electronica("PC Negro", 900, 125, 375, "media/ordenadorNegro.png"),
    Electronica("PC Verde", 900, 275, 375, "media/ordenadorVerde.png"),

    Electronica("Teclado Blanco", 60, 125, 550, "media/tecladoBlanco.png"),
    Electronica("Teclado Negro", 60, 275, 550, "media/tecladoNegro.png"),
    Electronica("Ratón Blanco", 35, 125, 675, "media/ratonBlanco.png"),
    Electronica("Ratón Negro", 35, 275, 675, "media/ratonNegro.png"),

    Electronica("Cascos Blancos A.", 150, 475, 550, "media/cascosBlancosAirPods.png"),
    Electronica("Cascos Blancos D.", 120, 625, 550, "media/cascosBlancosDiadema.png"),
    Electronica("Cascos Negros A.", 150, 475, 675, "media/cascosNegrosAirPods.png"),
    Electronica("Cascos Negros D.", 120, 625, 675, "media/cascosNegrosDiadema.png"),

    Electronica("PlayStation", 500, 475, 250, "media/consolaPlay.png"),
    Electronica("Xbox", 500, 625, 250, "media/consolaXbox.png"),
    Electronica("Nintendo Switch", 450, 475, 375, "media/consolaSwitch.png"),
]

# TIENDA 3: SUPERMERCADO
items_supermercado = [
    Alimento("Manzana", 2, 125, 250, "media/frutaManzana.png"),
    Alimento("Plátano", 2, 275, 250, "media/frutaPlatano.png"),
    Alimento("Brócoli", 3, 125, 375, "media/frutaBrocoli.png"),
    Alimento("Judías", 3, 275, 375, "media/frutaJudias.png"),

    Alimento("Agua", 1, 125, 550, "media/frescosAgua.png"),
    Alimento("Leche", 1.5, 275, 550, "media/frescosLeche.png"),
    Alimento("Huevos", 3, 125, 675, "media/fresosHuevos.png"),
    Alimento("Sushi", 6, 275, 675, "media/frescosSushi.png"),

    Alimento("Croissants", 2.5, 475, 250, "media/bolleriaCroisants.png"),
    Alimento("Napolitanas", 2.5, 625, 250, "media/bolleriaNapolitanas.png"),
    Alimento("Crepes", 3, 475, 375, "media/bolleriasCrepes.png"),
    Alimento("Tarta", 8, 625, 375, "media/bolleriasTartas.png"),

    Alimento("Nuggets", 4, 475, 550, "media/precocinadosNuggets.png"),
    Alimento("Patatas", 3, 625, 550, "media/precocinadosPatatas.png"),
    Alimento("Canelones", 4, 475, 675, "media/precocinadosCanelones.png"),
    Alimento("Migas", 3, 625, 675, "media/precocinadosMigas.png"),
]

tiendas_data = {
    0: Tienda("media/tiendaRopa.png", items_ropa),
    1: Tienda("media/tiendaAnimales.png", items_animales),
    2: Tienda("media/tiendaInformatica.png", items_informatica),
    3: Tienda("media/tiendaSupermercado.png", items_supermercado),
}

# Entradas en el pueblo (simulación de Rects)
entradas_rects = [
    {"id": 0, "x": 20, "y": 375, "w": 90, "h": 120, "img": "media/tienda1.png"},
    {"id": 1, "x": 175, "y": 375, "w": 90, "h": 120, "img": "media/tienda2.png"},
    {"id": 2, "x": 20, "y": 500, "w": 90, "h": 120, "img": "media/tienda3.png"},
    {"id": 3, "x": 175, "y": 500, "w": 90, "h": 120, "img": "media/tienda4.png"},
]


# =====================================================
# LÓGICA PRINCIPAL (MAIN)
# =====================================================

def main(page: ft.Page):
    page.title = "Simulador Completo Flet OOP"
    page.window_width = 800
    page.window_height = 800
    page.padding = 0
    page.theme_mode = ft.ThemeMode.DARK

    # --- ESTADO GLOBAL ---
    dinero = 5000
    carrito = []
    comprados = []
    en_tienda_id = -1

    # UI Componentes
    txt_dinero = ft.Text(f"{dinero}€", size=20, weight="bold", color="yellow")

    def notificar(mensaje):
        page.snack_bar = ft.SnackBar(ft.Text(mensaje), open=True)
        page.update()

    # --- CALLBACKS DE COMPRA ---
    def agregar_al_carrito(producto):
        carrito.append(producto)
        notificar(f"Añadido: {producto.nombre}")

        # Efecto visual simple al comprar
        producto.widget.opacity = 0.5
        producto.widget.update()
        time.sleep(0.1)
        producto.widget.opacity = 1.0
        producto.widget.update()

    # Asignamos el callback a todos los productos creados arriba
    for t_id in tiendas_data:
        for p in tiendas_data[t_id].items:
            p.asignar_callback(agregar_al_carrito)

    # --- LÓGICA CARRITO Y COMPRA (POLIMORFISMO) ---
    def abrir_carrito(e):
        items_view = ft.Column(scroll="auto")
        total = sum(p.precio for p in carrito)

        # Aquí usamos el método polimórfico de cada objeto
        for p in carrito:
            items_view.controls.append(ft.Text(p.obtener_info(), size=16))

        def pagar(e):
            nonlocal dinero
            if dinero >= total:
                dinero -= total
                txt_dinero.value = f"{round(dinero, 2)}€"
                comprados.extend(carrito)
                carrito.clear()
                notificar(f"¡Compra realizada! Total: {total}€")
                dlg_carrito.open = False
                page.update()
            else:
                notificar("Dinero insuficiente")

        def borrar_ultimo(e):
            if carrito:
                eliminado = carrito.pop()
                notificar(f"Borrado: {eliminado.nombre}")
                dlg_carrito.open = False
                abrir_carrito(None)  # Refrescamos
            else:
                notificar("Carrito vacío")

        def cerrar(e):
            dlg_carrito.open = False
            page.update()

        dlg_carrito = ft.AlertDialog(
            modal=True,
            title=ft.Text("Tu Carrito"),
            content=ft.Container(content=items_view, height=300, width=400),
            actions=[
                ft.TextButton("Borrar Último", on_click=borrar_ultimo),
                ft.TextButton("Cerrar", on_click=cerrar),
                ft.ElevatedButton(f"Pagar ({total}€)", on_click=pagar),
            ],
        )
        page.dialog = dlg_carrito
        dlg_carrito.open = True
        page.update()

    def abrir_historial(e):
        items_view = ft.Column(scroll="auto")
        for p in comprados:
            items_view.controls.append(ft.Text(p.obtener_info(), color="green"))

        dlg_hist = ft.AlertDialog(
            title=ft.Text("Historial de Compras"),
            content=ft.Container(content=items_view, height=300, width=400),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: setattr(dlg_hist, 'open', False) or page.update())]
        )
        page.dialog = dlg_hist
        dlg_hist.open = True
        page.update()

    # --- MONTAJE DE LA ESCENA (STACKS) ---

    # 1. JUGADOR (Instancia de la clase Ciudadano)
    jugador = Ciudadano(300, 300, 800, 800)

    # 2. PUEBLO
    entradas_widgets = []
    for ent in entradas_rects:
        img = ft.Image(src=ent["img"], width=ent["w"], height=ent["h"], fit=ft.ImageFit.FILL)
        # Contenedor absoluto para la tienda
        entradas_widgets.append(ft.Container(content=img, left=ent["x"], top=ent["y"]))

    escena_pueblo = ft.Stack(
        controls=[
            ft.Image(src="media/fondo.png", width=800, height=800, fit=ft.ImageFit.COVER),
            *entradas_widgets,
        ], width=800, height=800
    )

    # 3. TIENDA (Contenedor vacío que llenaremos dinámicamente)
    escena_tienda = ft.Stack(visible=False, width=800, height=800)

    # LAYOUT PRINCIPAL
    layout = ft.Stack(
        controls=[
            escena_pueblo,
            escena_tienda,
            jugador.widget,  # <--- Insertamos el widget controlado por la clase Ciudadano
            # HUD SUPERIOR
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.icons.EURO_SYMBOL, color="yellow"), txt_dinero,
                    ft.IconButton(ft.icons.SHOPPING_CART, on_click=abrir_carrito, tooltip="Carrito [V]"),
                    ft.IconButton(ft.icons.HISTORY, on_click=abrir_historial, tooltip="Historial [C]"),
                    ft.IconButton(ft.icons.EXIT_TO_APP, on_click=lambda e: salir_tienda(), tooltip="Salir [G]"),
                ], alignment=ft.MainAxisAlignment.END),
                top=10, right=10, width=780
            )
        ], width=800, height=800
    )

    # --- LÓGICA DE JUEGO ---

    def check_colision(x1, y1, w1, h1, x2, y2, w2, h2):
        """ Detecta superposición de rectángulos """
        return (x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2)

    def entrar_tienda(id_tienda):
        nonlocal en_tienda_id
        en_tienda_id = id_tienda

        tienda = tiendas_data[id_tienda]
        escena_tienda.controls.clear()

        # Fondo
        escena_tienda.controls.append(ft.Image(src=tienda.fondo_path, width=800, height=800, fit=ft.ImageFit.COVER))

        # Productos
        for p in tienda.items:
            # Añadimos etiqueta de precio
            etiqueta = ft.Container(
                content=ft.Text(f"{p.precio}€", size=10, color="black", weight="bold"),
                bgcolor="white", padding=2, border_radius=5,
                left=p.x, top=p.y + 60
            )
            escena_tienda.controls.append(p.widget)
            escena_tienda.controls.append(etiqueta)

        escena_pueblo.visible = False
        escena_tienda.visible = True

        jugador.set_posicion(400, 600)  # Entrar abajo centro
        notificar("¡Haz clic en los productos para comprar!")
        page.update()

    def salir_tienda():
        nonlocal en_tienda_id
        if en_tienda_id != -1:
            en_tienda_id = -1
            escena_tienda.visible = False
            escena_pueblo.visible = True
            jugador.set_posicion(300, 300)  # Volver al centro del pueblo
            page.update()

    def on_keyboard(e: ft.KeyboardEvent):
        # Teclas globales
        if e.key == "V": abrir_carrito(None)
        if e.key == "C": abrir_historial(None)
        if e.key == "G" or e.key == "Escape": salir_tienda()

        # Delegamos el movimiento a la clase Ciudadano
        se_movio = jugador.mover(e)

        # Si hubo movimiento y estamos en el pueblo, chequear colisiones con tiendas
        if se_movio and en_tienda_id == -1:
            for ent in entradas_rects:
                if check_colision(jugador.x, jugador.y, 60, 60, ent["x"], ent["y"], ent["w"], ent["h"]):
                    entrar_tienda(ent["id"])
                    break

    page.on_keyboard_event = on_keyboard
    page.add(layout)


ft.app(target=main, assets_dir=".")