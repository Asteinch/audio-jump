import pygame
from constants import *

import random

class Cacti:

    def __init__(self):

        images = [pygame.image.load("./assets/cacti2.png"), pygame.image.load("./assets/cacti1.png")]
    
        self.img = random.choice(images)

        self.mask = pygame.mask.from_surface(self.img)

        self.x, self.y = 500, GROUND_POS - self.img.get_height()

    def update(self):

        self.x -= 5

        if self.x < -50:

            self.x = 1300

    def draw(self, win):
        
        win.blit(self.img, (self.x, self.y))

    