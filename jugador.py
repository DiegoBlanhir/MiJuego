import pygame

def crear_jugador():
    return pygame.Rect(400, 500, 50, 50)

def mover_jugador(teclas, jugador, ANCHO):
    if teclas[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= 5
    if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += 5

def dibujar_jugador(pantalla, jugador):
    pygame.draw.rect(pantalla, (255, 255, 0), jugador)
