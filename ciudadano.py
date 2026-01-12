import pygame

class Ciudadano:
    def __init__(self, x, y, ancho_pantalla, alto_pantalla):
        self.x = x
        self.y = y
        self.vel = 6
        self.size = 68.5

        self.ancho_pantalla = ancho_pantalla
        self.alto_pantalla = alto_pantalla

        try:
            self.img_idle = pygame.image.load("media/quieto.png").convert_alpha()
            self.img_move = pygame.image.load("media/correr.png").convert_alpha()
            self.img_idle = pygame.transform.scale(self.img_idle, (int(self.size), int(self.size)))
            self.img_move = pygame.transform.scale(self.img_move, (int(self.size), int(self.size)))
        except:
            # Fallback simple por si no encuentra imagenes al ejecutar este test
            self.img_idle = pygame.Surface((int(self.size), int(self.size)))
            self.img_idle.fill((0, 0, 255))
            self.img_move = pygame.Surface((int(self.size), int(self.size)))
            self.img_move.fill((0, 255, 255))

        self.is_moving = False

    def mover(self, keys):
        self.is_moving = False

        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel
            self.is_moving = True
        if keys[pygame.K_RIGHT] and self.x < self.ancho_pantalla - self.size:
            self.x += self.vel
            self.is_moving = True
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel
            self.is_moving = True
        if keys[pygame.K_DOWN] and self.y < self.alto_pantalla - self.size:
            self.y += self.vel
            self.is_moving = True

        return self.is_moving

    def dibujar(self, win):
        if self.is_moving:
            imagen = self.img_move
        else:
            imagen = self.img_idle

        win.blit(imagen, (self.x, self.y))