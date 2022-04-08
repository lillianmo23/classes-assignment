import pygame
from pygame.draw import *
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from random import randint
from draw_super_apple import SuperApple, super_apple

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

apples = [super_apple()]
sup_app_img = pygame.image.load("super_apple.png")

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
    time += 1
    if time%120 == 0:
        apples.append(super_apple())
    
    for apple in apples:
        SuperApple.draw_it(self, screen)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()