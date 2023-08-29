import sys
from ft_filter import ft_filter


def str_to_int(s) -> int:
    try:
        return int(s)
    except ValueError:
        return None


def main():
    minWordlen = 0
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are not bad")
        minWordlen = str_to_int(sys.argv[2])
        if minWordlen is None:
            raise AssertionError("the arguments are not bad")
    except AssertionError as e:
        print("Assertion error:", e)
        return

    words = sys.argv[1].split(" ")
    filtered_sentence = []

    filtered_sentence = ft_filter(lambda word: len(word) > minWordlen, words)
    print(filtered_sentence)


if __name__ == "__main__":
    main()
