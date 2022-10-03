from Iplant import IPlant
import pygame

from projectile import Projectil

class Nut(IPlant):
    def __init__(self, pos_x, pos_y, screen_width, screen_height, index_garden, move_image):
        super().__init__("./assets/plants/nut.png", pos_x, pos_y, 20, screen_width, screen_height, index_garden, move_image)

    def update(self, projectiles, plants, sprites, suns, zombies, reason, matrix_garden):
        if reason == "die":
            self.get_damage(plants, zombies, sprites, matrix_garden, 0)
        