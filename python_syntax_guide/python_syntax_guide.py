import rosegraphics as rg


def names_and_variables():
    print("Variables")
    x = 17
    bob = "Bob"
    print(type(x), type(bob))
    t = rg.SimpleTurtle('turtle')
    print(type(t))
    rect = rg.Rectangle(rg.Point(1,1), rg.Point(2,2))
    print(type(rect), type(rect.corner_1), type(rect.corner_1.x))


def strings():
    str1 = "Don't is a word"
    str2 = 'He said "this is cool"'
    str3 = """   Use whatever "  or '
    even new 
    lines!"""
    print(str1, str2, str3)
    x = 42
    str4 = f"X is {x} seconds."
    print(str4)


def loops():
    weird_test = range(5)
    print(type(weird_test))

    for k in range(5):
        print(k)

    total = 0
    for k in range(100):
        total += k
    print(f"The sum of the integers from 0 to 99 is {total}.")

    x = 0
    while True:
        x += 1
        if x > 5:
            break
    print("x is equal to", x)


def sequences():
    my_list = [1, 2, 3, "Bob"]
    print(my_list)
    print(my_list[0])
    print(type(my_list), type(my_list[3]))
    # print(my_list[4])   # This would be a crash.  There is no index 4!
    print(my_list[-1], my_list[-2])

    # enhanced for loop
    for value in my_list:
        print(value)

    # indexed for loop
    for k in range(len(my_list)):
        print(my_list[k])


class MyPoint:

    def __init__(self, x, y):
        # print("This is the constructor!!!")
        self.x = x
        self.y = y
        self.moves = 0

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy


def classes():
    rosegraphics_point = rg.Point(3, 4)
    print(rosegraphics_point)
    rosegraphics_point.move_by(1, 1)
    print(rosegraphics_point)

    my_point = MyPoint(3, 5)
    print(my_point.x)
    my_point.move_by(2, 2)
    print(my_point.x, my_point.y)
    print(my_point)


def main():
    print("Python Syntax Guide")

    # names_and_variables()
    # print(type(x))  # Crash since x is a name within another function

    # strings()

    # loops()

    # sequences()

    classes()

main()
