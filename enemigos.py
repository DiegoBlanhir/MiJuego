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
        pygame.draw.rect(pantalla, (255, 0, 0), e)