#!/usr/bin/python3
def fizzbuzz():
    for fizzbuzz in range(1, 100):
        if fizzbuzz % 15 == 0:
            print("FizzBuzz", end=" ")
            continue
        elif fizzbuzz % 3 == 0:
            print("Fizz", end=" ")
            continue
        elif fizzbuzz % 5 == 0:
            print("Buzz", end=" ")
            continue
        print(fizzbuzz, end=" ")
