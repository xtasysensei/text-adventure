import os
import sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import random

# from ..lib import colors

class Begin:

    def stars(self):
        print("********************")
        print("********************")

    def choice(self, path):
        self.path = path

        if self.path == 1:
            # go_left()
            print("left")
        elif self.path == 2:
            # go_right()
            print("right")
        elif self.path == 3:
            print("You ran away like a little BITCH!! :(")
        else:
            print("Invalid option!!")


class PlayerName:
    def answer(self, answer, alt_name):
        self.answer = answer
        self.alt_name = alt_name

    def player_info(self, player_name):
        self.player_name = player_name

        if self.answer in ["y", "yes"]:
            self.player_name = self.alt_name
            print(
                f"You are fun, {self.player_name.upper()}! Let's begin our adventure!"
            )
        elif self.answer in ["n", "no"]:
            print(
                f"Ok, picky. {self.player_name.upper()} it is. Let's get started on our adventure."
            )
        else:
            print(
                f"Trying to be funny? Well, you will now be called {self.alt_name.upper()} anyway."
            )
            self.player_name = self.alt_name


class PlayerClass:
    def player_class(self, player_name):
        self.player_name = player_name
        # Choosing a class
        print("What path do you want to take")
        print("------------------")
        print("[1] Knight\n[2] Mage\n[3] Hunter")
        player_class = int(input("> Choose: "))

        if player_class == 1:
            player_class = "Knight"
            print(f"Welcome again, {player_class} {player_name}")
        elif player_class == 2:
            player_class = "Mage"
            print(f"Welcome again, {player_class} {player_name}")
        elif player_class == 3:
            player_class = "Hunter"
            print(f"Welcome again, {player_class} {player_name}")
        else:
            print("Invalid option")
