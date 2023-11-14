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
        plantation = self.aliments[self.legume]
        nb_employee = 22
        self.get_data()
        owner = Owner()
        owner.money = self.my_farm.money
        if self.game_data.day == 0:
            self.add_commands(ord.emprunter(100_000))
            for i in range(3):
                if owner.can_buy_tractor():
                    owner.money -= 30_000
                self.add_commands(ord.acheter_tracteur())
            for i in range(5):
                if owner.can_buy_field():
                    self.add_commands(ord.acheter_champ())
                    owner.money -= 5000
        # for i in range(len(self.my_fields)):
        #     field = Field()
        #     field.water_lvl = self.my_fields[i].needed_water
        #     field.content = self.my_fields[i].content
        #     print(field.needed_water())

        if self.game_data.day == self.start_day:
            for i in range(nb_employee):
                if owner.can_hire():
                    owner.money -= 1000
                    self.add_commands("0 EMPLOYER")

                # if len(self.my_farm.employees) > 0:
                #     if owner.can_fire(0 ):
                #         # self.add_commands("0 EMPRUNTER 20000")
                #         for i in range(nb_employee):
                #             self.add_commands(
                #                 "0 LICENCIER " + str(i + 1 + self.turnover * nb_employee)
                #             )

                self.start_day = self.game_data.day + 2
                self.turn = 0
                self.turnover += 1

        if self.game_data.day == self.start_day + 1:
            field = Field()
            field.water_lvl = self.my_fields[0].needed_water
            field.content = self.my_fields[0].content
            if field.is_sowable():
                self.add_commands(ord.semer(1, plantation[self.legume], 1))
                self.legume += 1

        if self.game_data.day == self.start_day + 2:
            field = Field()
            field.water_lvl = self.my_fields[1].needed_water
            field.content = self.my_fields[1].content
            if field.is_sowable():
                self.add_commands(ord.semer(1, plantation[self.legume], 2))
                self.legume += 1

            field = Field()
            field.water_lvl = self.my_fields[0].needed_water
            field.content = self.my_fields[0].content
            if field.needed_water():
                for i in range(10):
                    self.add_commands(ord.arroser(i + 3, 1))

        if self.game_data.day == self.start_day + 3:
            field = Field()
            field.water_lvl = self.my_fields[2].needed_water
            field.content = self.my_fields[2].content
            if field.is_sowable():
                self.add_commands(ord.semer(1, plantation[self.legume], 3))
                self.legume += 1

            field = Field()
            field.water_lvl = self.my_fields[1].needed_water
            field.content = self.my_fields[1].content
            if field.needed_water():
                for i in range(10):
                    self.add_commands(ord.arroser(i + 3, 2))

            field = Field()
            field.water_lvl = self.my_fields[0].needed_water
            field.content = self.my_fields[0].content
            if field.can_harvest_sell():
                self.add_commands(ord.stocker(12, 1, 1))

        if self.game_data.day == self.start_day + 4:
            field = Field()
            field.water_lvl = self.my_fields[3].needed_water
            field.content = self.my_fields[3].content
            if field.is_sowable():
                self.add_commands(ord.semer(1, plantation[self.legume], 4))
                self.legume += 1

            field = Field()
            field.water_lvl = self.my_fields[2].needed_water
            field.content = self.my_fields[2].content
            if field.needed_water():
                for i in range(10):
                    self.add_commands(ord.arroser(i + 3, 3))

            field = Field()
            field.water_lvl = self.my_fields[1].needed_water
            field.content = self.my_fields[1].content
            if field.can_harvest_sell():
                self.add_commands(ord.stocker(13, 2, 2))

            field = Field()
            field.water_lvl = self.my_fields[0].needed_water
            field.content = self.my_fields[0].content
            if field.is_sowable():
                self.add_commands(ord.semer(15, plantation[self.legume], 1))
                self.legume += 1

        if self.game_data.day == self.start_day + 5:
            field = Field()
            field.water_lvl = self.my_fields[4].needed_water
            field.content = self.my_fields[4].content
            if field.is_sowable():
                self.add_commands(ord.semer(1, plantation[self.legume], 5))
                self.legume += 1

            field = Field()
            field.water_lvl = self.my_fields[3].needed_water
            field.content = self.my_fields[3].content
            if field.needed_water():
                for i in range(10):
                    self.add_commands(ord.arroser(i + 3, 4))

            field = Field()
            field.water_lvl = self.my_fields[2].needed_water
            field.content = self.my_fields[2].content
            if field.can_harvest_sell():
                self.add_commands(ord.stocker(14, 3, 3))

            field = Field()
            field.water_lvl = self.my_fields[0].needed_water
            field.content = self.my_fields[0].content
            if field.needed_water():
                for i in range(5):
                    self.add_commands(ord.arroser(i + 15, 4))

        if self.legume == 5:
            self.legume = 0
        self.start_day += 1

    # /////////////////////////////////////////////////////////////

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
