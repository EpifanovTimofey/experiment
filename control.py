import pygame, model

def p():
    p1 = pygame.event.get()
    for f in p1:
        if f.type == pygame.QUIT:
            exit()
    for s in model.b:
        s.events(p1)
