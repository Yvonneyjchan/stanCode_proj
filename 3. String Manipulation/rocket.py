"""
File: rocket.py
Name: Yvonne Chan
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 10


def main():
    """
    This program creates the rocket
    whose size depends on users input.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print('')


def belt():
    print('+', end='')
    for i in range(SIZE*2):
        print('=', end='')
    print('+')


def upper():
    for i in range(SIZE):
        print('|', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range(i+1):
            print('/\\', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        print('|')


def lower():
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE-i):
            print('\\/', end='')
        for j in range(i):
            print('.', end='')
        print('|')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
