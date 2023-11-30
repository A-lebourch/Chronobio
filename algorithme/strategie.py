from algorithme.modules.data_form import General
from algorithme.modules.field import Field
from algorithme.modules.owner import Owner, all_vegetables
import algorithme.modules.order as ord


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

    def update_field(self, field_index):
        field = Field()
        field.water_lvl = self.my_fields[field_index].needed_water
        field.content = self.my_fields[field_index].content
        return field

    def main_propre(self):
        self.get_data()
        print("#" * 80)
        nb_employee = 22
        owner = Owner()
        owner.money = self.my_farm.money
        if self.game_data.day == 0:
            self.add_commands(ord.emprunter(100_000))
            for i in range(3):
                if owner.can_buy_tractor():
                    owner.money -= 30_000
                self.add_commands(ord.acheter_tracteur())

            for i in range(5):
                self.add_commands(ord.acheter_champ())

        if self.my_farm.fields[4].bought:
            for i in range(len(self.my_fields)):
                field = self.update_field(i)

        if self.game_data.day == self.start_day:
            for i in range(nb_employee):
                self.add_commands("0 EMPLOYER")

        if len(self.my_farm.employees) > 0:
            if self.game_data.day == self.start_day + (30 * 15) + 1:
                for i in range(nb_employee):
                    self.add_commands(
                        "0 LICENCIER "
                        + str(i + 1 + self.turnover * nb_employee)
                    )

                self.start_day = self.game_data.day + 4
                self.turn = 0
                self.turnover += 1

        if self.start_day + 1 <= self.game_data.day <= self.start_day + 4:
            field_index = self.game_data.day - (self.start_day + 1)
            field = self.update_field(field_index)
            if field.is_sowable():
                self.add_commands(
                    ord.semer(
                        (self.turnover * 22) + 1,
                        self.aliments[self.legume],
                        field_index + 1,
                    )
                )
            self.legume += 1
            self.legume %= 5

        if self.start_day + 2 <= self.game_data.day <= self.start_day + 4:
            field_index = self.game_data.day - (self.start_day + 2)
            field = self.update_field(field_index)
            if field.needed_water():
                for i in range(2, 12):
                    self.add_commands(
                        ord.arroser((self.turnover * 22) + i, field_index + 1)
                    )

        if self.start_day + 3 <= self.game_data.day <= self.start_day + 4:
            field_index = self.game_data.day - (self.start_day + 3)
            field = self.update_field(field_index)
            if field.can_harvest_sell():
                self.add_commands(
                    ord.stocker(
                        (self.turnover * 22) + 12 + field_index,
                        field_index + 1,
                        field_index + 1,
                    )
                )

        if self.game_data.day >= self.start_day + 5:
            jour_rose = (self.game_data.day - (self.start_day + 5)) % 4
            # print("jour rose", jour_rose)
            if jour_rose == 0:
                water_field_id = 4
            if jour_rose == 1:
                water_field_id = 5
            if jour_rose == 2:
                water_field_id = 3
            if jour_rose <= 2:
                field = self.update_field(water_field_id - 1)
                if field.needed_water():
                    for employee_id in range(2, 12):
                        self.add_commands(
                            ord.arroser(
                                (self.turnover * 22) + employee_id,
                                water_field_id,
                            )
                        )

            if jour_rose == 0:
                sow_field_id = 5
            if jour_rose == 1:
                sow_field_id = 3
            if jour_rose == 3:
                sow_field_id = 4
            if jour_rose in (0, 1, 3):
                field = self.update_field(sow_field_id - 1)
                if field.is_sowable():
                    self.add_commands(
                        ord.semer(
                            (self.turnover * 22) + 1,
                            self.aliments[self.legume],
                            sow_field_id,
                        )
                    )
                    self.legume += 1
                    self.legume %= 5

            if jour_rose == 0:
                stock_field_id = 3
                stock_farmer_id = 14
            if jour_rose == 1:
                stock_field_id = 4
                stock_farmer_id = 12
            if jour_rose == 2:
                stock_field_id = 5
                stock_farmer_id = 13
            if jour_rose in (0, 1, 2):
                field = self.update_field(stock_field_id - 1)
                if field.can_harvest_sell():
                    self.add_commands(
                        ord.stocker(
                            (self.turnover * 22) + stock_farmer_id,
                            stock_field_id,
                            stock_farmer_id - 11,
                        )
                    )

        if self.game_data.day >= self.start_day + 5:
            jour_bleu = (self.game_data.day - (self.start_day + 5)) % 6
            if jour_bleu == 1:
                water_field_id = 0
            if jour_bleu == 4:
                water_field_id = 1
            if jour_bleu in (1, 4):
                field = self.update_field(water_field_id)
                if field.needed_water():
                    for employee_id in range(18, 23):
                        self.add_commands(
                            ord.arroser(
                                (self.turnover * 22) + employee_id,
                                water_field_id + 1,
                            )
                        )

            if jour_bleu == 0:
                sow_field_id = 0
            if jour_bleu == 3:
                sow_field_id = 1
            if jour_bleu in (0, 3):
                field = self.update_field(sow_field_id)
                if field.is_sowable():
                    self.add_commands(
                        ord.semer(
                            (self.turnover * 22) + 18,
                            self.aliments[self.legume],
                            sow_field_id + 1,
                        )
                    )
                    self.legume += 1
                    self.legume %= 5

            if jour_bleu == 0:
                stock_field_id = 1
            if jour_bleu == 3:
                stock_field_id = 0
            if jour_bleu in (0, 3):
                field = self.update_field(stock_field_id)
                if field.can_harvest_sell():
                    self.add_commands(ord.vendre(stock_field_id + 1))

        if self.game_data.day == self.start_day + 11:
            self.add_commands(ord.cuisiner((self.turnover * 22) + 15))
            self.add_commands(ord.cuisiner((self.turnover * 22) + 16))
            self.add_commands(ord.cuisiner((self.turnover * 22) + 17))

        if self.game_data.day > self.start_day + 18 and all_vegetables(
            self.my_farm.soup_factory
        ):
            self.add_commands(ord.cuisiner((self.turnover * 22) + 15))
            self.add_commands(ord.cuisiner((self.turnover * 22) + 16))
            self.add_commands(ord.cuisiner((self.turnover * 22) + 17))
