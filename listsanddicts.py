# Write your code here :-)

import pygame
from pygame.locals import *
from time import sleep

BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
WHITE = [255,255,255]
YELLOW = [255,255,0]
GRAY = [127,127,127]
MAGENTA = [255,0,255]
CYAN = [0,255,255]

key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE, K_w:WHITE, K_y:YELLOW, K_l:GRAY, K_m:MAGENTA, K_c:CYAN}

pygame.init()
screen = pygame.display.set_mode([500,500])

#start game loop
running = True

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
                screen.fill(background)

    pygame.display.update()
    sleep(.01)

