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
        # Cuerpo de la bala
        pygame.draw.rect(pantalla, (255, 255, 0), b)
        pygame.draw.polygon(pantalla, (255, 165, 0), [
            (b.centerx, b.top),
            (b.left - 2, b.top + 3),
            (b.right + 2, b.top + 3)
        ])
        pygame.draw.line(pantalla, (255, 255, 150), (b.left + 1, b.centery), (b.right - 1, b.centery), 1)
