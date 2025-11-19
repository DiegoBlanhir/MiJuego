import pygame, random

def crear_monedas(cantidad):
    monedas = []
    for _ in range(cantidad):
        monedas.append(pygame.Rect(random.randint(0, 780), random.randint(-200, -50), 20, 20))
    return monedas

def mover_monedas(monedas, ALTO):
    for m in monedas:
        m.y += 3
        if m.y > ALTO:
            m.y = random.randint(-200, -50)
            m.x = random.randint(0, 780)

def dibujar_monedas(pantalla, monedas):
    for m in monedas:
        pygame.draw.rect(pantalla, (255, 215, 0), m)
