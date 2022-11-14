import sys
import os
from itertools import chain


def get_perc(value, basic) -> int:
    try:
        return (value / basic) * 100  # percent = w/g * 100
    except ZeroDivisionError:
        return 0


def char_main(char, file):
    counter: int = 0
    counter_: int = -1
    with open(file) as file:
        while True:
            char_ = file.read(1)
            counter_ += 1
            if char_ == char:
                counter += 1

            if not char_:
                break

    print(f'There are : {get_perc(counter, counter_)}% {char}´s in the file ')


def word_main(word: str, file: str):
    counter: int = 0
    arr_: list = []
    for line in open(file):
        res: list = line.lower().split()
        arr_.append(res)
    for i in arr_:
        for _ in i:
            if _ == word:
                counter += 1
    flat_list: list = list(chain(*arr_))
    print(f'There are : {get_perc(counter, len(flat_list))}% of {word}`s in the file')
    print("The are : ", len(flat_list), "words in the file and : ", counter, word, "`s")


if __name__ == '__main__':
    file: str = input('1. [+] File : ')
    if os.path.isfile(file):
        print("[+] File is valid")
    else:
        print("[!] Please enter a valid file")
        sys.exit(0)
    try:
        char: str = input('2. [+] Input char / word : ').lower()
        if len(char) > 1:
            word_main(char, file)
        else:
            char_main(char, file)
    except ValueError:
        print("[!] Please enter a valid char")
