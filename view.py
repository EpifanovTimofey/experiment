import pygame

dis = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

import model

def jjj():
    dis.fill([255, 255, 255])
    model.st.view()
    model.st2.view()
    pygame.display.flip()
jjj()
