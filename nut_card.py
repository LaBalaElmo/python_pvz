from Iplant_card import IPlantCard
from nut import Nut
from peashooter import Peashooter

class NutCard(IPlantCard):
    def __init__(self, pos_x, pos_y):
        super().__init__("nut", pos_x, pos_y, 50)
    
    def add_plant(self, plants, sprites, position, screen_width, screen_height, index_garden):
        peashooter = Nut(position[0], position[1], screen_width, screen_height, index_garden, True)
        plants.add(peashooter)
        sprites.add(peashooter)