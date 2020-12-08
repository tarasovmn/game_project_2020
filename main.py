import pygame
from Igra import Game

New_Game = Game()

while not New_Game.finished:
    New_Game.shag_igry()
    New_Game.obnovleniye_ecrana()
pygame.quit()
