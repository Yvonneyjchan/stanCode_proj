"""
File: hangman.py
Name: Yvonne Chan
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game.
    """
    ans = random_word()
    dash = ''
    new_turns = N_TURNS

    for i in range(len(ans)):
        dash += '-'
    print('The word looks like ' + dash)
    print('You have ' + str(N_TURNS) + ' wrong guess left.')
    input_ch = input('Your guess: ')
    input_ch = input_ch.upper()
    guess_word = dash

    while True:
        if len( input_ch) > 1 or not input_ch.isalpha():
            # 判斷使用者輸入的格式錯誤
            print('Illegal format.')
            input_ch = input('Your guess: ')
        else:
            if ans.find( input_ch) != -1:
                guess_word = replace(guess_word, input_ch, ans)
                if guess_word == ans:
                    print('You are correct!')
                    print('You win!')
                    break
                else:
                    print('You are correct!')
                    print('The word looks like ' + guess_word)
                    print('You have ' + str(new_turns) + ' wrong guess left.')
            else:
                new_turns -= 1  # 錯誤答案，玩家少一條命
                if new_turns != 0:
                    print('There is no ' + input_ch + "'s in the world.")
                    print('The word looks like ' + guess_word)
                    print('You have ' + str(new_turns) + ' wrong guess left.')
                else:
                    print('There is no ' + input_ch + "'s in the world.")
                    print('The word looks like ' + guess_word)
                    print('You are completely hung:(')
                    break
            input_ch = input('Your guess: ')
            input_ch = input_ch.upper()
    print('The word was: ' + ans)


def replace(old_guess, input_ch, ans):
    guess_word = ''
    for i in range(len(ans)):
        if input_ch != ans[i]:
            guess_word += old_guess[i]
        else:
            guess_word += input_ch
    return guess_word


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
