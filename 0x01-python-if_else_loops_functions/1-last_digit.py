#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nb_str = repr(number)
last_digit = int(nb_str[-1])
if number < 0:
    checkNumber = last_digit * (-1)
else:
    checkNumber = last_digit

if (checkNumber < 6 and checkNumber != 0):
    msg = "and is less than 6 and not 0"
elif (checkNumber == 0):
    msg = "and is 0"
else:
    msg = "and is greater than 5"

print(f"Last digit of {number} is {checkNumber} {msg}")
