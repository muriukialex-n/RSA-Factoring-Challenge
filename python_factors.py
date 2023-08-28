#!/usr/bin/python3
import sys

def factorize(number):
    for i in range(2, number):
        if number % i == 0:
            return i, number // i
    return None, None

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            p, q = factorize(number)
            if p and q:
                print(f"{number}={p}*{q}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
    else:
        filename = sys.argv[1]
        main(filename)
