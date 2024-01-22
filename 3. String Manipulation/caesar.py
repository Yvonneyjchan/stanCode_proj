"""
File: caesar.py
Name: Yvonne Chan
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program deciphers
    among users input the shifted number and the Caesar Cipher.
    """
    secret = int(input('Secret number: '))
    cipher = input("What's the cipher number? ")
    print('The deciphered string is: ' + decipher(cipher, secret))


def decipher(cipher, secret):
    new_alphabet = ''
    for i in range(len(ALPHABET)):
        ch = ALPHABET[i]
        n = (ALPHABET.find(ch) - secret) % len(ALPHABET)
        new_alphabet += ALPHABET[n]
    # Create new_alphabet by shifted the number of the secret.
    new_cipher = ''
    cipher = cipher.upper()
    for i in range(len(cipher)):
        ch = cipher[i]
        n = new_alphabet.find(ch)
        if 0 <= n <= 25:
            new_cipher += ALPHABET[n]
        else:
            new_cipher += cipher[i]
    return new_cipher


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
