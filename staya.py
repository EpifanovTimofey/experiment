import pygame, random
import shar

display = pygame.display.get_surface()


class Staya:
    def __init__(self):
        self.b = []
        self.main = shar.Shar(100, 500, 500, None, self.b)
        self.b.append(self.main)


    def create(self):
        for sh in range(20):
            c = shar.Shar(100, random.randint(100, display.get_width() - 100),
                          random.randint(100, display.get_height() - 100), self.main, self.b)
            self.b.append(c)

    def go(self):
        for sh in self.b:
            sh.go()

    def view(self):
        for sh in self.b:
            sh.draw(display)

    def control(self, p1):
        for sh in self.b:
            sh.events(p1)
