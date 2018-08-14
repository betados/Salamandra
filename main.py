# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
from salamandra import Salamandra

#
# def draw(screen, snake, food):
#     # screen.blit(pygame.Surface(screen.get_size()), (0, 0))
#     pygame.draw.rect(screen, RED, Rect(food, (2 * RAD, 2 * RAD)))
#     for ring in snake["rings"]:
#         pygame.draw.circle(screen, GREEN, (ring[0] + RAD, ring[1] + RAD), RAD)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))

salamandra = Salamandra(screen)

key_pressed = None

while True:

    clock.tick(60)
    # print(clock.get_time())
    screen.fill((0, 0, 0))
    salamandra.draw(pygame.mouse.get_pos(), clock.get_time())

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)
            # if event.type == KEYUP:
            #     key_pressed = None

    pygame.display.flip()
