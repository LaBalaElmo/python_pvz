from Iplant_card import IPlantCard
from sunflower import Sunflower

class SunflowerCard(IPlantCard):
    def __init__(self, pos_x, pos_y):
        super().__init__("sunflower", pos_x, pos_y, 50)
    
    def add_plant(self, plants, sprites, position, screen_width, screen_height, index_garden):
        sunflower = Sunflower(position[0], position[1], screen_width, screen_height, index_garden, True)
        plants.add(sunflower)
        sprites.add(sunflower)