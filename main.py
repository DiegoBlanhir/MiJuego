import pygame
import random

from fondo import cargar_fondo, mover_fondo, dibujar_fondo
from jugador_direccional import (
    cargar_sprite_sheet, mover_jugador_direccional,
    animar_sprite, dibujar_jugador_direccional
)

from enemigos import crear_enemigos, mover_enemigos, dibujar_enemigos
from balas import disparar, mover_balas, dibujar_balas
from monedas import crear_monedas, mover_monedas, dibujar_monedas
from colisiones import revisar_colisiones


# Inicialización
pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi juego con sprites y dirección")
reloj = pygame.time.Clock()


# Fondo
fondo, fondo_y = cargar_fondo()


# Jugador Direccional
animaciones, jugador, direccion, frame, ultimo_tiempo = cargar_sprite_sheet()


# Objetos
enemigos = crear_enemigos(5)
balas = []
monedas = crear_monedas(3)
puntos = 0


# Bucle
ejecutando = True
while ejecutando:

    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            balas.append(disparar(jugador))


    teclas = pygame.key.get_pressed()


    # Mover Fondo
    fondo_y = mover_fondo(fondo_y, 2, ALTO)
    dibujar_fondo(pantalla, fondo, fondo_y)


    # Jugador con sprite
    direccion, moviendo = mover_jugador_direccional(teclas, jugador, ANCHO, ALTO)
    frame, ultimo_tiempo = animar_sprite(animaciones, direccion, frame, ultimo_tiempo, moviendo)
    dibujar_jugador_direccional(pantalla, animaciones, direccion, frame, jugador)


    # Otros objetos
    mover_balas(balas)
    mover_enemigos(enemigos, ALTO)
    mover_monedas(monedas, ALTO)

    # Colisiones
    puntos, ejecutando = revisar_colisiones(jugador, enemigos, balas, monedas, puntos)

    # Dibujar balas, enemigos, monedas
    dibujar_balas(pantalla, balas)
    dibujar_enemigos(pantalla, enemigos)
    dibujar_monedas(pantalla, monedas)

    # Texto
    fuente = pygame.font.SysFont(None, 36)
    texto = fuente.render("Llevas: " + str(puntos), True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
pygame.quit()
