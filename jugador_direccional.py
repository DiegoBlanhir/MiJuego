import pygame

FRAME_W = 64
FRAME_H = 64
COLUMNAS = 4
FILAS = 4

def cargar_sprite_sheet():
    sheet = pygame.image.load("personaje_direcciones.png").convert_alpha()

    def obtener_frames(fila):
        frames = []
        for col in range(COLUMNAS):
            rect = pygame.Rect(col * FRAME_W, fila * FRAME_H, FRAME_W, FRAME_H)
            frames.append(sheet.subsurface(rect))
        return frames

    animaciones = {
        "arriba": obtener_frames(0),
        "izquierda": obtener_frames(1),
        "abajo": obtener_frames(2),
        "derecha": obtener_frames(3)
    }

    rect = animaciones["abajo"][0].get_rect(center=(400, 500))
    return animaciones, rect, "abajo", 0, pygame.time.get_ticks()

def mover_jugador_direccional(teclas, rect, ANCHO, ALTO):
    velocidad = 4
    moviendo = False
    direccion = "abajo"

    if teclas[pygame.K_UP] and rect.top > 0:
        rect.y -= velocidad
        direccion = "arriba"
        moviendo = True
    if teclas[pygame.K_DOWN] and rect.bottom < ALTO:
        rect.y += velocidad
        direccion = "abajo"
        moviendo = True
    if teclas[pygame.K_LEFT] and rect.left > 0:
        rect.x -= velocidad
        direccion = "izquierda"
        moviendo = True
    if teclas[pygame.K_RIGHT] and rect.right < ANCHO:
        rect.x += velocidad
        direccion = "derecha"
        moviendo = True

    return direccion, moviendo

def animar_sprite(animaciones, direccion, frame, ultimo_tiempo, moviendo):
    ahora = pygame.time.get_ticks()

    if moviendo:
        if ahora - ultimo_tiempo > 120:
            frame = (frame + 1) % len(animaciones[direccion])
            ultimo_tiempo = ahora
    else:
        frame = 0

    return frame, ultimo_tiempo

def dibujar_jugador_direccional(pantalla, animaciones, direccion, frame, rect):
    pantalla.blit(animaciones[direccion][frame], rect)
