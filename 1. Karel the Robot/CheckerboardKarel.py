"""
File: CheckerboardKarel.py
Name: Yvonne Chan
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will draw a checkerboard by beeper in any world.
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at the last street, 1st avenue, facing North.
    """
    fill_one_street()
    draw_checkerboard_one_street()
    repeat_fill_and_draw()


def fill_one_street():
    """
    Karel will fill one street with one beeper each avenue.
    pre-condition:Karel is at (1,1), facing East.
    post-condition: Karel is at (1,1), facing East.
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
    put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def draw_checkerboard_one_street():
    """
    Karel will draw checkerboard one street by pick up beeper on the street be filled.
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at (1,1), facing North.
    """
    while front_is_clear():
        if on_beeper():
            move()
            pick_beeper()
        else:
            move()
    turn_around()
    while front_is_clear():
        move()
    turn_right()


def repeat_fill_and_draw():
    """
    Karel will draw checkerboard every street according to avenue 1 is with or without beeper.
    pre-condition: Karel is at (1,1), facing North.
    post-condition: Karel is at the last street, 1st avenue, facing North.
    """
    while front_is_clear():
        if on_beeper():
            move()
            turn_right()
            fill_one_street()
            pick_beeper()
            # make the next street starts with no beeper to ensure the checkerboard.
            draw_checkerboard_one_street()
        else:
            move()
            turn_right()
            fill_one_street()
            draw_checkerboard_one_street()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
