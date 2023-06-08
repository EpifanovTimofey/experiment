import pygame, random


class Shar:
    def __init__(self, chislo, koordinat1, koordinat2):
        self.a = chislo
        self.b1 = koordinat1
        self.b2 = koordinat2
        self.l1 = random.randint(0, 255)
        self.l2 = random.randint(0, 255)
        self.l3 = random.randint(0, 255)

    def pluspat(self):
        self.a += 5

    def plus(self, chislo):
        self.a += chislo

    def draw(self, ekran):
        pygame.draw.circle(ekran, [self.l1, self.l2, self.l3], [self.b1, self.b2], self.a)

    def go(self):
        self.b1 += 1
