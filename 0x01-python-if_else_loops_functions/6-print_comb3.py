#!/usr/bin/python3
for nb in range(0, 100):
    for nb2 in range(0, 100):
        if (str(nb) == (str(nb2)[::-1])):
            continue
        else:
            print("{:02d}, ".format(nb), end="")
print("{}\n".format(nb), end="")
