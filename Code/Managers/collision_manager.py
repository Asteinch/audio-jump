import pygame

class collisionManager:

    def __init__(self):

        self.hostile_data = []

    def add_hostile(self, hostile):

        self.hostile_data.append(

            [pygame.mask.from_surface(hostile.img), (hostile.x, hostile.y)]
            
            )

    def update_pos(self, hostile_list):

        for hostile_index, hostile in enumerate(hostile_list):

            self.hostile_data[hostile_index][1] = (hostile.x, hostile.y)



    def is_player_collideing(self, player):

        for hostile in self.hostile_data:

            offset_x = hostile[1][0] - player.x
            offset_y = hostile[1][1] - player.y  

            return player.mask.overlap(hostile[0], (offset_x, offset_y))
    



