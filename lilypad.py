from Iplant import IPlant
import pygame

from projectile import Projectil

class Lilypad(IPlant):
    def __init__(self, pos_x, pos_y, screen_width, screen_height, index_garden, move_image):
        super().__init__("./assets/plants/lilypad.png", pos_x, pos_y, 5, screen_width, screen_height, index_garden, move_image)

    def update(self, projectiles, plants, sprites, suns, zombies, reason, matrix_garden):
        if reason == "die":
            self.get_damage(plants, zombies, sprites, matrix_garden, 1)
        
    