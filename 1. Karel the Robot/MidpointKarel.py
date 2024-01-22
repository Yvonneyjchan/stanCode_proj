"""
File: MidpointKarel.py
Name:  Yvonne Chan
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
    Karel will leave a beeper on the corner closest to the center of 1st Street
    by putting beeper each side at the 1st street,
    then moving to the middle.
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at the last avenue, 1st street, facing East in odd world.
    (or Karel is at (1,1), facing West in even world.)
    """
    put_beeper_each_side()
    move_beeper_to_mid()
    the_last_beeper()


def put_beeper_each_side():
    """
    Karel will put one beeper at (1,1) and one at 1st street, the last avenue.
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at 1st street, the last avenue, facing West.
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()


def move_beeper_to_mid():
    """
    Karel will move 2 beeper to the middle.
    pre-condition: Karel is at 1st street, the last avenue, facing West.
    post-condition: Karel is at (1,1), facing West in odd world.
    (or Karel is at the last avenue, 1st street, facing East in even world.)
    """
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            turn_around()
            move()
            put_beeper()


def the_last_beeper():
    """
    Karel will make the middle only 1 beeper.
    pre-condition: Karel is at  (1,1), facing West.
    (or Karel is at the last avenue, 1st street, facing East in even world.)
    post-condition: Karel is at the last avenue, 1st street, facing East in odd world.
    (or Karel is at (1,1), facing West in even world.)
    """
    turn_around()
    if on_beeper():
        pick_beeper()
        # make Midpoint1 and 2 success.
    else:
        while front_is_clear():
            move()
            if on_beeper():
                pick_beeper()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
