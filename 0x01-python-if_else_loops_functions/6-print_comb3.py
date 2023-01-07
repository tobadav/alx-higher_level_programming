#!/usr/bin/python3
for f in range(0, 10):
    for s in range(1, 10):
        if s > f:
            print("{}{}".format(f, s), end='')
            if int(str(f) + str(s)) != 89:
                print(end=",")
print()
