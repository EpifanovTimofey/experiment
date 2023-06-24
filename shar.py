import pygame, random, math

display = pygame.display.get_surface()


class Shar:
    def __init__(self, chislo, koordinat1, koordinat2, main, spisok_shar):
        self.a = chislo
        self.b1 = koordinat1
        self.b2 = koordinat2
        self.l1 = random.randint(0, 255)
        self.l2 = random.randint(0, 255)
        self.l3 = random.randint(0, 255)
        self.x = 1
        self.y = 1
        self.speed_x = random.randint(1, 4)
        self.speed_y = random.randint(1, 4)
        self.obvodka = False
        self.red_obvodka = False
        self.main = main
        self.spisok_shar = spisok_shar
        self.rastoanie = 1000

    def pluspat(self):
        self.a += 5

    def plus(self, chislo):
        self.a += chislo

    def draw(self, ekran):
        if self.main != None:
            pygame.draw.line(ekran, [0, 0, 0], [self.b1, self.b2], [self.main.b1, self.main.b2])
        pygame.draw.circle(ekran, [self.l1, self.l2, self.l3], [self.b1, self.b2], self.a)
        pygame.draw.circle(ekran, [0, 0, 0], [self.b1, self.b2], (self.speed_y + self.speed_x) / 2)
        if self.obvodka:
            pygame.draw.circle(ekran, [0, 0, 0], [self.b1, self.b2], self.a, 5)
        if self.red_obvodka:
            pygame.draw.circle(ekran, [255, 0, 0], [self.b1, self.b2], self.a, 5)


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

        self.a += 1
        if self.a == 101:
            self.a = 10

        for s in self.spisok_shar:
            a = math.dist([self.b1, self.b2], [s.b1, s.b2])
            if s is not self:
                self.rastoanie = a
                print(self.rastoanie)
                # if a <= self.a + s.a:
                #     self.red_obvodka = True
                # else:
                #     self.red_obvodka = False


    def events(self, p1):
        for p2 in p1:
            if p2.type == pygame.KEYDOWN and p2.key == pygame.K_SPACE:
                self.l1 = random.randint(0, 255)
                self.l2 = random.randint(0, 255)
                self.l3 = random.randint(0, 255)
            if p2.type == pygame.MOUSEBUTTONDOWN and p2.button == pygame.BUTTON_LEFT:
                if math.dist(p2.pos, [self.b1, self.b2]) <= self.a:
                    self.speed_y += 1
                    self.speed_x += 1
        if math.dist(pygame.mouse.get_pos(), [self.b1, self.b2]) <= self.a:
            self.obvodka = True
        else:
            self.obvodka = False
