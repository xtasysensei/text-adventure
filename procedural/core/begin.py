import os
import sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import random
from lib.colors import *


# make more items(4 treasre chest, 3 goblins, 1 dragon)
# escape number should be in binary

items = [
    "treasure chest",
    "treasure chest",
    "goblin",
    "goblin",
    "treasure chest",
    "goblin",
    "dragon",
    "treasure chest",
]


def begin():
    print("********************")
    print("********************")
    print("")

    print(
        "You see two paths, one Left and ond Right. Which do you follow?\n[1] go Left\n[2] go Right\n[3] Exit the dungeon(like a coward!!)"
    )
    path = int(input("> Choose?: "))

    if path == 1:
        go_left()
    elif path == 2:
        go_right()
    elif path == 3:
        print("You ran away like a little BITCH!! :(")
    else:
        print("Invalid option!!")


def go_left():
    doors()


def go_right():
    doors()


def doors():
    print("********************")
    print(
        f"As you walk foward you stop at two doors,{red}RED{end} and {blue}BLUE{end}. Which do you enter?\n[1] Red\n[2] Blue"
    )
    choice = int(input("> Choice?: "))
    if choice == 1:
        print("----------")
        print("you entered the Red door")
        print("----------")
        item_arr()
    elif choice == 2:
        print("You enter the Blue door")
        item_arr()


def fight():
    monster_no = random.randint(1, 3)
    escape_no = random.randint(1, 2)
    choice = int(input("> Choice?: "))
    if choice == 1:
        print("You decide to fight!!")
        print(
            "Enter a number between 1 - 3, if number matches monster number u win else....."
        )
        fight_no = int(input("> Number: "))
        if fight_no == monster_no:
            print("You slayed the monster")
            doors()
        else:
            print("You Died!?!")
    elif choice == 2:
        print(
            "Enter a number between 1 - 2, if number matches monster number u escape else....."
        )
        run_no = int(input("> Number: "))
        if run_no == escape_no:
            print("You escaped the monster")
            doors()
        else:
            print("You Died!?!")


def fight_dragon():
    dragon_no = random.randint(1, 6)
    dragon_escape_no = random.randint(1, 6)
    choice = int(input("> Choice?: "))
    if choice == 1:
        print("You decide to fight!!")
        print(
            "Enter a number between 1 - 6, if number matches monster number u win else....."
        )
        fight_no = int(input("> Number: "))
        if fight_no == dragon_no:
            print("You slayed the Dragon!!")
            doors()
        else:
            print("You Died!?!")
    elif choice == 2:
        print(
            "Enter a number between 1 - 6, if number matches monster number u escape else....."
        )
        run_no = int(input("> Number: "))
        if run_no == dragon_escape_no:
            print("You escaped the monster")
            doors()
        else:
            print("You Died!?!")


def item_arr():
    global item
    item_no = random.randint(0, 7)
    print(item_no)
    item = items[item_no]
    print(f"You encounter a {item}!!")
    if item == "goblin":
        print("!!!!!!!!!!!!!!!!")
        print("What will you do?")
        print("\t[1] Fight!! \n\t[2] Run way")
        fight()
    elif item == "dragon":
        print("##++**!!!###")
        print("What will you do?")
        print("\t[1] Fight!! \n\t[2] Run way")
        fight_dragon()
    elif item == "treasure chest":
        print("$$$$$$$$$$$")
        open_chest()


def open_chest():
    chest_no = random.randint(2, 3)
    print("What will you do?")
    print("\t[1] Open the chest \n\t[2] Ignore it")
    choice = int(input("> Choice?: "))
    if choice == 1 and chest_no == 2:
        print("You find gold coins")
        doors()
    elif choice == 1 and chest_no == 3:
        print("The chest turns into a MIMIC!!")
        print("What will you do?")
        print("\t[1] Fight!! \n\t[2] Run way")
        fight()
    elif choice == 2:
        print("You ignore the chest and continue")
        begin()
