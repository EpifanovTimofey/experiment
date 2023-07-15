import pygame, model

def p():
    p1 = pygame.event.get()
    for f in p1:
        if f.type == pygame.QUIT:
            exit()
    model.st.control(p1)
    model.st2.control(p1)

