#!/usr/bin/python3
for nb in range(0, 100):
    if (nb < 10):
        print("0", end="")
    if (nb < 99):
        print("{}, ".format(nb), end="")
    else:
        print("{}\n".format(nb), end="")
