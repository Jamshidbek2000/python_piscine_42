import sys


def str_to_int(s) -> int:
    try:
        return int(s)
    except ValueError:
        return None


try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 1:
        exit(0)
    number = str_to_int(sys.argv[1])
    if number is None:
        raise AssertionError("argument is not an integer")
except AssertionError as e:
    print("AssertionError:", e)
    exit()

if (number % 2) == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
