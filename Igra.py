import pygame
from Map import Karta
from enemies import Enemy
from defenders import Defender

pygame.display.update()
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        pygame.init()

        self.FPS = 30
        self.Ecrx = 1200
        self.Ecry = 720
        self.screen = pygame.display.set_mode((self.Ecrx, self.Ecry))
        self.screen.fill((33, 7, 56))
        self.clock = pygame.time.Clock()
        self.count = 0

        self.Novaya_Karta = Karta(self.screen, 20)
        self.Novaya_Karta.generate_road()
        self.Novaya_Karta.generate_frame()
        self.Novaya_Karta.generate_buildings()
        self.Novaya_Karta.generate_environment()
        self.Enemies = []
        self.Enemies.append(Enemy(self.Novaya_Karta.Road[0]))
        self.Towers = []
        self.finished = False

    def shag_igry(self):
        """
        makes all calculations
        :return: NONE
        """
        self.count += 1
        clock.tick(self.FPS)
        if self.count / self.FPS == 2:
            self.Enemies.append(Enemy(self.Novaya_Karta.Road[0]))
            self.count = 0
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 1) or (event.button == 3):
                    cursor_pos = event.pos
                    for coord in self.Novaya_Karta.Buildings:
                        if (coord[0] - cursor_pos[0]) ** 2 + (coord[1] - cursor_pos[1]) ** 2 < 15 * 15:
                            self.Towers += [Defender(self.screen, coord)]
            if event.type == pygame.QUIT:
                self.finished = True

    def check_dead_enemies(self):
        new_enemies = []
        for enemy in self.Enemies:
            enemy.check_if_alive()
            if enemy.is_alive:
                new_enemies.append(enemy)
        self.Enemies = new_enemies

    def obnovleniye_ecrana(self):
        """
        draws all existing objects
        :return:
        """
        self.screen.fill((33, 7, 56))
        self.Novaya_Karta.draw_road()
        self.Novaya_Karta.draw_buildings()
        self.check_dead_enemies()
        for enemy in self.Enemies:
            enemy.move(self.Novaya_Karta.Road)
            enemy.draw(self.screen)
            for tower in self.Towers:
                tower.shoot(enemy)
        for tower in self.Towers:
            tower.draw()
        pygame.display.update()
