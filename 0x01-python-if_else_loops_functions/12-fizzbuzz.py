#!/usr/bin/python3
def fizzbuzz():
    for fizzbuzz in range(1, 100):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz".format(), end=" ")
            continue
        elif fizzbuzz % 3 == 0:
            print("Fizz".format(), end=" ")
            continue
        elif fizzbuzz % 5 == 0:
            print("Buzz".format(), end=" ")
            continue
        print("{}".format(fizzbuzz), end=" ")
print(fizzbuzz)
