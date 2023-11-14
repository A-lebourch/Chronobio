from algorithme.modules.data_form import General
from algorithme.modules.employees import Employee
from algorithme.modules.field import Field
from algorithme.modules.owner import Owner, all_vegetables
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
            print(field.needed_water())

    def main_pas_propre(self):
        nb_employee = 22
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
                for i in range(nb_employee):
                    self.add_commands(
                        "0 LICENCIER " + str(i + 1 + self.turnover * nb_employee)
                    )

                self.start_day = self.game_data.day + 2
                self.turn = 0
                self.turnover += 1

        if self.game_data.day == self.start_day:
            for i in range(nb_employee):
                self.add_commands("0 EMPLOYER")

        if len(self.my_farm.employees) > 0:
            plantation = self.aliments[self.legume]
            if self.my_farm.employees[0].salary < 1161:
                if self.game_data.day == self.start_day + 1 + self.turn * 10:
                    self.legume += 1
                    self.add_commands(
                        str(11 + self.turnover * nb_employee)
                        + " SEMER "
                        + plantation
                        + " 3"
                    )

                if self.game_data.day == self.start_day + 2 + self.turn * 10:
                    for i in range(10):
                        string = str(i + 1 + self.turnover * nb_employee) + " ARROSER 3"
                        self.add_commands(string)

                if self.game_data.day == self.start_day + 4 + self.turn * 10:
                    self.legume += 1
                    self.add_commands(
                        str(11 + self.turnover * nb_employee)
                        + " SEMER "
                        + plantation
                        + " 4"
                    )

                if self.game_data.day == self.start_day + 6 + self.turn * 10:
                    self.add_commands(
                        str(12 + self.turnover * nb_employee) + " STOCKER 3 1"
                    )
                    self.legume += 1
                    self.add_commands(
                        str(11 + self.turnover * nb_employee)
                        + " SEMER "
                        + plantation
                        + " 5"
                    )
                    for i in range(10):
                        string = str(i + 1 + self.turnover * nb_employee) + " ARROSER 4"
                        self.add_commands(string)

                if self.game_data.day == self.start_day + 8 + self.turn * 10:
                    self.add_commands(
                        str(13 + self.turnover * nb_employee) + " STOCKER 4 2"
                    )
                    for i in range(10):
                        string = str(i + 1 + self.turnover * nb_employee) + " ARROSER 5"
                        self.add_commands(string)

                if self.game_data.day == self.start_day + 10 + self.turn * 10:
                    self.add_commands(
                        str(14 + self.turnover * nb_employee) + " STOCKER 5 3"
                    )
                    self.turn += 1

                if self.game_data.day == self.start_day + 11:
                    self.add_commands(
                        str(15 + self.turnover * nb_employee) + " CUISINER"
                    )
                    self.add_commands(
                        str(16 + self.turnover * nb_employee) + " CUISINER"
                    )
                    self.add_commands(
                        str(17 + self.turnover * nb_employee) + " CUISINER"
                    )

                if self.game_data.day > 1600:
                    self.add_commands(
                        str(15 + self.turnover * nb_employee) + " CUISINER"
                    )
                    self.add_commands(
                        str(16 + self.turnover * nb_employee) + " CUISINER"
                    )
                    self.add_commands(
                        str(17 + self.turnover * nb_employee) + " CUISINER"
                    )

                elif self.game_data.day > self.start_day + 18 and all_vegetables(
                    self.my_farm.soup_factory
                ):
                    self.add_commands(
                        str(15 + self.turnover * nb_employee) + " CUISINER"
                    )
                    self.add_commands(
                        str(16 + self.turnover * nb_employee) + " CUISINER"
                    )
                    self.add_commands(
                        str(17 + self.turnover * nb_employee) + " CUISINER"
                    )

                if self.legume == 5:
                    self.legume = 0
