import pygame
from pygame.draw import *

class basic_fruit:
    def __init__(self, x: int, y:int, dx:int, dy:int) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

fruits = [
    basic_fruit(20, 20, 50, 50)
]

health = 20
while health>0:
    pass
