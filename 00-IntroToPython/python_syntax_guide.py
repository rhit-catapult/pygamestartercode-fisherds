import random
import math


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
    print(str1)
    print(str2)
    print(str3)
    print(str4)
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

    total = 1
    for k in range(100):
        total = total * (k + 1)
    print(f"The numbers 1 to 100 multiply to {total}.")

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


def functions(a, b, c):
    print("----- Functions -------")
    print("Input Arguments:", a, b, c)
    return (a + b) / c


def imports():
    print("----- Imports -------")
    print(random.randint(1, 1000))
    print(random.randint(1, 1000))
    print(random.randrange(20, 40, 2))
    print(random.randrange(20, 40, 2))
    print(random.randrange(20, 40, 2))
    print(math.cos(2))
    print(math.cos(3.1415926535897))
    print(math.cos(math.pi))



def main():
    # This line is a comment.  The next line is Python code.
    print("Python Syntax Guide!")
    # variables()
    # strings()
    # loops()
    # sequences()
    # result = functions(2, 3, 1)
    # print(result)
    # result = functions(60, 9, 3)
    # print(result)
    imports()



main()
