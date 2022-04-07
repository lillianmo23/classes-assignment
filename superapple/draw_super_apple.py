import pygame
from random import randint

class SuperApple:
    def __init__(self, dx:int, dy:int) -> None:
        self.dx = dx
        self.dy = dy


    def draw_super_apple(self, surface):
        pygame.draw.circle(surface)
        pass  

class SuperAppleImg:
    def __init__(self, x: int, y:int, dx:int, dy:int) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    
    def super_apple_draw():
        pass