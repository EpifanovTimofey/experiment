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
        self.figura = random.choice(["krug", "romb"])
        # self.rastoanie = 1000

    def pluspat(self):
        self.a += 5

    def plus(self, chislo):
        self.a += chislo

    def draw(self, ekran):
        if self.figura == "krug":
            pygame.draw.circle(ekran, [self.l1, self.l2, self.l3], [self.b1, self.b2], self.a, 5)
            pygame.draw.circle(ekran, [0, 0, 0], [self.b1, self.b2], (self.speed_y + self.speed_x) / 2)
        if self.figura == "romb":
            pygame.draw.polygon(ekran, [self.l1, self.l2, self.l3],
                                [[self.b1, self.b2 - self.a], [self.b1 - self.a, self.b2], [self.b1, self.b2 + self.a],
                                 [self.b1 + self.a, self.b2]], 5)
            pygame.draw.polygon(ekran, [0, 0, 0],
                                [[self.b1, self.b2 - self.speed_y], [self.b1 - self.speed_x, self.b2],
                                 [self.b1, self.b2 + self.speed_y],
                                 [self.b1 + self.speed_x, self.b2]])
        if self.obvodka:
            pygame.draw.circle(ekran, [0, 0, 0], [self.b1, self.b2], self.a, 5)

        # if self.main == None:
        #     pygame.draw.circle(ekran, [255, 0, 0], [self.b1, self.b2], self.a, 5)

    def go(self):
        if self.x == 1:
            self.b1 -= self.speed_x
            if 200 + self.a >= self.b1:
                self.x = 0

        elif self.x == 0:
            self.b1 += self.speed_x
            if 500 - self.a <= self.b1:
                self.x = 1

        if self.y == 1:
            self.b2 -= self.speed_y
            if 200 + self.a >= self.b2:
                self.y = 0

        elif self.y == 0:
            self.b2 += self.speed_y
            if 500 - self.a <= self.b2:
                self.y = 1
        self.a = 100

        # self.blizh_shar = self.spisok_shar[0]
        # if self.spisok_shar[0] is self:
        #     self.blizh_shar = self.spisok_shar[1]
        #
        # for s in self.spisok_shar:
        #     a1 = math.dist([self.b1, self.b2], [s.b1, s.b2])
        #     a2 = math.dist([self.b1, self.b2], [self.blizh_shar.b1, self.blizh_shar.b2])
        #     if s is not self:
        #         if a1 < a2:
        #             self.blizh_shar = s
        # a2 = math.dist([self.b1, self.b2], [self.blizh_shar.b1, self.blizh_shar.b2])
        # if a2 < self.blizh_shar.a + self.a:
        #     self.red_obvodka = True
        # else:
        #     self.red_obvodka = False
        for s in self.spisok_shar:
            if s is self:
                continue
            a1 = math.dist([self.b1, self.b2], [s.b1, s.b2])
            if a1 <= s.a + self.a:
                self.a = a1 - s.a
                if self.a < 0:
                    self.a = 0

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
