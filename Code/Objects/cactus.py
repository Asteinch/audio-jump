import pygame
from constants import *

import random

class Cacti:

    def __init__(self):

        self.images = [pygame.image.load("./assets/cacti2.png"), pygame.image.load("./assets/cacti1.png")]
    
        self.img = random.choice(self.images)

        self.mask = pygame.mask.from_surface(self.img)

        self.x, self.y = random.randint(1280, 2000), GROUND_POS - self.img.get_height()

    def update(self):

        self.x -= 10

    def is_out_of_bounds(self):

        if self.x < -200:
            return True

    def reset(self):

        self.img = random.choice(self.images)
        self.mask = pygame.mask.from_surface(self.img)
        self.x = random.randint(1280, 2000)
        self.y = GROUND_POS - self.img.get_height()


    def draw(self, win):
        
        win.blit(self.img, (self.x, self.y))

    