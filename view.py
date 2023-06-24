import pygame

dis = pygame.display.set_mode([600,600])

import model

def jjj():
    dis.fill([255, 255, 255])
    for s in model.b:
        s.draw(dis)

    pygame.display.flip()


jjj()
