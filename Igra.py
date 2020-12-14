import pygame
from Map import Karta
from enemies import Enemy, StrongEnemy
from defenders import Defender

pygame.display.update()
clock = pygame.time.Clock()


class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.init()

        pygame.sprite.Sprite.__init__(self)
        bg = pygame.image.load("bg.png")
        self.bg = pygame.transform.scale(bg, (1200, 720))
        self.FPS = 30
        self.Ecrx = 1200
        self.Ecry = 720
        self.screen = pygame.display.set_mode((self.Ecrx, self.Ecry))
        self.screen.fill((255, 255, 255))
        self.clock = pygame.time.Clock()
        self.count = 0
        self.score = 0
        self.coins = 5

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
            if len(self.Enemies) % 3 == 0:
                self.Enemies.append(StrongEnemy(self.Novaya_Karta.Road[0]))
            else:
                self.Enemies.append(Enemy(self.Novaya_Karta.Road[0]))
            self.count = 0
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    cursor_pos = event.pos
                    for tower in self.Towers:
                        if (tower.coordinates[0] - cursor_pos[0]) ** 2 + (
                                tower.coordinates[1] - cursor_pos[1]) ** 2 < 15 * 15:
                            if self.coins >= 1:
                                tower.change()
                                self.coins -= 1
                    for coord in self.Novaya_Karta.Buildings:
                        if (coord[0] - cursor_pos[0]) ** 2 + (coord[1] - cursor_pos[1]) ** 2 < 15 * 15:
                            if self.coins >= 1:
                                self.Towers += [Defender(self.screen, coord)]
                                self.Novaya_Karta.Buildings.remove(coord)
                                self.coins -= 1
            if event.type == pygame.QUIT:
                self.finished = True

    def check_dead_enemies(self):
        new_enemies = []
        for enemy in self.Enemies:
            if enemy.check_if_alive():
                new_enemies.append(enemy)
            else:
                self.score += enemy.points
                self.coins += enemy.coins
        self.Enemies = new_enemies

    def obnovleniye_ecrana(self):
        """
        draws all existing objects
        :return:
        """
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.bg, (0, 0))
        self.Novaya_Karta.draw_road()
        self.Novaya_Karta.draw_buildings()
        self.check_dead_enemies()

        score = str(self.score)
        f1 = pygame.font.Font(None, 40)
        text_score = f1.render('score: ' + score, 0, (255, 0, 191))
        self.screen.blit(text_score, (5, 5))

        coins = str(self.coins)
        f2 = pygame.font.Font(None, 40)
        text_coins = f2.render('coins: ' + coins, 0, (255, 0, 191))
        self.screen.blit(text_coins, (5, 30))

        for tower in self.Towers:
            tower.draw(self)
        for enemy in self.Enemies:
            enemy.time += 1
            enemy.sprite_update()
            enemy.move(self.Novaya_Karta.Road)
            enemy.draw(self.screen)
            for tower in self.Towers:
                tower.shoot(enemy)
        pygame.display.update()
