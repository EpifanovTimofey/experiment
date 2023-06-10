import pygame

dis = pygame.display.set_mode([0,0],pygame.FULLSCREEN)

import model

def jjj():
    dis.fill([0, 0, 0])
    for s in model.b:
        s.draw(dis)
    pygame.display.flip()


jjj()
