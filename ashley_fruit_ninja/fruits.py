import pygame
import random


IMAGE_PATH = "image/"

FRUIT_WIDTH = 100
FRUIT_HEIGHT = 100

# CLASSES - Create apple and banana classes

class Fruit(pygame.Rect):
    def __init__(self, filename: str, screen: pygame.Surface) -> None:
        self.width = FRUIT_WIDTH
        self.height = FRUIT_HEIGHT
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.set_random_point(screen)

    def display(self, screen: pygame.Surface) -> None: #defined the screen variable in main.py
        """ Displays the Fruit object's image at a coordinate.

            Returns: None.
        """
        screen.blit(self.image, (self.x, self.y))
    
    def set_random_point(self, screen: pygame.Surface) -> None:
        self.x = random.randrange(0, screen.get_width() - self.width)
        self.y = random.randrange(0, screen.get_height() - self.height)


class Apple(Fruit):
    def __init__(self, screen: pygame.Surface) -> None:
        #this is to set the Fruit class's filename: str to 'apple.png' to load the image.
        super().__init__(IMAGE_PATH + 'apple.png', screen)
    
    def get_score(self):
        return 10


class Banana(Fruit):
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(IMAGE_PATH + 'banana.png', screen)

    def get_score(self):
        return 5
