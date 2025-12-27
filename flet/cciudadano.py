import flet as ft


class Ciudadano:
    def __init__(self, x, y, ancho_pantalla, alto_pantalla):
        self.x = x
        self.y = y
        self.vel = 20  # Velocidad un poco más alta para que se sienta fluido en Flet
        self.size = 60
        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla

        # Rutas de imágenes
        self.img_idle = "media/quieto.png"
        self.img_move = "media/correr.png"

        # --- COMPONENTE VISUAL (WIDGET) ---
        # Usamos una imagen dentro de un contenedor para poder moverlo (top/left)
        self.imagen = ft.Image(
            src=self.img_idle,
            width=self.size,
            height=self.size,
            fit=ft.ImageFit.CONTAIN
        )

        self.widget = ft.Container(
            content=self.imagen,
            left=self.x,
            top=self.y,
            width=self.size,
            height=self.size,
            animate_position=ft.animation.Animation(100, "easeOut")  # Suavizado de movimiento
        )

    def mover(self, e: ft.KeyboardEvent):
        """
        Calcula la nueva posición basada en la tecla pulsada.
        Retorna True si el personaje se movió.
        """
        moved = False
        key = e.key

        # Guardamos posición anterior por si hay colisión
        old_x, old_y = self.x, self.y

        if key == "Arrow Left" or key == "A":
            self.x = max(0, self.x - self.vel)
            moved = True
        elif key == "Arrow Right" or key == "D":
            self.x = min(self.ancho_pantalla - self.size, self.x + self.vel)
            moved = True
        elif key == "Arrow Up" or key == "W":
            self.y = max(0, self.y - self.vel)
            moved = True
        elif key == "Arrow Down" or key == "S":
            self.y = min(self.alto_pantalla - self.size, self.y + self.vel)
            moved = True

        # Actualizamos la UI solo si hubo movimiento
        if moved:
            self.imagen.src = self.img_move
            self.widget.left = self.x
            self.widget.top = self.y
            self.widget.update()
        else:
            # Si soltamos teclas o no es tecla de movimiento, volvemos a estado quieto
            if self.imagen.src != self.img_idle:
                self.imagen.src = self.img_idle
                self.imagen.update()

        return moved

    def set_posicion(self, x, y):
        """ Teletransporta al personaje (para entrar/salir de tiendas) """
        self.x = x
        self.y = y
        self.widget.left = x
        self.widget.top = y
        self.widget.update()