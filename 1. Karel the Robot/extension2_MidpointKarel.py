"""
File: extension2_MidpointKarel.py
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
    Karel will keep fill beeper from the side to the middle,
    then pick up all and put the last beeper in the middle.
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at 1st street, the middle of the avenue.
    """
    fill_side_to_middle()
    pick_all_put_last()


def fill_side_to_middle():
    """
    Karel will keep fill beeper from the side to the middle.
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at the middle,
    facing West in odd world
    or facing East in even world.
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    if front_is_clear():
        move()
        # avoid world 1 fail and fill two side.
        while not on_beeper():
            move()
            if on_beeper():
                turn_around()
                move()
                put_beeper()
                move()
        turn_around()
        move()


def pick_all_put_last():
    """
    Karel will pick all beepers, then put the last beeper in the middle.
    pre-condition: Karel is at the middle,
    facing West in odd world
    or facing East in even world.
    post-condition: Karel is at 1st street, the middle of the avenue,
    facing East in odd world (except world 1)
    or facing West in even world (except world 2)
    """
    if front_is_clear():
        move()
        # avoid world 2 fail.
        while front_is_clear():
            if on_beeper():
                pick_beeper()
                move()
        pick_beeper()
        turn_around()
        while front_is_clear():
            move()
        turn_around()
        while on_beeper():
            pick_beeper()
            move()
        # Karel is next to the middle.
        turn_around()
        move()
        put_beeper()
    else:
        pick_beeper()
        # avoid world 2 has two beeper.


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
