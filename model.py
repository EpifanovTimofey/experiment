import random
import shar
b = []
jjjj = shar.Shar(100,800,800)
jjjj.go()
shar.Shar.go(jjjj)
exit()
kkk = 0
while kkk != 100:
    r1 = random.randint(50,100)
    c = shar.Shar(r1, 200, 100)
    b.append(c)
    kkk += 1

def go():
    for s in b:
        s.go()
