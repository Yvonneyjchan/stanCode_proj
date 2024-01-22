"""
File: CollectNewspaperKarel.py
Name: Yvonne Chan
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will move from the upper left corner of the home to the news at (3,6)
    and pick up the news then return to the initial position.
    """
    move_to_news()
    pick_news_and_return_home()


def move_to_news():
    """
    pre-condition: Karel is at the upper left corner, facing East.
    post-condition: Karel is on the news, facing East.
    """
    while front_is_clear():
        move()
    turn_right()
    # Karel is facing South.
    while not left_is_clear():
        move()
    turn_left()
    move()


def pick_news_and_return_home():
    """"
    pre-condition: Karel is on the news, facing East.
    post-condition: Karel is at the upper left corner with news, facing East.
    """
    pick_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    # Karel is facing North.
    while front_is_clear():
        move()
    turn_right()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
