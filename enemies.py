import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, startpoint):
        pygame.sprite.Sprite.__init__(self)
        enemy_image = pygame.image.load('enemy_image.png')
        self.image = pygame.transform.scale(enemy_image, (50, 50))
        self.rect = self.image.get_rect(center=startpoint)
        self.x, self.y = startpoint
        self.vel = 2
        self.corners_passed = 0
        self.motion = [1, 0]  # определяет направление движения

        self.hp = 500
        self.points = 1

    def move(self, massiv):
        self.x += self.vel * self.motion[0]
        self.y += self.vel * self.motion[1]
        self.check_angle(massiv)

    def check_angle(self, massiv):
        if self.motion[0] == 1:
            if self.x >= massiv[self.corners_passed + 1][0]:
                self.x = massiv[self.corners_passed + 1][0]
                next_y = (massiv[self.corners_passed + 2][1] - massiv[self.corners_passed + 1][1]) / abs(
                    (massiv[self.corners_passed + 2][1] - massiv[self.corners_passed + 1][1]))
                self.motion = [0, next_y]
                self.corners_passed += 1
        else:
            if self.motion[1] * self.y > self.motion[1] * massiv[self.corners_passed + 1][1]:
                self.y = massiv[self.corners_passed + 1][1]
                self.motion = [1, 0]
                self.corners_passed += 1

    def check_if_alive(self):
        return self.hp > 0

    def draw(self, screen):
        """
        Функция рисует врага по его текущим координатам
        """
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect)


class StrongEnemy(Enemy):
    def __init__(self, startpoint):
        super().__init__(startpoint)
        self.vel = 3
        strong_enemy_image = pygame.image.load('strong_enemy_image.png')
        self.image = pygame.transform.scale(strong_enemy_image, (50, 50))
        self.rect = self.image.get_rect(center=startpoint)
        self.hp = 1000
        self.points = 2
