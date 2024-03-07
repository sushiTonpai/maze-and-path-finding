import sys

from constants import *
import random

import pygame


pygame.init()
screen = pygame.display.set_mode((WIDTH,WIDTH))
while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
