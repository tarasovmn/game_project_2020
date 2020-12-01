import pygame
from Igra import Game


pygame.init()

FPS = 30
Ecrx = 1200
Ecry = 720
screen = pygame.display.set_mode((Ecrx, Ecry))
screen.fill((100, 200, 0))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

New_Game = Game()


while not New_Game.finished:
    New_Game.shag_Igry()
pygame.quit()
