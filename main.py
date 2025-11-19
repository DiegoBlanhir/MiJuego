import pygame
import random
from jugador import crear_jugador, mover_jugador, dibujar_jugador
from enemigos import crear_enemigos, mover_enemigos, dibujar_enemigos
from balas import disparar, mover_balas, dibujar_balas
from monedas import crear_monedas, mover_monedas, dibujar_monedas
from colisiones import revisar_colisiones

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi juego fake")
reloj = pygame.time.Clock()

#Objetos
jugador = crear_jugador()
enemigos = crear_enemigos(5)
balas = []
monedas = crear_monedas(3)

puntos = 0  
ejecutando = True

#Bucle
while ejecutando:
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            balas.append(disparar(jugador))

    teclas = pygame.key.get_pressed()
    mover_jugador(teclas, jugador, ANCHO)
    mover_balas(balas)
    mover_enemigos(enemigos, ALTO)
    mover_monedas(monedas, ALTO)

    #Revisar colision
    puntos, ejecutando = revisar_colisiones(jugador, enemigos, balas, monedas, puntos)

    #Pantalla
    pantalla.fill((0, 0, 0))
    dibujar_jugador(pantalla, jugador)
    dibujar_balas(pantalla, balas)
    dibujar_enemigos(pantalla, enemigos)
    dibujar_monedas(pantalla, monedas)

    fuente = pygame.font.SysFont(None, 36)
    texto = fuente.render("Llevas: " + str(puntos), True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))
    pygame.display.flip()

pygame.quit()