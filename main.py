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
from database import crear_base_datos, guardar_puntuacion, obtener_mejores_puntuaciones, obtener_puntuacion_maxima, es_top_3


# Inicialización
pygame.init()
crear_base_datos()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("SPACE FLIGHT")
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


# Pantalla de Inicio
def pantalla_inicio():
    """Muestra la pantalla de inicio y espera a que el usuario presione una tecla"""
    esperando = True
    while esperando:
        reloj.tick(60)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                return True
        
        pantalla.fill((0, 0, 0))
        
        fuente_titulo = pygame.font.SysFont(None, 72)
        fuente_texto = pygame.font.SysFont(None, 36)
        
        titulo = fuente_titulo.render("SPACE FLIGHT", True, (255, 0, 0))
        instrucciones = fuente_texto.render("Presiona cualquier tecla para comenzar", True, (255, 255, 255))
        controles = fuente_texto.render("WASD/Flechas: Mover | ESPACIO: Disparar", True, (200, 200, 200))
        
        pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 150))
        pantalla.blit(instrucciones, (ANCHO // 2 - instrucciones.get_width() // 2, 300))
        pantalla.blit(controles, (ANCHO // 2 - controles.get_width() // 2, 400))
        
        pygame.display.flip()


# Pantalla para ingresar nombre
def pantalla_ingresar_nombre(puntos_finales):
    """Muestra una pantalla para que el jugador ingrese su nombre"""
    nombre = ""
    esperando = True
    
    while esperando:
        reloj.tick(60)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre.strip():
                    return nombre.strip()
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif evento.unicode.isalnum() or evento.unicode == " ":
                    if len(nombre) < 20:
                        nombre += evento.unicode
        
        pantalla.fill((0, 0, 0))
        
        fuente_titulo = pygame.font.SysFont(None, 60)
        fuente_texto = pygame.font.SysFont(None, 40)
        fuente_pequeña = pygame.font.SysFont(None, 30)
        
        titulo = fuente_titulo.render("¡TOP 3!", True, (0, 255, 0))
        puntos = fuente_texto.render(f"Puntuación: {puntos_finales}", True, (255, 255, 0))
        instrucciones = fuente_texto.render("Ingresa tu nombre:", True, (255, 255, 255))
        
        # Caja para el nombre
        nombre_rect = pygame.Rect(ANCHO // 2 - 150, 300, 300, 50)
        pygame.draw.rect(pantalla, (100, 100, 100), nombre_rect, 2)
        
        nombre_texto = fuente_pequeña.render(nombre if nombre else "Escribe aquí...", True, (200, 200, 200))
        pantalla.blit(nombre_texto, (nombre_rect.x + 10, nombre_rect.y + 10))
        
        presiona = fuente_pequeña.render("Presiona ENTER para confirmar", True, (150, 150, 150))
        
        pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 50))
        pantalla.blit(puntos, (ANCHO // 2 - puntos.get_width() // 2, 150))
        pantalla.blit(instrucciones, (ANCHO // 2 - instrucciones.get_width() // 2, 220))
        pantalla.blit(presiona, (ANCHO // 2 - presiona.get_width() // 2, 400))
        
        pygame.display.flip()


# Pantalla Final
def pantalla_final(puntos_finales, nombre):
    """Muestra la pantalla de Game Over con los puntos y mejores puntuaciones"""
    # Guardar la puntuación
    guardar_puntuacion(nombre, puntos_finales)
    
    # Obtener mejores puntuaciones
    mejores = obtener_mejores_puntuaciones(3)
    
    esperando = True
    while esperando:
        reloj.tick(60)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                return True
        
        pantalla.fill((0, 0, 0))
        
        fuente_titulo = pygame.font.SysFont(None, 72)
        fuente_texto = pygame.font.SysFont(None, 48)
        fuente_instrucciones = pygame.font.SysFont(None, 30)
        fuente_pequena = pygame.font.SysFont(None, 24)
        
        titulo = fuente_titulo.render("GAME OVER", True, (255, 0, 0))
        puntos_texto = fuente_texto.render(f"Puntuación: {puntos_finales}", True, (255, 255, 0))
        reiniciar = fuente_instrucciones.render("Presiona cualquier tecla para reiniciar", True, (200, 200, 200))
        
        pantalla.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 50))
        pantalla.blit(puntos_texto, (ANCHO // 2 - puntos_texto.get_width() // 2, 150))
        
        # Mostrar mejores puntuaciones
        mejores_titulo = fuente_instrucciones.render("TOP 3 PUNTUACIONES:", True, (0, 255, 0))
        pantalla.blit(mejores_titulo, (ANCHO // 2 - mejores_titulo.get_width() // 2, 250))
        
        y_pos = 300
        for i, (nombre_top, puntos) in enumerate(mejores, 1):
            mejor = fuente_pequena.render(f"{i}. {nombre_top} - {puntos} pts", True, (100, 255, 100))
            pantalla.blit(mejor, (ANCHO // 2 - mejor.get_width() // 2, y_pos))
            y_pos += 35
        
        pantalla.blit(reiniciar, (ANCHO // 2 - reiniciar.get_width() // 2, 500))
        
        pygame.display.flip()


# Bucle principal del juego
ejecutando = True
while ejecutando:
    juego_iniciado = pantalla_inicio()
    
    if not juego_iniciado:
        break
    
    # Reiniciar variables del juego
    enemigos = crear_enemigos(5)
    balas = []
    monedas = crear_monedas(3)
    puntos = 0
    animaciones, jugador, direccion, frame, ultimo_tiempo = cargar_sprite_sheet()
    fondo_y = 0
    
    juego_activo = True
    while juego_activo and ejecutando:
        reloj.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                juego_activo = False

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
        puntos, juego_activo = revisar_colisiones(jugador, enemigos, balas, monedas, puntos)

        # Dibujar balas, enemigos, monedas
        dibujar_balas(pantalla, balas)
        dibujar_enemigos(pantalla, enemigos)
        dibujar_monedas(pantalla, monedas)

        # Texto
        fuente = pygame.font.SysFont(None, 36)
        texto = fuente.render("Llevas: " + str(puntos), True, (255, 255, 255))
        pantalla.blit(texto, (10, 10))

        pygame.display.flip()
    
    # Mostrar pantalla final si el juego terminó
    if not ejecutando:
        break
    
    # Verificar si está en TOP 3
    if es_top_3(puntos):
        nombre = pantalla_ingresar_nombre(puntos)
        if nombre is None:
            ejecutando = False
            break
    else:
        nombre = "Anónimo"
    
    continuar = pantalla_final(puntos, nombre)
    if not continuar:
        ejecutando = False

pygame.quit()
