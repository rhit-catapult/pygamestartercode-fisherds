import rosegraphics
import math

import random


def variables():
    print("----- Variables (i.e. names) -------")

    x = 7

    b = "Bob"

    print(x + 3)

    print(b * 3)

    print(type(x))

    print(type(b))


def strings():
    print("----- Strings -------")

    str1 = "Don't"

    str2 = 'Dave'

    str3 = """ Allows

   multiple

   lines even!"""

    str4 = ''' Allows

   single or double triples. use " or ' or whatever '''

    print(str1, str2, str3, str4)

    x = 42

    str5 = f"X equals {x}. Fun."

    print(str5)


def loops():
    print("----- Loops -------")

    for k in range(5):
        print(k)

    total = 0

    for k in range(101):
        total = total + k

    print(f"The numbers 1 to 100 add up to {total}.")

    x = 0

    while True:

        x += 1

        if x > 5:
            break

    print(f"x is equal to {x}")


def sequences():
    print("----- Sequences -------")

    my_list = [4, 5, 6, 7]

    print(my_list)

    my_list[2] = 99

    my_list.append(101)

    print(my_list)

    print(f"The length of the list is {len(my_list)}.")

    for k in range(len(my_list)):
        my_list[k] = my_list[k] + 10

    print(my_list)

    total = 0

    for value in my_list:
        total += value

    print(f"The total value of all items is {total}")


def imports():
    print("\n--- Imports ---")

    print(math.cos(2))

    print(random.randrange(4, 10))


class Point():

    def __init__(self, x, y):
        self.x = x

        self.y = y

    def move(self, x, y):
        self.x = self.x + x

        self.y = self.y + y

    def swap_values(self):
        t = self.x

        self.x = self.y

        self.y = t


def classes():
    print("\n--- Classes ---")

    p1 = Point(3, 5)

    p2 = Point(4, 6)

    print(p1.x, p1.y, p2.x, p2.y)

    p1.move(1, 100)

    print(p1.x, p1.y, p2.x, p2.y)

    p1.swap_values()

    print(p1.x, p1.y, p2.x, p2.y)


def main():
    print("Syntax reference guide:")

    variables()

    strings()

    sequences()

    loops()

    imports()

    classes()


main()