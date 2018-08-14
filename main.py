# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
from salamandra import Salamandra

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
