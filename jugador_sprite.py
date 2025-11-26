import pygame

def cargar_sprite_jugador():
    sprites = [
        pygame.image.load("jugador1.png").convert_alpha(),
        pygame.image.load("jugador2.png").convert_alpha()
    ]
    rect = sprites[0].get_rect()
    rect.x = 400
    rect.y = 500
    return sprites, rect, 0, pygame.time.get_ticks()

def mover_sprite_jugador(teclas, rect, ANCHO):
    if teclas[pygame.K_LEFT] and rect.left > 0:
        rect.x -= 5
    if teclas[pygame.K_RIGHT] and rect.right < ANCHO:
        rect.x += 5

def animar_jugador(sprites, frame, ultimo_tiempo):
    ahora = pygame.time.get_ticks()
    if ahora - ultimo_tiempo > 150:
        frame = (frame + 1) % len(sprites)
        ultimo_tiempo = ahora
    return frame, ultimo_tiempo

def dibujar_sprite_jugador(pantalla, sprites, rect, frame):
    pantalla.blit(sprites[frame], rect)