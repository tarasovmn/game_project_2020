import pygame
import os
from enemies import Enemy


class Defender(pygame.sprite.Sprite):
    def __init__(self, screen, coord):
        pygame.sprite.Sprite.__init__(self)
        defender_image = pygame.image.load('defender_image.png')
        self.image = pygame.transform.scale(defender_image, (25, 25))
        self.reach_radius = 70
        self.rect = self.image.get_rect(center=coord)
        self.coordinates = coord
        self.screen = screen

    def draw(self):
        """
        This function draws the defender in the place of mouse click
        """
        self.screen.blit(self.image, self.rect)

    def shoot(self, enemy):
        """
        This function is responsible for making defenders shoot at enemies
        """
        if (self.coordinates[0] - enemy.rect.x) ** 2 + (self.coordinates[1] - enemy.rect.y) ** 2 \
                < self.reach_radius ** 2:
            enemy.hp -= 1
