#!/usr/bin/python3
def fizzbuzz():
    for fizzbuzz in range(1, 100):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print(f"FizzBuzz", end=" ")
            continue
        elif fizzbuzz % 3 == 0:
            print(f"Fizz", end=" ")
            continue
        elif fizzbuzz % 5 == 0:
            print(f"Buzz", end=" ")
            continue
        print("{}".format(fizzbuzz), end=" ")
