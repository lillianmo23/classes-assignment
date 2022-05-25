import pygame
from pygame.draw import *
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from random import randint
from draw_super_apple import SuperApple

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#makes a list for the super apples
apples = [SuperApple.get()]

running = True
time = 0
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill((255, 255, 255)) # always the first drawing command

    #adds a new super apple every 3 seconds
    time += 1
    if time%120 == 0:
        apples.append(SuperApple.get())
    
    for apple in apples:
        apple.draw_it(screen)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()