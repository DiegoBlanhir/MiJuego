import random, pygame
from enemigos import crear_enemigos
from monedas import crear_monedas

def revisar_colisiones(jugador, enemigos, balas, monedas, puntos):
    #BALA CON ENEMIGO
    for b in balas[:]:
        for e in enemigos[:]:
            if b.colliderect(e):
                balas.remove(b)
                enemigos.remove(e)
                enemigos.append(pygame.Rect(random.randint(0, 750), random.randint(-100, -40), 40, 40))
                puntos += 10
                break

    #JUGADOR CON ENEMIGO
    for e in enemigos:
        if jugador.colliderect(e):
            print("Fin del juego.")
            return puntos, False

    #JUGADOR CON MONEDAS
    for m in monedas[:]:
        if jugador.colliderect(m):
            monedas.remove(m)
            monedas.append(pygame.Rect(random.randint(0, 780), random.randint(-200, -50), 20, 20))
            puntos += 5

    return puntos, True