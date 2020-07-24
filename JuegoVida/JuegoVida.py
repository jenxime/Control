import pygame
import numpy as np
import time

#ANCHO Y ALTO DE LA PANTALLA
WIDTH, HEIGHT = 600, 600
#CREACION DE LA PANTALLA
screen = pygame.display.set_mode([WIDTH,HEIGHT]) # Set size of screen
#COLOR DEL FONDO CASI NEGRO CASI OSCURO
BG_COLOR = (25, 25, 25) # Define background color
#PINTAMOS EL FONDO CON EL COLOR ELEGIDO
screen.fill(BG_COLOR)

#NUMERO CELDAS
nX, nY =50, 50
#DIMENSIONES CELDA
xSize = WIDTH/nX
ySize = HEIGHT/nY

pygame.init() # inicializando pygame

LIVE_COLOR = (255,255,255)
DEAD_COLOR = (128,128,128)

# Estado del juego Celdas vivas = 1; Celdas muertas = 0
status = np.zeros((nX,nY)) # Intialize status of cells

# #AUTOMATA PALO
# status[5, 3] = 1
# status[5, 4] = 1
# status[5, 5] = 1

# #AUTOMATA MOVIL
# status[21, 21] = 1
# status[22, 22] = 1
# status[22, 23] = 1
# status[21, 23] = 1
# status[20, 23] = 1

#AUTOMATA NAVE
status[15, 15] = 1
status[14, 16] = 1
status[16, 15] = 1
status[17, 15] = 1
status[18, 15] = 1
status[19, 16] = 1
status[19, 17] = 1
status[18, 18] = 1
status[18, 18] = 1
status[18, 18] = 1
status[16, 19] = 1
status[14, 18] = 1
status[15, 19] = 1

#CONTROL DE LA EJECUCION
pauseRun = False
running = True

#BUCLE DE EJECUCION
while running:

    newStatus = np.copy(status) # Copy status
    screen.fill(BG_COLOR)  # Clean background
    time.sleep(0.1)

    #REGISTROS EVENTOS TECLADO Y RATON
    ev = pygame.event.get()

    for event in ev:
        #DETECTAMOS SI SE PRESIONA UNA TECLA
        if event.type == pygame.KEYDOWN:
            pauseRun = not pauseRun
        #DETECTAMOS SI SE PRESIONA EL RATON
        mouseClick = pygame.mouse.get_pressed()
        print(mouseClick)

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / xSize)), int(np.floor(posY / ySize))
            #newStatus[x,y] = np.abs(newStatus[x,y]-1)
            newStatus[celX, celY] = not mouseClick[2]

    for x in range(0, nX):
        for y in range(0, nY):

            if not pauseRun:

                # Numero de vecinos cercanos #NUMERO DE CELDAS
                nNeigh = status[(x - 1) % nX, (y - 1) % nY] + \
                         status[(x)     % nX, (y - 1) % nY] + \
                         status[(x + 1) % nX, (y - 1) % nY] + \
                         status[(x - 1) % nX, (y)     % nY] + \
                         status[(x + 1) % nX, (y)     % nY] + \
                         status[(x - 1) % nX, (y + 1) % nY] + \
                         status[(x)     % nX, (y + 1) % nY] + \
                         status[(x + 1) % nX, (y + 1) % nY]

                # Rule 1: Una celula muerta con 3 vecinas revive
                if status[x, y] == 0 and nNeigh == 3:
                    newStatus[x, y] = 1

                # Rule 2: Una celula viva con mas de 3 vecinos o menos de 2 muere
                elif status[x, y] == 1 and (nNeigh < 2 or nNeigh > 3):
                    newStatus[x, y] = 0

            #CREACION DEL POLIGONO DE CADA CELDA A DIBUJAR
            poly = [((x) * xSize, y * ySize),
                    ((x+1) * xSize, y * ySize),
                    ((x+1) * xSize, (y+1) * ySize),
                    ((x) * xSize, (y+1) * ySize)]

            # dibujamos la celda para cada par de x e y
            if newStatus[x,y] == 0:
                pygame.draw.polygon(screen, DEAD_COLOR, poly, 1)
            else:
                pygame.draw.polygon(screen, LIVE_COLOR, poly, 0)

    #ACTUALIZAMOS EL ESTADO DEL JUEGO
    status = np.copy(newStatus)
    pygame.display.flip()

pygame.quit()


