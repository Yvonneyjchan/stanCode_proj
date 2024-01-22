"""
File: name_sq.py (extension)
Name: Yvonne Chan
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main() :
    """
    This program prints the square pattern of the given name.
    """
    print('This programs prints a name in a square pattern!')
    name = input('Name: ')
    print(name)
    for i in range(1, len(name)-1):
        print(name[i], end='')
        for j in range(len(name)-2):
            print(' ', end='')
        print(name[len(name)-(i+1)])

    reverse_name = ''
    for i in range(len(name)):
        ch = name[i]
        reverse_name = name[i] + reverse_name
    print(reverse_name)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
