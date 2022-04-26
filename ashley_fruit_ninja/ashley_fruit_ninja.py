# created by Ashley Leung, April 11, 2022

# a simplified version of fruit ninja, click the fruits to increase your score!
# fruits will relocate randomly when clicked.

from typing import Any, List
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from fruits import *

# ---------------------------
# Functions can be called by other groupmates

def init_fruits(screen: pygame.Surface, max_apples: int, max_bananas: int, apples: List, bananas: List) -> None:
    # create a list of apples to display on screen
    for i in range(max_apples):
        apples.append(Apple(screen)) 

    # create a list of bananas to display on screen
    for i in range(max_bananas):
        bananas.append(Banana(screen))


def click_fruits(screen: pygame.Surface, max_fruits: int, fruits: List, point: Any):
    clicked = False
    score = 0

    for i in range(max_fruits):
        if fruits[i].collidepoint(point):
            fruits[i].set_random_point(screen)
            score += fruits[i].get_score()
            clicked = True
            break
    
    return clicked, score


def display_fruits(screen: pygame.Surface, max_fruits: int, fruits: List) -> None:
    for i in range(max_fruits):
            fruits[i].display(screen) 


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
    total_score = 0

    MAX_APPLES = 3
    MAX_BANANAS = 5
    
    apples = []
    bananas = []

    init_fruits(screen, MAX_APPLES, MAX_BANANAS, apples, bananas)

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
                
                click_apple, score_apple = click_fruits(screen, MAX_APPLES, apples, point)
                total_score += score_apple
                
                click_banana, score_banana = click_fruits(screen, MAX_BANANAS, bananas, point)
                total_score += score_banana

                # Display score and confirmation when fruits are clicked
                if click_apple and click_banana: 
                    pygame.display.set_caption(f"Your score: {total_score}, you got both! Nice punch!")
                elif click_apple:
                    pygame.display.set_caption(f"Your score: {total_score}, bright and shiny!")
                elif click_banana:
                    pygame.display.set_caption(f"Your score: {total_score}, that's bananas!")

        # DRAWING
        screen.fill((255, 255, 255))  # always the first drawing command

        display_fruits(screen, MAX_APPLES, apples)
        display_fruits(screen, MAX_BANANAS, bananas)

        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(30)
        #---------------------------

    pygame.quit()


if __name__ == "__main__":
    main()