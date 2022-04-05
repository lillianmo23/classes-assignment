from types import DynamicClassAttribute
import pygame
from pygame.draw import *

class basic_fruit:
    def __init__(self, x: int, y:int, dx:int, dy:int) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy