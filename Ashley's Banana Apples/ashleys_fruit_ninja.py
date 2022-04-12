# created by Ashley Leung, April 11, 2022

# a simplified version of fruit ninja, click the fruits to increase your score!
# fruits will relocate randomly when clicked.

import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT


# CLASSES - Create apple and banana classes
class Fruit(pygame.Rect):
    def __init__(self, x: int, y: int, filename: str):
        self.x = x
        self.y = y
        self.width = FRUIT_WIDTH
        self.height = FRUIT_HEIGHT
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        super().__init__(x, y, self.width, self.height)

    def display(self):
        screen.blit(self.image, (self.x, self.y))

class Apple(Fruit):
    def __init__(self, x: int, y: int):
        self.add_score = 10
        self.filename = 'apple.png'
        super().__init__(x, y, self.filename)
  
class Banana(Fruit):
    def __init__(self, x: int, y: int):
        self.add_score = 5
        self.filename = 'banana.png'
        super().__init__(x, y, self.filename)


# initialize pygame
pygame.init()
pygame.display.set_caption("Click the fruits to have fun!")

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
FRUIT_WIDTH = 100
FRUIT_HEIGHT = 100

MAX_APPLES = 3
MAX_BANANAS = 5

apples = []
for i in range(MAX_APPLES):
    apple = Apple(random.randrange(0, SCREEN_WIDTH - FRUIT_WIDTH), random.randrange(0, SCREEN_HEIGHT - FRUIT_HEIGHT))
    apples.append(apple)

bananas = []
for i in range(MAX_BANANAS):
    banana = Banana(random.randrange(0, SCREEN_WIDTH - FRUIT_WIDTH), random.randrange(0, SCREEN_HEIGHT - FRUIT_HEIGHT))
    bananas.append(banana)

score = 0

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

            # GAME STATE UPDATES
            # Increase score when apples and bananas are clicked
            # Randomize apple and banana positions when clicked
            for i in range(MAX_APPLES):
                if apples[i].collidepoint(point):
                    apples[i].x = random.randrange(0, SCREEN_WIDTH - apples[i].width)
                    apples[i].y = random.randrange(0, SCREEN_HEIGHT - apples[i].height)
                    score += apples[i].add_score
                    click_apple = True
                    break

            for i in range(MAX_BANANAS):
                if bananas[i].collidepoint(point):
                    bananas[i].x = random.randrange(0, SCREEN_WIDTH - bananas[i].width)
                    bananas[i].y = random.randrange(0, SCREEN_HEIGHT - bananas[i].height)
                    score += bananas[i].add_score
                    click_banana = True
                    break

            # Display score and confirmation when fruits are clicked
            if click_apple and click_banana: 
                pygame.display.set_caption(f"Your score: {score}, you got both! Nice punch!")
            elif click_apple:
                pygame.display.set_caption(f"Your score: {score}, bright and shiny!")
            elif click_banana:
                pygame.display.set_caption(f"Your score: {score}, that's bananas!")


    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    for i in range(MAX_APPLES):
        apples[i].display() 

    for i in range(MAX_BANANAS):
        bananas[i].display()


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()



