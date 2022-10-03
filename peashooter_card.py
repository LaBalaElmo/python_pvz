from Iplant_card import IPlantCard
from peashooter import Peashooter

class PeashooterCard(IPlantCard):
    def __init__(self, pos_x, pos_y):
        super().__init__("peashooter", pos_x, pos_y, 100)
    
    def add_plant(self, plants, sprites, position, screen_width, screen_height, index_garden):
        peashooter = Peashooter(position[0], position[1], screen_width, screen_height, index_garden, True)
        plants.add(peashooter)
        sprites.add(peashooter)