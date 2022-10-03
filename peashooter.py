from Iplant import IPlant
import pygame

from projectile import Projectil

class Peashooter(IPlant):
    def __init__(self, pos_x, pos_y, screen_width, screen_height, index_garden, move_image):
        super().__init__("./assets/plants/peashooter.png", pos_x, pos_y, 5, screen_width, screen_height, index_garden, move_image)

    def update(self, projectiles, plants, sprites, suns, zombies, reason, matrix_garden):
        if reason == "shoot":
            projectile = Projectil(self.pos_X, self.pos_y, "./assets/projectiles/pea.png", self.screen_width)
            projectiles.add(projectile)
            sprites.add(projectile)
        if reason == "die":
            self.get_damage(plants, zombies, sprites, matrix_garden, 0)
        
    