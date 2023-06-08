import pygame, model

dis = pygame.display.set_mode([800, 600])


def jjj():
    dis.fill([0, 0, 0])
    model.c.draw(dis)
    model.f.draw(dis)
    pygame.display.flip()


jjj()
