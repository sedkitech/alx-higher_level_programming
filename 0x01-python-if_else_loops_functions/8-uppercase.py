#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if (97 <= ord(letter) <= 129):
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print(end="\n")
