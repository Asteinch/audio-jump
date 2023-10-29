import pygame






class Bird:

    def __init__(self):

        self.imgs = [pygame.image.load("./assets/bird1.png"), pygame.image.load("./assets/bird2.png")]
        self.anim_index = 0

        self.x, self.y = 500, 0

        self.frames = 0

    def update(self):

        self.animate_player()

    def animate_player(self):

        self.frames += 1

        if self.frames == 10:

            self.anim_index = 0 if self.anim_index == 1 else 1
            self.frames = 0

    def draw(self, win):

        win.blit(self.imgs[self.anim_index], (self.x, self.y))