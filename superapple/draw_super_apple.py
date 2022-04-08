import pygame
from random import randint

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
class SuperApple:

    sup_app_img = pygame.image.load("super_apple.png")
    sup_app_img_rect = sup_app_img.get_rect()

    def __init__(self, x: int, y: int, colour:pygame.Color, radius, factor) -> None:
        self.x = x
        self.y = y
        self.colour = colour
        self.radius = radius
        self.factor = factor
    
    def transform_apples(self, image):
        global scaled, scaled_rect
        scaled = pygame.transform.scale(image, self.factor, self.factor/10)
        scaled_rect = scaled.get_rect()
        return scaled
    
    def draw_it(self, surface):
        screen.blit(scaled, (self.x, self.y))
        pygame.draw.circle(surface, self.colour, (self.x, self.y), self.radius)
    
def super_apple():
    return SuperApple(randint(80, 580), randint(80, 380), (255, 0, 0), randint(50, 100), randint(0, 4))


