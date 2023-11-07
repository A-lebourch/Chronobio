from algorithme.modules.locations import Location
from algorithme.modules.aliments import Aliment


class Field:
    def __init__(self, location: Location):
        self.content: Aliment = Aliment.NONE
        self.water_lvl: int = 10

    def is_sowable(self):
        return self.content == Aliment.NONE

    def needed_water(self):
        return self.content != Aliment.NONE and self.water_lvl != 0

    def can_harvest_sell(self):
        return self.content != Aliment.NONE and self.water_lvl == 0

    def sow(self, aliment):
        self.content = aliment
        return

    def water(self):
        self.water_lvl -= 1
        return
