import os
import pygame
import random

startpoint = (0, 0)


class enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        im = load_image("enemy.png", -1)
        self.image = pygame.transform.scale(im, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = startpoint

        self.hp = 10
        self.points = 1

    def process(self):
        if self.hp <= 0:
            player.score += self.points
            self.kill()
