"""
File: hailstone.py
Name: Yvonne Chan
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program shows Hailstone sequence.
    """
    print('This program computes Hailstone sequence.')
    """
    :param: h: int, the number to be computed Hailstone sequence.
    """
    h = int(input('Enter a number: '))
    counts = 0
    while True:
        if h != 1:
            if h % 2 == 1:
                print(str(h) + ' is even, so I make 3n+1: ' + str(3*h+1))
                h = 3 * h + 1
            else:
                print(str(h) + ' is odd, so I take half: ' + str(h//2))
                h = h//2
        else:
            break
        counts = counts + 1
    print('It took '+str(counts)+' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
