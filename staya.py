import pygame, random
import shar

display = pygame.display.get_surface()


class Staya:
    def __init__(self, lev, prav, verh, niz, krug_ili_romb, zhiteli):
        self.b = []
        self.main = shar.Shar(100, 500, 500, None, self.b, krug_ili_romb)
        self.b.append(self.main)
        self.lev = lev
        self.prav = prav
        self.verh = verh
        self.niz = niz
        self.figura = krug_ili_romb
        self.zhiteli = zhiteli
        self.create()

    def create(self):
        for sh in range(self.zhiteli - 1):
            c = shar.Shar(100, random.randint(100, display.get_width() - 100),
                          random.randint(100, display.get_height() - 100), self.main, self.b, self.figura)
            self.b.append(c)

    def go(self):
        for sh in self.b:
            sh.go(self.lev, self.prav, self.verh, self.niz)

    def view(self):
        for sh in self.b:
            sh.draw(display)
        pygame.draw.rect(display,[0,0,0],[self.lev, self.verh, self.prav - self.lev, self.niz - self.verh], 4)

    def control(self, p1):
        for sh in self.b:
            sh.events(p1)
