import pygame
from random import randint

# screen params
pygame.init()
FPS = 30
Ecrx = 1200
Ecry = 720
screen = pygame.display.set_mode((Ecrx, Ecry))
screen.fill((255, 255, 255))


class Karta:
    def __init__(self, screen, r):
        """
        initialisation
        :param screen:
        :param r:
        """
        self.r = r
        self.screen = screen
        self.FPS = 30
        self.Ecrx = 1200
        self.Ecry = 720
        self.Road = []
        self.Buildings = []
        self.min_x, self.min_y, self.max_x, self.max_y = 1000, 1000, 0, 0
        self.road = [[-1000, -100]]
        self.decor = [[-1000, -100]]
        self.tower_image = pygame.transform.scale(pygame.image.load('tower_image.png'), (6 * self.r, 6 * self.r))
        self.decor_image = pygame.transform.scale(pygame.image.load('decor_image.png'), (3 * self.r, 6 * self.r))

    def generate_road(self):
        """
        generates array of points useful for drawing road on them
        :return: array of points
        """
        x = self.Ecrx / 10
        y = self.Ecry / 2
        shag = 0
        massiv = [[int(x), int(y)]]
        while x < 8 * self.Ecrx / 10 - 50:
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
        draws the road
        :return: нан
        """
        for pos in self.Road:
            pygame.draw.circle(screen, [255, 0, 191], pos, 12)
        pygame.draw.lines(screen, [255, 0, 191], False, self.Road, self.r + 4)
        for pos in self.Road:
            pygame.draw.circle(screen, [255, 255, 255], pos, 10)
        pygame.draw.lines(screen, [255, 255, 255], False, self.Road, self.r)

    def generate_frame(self):
        """
        TODO
        :return:
        """
        for pos in self.Road:
            self.min_x = min(self.min_x, pos[0])
            self.max_x = max(self.max_x, pos[0])
            self.min_y = min(self.min_y, pos[1])
            self.max_y = max(self.max_y, pos[1])
        for i in range(len(self.Road) - 1):
            t = 0.0
            while t < 1:
                self.road += [[int((self.Road[i][0] * t + self.Road[i + 1][0] * (1 - t))), int(
                    (self.Road[i][1] * t + self.Road[i + 1][1] * (1 - t)))]]
                t += 0.251

    def generate_buildings(self):
        """
        generate places for defenders
        :return:
        """
        buildings = [[-100, -100]]
        for deltay in range(0, 100, 10):
            for tck in self.road:
                for lol in [-1, 1]:
                    x = tck[0]
                    y = tck[1] + lol * deltay
                    if y < self.min_y - 2 * self.r or y > self.max_y + 2 * self.r:
                        continue
                    zanyato = False
                    for coord in self.road:
                        if (coord[0] - x) ** 2 + (coord[1] - y) ** 2 < (self.r + 13) ** 2:
                            zanyato = True
                    for coord in buildings:
                        if (coord[0] - x) ** 2 + (coord[1] - y) ** 2 < 4 * self.r * self.r:
                            zanyato = True
                    if not zanyato:
                        buildings += [[x, y]]
        self.Buildings = buildings

    def generate_environment(self):
        """
        creates decorations
        :return:
        """
        mega_buildings = [[-100, -100]]
        for delay in range(0, 600, 10):
            for tsk in self.road:
                for kek in [-1, 1]:
                    x = tsk[0]
                    y = tsk[1] + kek * delay
                    if y < self.min_y - 2 * self.r or y > self.max_y + 2 * self.r:
                        continue
                    zanyat = False
                    for coord1 in self.road:
                        if (coord1[0] - x) ** 2 + (coord1[1] - y) ** 2 < (5 * self.r + 13) ** 2:
                            zanyat = True
                    for coord1 in mega_buildings:
                        if (coord1[0] - x) ** 2 + (coord1[1] - y) ** 2 < 100 * self.r * self.r:
                            zanyat = True
                    for coord1 in self.Buildings:
                        if (coord1[0] - x) ** 2 + (coord1[1] - y) ** 2 < 25 * self.r * self.r:
                            zanyat = True
                    if not zanyat:
                        mega_buildings += [[x, y]]
        self.decor = mega_buildings

    def draw_buildings(self):
        """
        draws empty places for defenders and decorations
        :return:
        """
        self.screen.blit(self.tower_image,
                         [self.Road[len(self.Road) - 1][0], self.Road[len(self.Road) - 1][1] - 3 * self.r])
        print(self.Road[len(self.Road) - 1][0], self.Road[len(self.Road) - 1][1] - 3 * self.r)
        for coord in self.Buildings:
            pygame.draw.circle(screen, [255, 0, 191], [coord[0], coord[1]], self.r)
        for coord in self.decor:
            self.screen.blit(self.decor_image, [coord[0] - 2 * self.r, coord[1] - 2 * self.r])
