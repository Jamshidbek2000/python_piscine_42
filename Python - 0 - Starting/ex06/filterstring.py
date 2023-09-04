import sys
from ft_filter import ft_filter


def str_to_int(s) -> int:
    """
    Takes an argument, tries converting to int
    in sucsess returns the int
    if fails returns None
    """

    try:
        return int(s)
    except ValueError:
        return None


def main():
    """
    The program accepts 2 arguments.
    1: str S. 2: int N.
    The program prints all words inside S which are
    longer than N.
    If other arguments are passed it prints error message and quits.
    """

    minWordlen = 0
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        minWordlen = str_to_int(sys.argv[2])
        if minWordlen is None:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print("Assertion error:", e)
        return

    words = sys.argv[1].split(" ")
    filtered_sentence = []

    filtered_sentence = ft_filter(lambda word: len(word) > minWordlen, words)
    print(filtered_sentence)


if __name__ == "__main__":
    main()
