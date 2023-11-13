from .modules.data_form import general


class Strategy:
    def __init__(self, username):
        self.game_data = None
        self.username = username
        self.my_farm = None
        self.commands = []
        self.turn = 0
        self.start_day = 0
        self.turnover = 0

    def get_data(self):
        self.game_data = general(**self.game_data)
        for i in range(len(self.game_data.farms)):
            if self.game_data.farms[i].name == self.username:
                self.my_farm = self.game_data.farms[i]

    def return_commands(self):
        return self.commands

    def add_commands(self, command):
        self.commands.append(command)

    def main_propre(self):
        self.get_data()
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

    def main_pas_propre(self):
        self.get_data()
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

        if len(self.my_farm.employees) > 0:
            if self.my_farm.employees[0].salary >= 1161:
                self.add_commands("0 EMPRUNTER 20000")
                for i in range(17):
                    self.add_commands("0 LICENCIER "
                                      + str(i + 1 + self.turnover * 17))

                self.start_day = self.game_data.day + 2
                self.turn = 0
                self.turnover += 1

        if self.game_data.day == self.start_day:
            for i in range(17):
                self.add_commands("0 EMPLOYER")

        if len(self.my_farm.employees) > 0:
            if self.my_farm.employees[0].salary < 1161:

                if self.game_data.day == self.start_day + 1 + self.turn * 10:
                    self.add_commands(str(11 + self.turnover * 17)
                                      + " SEMER TOMATE 3")

                if self.game_data.day == self.start_day + 2 + self.turn * 10:

                    for i in range(10):
                        string = str(i + 1 + self.turnover * 17) + " ARROSER 3"
                        self.add_commands(string)

                if self.game_data.day == self.start_day + 4 + self.turn * 10:
                    self.add_commands(str(11 + self.turnover * 17)
                                      + " SEMER PATATE 4")

                if self.game_data.day == self.start_day + 6 + self.turn * 10:
                    self.add_commands(str(12 + self.turnover * 17)
                                      + " STOCKER 3 1")
                    self.add_commands(
                        str(11 + self.turnover * 17) + " SEMER COURGETTE 5"
                    )
                    for i in range(10):
                        string = str(i + 1 + self.turnover * 17) + " ARROSER 4"
                        self.add_commands(string)

                if self.game_data.day == self.start_day + 8 + self.turn * 10:
                    self.add_commands(str(13 + self.turnover * 17)
                                      + " STOCKER 4 2")
                    for i in range(10):
                        string = str(i + 1 + self.turnover * 17) + " ARROSER 5"
                        self.add_commands(string)

                if self.game_data.day == self.start_day + 10 + self.turn * 10:
                    self.add_commands(str(14 + self.turnover * 17)
                                      + " STOCKER 5 3")
                    self.turn += 1

                if self.game_data.day == self.start_day + 11:
                    self.add_commands(str(15 + self.turnover * 17)
                                      + " CUISINER")
                    self.add_commands(str(16 + self.turnover * 17)
                                      + " CUISINER")
                    self.add_commands(str(17 + self.turnover * 17)
                                      + " CUISINER")

                if self.game_data.day > self.start_day + 18:
                    self.add_commands(str(15 + self.turnover * 17)
                                      + " CUISINER")
                    self.add_commands(str(16 + self.turnover * 17)
                                      + " CUISINER")
                    self.add_commands(str(17 + self.turnover * 17)
                                      + " CUISINER")
