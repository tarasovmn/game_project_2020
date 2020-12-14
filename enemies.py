import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, startpoint):
        """
        initialisation
        :param startpoint: enemies start from this point
        """
        self.time = 0
        pygame.sprite.Sprite.__init__(self)
        self.enemy_sprites = [pygame.image.load('0.gif'), pygame.image.load('1.gif'),
                              pygame.image.load('2.gif'), pygame.image.load('3.gif'),
                              pygame.image.load('4.gif'), pygame.image.load('5.gif'),
                              pygame.image.load('6.gif'), pygame.image.load('7.gif'),
                              pygame.image.load('8.gif'), pygame.image.load('9.gif')]
        self.enemy_sprites_rect = []
        for i in range(0, len(self.enemy_sprites)):
            self.enemy_sprites[i] = pygame.transform.scale(self.enemy_sprites[i], (50, 50))
            self.enemy_sprites_rect.append(self.enemy_sprites[i].get_rect(center=startpoint))
        self.k = 0  # number of sprite in the array
        self.x, self.y = startpoint
        self.vel = 2
        self.corners_passed = 0
        self.motion = [1, 0]  # defines direction of movement
        self.image = self.enemy_sprites[0]
        self.rect = self.enemy_sprites_rect[0]

        start_hp = 500
        self.hp = start_hp
        self.points = 1
        self.coins = 1
        self.hp_per_pix = start_hp / 50

    def sprite_update(self):
        """
        makes enemies change their appearance
        :return:
        """
        self.k = (self.time // 2) % 10  # /2 чтобы каждые два кадра
        self.image = self.enemy_sprites[self.k]
        self.rect = self.enemy_sprites_rect[self.k]

    def move(self, massiv):
        """
        makes enemies go
        :param massiv:
        :return:
        """
        self.x += self.vel * self.motion[0]
        self.y += self.vel * self.motion[1]
        self.check_angle(massiv)

    def check_angle(self, massiv):
        """
        makes enemies go on the road
        :param massiv:
        :return:
        """
        if self.corners_passed == len(massiv) - 1:
            pass
        else:
            if self.motion[0] == 1:
                if self.x >= massiv[self.corners_passed + 1][0]:
                    self.x = massiv[self.corners_passed + 1][0]
                    distance = massiv[self.corners_passed + 2][1] - massiv[self.corners_passed + 1][1]
                    next_y = 1
                    if distance != 0:
                        next_y = distance / abs(distance)
                    self.motion = [0, next_y]
                    self.corners_passed += 1
            else:
                if self.motion[1] * self.y > self.motion[1] * massiv[self.corners_passed + 1][1]:
                    self.y = massiv[self.corners_passed + 1][1]
                    self.motion = [1, 0]
                    self.corners_passed += 1

    def check_if_alive(self):
        """
        checks if enemy is alive
        :return: enemy's hp
        """
        return self.hp > 0

    def draw(self, screen):
        """
        draws enemy in it's current coordinates
        :param screen: where to draw enemies
        :return:
        """
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect)
        pygame.draw.line(screen, (0, 0, 0), (self.x - 25, self.y + 30),
                         (self.x - 25 + self.hp / self.hp_per_pix, self.y + 30), 3)


class StrongEnemy(Enemy):
    def __init__(self, startpoint):
        super().__init__(startpoint)
        self.vel = 3

        self.strongenemy_sprites = [pygame.image.load('0 (2).gif'), pygame.image.load('1 (2).gif'),
                                    pygame.image.load('2 (2).gif'), pygame.image.load('3 (2).gif'),
                                    pygame.image.load('4 (2).gif'), pygame.image.load('5 (2).gif'),
                                    pygame.image.load('6 (2).gif'), pygame.image.load('7 (2).gif'),
                                    pygame.image.load('8 (2).gif'), pygame.image.load('9 (2).gif')]
        self.strongenemy_sprites_rect = []
        for i in range(0, len(self.strongenemy_sprites)):
            self.strongenemy_sprites[i] = pygame.transform.scale(self.strongenemy_sprites[i], (50, 50))
            self.strongenemy_sprites_rect.append(self.strongenemy_sprites[i].get_rect(center=startpoint))
        self.k = 0  # номер спрайта в массиве

        self.image = self.strongenemy_sprites[0]
        self.rect = self.strongenemy_sprites_rect[0]

        start_hp = 800
        self.hp = start_hp
        self.points = 3
        self.coins = 2

    def sprite_update(self):
        self.k = (self.time // 2) % 10
        self.image = self.strongenemy_sprites[self.k]
        self.rect = self.strongenemy_sprites_rect[self.k]
