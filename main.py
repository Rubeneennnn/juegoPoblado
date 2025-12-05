import pygame
import sys
from ciudadano import Ciudadano

pygame.init()
win = pygame.display.set_mode((800, 800))

jugador = Ciudadano(100,100)
tiendas = [
    pygame.Rect(50, 150, 60, 80),
    pygame.Rect(150, 150, 60, 80),
    pygame.Rect(250, 150, 60, 80),
    pygame.Rect(350, 150, 60, 80),
    pygame.Rect(450, 150, 60, 80)
]
colores = [
    pygame.color
]

run = True
while run:
    for e in pygame.event.get():
        if e.type = pygame.QUIT:
            run = False
        keys = pygame.key.get_pressed()
        quieto = jugador.mover(keys)
        tienda_actual = -1
        if quieto:
            for i,t in enumerate(tiendas):

