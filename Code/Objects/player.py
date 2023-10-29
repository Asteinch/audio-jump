import pygame

from constants import *

class Player:

    def __init__(self, img, pos):

        self.img = pygame.image.load("./assets/him.png")
        self.mask = pygame.mask.from_surface(self.img)

        self.anim = [pygame.image.load("./assets/him_walk1.png"), pygame.image.load("./assets/him_walk2.png"), pygame.image.load("./assets/him_jump.png")]
        self.anim_index = 0

        self.x, self.y = pos[0], pos[1]

        self.jump_vel = 0

        self.is_jumping = False

        self.frames = 0


    def update(self):

        self.apply_gravity()
        self.apply_jump_velocity()
        self.animate_player()


    def apply_gravity(self):

        if self.y + self.img.get_height() < GROUND_POS:

            self.y -= GRAVITY

        else:

            self.y = GROUND_POS - self.img.get_height()
            self.is_jumping = False

    def apply_jump_velocity(self):

        self.y -= self.jump_vel

        if self.jump_vel >= 0:
            self.jump_vel -= 1

    def animate_player(self):

        self.frames += 1

        if self.frames == 10:

            self.anim_index = 0 if self.anim_index == 1 else 1
            self.frames = 0

        if self.is_jumping:

            self.anim_index = 2


    def jump(self, audioManager):

        if not self.is_jumping and audioManager.get_volume() > 10:

            if 5 > (audioManager.get_frequency() / 100) > 1:

                self.jump_vel = (audioManager.get_frequency() / 10) - 10
                print(self.jump_vel)
                self.is_jumping = True

    def draw(self, win):

        win.blit(self.anim[self.anim_index], (self.x, self.y))