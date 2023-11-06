import argparse
from typing import NoReturn
from chronobio.network.client import Client

import get_data

# print('toto')
class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int, username: str
    ) -> None:
        super().__init__(server_addr, port, username, spectator=False)
        self._commands: list[str] = []

    def run(self: "PlayerGameClient") -> NoReturn:
        '''
        fonction run 
        '''
        turn = 0
        while True:
            game_data = self.read_json()
            for farm in game_data["farms"]:
                if farm["name"] == self.username:
                    my_farm = farm
                    break
            else:
                raise ValueError(f"My farm is not found ({self.username})")
            get_data.observateur(game_data, self.username)

            if game_data["day"] == 0:
                self.add_command("0 EMPRUNTER 100000")
                self.add_command("0 ACHETER_TRACTEUR")
                self.add_command("0 ACHETER_TRACTEUR")
                self.add_command("0 ACHETER_TRACTEUR")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                for i in range(17):
                    self.add_command("0 EMPLOYER")

            if game_data["day"] == 1 + turn * 10:
                self.add_command("11 SEMER TOMATE 3")

            if game_data["day"] == 2 + turn * 10:

                for i in range(10):
                    string = str(i+1) + " ARROSER 3"
                    self.add_command(string)

            if game_data["day"] == 4 + turn * 10:
                self.add_command("11 SEMER PATATE 4")

            if game_data["day"] == 6 + turn * 10:
                self.add_command("12 STOCKER 3 1")
                self.add_command("11 SEMER COURGETTE 5")
                for i in range(10):
                    string = str(i+1) + " ARROSER 4"
                    self.add_command(string)

            if game_data["day"] == 8 + turn * 10:
                self.add_command("13 STOCKER 4 2")
                for i in range(10):
                    string = str(i+1) + " ARROSER 5"
                    self.add_command(string)

            if game_data["day"] == 10 + turn * 10:
                self.add_command("14 STOCKER 5 3")
                turn += 1

            if game_data["day"] == 11:
                self.add_command("15 CUISINER")
                self.add_command("16 CUISINER")
                self.add_command("17 CUISINER")

            if game_data["day"] > 18:
                self.add_command("15 CUISINER")
                self.add_command("16 CUISINER")
                self.add_command("17 CUISINER")

            self.send_commands()

    def add_command(self: "PlayerGameClient", command: str) -> None:
        self._commands.append(command)

    def send_commands(self: "PlayerGameClient") -> None:
        data = {"commands": self._commands}
        print("sending", data)
        self.send_json(data)
        self._commands.clear()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game client.")
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        help="name of server on the network",
        default="localhost",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help="location where server listens",
        default=16210,
    )
    parser.add_argument(
        "-u",
        "--username",
        type=str,
        help="name of the user",
        default="unknown",
        required=True,
    )
    args = parser.parse_args()

    client = PlayerGameClient(args.address, args.port, args.username).run()
