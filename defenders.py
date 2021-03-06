import pygame
from Map import screen


class Defender(pygame.sprite.Sprite):
    def __init__(self, screen, coord):
        """
        initialisation
        :param screen: where to draw defender
        :param coord: defender's coordinates
        """
        pygame.sprite.Sprite.__init__(self)
        defender_image = pygame.image.load('defender_image.png')
        self.image = pygame.transform.scale(defender_image, (25, 25))
        self.reach_radius = 100
        self.rect = self.image.get_rect(center=coord)
        self.coordinates = coord
        self.screen = screen
        self.damage = 1

    def draw(self, game):
        """
        draws the defender in the place of mouse click
        """
        self.screen.blit(self.image, self.rect)

    def shoot(self, enemy):
        """
        makes defenders shoot at enemies
        """
        if (self.coordinates[0] - enemy.rect.x) ** 2 + (self.coordinates[1] - enemy.rect.y) ** 2 \
                < self.reach_radius ** 2:
            pygame.draw.line(screen, (0, 0, 0), (self.coordinates[0], self.coordinates[1]),
                             (enemy.rect.x + 25, enemy.rect.y + 25), 2)
            enemy.hp -= self.damage

    def change(self):
        """
        makes defender stronger
        """
        self.image = pygame.transform.scale(pygame.image.load('strong_defender_image.png'), (25, 25))
        self.damage = 2
