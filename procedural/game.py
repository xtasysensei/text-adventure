import random
from lib.colors import *
from core.begin import *

print("-------------------------------------------")
print(f"{bold}{yellow}!!! ADVENTUREland !!!{end}")
print("-------------------------------------------")
print("")

alt = ["Rainbow Unicorn", "Sir Failsalot", "Just Bob"]
rand_no = random.randint(0, 2)


def player_name():
    global player_name
    player_name = input("[?] What is your name ?> ")
    alt_name = alt[rand_no]
    answer = input(f"Your name is {alt_name.upper()}, is that correct? [Y|N] > ")

    if answer.lower() in ["y", "yes"]:
        player_name = alt_name
        print(f"You are fun, {player_name.upper()}! Let's begin our adventure!")

    elif answer.lower() in ["n", "no"]:
        print(
            f"Ok, picky. {player_name.upper()} it is. Let's get started on our adventure."
        )
    else:
        print(
            f"Trying to be funny? Well, you will now be called {alt_name.upper()} anyway."
        )
        player_name = alt_name


def start():
    player_name()
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

    print("------------------")
    print("")
    begin_game = input("Do you want to begin?(y/n): ")
    if begin_game == "y":
        begin()
    elif begin_game == "n":
        exit()
    else:
        print("Invalid Input")


if __name__ == "__main__":
    start()
