import pygame, sys

mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500), 0, 32)

img = pygame.image.load('pic.png').convert()

offset = [0, 0]

clicking = False
right_clicking = False
middle_click = False

while True:

    # фон
    screen.fill((0, 0, 0))

    mx, my = pygame.mouse.get_pos()

    rot = 0
    loc = [mx, my]
    if clicking:
        rot = 0
    if right_clicking:
        rot = 0
    if middle_click:
        rot = 0
    screen.blit(pygame.transform.rotate(img, rot), (loc[0] + offset[0], loc[1] + offset[1]))

    # кнопки
    right_clicking = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
            if event.button == 3:
                right_clicking = True
            if event.button == 2:
                middle_click = not middle_click
            if event.button == 4:
                offset[1] -= 10
            if event.button == 5:
                offset[1] += 10
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)
