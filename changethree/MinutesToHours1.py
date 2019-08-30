#!/usr/bin/env python3

import sys

def Hours():
    if len(sys.argv) < 2:
        print("Wrong parameter.")
        print("python3 MinutersToHours.py number")
        sys.exit(1)
    else:
        if sys.argv[1].isdigit() and int(sys.argv[1]) >= 0:
            h = int(sys.argv[1]) // 60
            m = int(sys.argv[1]) % 60
            print("{} H, {} M".format(h, m))
        else:
            raise ValueError("A value error happened.")

if __name__ == '__main__':
    try:
        Hours()
    except ValueError:
        print("Parameter Error")
