import os
import pygame
import random

startpoint = (0, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        enemy_image = pygame.image.load('enemy_image.png')
        self.image = pygame.transform.scale(enemy_image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = startpoint

        self.hp = 10
        self.points = 1

    def draw(self):
        """
        This function draws the defender in the place of mouse click
        """
        self.image(self.rect.x, self.rect.y)

