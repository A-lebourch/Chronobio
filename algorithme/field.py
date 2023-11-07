from algorithme.locations import Location
from algorithme.aliments import Aliment


class Field:
    def __init__(self, location: Location):
        self.content = Aliment.NONE
        self.water_lvl: int

    def is_sowable(self):
        return self.content == Aliment.NONE

    def needed_water(self):
        return self.content != Aliment.NONE and self.water_lvl != 0

    def can_harvest_sell(self):
        return self.content != Aliment.NONE and self.water_lvl == 0
