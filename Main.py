import sys
import os


def get_perc(value, basic):
    try:
        return (value / basic) * 100  # p = w/g * 100
    except ZeroDivisionError:
        return "0"


def char_main(char, file):
    counter = 0
    counter_ = -1
    with open(file) as file:
        while True:
            char_ = file.read(1)
            counter_ += 1
            if char_ == char:
                counter += 1

            if not char_:
                break

    print(f'There are : {get_perc(counter, counter_)}% {char}´s in the file ')


def word_main(word, file):
    counter = 0
    counter_ = 0
    with open(file) as file:
        for line in file:
            print(line)
            if word in line:
                counter += 1
            counter_ += 1
    print(counter, counter_)
    print(f'There are : {get_perc(counter, counter_)}% of {word}`s in the file')


if __name__ == '__main__':
    file = input('1. [+] File : ')
    if os.path.isfile(file):
        print("[+] File is valid")
    else:
        print("[!] Please enter a valid file")
        sys.exit(0)
    try:
        char = input('2. [+] Char to search for : ')
        if len(char) > 1:
            word_main(char, file)
        else:
            char_main(char, file)
    except ValueError:
        print("[!] Please enter a valid char / Dont speak chinese")
