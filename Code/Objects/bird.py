import pygame, random

class Bird:

    def __init__(self):

        self.imgs = [pygame.image.load("./assets/bird1.png"), pygame.image.load("./assets/bird2.png")]
        self.anim_index = 0

        self.x, self.y = random.randint(1280, 2000), random.randint(0, 50)

        self.frames = 0

    def update(self):

        self.x -=5
        self.animate_player()

    def animate_player(self):

        self.frames += 1
        
        if self.frames == 10:

            self.anim_index = 0 if self.anim_index == 1 else 1
            self.frames = 0

    def is_out_of_bounds(self):

        if self.x < -200:

            return True


    def reset(self):

        self.x = random.randint(1280, 2000)
        self.y = random.randint(0, 50)


    def draw(self, win):

        win.blit(self.imgs[self.anim_index], (self.x, self.y))