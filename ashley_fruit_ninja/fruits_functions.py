from typing import Any, List
import pygame
from fruits_classes import *

# ---------------------------
# Functions can be called by other groupmates

def init_fruits(screen: pygame.Surface, max_fruits: int, fruits: List, fruit_class) -> None:
    """Adds fruit objects to lists to display on screen.
    
    Args:
        screen: A surface object, the game's screen
        max_fruits: Maximum number of that particular fruit
        fruits: List of fruit objects
        fruit_class: Class of that particular fruit

    Returns: None
    """
    for i in range(max_fruits):
        fruits.append(fruit_class(screen)) 


def click_fruits(screen: pygame.Surface, fruits: List, point: Any):
    """If fruit is clicked, it randomizes new position for fruit and adds score

    Args:
        screen: A surface object, the game's screen
        fruits: List of fruit objects
        point: Point clicked on screen

    Returns:
        bool: True if fruit is clicked, False if not
        int: The score to be added to the total score
    """
    clicked = False
    score = 0

    for i in range(len(fruits)):
        if fruits[i].collidepoint(point):
            fruits[i].set_random_point(screen)
            score += fruits[i].get_score()
            clicked = True
            break
    
    return clicked, score


def display_fruits(screen: pygame.Surface, fruits: List) -> None:
    """Displays the fruits on screen.

    Args:
        screen: A surface object, the game's screen
        fruits: List of fruit objects

    Returns: None
    """
    for i in range(len(fruits)):
            fruits[i].display(screen) 
