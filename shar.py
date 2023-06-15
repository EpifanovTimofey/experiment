import pygame, random

display = pygame.display.get_surface()

class Shar:
    def __init__(self, chislo, koordinat1, koordinat2):
        self.a = chislo
        self.b1 = koordinat1
        self.b2 = koordinat2
        self.l1 = random.randint(0, 255)
        self.l2 = random.randint(0, 255)
        self.l3 = random.randint(0, 255)
        self.x = 1
        self.y = 1
        self.speed_x = random.randint(1, 10)
        self.speed_y = random.randint(1, 10)

    def pluspat(self):
        self.a += 5

    def plus(self, chislo):
        self.a += chislo

    def draw(self, ekran):
        pygame.draw.circle(ekran, [self.l1, self.l2, self.l3], [self.b1, self.b2], self.a)
        pygame.draw.circle(ekran, [0, 0, 0], [self.b1, self.b2], (self.speed_y+self.speed_x)/2)

    def go(self):
        if self.x == 1:
            self.b1 -= self.speed_x
            if 0 + self.a >= self.b1:
                self.x = 0

        elif self.x == 0:
            self.b1 += self.speed_x
            if display.get_width() - self.a <= self.b1:
                self.x = 1

        if self.y == 1:
            self.b2 -= self.speed_y
            if 0 + self.a >= self.b2:
                self.y = 0

        elif self.y == 0:
            self.b2 += self.speed_y
            if display.get_height() - self.a <= self.b2:
                self.y = 1

    def ggg(self):
        k = 1
        k += k
        self.append(k)