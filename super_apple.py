import pygame
from pygame.draw import *
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

class basic_fruit:
    def __init__(self, x: int, y:int, dx:int, dy:int) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

super_apple_img = pygame.image.load("super_apple.png")
print(super_apple_img)

fruits = [
    basic_fruit(20, 20, 50, 50)
]

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
    screen.fill((255, 255, 255))  # always the first drawing command

    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), 30)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()