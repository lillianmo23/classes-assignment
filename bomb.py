import pygame
from random import randint
from math import sqrt

class Bomb:
    def __init__(self, x, y):
        self.colour = (0, 0, 0)
        self.x = x
        self.y = y
        self.radius = 25
        self.growth = 1

    def draw(self, surface):
        """Draws the circle on the screen and the circle's location"""
        pygame.draw.circle(surface, self.colour, (self.x, self.y), self.radius)

    def click_distance(self, location):
        """Finds the distance between a mouse click and the centre of the circle
        
        Returns:
            The distance between the mouse click and centre of the circle
        """
        x = abs(self.x - location[0])
        y = abs(self.y - location[1])
        return sqrt(x*x + y*y)

def generate_bomb():
    """Generates a bomb at a random location
    
    Returns:
        Random bomb"""
    return Bomb(randint(30, 610), randint(30, 450))