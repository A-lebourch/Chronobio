from .modules.data_form import general


class Strategy:
    def __init__(self, username):
        self.game_data = None
        self.username = username
        self.my_farm = None
        self.commands = []
        self.turn = 0

    def get_data(self):
        self.game_data = general(**self.game_data)
        for i in range(len(self.game_data.farms)):
            if self.game_data.farms[i].name == self.username:
                self.my_farm = self.game_data.farms[i]

    def return_commands(self):
        return self.commands

    def add_commands(self, command):
        self.commands.append(command)

    def main_pas_propre(self):
        self.get_data()
        print(self.game_data)
        if self.game_data.day == 0:
            self.add_commands("0 EMPRUNTER 100000")
            self.add_commands("0 ACHETER_TRACTEUR")
            self.add_commands("0 ACHETER_TRACTEUR")
            self.add_commands("0 ACHETER_TRACTEUR")
            self.add_commands("0 ACHETER_CHAMP")
            self.add_commands("0 ACHETER_CHAMP")
            self.add_commands("0 ACHETER_CHAMP")
            self.add_commands("0 ACHETER_CHAMP")
            self.add_commands("0 ACHETER_CHAMP")
            for i in range(17):
                self.add_commands("0 EMPLOYER")

        if len(self.my_farm.employees) > 0:
            if self.game_data.day == 1 + self.turn * 10:
                self.add_commands("11 SEMER TOMATE 3")

            if self.game_data.day == 2 + self.turn * 10:

                for i in range(10):
                    string = str(i + 1) + " ARROSER 3"
                    self.add_commands(string)

            if self.game_data.day == 4 + self.turn * 10:
                self.add_commands("11 SEMER PATATE 4")

            if self.game_data.day == 6 + self.turn * 10:
                self.add_commands("12 STOCKER 3 1")
                self.add_commands("11 SEMER COURGETTE 5")
                for i in range(10):
                    string = str(i + 1) + " ARROSER 4"
                    self.add_commands(string)

            if self.game_data.day == 8 + self.turn * 10:
                self.add_commands("13 STOCKER 4 2")
                for i in range(10):
                    string = str(i + 1) + " ARROSER 5"
                    self.add_commands(string)

            if self.game_data.day == 10 + self.turn * 10:
                self.add_commands("14 STOCKER 5 3")
                self.turn += 1

            if self.game_data.day == 11:
                self.add_commands("15 CUISINER")
                self.add_commands("16 CUISINER")
                self.add_commands("17 CUISINER")

            if self.game_data.day > 18:
                self.add_commands("15 CUISINER")
                self.add_commands("16 CUISINER")
                self.add_commands("17 CUISINER")

        # if len(self.my_farm.employees) > 0:
        #     if self.my_farm.employees[0].salary >= 1161:
        #         self.add_commands("0 EMPRUNTER 20000")
        #         for i in range(17):
        #             self.add_commands("0 LICENCIER " + str(i))

        #             self.add_commands("0 EMPLOYER")
