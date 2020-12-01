import pygame
import PIL
from PIL import Image


class Defender(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        defender_image = Image.open('defender_image.png')
        self.image = pygame.transform.scale(defender_image, ())


    def defender_shoot(self):
        """This function is responsible for making defenders shoot at enemies"""
        pass # TODO - not done yet