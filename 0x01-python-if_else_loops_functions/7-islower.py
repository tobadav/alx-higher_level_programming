#!/usr/bin/python3

def islower(c):
    for i in c:
        if ord(c) >= 97 and ord(c) <= 122:
            return True
        elif ord(c) >= 65 and ord(c) <= 90:
            return False
