import pygame

class Ciudadano:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 1
        self.size = 20
        self.color = (0, 150, 255)

    def mover(self, keys):
        personaje = (self.x, self.y)
        if keys [pygame.K_LEFT]: self.x -= self.vel
        if keys [pygame.K_RIGHT]: self.x += self.vel
        if keys [pygame.K_UP]: self.y -= self.vel
        if keys [pygame.K_DOWN]: self.y += self.vel
        return (self.x, self.y)

    def dibujar(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.size, self.size))

