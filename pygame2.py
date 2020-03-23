# Write your code here :-)
# First PyGame program

# Import the PyGame library
import random

import pygame
pygame.init()

dx = random.randint(10,40)
dy = random.randint(5,20)
print(dx)
print(dy)
x=250
y=250
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
    pygame.draw.circle(screen, (0,0,255), (x,y), 10)

    #Flip the display
    pygame.display.flip()

    x = x+dx
    if x >= screenx:
        dx = dx*(-1)
        x = screenx - 5
    if x <= 0:
        dx = dx*(-1)
        x = 5

    y = y+dy
    if y >= screeny:
        dy = dy*(-1)
        y = screeny - 5
    if y <= 0:
        dy = dy*(-1)
        y = 5

    print(x)
    print(y)
    print("  ")
# Done! Time to quit!
pygame.quit()
