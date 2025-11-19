import pygame

def disparar(jugador):
    return pygame.Rect(jugador.x + 23, jugador.y, 5, 10)

def mover_balas(balas):
    for b in balas[:]:
        b.y -= 10
        if b.y < 0:
            balas.remove(b)

def dibujar_balas(pantalla, balas):
    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 255), b)