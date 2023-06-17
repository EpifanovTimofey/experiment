import random
import shar
b = []
r1 = random.randint(10, 100)
main = shar.Shar(r1, 200, 100, None)
b.append(main)
kkk = 0
while kkk != 50:
    r1 = random.randint(10,100)
    c = shar.Shar(r1, 200, 100, main)
    b.append(c)
    kkk += 1

def go():
    for s in b:
        s.go()
