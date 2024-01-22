"""
File: StoneMasonKarel.py
Name: Yvonne Chan
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will repair all the column in any worlds
    which has column at the first and the last, also every column's interval is 3.
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at the 1st street, the last avenue with all column be filled, facing East.
    """
    repair_column()
    move_repeat_repair()


def repair_column():
    """
    Karel will fill one beeper in each street for the column.
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at (1,1) with the column be filled, facing East.
    """
    turn_left()
    # facing North.
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()
    if not on_beeper():
        put_beeper()
        # check the top of the column with or without beeper.
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def move_repeat_repair():
    """
    Karel will move the next column and fill til the end.
    pre-condition: Karel is at (1,1) with the column be filled, facing East.
    post-condition: Karel is at the 1st street, the last avenue with all column be filled, facing East.
    """
    while front_is_clear():
        for i in range(4):
            move()
        repair_column()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
