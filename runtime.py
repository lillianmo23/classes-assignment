import pygame
from bomb import *
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

hitboxes = []
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
            for hitbox in hitboxes:
                if hitbox.click_distance(event.pos) <= hitbox.radius:
                    hitboxes.remove(hitbox)
                    if type(hitbox) == Bomb:
                        running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    frame += 1
    if frame%90 == 0:
        hitboxes.append(generate_bomb())
    for hitbox in hitboxes:
        if hitbox.radius >= 60:
            hitbox.growth = -1
        hitbox.radius += hitbox.growth

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    for hitbox in hitboxes:
        hitbox.draw(screen)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()