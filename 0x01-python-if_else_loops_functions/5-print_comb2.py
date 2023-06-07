#!/usr/bin/python3
for n in range(0, 100):
    if n < 99:
        seperator = ', '
    else:
        seperator = '\n'
    print("{:0>2}{}".format(n, seperator), end='')
