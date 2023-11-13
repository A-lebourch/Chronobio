from algorithme.modules.data_form import General
from algorithme.modules.employees import Employee
from algorithme.modules.field import Field
from algorithme.modules.owner import Owner
import algorithme.modules.order as ord
from random import choice


class Strategy:
    def __init__(self, username):
        self.game_data = None
        self.username = username
        self.my_farm = None
        self.my_fields = []
        self.commands = []
        self.turn = 0
        self.start_day = 0
        self.turnover = 0
        self.aliments = ["TOMATE", "PATATE", "OIGNON", "COURGETTE", "POIREAU"]
        self.legume = 0

    def get_data(self):
        self.game_data = General(**self.game_data)
        for i in range(len(self.game_data.farms)):
            if self.game_data.farms[i].name == self.username:
                self.my_farm = self.game_data.farms[i]
        self.my_fields = self.my_farm.fields

    def return_commands(self):
        return self.commands

    def add_commands(self, command):
        self.commands.append(command)

    def main_propre(self):
        self.get_data()
        if self.game_data.day == 0:
            self.add_commands(ord.emprunter(100_000))
            for i in range(3):
                self.add_commands(ord.acheter_tracteur())
            for i in range(5):
                self.add_commands(ord.acheter_champ())
        for field in range(len(self.fields)):
            field = Field()
            field.water_lvl = self.my_fields[field].needed_water
            field.content = self.my_fields[field].content
            # if field.needed_water():

    def main_pas_propre(self):
        self.get_data()
        if self.game_data.day == 0:
            self.add_commands(ord.emprunter(100_000))
            for i in range(3):
                self.add_commands(ord.acheter_tracteur())
            for i in range(5):
                self.add_commands(ord.acheter_champ())

        if len(self.my_farm.employees) > 0:
            if self.my_farm.employees[0].salary >= 1161:
                self.add_commands("0 EMPRUNTER 20000")
                for i in range(17):
                    self.add_commands("0 LICENCIER " + str(i + 1 + self.turnover * 17))

                self.start_day = self.game_data.day + 2
                self.turn = 0
                self.turnover += 1

        if self.game_data.day == self.start_day:
            for i in range(17):
                self.add_commands("0 EMPLOYER")

        if len(self.my_farm.employees) > 0:
            plantation = self.aliments[self.legume]
            if self.my_farm.employees[0].salary < 1161:
                if self.game_data.day == self.start_day + 1 + self.turn * 10:
                    self.legume += 1
                    self.add_commands(
                        str(11 + self.turnover * 17) + " SEMER " + plantation + " 3"
                    )
                    for i in range(10):
                        self.add_commands(
                            str(i + 1 + self.turnover * 17) + " ARROSER 3"
                        )

                # if self.game_data.day == self.start_day + 2 + self.turn * 10:

                if self.game_data.day == self.start_day + 4 + self.turn * 10:
                    self.legume += 1
                    self.add_commands(
                        str(11 + self.turnover * 17) + " SEMER " + plantation + " 4"
                    )
                    for i in range(10):
                        self.add_commands(
                            str(i + 1 + self.turnover * 17) + " ARROSER 4"
                        )
                    self.add_commands(str(12 + self.turnover * 17) + " STOCKER 3 1")

                if self.game_data.day == self.start_day + 6 + self.turn * 10:
                    self.legume += 1
                    self.add_commands(
                        str(11 + self.turnover * 17) + " SEMER " + plantation + " 5"
                    )
                    for i in range(10):
                        self.add_commands(
                            str(i + 1 + self.turnover * 17) + " ARROSER 5"
                        )
                    self.add_commands(str(13 + self.turnover * 17) + " STOCKER 4 2")

                if self.game_data.day == self.start_day + 8 + self.turn * 10:
                    self.add_commands(str(14 + self.turnover * 17) + " STOCKER 5 3")
                    self.turn += 1

                # if self.game_data.day == self.start_day + 10 + self.turn * 10:

                if self.game_data.day == self.start_day + 23:
                    self.add_commands(str(15 + self.turnover * 17) + " CUISINER")
                    self.add_commands(str(16 + self.turnover * 17) + " CUISINER")
                    self.add_commands(str(17 + self.turnover * 17) + " CUISINER")

                if self.game_data.day > self.start_day + 30:
                    self.add_commands(str(15 + self.turnover * 17) + " CUISINER")
                    self.add_commands(str(16 + self.turnover * 17) + " CUISINER")
                    self.add_commands(str(17 + self.turnover * 17) + " CUISINER")

                if self.legume == 5:
                    self.legume = 0
