import random

import shar
kkk = 0
b = []
while kkk != 100:
    r1 = random.randint(50,100)
    c = shar.Shar(r1, 200, 100)
    b.append(c)
    kkk += 1

def go():
    for s in b:
        s.go()
