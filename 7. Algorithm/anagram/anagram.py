"""
File: anagram.py
Name: Yvonne Chan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program finds all anagrams among the word user inputs.
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')

    ####################
    while True:
        s = str(input('Find anagram for: '))
        if s == EXIT:
            break
        else:
            start = time.time()
            find_anagrams(s)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')

    ####################


def read_dictionary(s):
    word_dic = {}
    word_key = 0

    with open(FILE, 'r') as f:
        for line in f:
            tokens = line.split()
            for token in tokens:
                if len(token) == len(s):
                    word_dic[word_key] = token   # 篩選字典單字, dict越小越好: 只要找幾個字母, 或"沒有哪些字母" -> 還沒寫
                word_key += 1
    print(word_dic)
    return word_dic


def find_anagrams(s):
    """
    :param s: str, the word user inputs.
    :return: target_l: list, the list of all anagrams among the word.
    """
    # s_dict = {}
    current_l = []
    target_l = []
    dic = read_dictionary(s)
    used_index = []

    find_anagrams_helper(s, current_l, target_l, dic, used_index)
    print(f'{len(target_l)} anagrams: {target_l}')


def find_anagrams_helper(s, current_l, target_l, dic, used_index):
    """
    :param s: str, the word user inputs.
    :param current_l: list, the anagram among the word.
    :param target_l: list, all anagrams found.
    :param dic: dict, the dictionary.
    :param used_index: list, the used alphabet.
    :return: target_l: list, the list of all anagrams among the word.
    """
    # s_key = 0
    # for i in list(s):
    #     s_dict[s_key] = list(s)[s_key]
    #     s_key += 1

    if len(current_l) == len(list(s)):
        print('Searching...')
        current_s = ''.join(current_l)
        if current_s not in target_l:
            target_l.append(current_s)
            print(f'Found: {current_s}')

    else:

        for i in range(len(s)):
            if i not in used_index:
                # choose
                current_l.append(s[i])
                used_index.append(i)

                # Explore
                current_s = ''.join(current_l)

                if has_prefix(current_s, dic):
                    find_anagrams_helper(s, current_l, target_l, dic, used_index)

                # un-choose
                current_l.pop()
                used_index.pop()


def has_prefix(sub_s, dic):
    """
    :param sub_s: the starting word to be search for early stopping.
    :param dic: dict, the dictionary.
    :return: boolean
    """
    for key, word in dic.items():
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
