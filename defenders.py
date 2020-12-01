import pygame
import os
from enemies import *


class Defender(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        defender_image = pygame.image.load('defender_image.png')
        self.image = pygame.transform.scale(defender_image, (10, 10))
        global reach_radius
        reach_radius = 70

    def defender_draw(self):
        """
        This function draws the defender in the place of mouse click
        """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.rect.x, self.rect.y = event.pos
                self.image(event.pos)

    def defender_shoot(self):
        """
        This function is responsible for making defenders shoot at enemies
        """
        if (self.rect.x - enemy.rect.x) ** 2 + (self.rect.y - enemy.rect.y) ** 2 \
                < reach_radius ** 2:
            enemy.hp -= 1
