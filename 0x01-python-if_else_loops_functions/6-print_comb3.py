#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if (i != j):
            if i < 8 or j < 9:
                separator = ', '
            else:
                separator = '\n'
            print("{}{}{}".format(i, j, separator), end="")
