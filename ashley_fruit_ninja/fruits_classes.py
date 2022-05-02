import pygame
import random


IMAGE_PATH = "image/"

FRUIT_WIDTH = 100
FRUIT_HEIGHT = 100

# CLASSES - Create apple and banana classes
class Lifespan:
    def __init__(self):
        self._default_lifespan = 3
        self.set_lifespan(self._default_lifespan)

    def get_lifespan(self) -> int:
        return self._lifespan
    
    def set_lifespan(self, lifespan: int) -> None:
        self._lifespan = lifespan
    
    def countdown(self):
        self.set_lifespan(self.get_lifespan() - 1)


class Fruit(pygame.Rect):
    def __init__(self, filename: str, screen: pygame.Surface) -> None:
        # cannot make width and height private because they're inherited from pygame.Rect
        self.width = FRUIT_WIDTH 
        self.height = FRUIT_HEIGHT
        self.set_image(filename)
        self.set_random_point(screen)
    
    def get_image(self) -> pygame.Surface:
        return self._image
    
    def set_image(self, filename: str) -> None:
        self._image = pygame.image.load(filename)
        self._image = pygame.transform.scale(self.get_image(), (self.width, self.height))

    def display(self, screen: pygame.Surface) -> None: #defined the screen variable in main.py
        """ Displays the Fruit object's image at a coordinate.

            Returns: None.
        """
        screen.blit(self._image, (self.x, self.y))
    
    def set_random_point(self, screen: pygame.Surface) -> None:
        """ Sets the fruit at a random point on the screen.

            Returns: None
        """
        # cannot make x and y private because they're inherited from pygame.Rect
        self.x = random.randrange(0, screen.get_width() - self.width) 
        self.y = random.randrange(0, screen.get_height() - self.height)


class Apple(Fruit):
    def __init__(self, screen: pygame.Surface) -> None:
        #this is to set the Fruit class's filename: str to 'apple.png' to load the image.
        super().__init__(IMAGE_PATH + 'apple.png', screen)

        # Aggregated class cannot be inherited. That's why Apple has its own Lifespan()
        self.lifespan = Lifespan()
    
    def get_score(self):
        """ Gets the score to be added when you click an apple.
        
            Returns:
                int: The amount that an apple adds to the score.
        """
        return 10


class Banana(Fruit):
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(IMAGE_PATH + 'banana.png', screen)

        # Aggregated class cannot be inherited. That's why Banana has its own Lifespan()
        self.lifespan = Lifespan()

    def get_score(self):
        """ Gets the score to be added when you click a banana.
        
            Returns:
                int: The amount that a banana adds to the score.
        """
        return 5



