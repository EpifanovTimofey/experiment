import random
import shar, pygame
b = []
display = pygame.display.get_surface()
r1 = random.randint(10, 100)
main = shar.Shar(r1, 500, 500, None, b)
b.append(main)
kkk = 0
while kkk != 50:
    r1 = random.randint(10,100)
    x1 = random.randint(100, display.get_width()-100)
    y1 = random.randint(100, display.get_height()-100)
    c = shar.Shar(r1, x1, y1, main, b)
    b.append(c)
    kkk += 1

def go():
    for s in b:
        s.go()

