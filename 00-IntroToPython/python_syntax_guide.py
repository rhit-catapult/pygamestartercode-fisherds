
def variables():
    print("----- Variables (i.e. names) -------")
    x = 7
    b = "Bob"
    print(x + 3)
    print(b * 3)


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


def main():
    # This line is a comment.  The next line is Python code.
    print("Python Syntax Guide!")
    variables()
    strings()


main()
