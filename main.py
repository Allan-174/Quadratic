import math
import sys
import os
import math


def calculate(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    return x1, x2


def main():
    a = 1
    b = 2
    c = 1
    x1, x2 = calculate(a, b, c)
    print(f"x1={x1} ,x2={x2}")
    # Return value of the exit status
    return os.EX_OK


if __name__ == "__main__":
    # exit status sent to the OS
    # 0 Means ok
    sys.exit(main())
