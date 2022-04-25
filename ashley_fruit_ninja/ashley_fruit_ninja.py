# created by Ashley Leung, April 11, 2022

# a simplified version of fruit ninja, click the fruits to increase your score!
# fruits will relocate randomly when clicked.

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from fruits import *

def main():
    # initialize pygame
    pygame.init()
    pygame.display.set_caption("Click the fruits to increase your score! Esc to end game.")

    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    # ---------------------------
    # Initialize global variables

    MAX_APPLES = 3
    MAX_BANANAS = 5

    # create a list of apples to display on screen
    apples = []
    for i in range(MAX_APPLES):
        apples.append(Apple(screen)) 

    # create a list of bananas to display on screen
    bananas = []
    for i in range(MAX_BANANAS):
        bananas.append(Banana(screen))

    score = 0

    # ---------------------------
    # game loop
    running = True
    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                point = event.pos
                click_apple = False
                click_banana = False

                # GAME STATE UPDATES
                # Increase score when apples and bananas are clicked
                # Randomize apple and banana positions when clicked
                for i in range(MAX_APPLES):
                    if apples[i].collidepoint(point):
                        apples[i].set_random_point(screen)
                        score += apples[i].get_score()
                        click_apple = True
                        break

                for i in range(MAX_BANANAS):
                    if bananas[i].collidepoint(point):
                        bananas[i].set_random_point(screen)
                        score += bananas[i].get_score()
                        click_banana = True
                        break

                # Display score and confirmation when fruits are clicked
                if click_apple and click_banana: 
                    pygame.display.set_caption(f"Your score: {score}, you got both! Nice punch!")
                elif click_apple:
                    pygame.display.set_caption(f"Your score: {score}, bright and shiny!")
                elif click_banana:
                    pygame.display.set_caption(f"Your score: {score}, that's bananas!")

        # DRAWING
        screen.fill((255, 255, 255))  # always the first drawing command

        for i in range(MAX_APPLES):
            apples[i].display(screen) 

        for i in range(MAX_BANANAS):
            bananas[i].display(screen)

        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(30)
        #---------------------------

    pygame.quit()


if __name__ == "__main__":
    main()