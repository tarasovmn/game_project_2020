import pygame
from Map import Karta
# import defenders as defen
import enemies as enem

pygame.init()

FPS = 30
Ecrx = 1200
Ecry = 720
screen = pygame.display.set_mode((Ecrx, Ecry))
screen.fill((100, 200, 0))


# Эта функция должна быть не здесь, но пока так
def draw_tower(x, y, r):
    r = int(r)
    pygame.draw.rect(screen, [100, 100, 100], [[int(x) - r // 2, int(y) - r // 2], [r, r]])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

Novaya_Karta = Karta()
Novaya_Karta.generate_road()
Novaya_Karta.generare_buildings(30)
Enemies = [[0, 0]]
Towers = [[0, 0]]


while not finished:
    clock.tick(FPS)
    Novaya_Karta.draw_road()
    Novaya_Karta.draw_buildings(30)
    for tower in Towers:
        draw_tower(int(tower[0]), int(tower[1]), 30)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.button == 1) or (event.button == 3):
                cursor_pos = event.pos
                for coord in Novaya_Karta.Buildings:
                    if (coord[0] - cursor_pos[0]) ** 2 + (coord[1] - cursor_pos[1]) ** 2 < 25 * 25:
                        Towers += [coord]
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
