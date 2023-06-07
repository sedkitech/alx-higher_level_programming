#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
    lastDigit = -lastDigit
if lastDigit == 0:
    lastOutput = 'and is 0'
elif lastDigit < 6:
    lastOutput = 'and is less than 6 and not 0'
else:
    lastOutput = 'and is greater than 5'
print(f"Last digit of {number} is {lastDigit} {lastOutput}")
