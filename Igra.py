import pygame
from Map import Karta
from defenders import Defender

# Эта функция должна быть не здесь, но пока так

pygame.display.update()
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        pygame.init()

        self.FPS = 30
        self.Ecrx = 1200
        self.Ecry = 720
        self.screen = pygame.display.set_mode((self.Ecrx, self.Ecry))
        self.screen.fill((100, 200, 0))
        self.clock = pygame.time.Clock()

        self.Novaya_Karta = Karta()
        self.Novaya_Karta.generate_road()
        self.Novaya_Karta.generare_buildings(20)
        self.Enemies = []
        self.Towers = []
        self.finished = False

    def draw_tower(self, x, y, r):
        """ draws tower (rect)"""
        r = int(r)
        pygame.draw.rect(self.screen, [100, 100, 100], [[int(x) - r // 2, int(y) - r // 2], [r, r]])

    def shag_Igry(self):
        """
        makes all calculations
        :return: NONE
        """
        clock.tick(self.FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1) or (event.button == 3):
                    cursor_pos = event.pos
                    for coord in self.Novaya_Karta.Buildings:
                        if (coord[0] - cursor_pos[0]) ** 2 + (coord[1] - cursor_pos[1]) ** 2 < 15 * 15:
                            self.Towers += [Defender(self.screen, coord)]
            if event.type == pygame.QUIT:
                self.finished = True

    def obnovleniye_ecrana(self):
        """
        draws all existing objects
        :return:
        """
        self.Novaya_Karta.draw_road()
        self.Novaya_Karta.draw_buildings(20)
        for tower in self.Towers:
            tower.draw()
        pygame.display.update()