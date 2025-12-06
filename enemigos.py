import pygame, random

def crear_enemigos(cantidad):
    enemigos = []
    for _ in range(cantidad):
        enemigos.append(pygame.Rect(random.randint(0, 750), random.randint(-200, -50), 40, 40))
    return enemigos

def mover_enemigos(enemigos, ALTO):
    for e in enemigos:
        e.y += 5
        if e.y > ALTO:
            e.y = random.randint(-100, -40)
            e.x = random.randint(0, 750)

def dibujar_enemigos(pantalla, enemigos):
    for e in enemigos:
        # Cara de enemigo
        pygame.draw.circle(pantalla, (150, 0, 0), e.center, 22)
        pygame.draw.circle(pantalla, (255, 0, 0), e.center, 20)
        pygame.draw.circle(pantalla, (255, 255, 255), (e.centerx - 7, e.centery - 3), 3)
        pygame.draw.circle(pantalla, (255, 255, 255), (e.centerx + 7, e.centery - 3), 3)
        pygame.draw.circle(pantalla, (0, 0, 0), (e.centerx - 7, e.centery - 3), 1)
        pygame.draw.circle(pantalla, (0, 0, 0), (e.centerx + 7, e.centery - 3), 1)
        pygame.draw.line(pantalla, (255, 255, 255), (e.centerx - 5, e.centery + 5), (e.centerx + 5, e.centery + 5), 2)
