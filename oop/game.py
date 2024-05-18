import random

# from lib import colors
from core import begin

alt = ["Rainbow Unicorn", "Sir Failsalot", "Just Bob"]
rand_no = random.randrange(0, 2)


def player_setup():
    global player_name
    player_name = input("[?] What is your name ?> ")
    alt_name = alt[rand_no]
    answer = input(f"Your name is {alt_name.upper()}, is that correct? [Y|N] > ")

    player = begin.PlayerName()
    character = begin.PlayerClass()

    player.answer(answer, alt_name)
    player.player_info(player_name)

    character.player_class(player.player_name)


def path():
    print(
        "You see two paths, one Left and ond Right. Which do you follow?\n[1] go Left\n[2] go Right\n[3] Exit the dungeon(like a coward!!)"
    )
    global direction
    direction = int(input("> Choose?: "))


def start():
    player_setup()
    game = begin.Begin()

    game.stars()
    path()
    game.choice(direction)


if __name__ == "__main__":
    start()
