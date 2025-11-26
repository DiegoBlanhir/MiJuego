import pygame

def cargar_fondo():
    fondo = pygame.image.load("fondo.png").convert()
    fondo = pygame.transform.scale(fondo, (800, 600))
    return fondo, 0

def mover_fondo(fondo_y, velocidad, ALTO):
    fondo_y += velocidad
    if fondo_y >= ALTO:
        fondo_y = 0
    return fondo_y

def dibujar_fondo(pantalla, fondo, fondo_y):
    pantalla.blit(fondo, (0, fondo_y))
    pantalla.blit(fondo, (0, fondo_y - pantalla.get_height()))