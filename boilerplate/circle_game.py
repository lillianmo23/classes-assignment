# pygame template

import pygame
from shapes import Circle, generate_circle
from random import randint
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circles = [generate_circle()]
frame = 0

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            for circle in circles:
                if circle.click_distance(event.pos) <= circle.radius:
                    circles.remove(circle)
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    frame += 1
    if frame%60 == 0:
        circles.append(generate_circle())
        for circle in circles:
            if circle.size <= 0:
                circles.remove(circle)
    for circle in circles:
        if circle.radius >= 60:
            circle.growth = -1
        circle.radius += circle.growth
    
    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    for circle in circles:
        circle.draw(screen)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()
