#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            element = "FizzBuzz"
        elif n % 3 == 0:
            element = "Fizz"
        elif n % 5 == 0:
            element = "Buzz"
        else:
            element = n
        print(element, '', end='')
