import pygame

class Ciudadano:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 1
        self.size = 20

        self.img_idle = pygame.image.load("media/quieto.png").convert_alpha()
        self.img_move = pygame.image.load("media/correr.png").convert_alpha()

        self.img_idle = pygame.transform.scale(self.img_idle, (self.size, self.size))
        self.img_move = pygame.transform.scale(self.img_move, (self.size, self.size))

        self.is_moving = False

    def mover(self, keys):
        self.is_moving = False

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            self.is_moving = True
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            self.is_moving = True
        if keys[pygame.K_UP]:
            self.y -= self.vel
            self.is_moving = True
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            self.is_moving = True

        return self.is_moving

    def dibujar(self, win):
        if self.is_moving:
            imagen = self.img_move
        else:
            imagen = self.img_idle

        win.blit(imagen, (self.x, self.y))