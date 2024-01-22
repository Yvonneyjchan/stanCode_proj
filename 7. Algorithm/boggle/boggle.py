"""
File: boggle.py
Name: Yvonne Chan
----------------------------------------
Boggle game which finds all possible characters among 4x4 letters that user inputs.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ROW = 4
NEIGHBORS = [(-1, -1), (0, -1), (1, -1), (1, 0), (-1, 0), (-1, 1), (0, 1), (1, 1)]


def main():
    """
    Finds all possible characters among 4x4 letters that user inputs.
    """

    start = time.time()

    current_r = []  # ['fycl', 'iomg', 'oril', 'hjhu']
    for i in range(ROW):
        row = input(f'{i + 1} row of letters: ')

        while len(row) != (ROW * 2 - 1) or blank(row) != (ROW - 1):  # 7表示4個字母+3個空白
            print('Illegal input')
            row = input(f'{i + 1} row of letters: ')

        current_letter = ''  # 'fycl'
        for letter in row:
            if letter != ' ':  # 不是空白, 是字母
                current_letter += letter.lower()
        current_r.append(current_letter)

    if len(current_r) == ROW:
        find_boggle(current_r)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def blank(s):
    count_b = 0
    for i in s:
        if i == ' ':  # 是空白
            count_b += 1
    return count_b


def read_dictionary(s):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    word_d = []

    with open(FILE, 'r') as f:
        for line in f:
            tokens = line.split()
            for token in tokens:
                if len(token) >= ROW:  # 只存>=4(ROW)的單字
                    word_d.append(token)

    return word_d


def find_boggle(current_r):
    letters = {}
    for x in range(len(current_r)):
        for y in range(len(current_r)):
            if current_r[x][y] not in letters:
                letters[current_r[x][y]] = 1
            else:
                letters[current_r[x][y]] += 1

    dic = read_dictionary(letters)

    results = []

    for x in range(len(current_r)):
        for y in range(len(current_r)):
            found_l = []  # 空list放在loop裡, 單字才不一直重複加
            used_l = [(x, y)]  # 如果不放裡面loop, x和y會沒被算到
            results += find_boggle_helpers(current_r, current_r[x][y], dic, x, y, used_l, results, found_l)

    # for result in results:
    #     print(f'Found "{result}')
    print(f'There are {len(results)} words in total.')


def find_boggle_helpers(current_r, cur, dic, x, y, used_l, results, found_l):
    if cur in dic and cur not in found_l:
        found_l.append(cur)
        print(f'Found "{cur}"')  # 放到cur, 才會有每找到一個單字print一次的效果

    for dx, dy in NEIGHBORS:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= 3 and 0 <= ny <= 3:  # 如果不限制nx和ny(代表下一個的x和y, 就會有over range的nx和ny)
            if in_game(nx, ny, current_r) and (nx, ny) not in used_l:

                cur += current_r[nx][ny]
                used_l.append((nx, ny))

                if has_prefix(cur, dic):
                    find_boggle_helpers(current_r, cur, dic, nx, ny, used_l, results, found_l)

                cur = cur[:-1]
                used_l.pop()
    return found_l


def in_game(x, y, current_r):
    return 0 <= x < len(current_r) and 0 <= y <= len(current_r[x])


def has_prefix(sub_s, dic):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dic:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
