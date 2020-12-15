import pygame
from Igra import Game

New_Game = Game()

pygame.mixer.music.load('veya.mp3')
pygame.mixer.music.play(-1)

while not New_Game.finished:
    New_Game.shag_igry()
    New_Game.obnovleniye_ecrana()
pygame.quit()
