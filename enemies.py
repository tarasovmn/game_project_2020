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
        self.is_alive = True

        self.hp = 50
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
        if self.hp <= 0:
            self.is_alive = False

    def draw(self, screen):
        """
        Функция рисует врага по его текущим координатам
        """
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect)
