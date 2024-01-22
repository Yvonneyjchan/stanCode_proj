"""
File: extension1_MidpointKarel.py
Name: Yvonne Chan
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will go north two and east one to find the middle,
    then go down to the 1st street and put beeper.
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at the middle of the avenue, the 1st street, facing South.
    """
    north_two_east_one()
    go_down()


def north_two_east_one():
    """
    Karel will go north two and east one to find the middle, at the last street.
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at the middle of the avenue, the last street, facing North.
    """
    turn_left()
    # facing North.
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            turn_right()
            move()
            turn_left()
        else:
            turn_right()
            move()
            turn_left()


def go_down():
    """
    Karel will go to the 1st street from the last.
    pre-condition: Karel is at the middle of the avenue, the last street, facing North.
    post-condition: Karel is at the middle of the avenue, the 1st street, facing South.
    """
    turn_around()
    while front_is_clear():
        move()
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