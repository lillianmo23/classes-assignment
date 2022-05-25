# created by Ashley Leung, April 11, 2022

# a simplified version of fruit ninja, click the fruits to increase your score!
# fruits will relocate randomly when clicked.

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from fruits_functions import *
from fruits_classes import *
from ashley_fruit_ninja import *


def main():
    # initialize pygame
    pygame.init()
    pygame.display.set_caption("Click the fruits to increase your score! Click the same fruit 3 times to kill it! Esc to end game.")

    afn_main = AshleyFruitNinja(720, 480)

    screen = pygame.display.set_mode((afn_main.get_screen_width(), afn_main.get_screen_height()))
    clock = pygame.time.Clock()

    # ---------------------------
    # Initialize global variables

    MAX_APPLES = 3
    MAX_BANANAS = 5
    
    apples = []
    bananas = []

    init_fruits(screen, MAX_APPLES, apples, Apple)
    init_fruits(screen, MAX_BANANAS, bananas, Banana)

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
                score_apple = 0
                score_banana = 0

                # GAME STATE UPDATES
                # Increase score when apples and bananas are clicked
                # Randomize apple and banana positions when clicked
                
                click_apple, score_apple = click_fruits(screen, apples, point)
                afn_main.set_total_score(score_apple)
                
                click_banana, score_banana = click_fruits(screen, bananas, point)
                afn_main.set_total_score(score_banana)

                # Display score and confirmation when fruits are clicked
                if click_apple and click_banana: 
                    pygame.display.set_caption(f"Your score: {afn_main.get_total_score()}, you got both! Nice punch!")
                elif click_apple:
                    pygame.display.set_caption(f"Your score: {afn_main.get_total_score()}, bright and shiny!")
                elif click_banana:
                    pygame.display.set_caption(f"Your score: {afn_main.get_total_score()}, that's bananas!")

        # DRAWING
        screen.fill((255, 255, 255))  # always the first drawing command

        display_fruits(screen, apples)
        display_fruits(screen, bananas)

        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(30)
        #---------------------------

    pygame.quit()


if __name__ == "__main__":
    main()