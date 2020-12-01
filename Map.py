import pygame
from random import randint

pygame.init()
FPS = 30
Ecrx = 1200
Ecry = 720
screen = pygame.display.set_mode((Ecrx, Ecry))
screen.fill((100, 200, 0))


class Karta:
    FPS = 30
    Ecrx = 1200
    Ecry = 720
    Road = []
    Buildings = []

    def generate_road(self):
        """
        генерирует массив точек, пригодный для построения по ним дороги
        :return: собсна массив
        """
        x = self.Ecrx / 10
        y = self.Ecry / 2
        shag = 0
        massiv = [[int(x), int(y)]]
        while x < 9 * self.Ecrx / 10 - 50:
            shag += 1
            dl = randint(-100, 100)
            if dl == 0:
                dl = 1
            if shag % 2 == 1:
                x = x + 50 + dl ** 2 / abs(dl)
            else:
                y += dl / abs(dl) * (50 + abs(dl))
            if y < 100 or y > 600:
                y -= 2 * dl / abs(dl) * (50 + abs(dl))
            massiv = massiv + [[int(x), int(y)]]
        if x < 9 * Ecrx / 10:
            massiv = massiv + [[int(9 * Ecrx / 10), int(y)]]
        self.Road = massiv

    def draw_road(self):
        """
        дорогу рисует
        :return: нан
        """
        for pos in self.Road:
            pygame.draw.circle(screen, [0, 0, 0], pos, 12)
        pygame.draw.lines(screen, [0, 0, 0], False, self.Road, 24)
        for pos in self.Road:
            pygame.draw.circle(screen, [200, 100, 0], pos, 10)
        pygame.draw.lines(screen, [200, 100, 0], False, self.Road, 20)

    def generare_buildings(self, r):
        min_x, min_y, max_x, max_y = 1000, 1000, 0, 0
        road = [[-100, -100]]
        buildings = [[-100, -100]]
        for pos in self.Road:
            min_x = min(min_x, pos[0])
            max_x = max(max_x, pos[0])
            min_y = min(min_y, pos[1])
            max_y = max(max_y, pos[1])
        x = min_x
        y = min_y - r
        if y < 100:
            y = 100
        for i in range(len(self.Road) - 1):
            t = 0.0
            while t < 1:
                road += [[int((self.Road[i][0] * t + self.Road[i + 1][0] * (1 - t))), int(
                    (self.Road[i][1] * t + self.Road[i + 1][1] * (1 - t)))]]
                t += 0.251
        for deltay in range(0, 300, 10):
            for tck in road:
                for lol in [-1, 1]:
                    x = tck[0]
                    y = tck[1] + lol*deltay
                    if y < min_y - 2*r or y > max_y + 2*r:
                        continue
                    zanyato = False
                    for coord in road:
                        if (coord[0] - x) ** 2 + (coord[1] - y) ** 2 < (r + 13) ** 2:
                            zanyato = True
                    for coord in buildings:
                        if (coord[0] - x) ** 2 + (coord[1] - y) ** 2 < 4 * r * r:
                            zanyato = True
                    if not zanyato:
                        buildings += [[x, y]]
        self.Buildings = buildings

    def draw_buildings(self, r):
        for coor in self.Buildings:
            pygame.draw.circle(screen, [51, 35, 18], [coor[0], coor[1]], r)
