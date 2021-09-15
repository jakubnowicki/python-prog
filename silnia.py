#!/usr/bin/env python

import sys

def silnia(n):
    if n == 1:
        return 1
    return n * silnia(n - 1)

def main():
    if len(sys.argv) < 2:
        print("Podaj liczbe jako argument")
    else:
        print(silnia(int(sys.argv[1])))

if __name__ == "__main__":
    main()