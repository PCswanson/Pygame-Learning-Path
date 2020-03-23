# First PyGame program

# Import the PyGame library

import random
import pygame
pygame.init()

# choose random numbers to control initial movement
dx = random.randint(10,40)
dy = random.randint(5,20)

#set initial position of ball
ballx = 250
bally = 250

# set screen size
screenx = 500
screeny = 500

# Set up the drawing window
screen = pygame.display.set_mode([screenx,screeny])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the background screen with white
    screen.fill((255,255,255))


    # Draw a solid blue circle in the center of the screen
    pygame.draw.circle(screen, (0,0,255), (ballx, bally), 10)

    ballx = ballx + dx
    if ballx >= screenx:
        dx = dx*(-1)
        ballx = screenx - 5
    elif ballx <= 0:
        dx = dx*(-1)
        ballx = 5

    bally = bally + dy
    if bally >= screeny:
        dy = dy*(-1)
        bally = screeny - 5
    elif bally <=0:
        dy = dy*(-1)
        bally = 5

    #Flip the display
    pygame.display.flip()


# Done! Time to quit!
pygame.quit()

