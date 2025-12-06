import pygame

def cargar_sprite_sheet():
    try:
        sheet = pygame.image.load("personaje_direcciones.png").convert_alpha()
        # Escalar la imagen a un tamaño visible
        sheet = pygame.transform.scale(sheet, (192, 192))
    except:
        # Si falla cargar la imagen, crear un sprite simple
        sheet = pygame.Surface((192, 192))
        pygame.draw.rect(sheet, (0, 100, 255), pygame.Rect(0, 0, 192, 192))

    # Crear animaciones simplemente usando la misma imagen
    # (4 frames de la misma imagen)
    frame = pygame.transform.scale(sheet, (64, 64))
    
    animaciones = {
        "arriba": [frame, frame, frame, frame],
        "izquierda": [frame, frame, frame, frame],
        "abajo": [frame, frame, frame, frame],
        "derecha": [frame, frame, frame, frame]
    }

    rect = frame.get_rect(center=(400, 500))
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
