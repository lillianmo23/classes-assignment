import pygame
from pygame.draw import *
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from random import randint

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


class SuperApple:

    sup_app_img = pygame.image.load("super_apple.png")

    def __init__(self, x: int, y: int, dx: int, dy: int) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def transform_apples(image, x:int, y:int):
        scaled = pygame.transform.scale(image, x, y)
        x_factor = round(50/x, 2)
        y_factor = round(50/y, 2)
        return scaled, x_factor, y_factor

    apple_width = randint(10, 100)
    apple_height = randint(10, 100)

apple_draw = SuperApple()

health = 20
running = True
while health>0:
    running = True

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
    screen.blit(SuperApple()) 

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()