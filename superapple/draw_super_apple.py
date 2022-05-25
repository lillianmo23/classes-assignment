import pygame
from random import randint
from math import sqrt

sup_app_img = pygame.image.load("super_apple.png")
sup_app_img_rect = sup_app_img.get_rect()

#class for the inside of the apple
class InnerApple:
    def __init__(self, x, y, factor) -> None:
        self.x = x
        self.y = y
        self.factor = factor

#the main class for the entire super apple
class SuperApple:

    def __init__(self, x, y, colour, radius, image) -> None:
        self.x = x
        self.y = y
        self.colour = colour
        self.radius = radius
        self.factor = 0.01
        self.image = pygame.transform.scale(image, (self.factor, self.factor))
    
    def draw_it(self, surface:pygame.Surface) -> None:
        """draws the super apple

        Args:
            surface (Surface): the surface of the image
        """
        surface.blit(self.image, (self.x, self.y))
        pygame.draw.circle(surface, self.colour, (self.x, self.y), self.radius)

    def grow(self, amount:int) -> None:
        """makes the super apple bigger

        Args:
            amount (int): the amount to grow the super apple by
        """
        self.radius += amount
        scale = 0

    def shrink(self, amount:int) -> None:
        """makes the super apple smaller

        Args:
            amount (int): the amount to shrink the super apply by
        """
        self.radius -= amount
    
    def distance(self, point:int) -> None:
        global click_dist
        click_dist = sqrt((point[0]-self.x)^2+(point[2]-self.y)^2)


    @staticmethod
    def get() -> object:
        """generates a random super apple

        Returns:
            SuperApple (object): a super apple with randomly generated location and size
        """
        return SuperApple(randint(80, 480), randint(80, 380), (0, 0, 255), randint(0, 100), sup_app_img)


