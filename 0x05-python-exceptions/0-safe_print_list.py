#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for el in range(x):
        try:
            print("{:d}".format(my_list[el]), end="")
            count = count + 1
        except IndexError:
            break
    print()
    return count
