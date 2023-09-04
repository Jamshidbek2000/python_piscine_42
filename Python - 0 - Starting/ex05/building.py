import sys


def analyze_text(args):
    """Analyze the text content and count the number of
    characters, upper case letters, lower case letters,
    spaces, digits, and punctuation marks.

    Args:
        args (str): The text content to be analyzed.

    Returns:
        None.
    """

    characterCount = 0
    upperCaseCount = 0
    lowerCaseCount = 0
    spaceCount = 0
    digitCount = 0
    punctuationCount = 0

    characterCount += len(args)
    for char in args:
        if (char.isupper()):
            upperCaseCount += 1
        elif (char.islower()):
            lowerCaseCount += 1
        elif (char.isspace()):
            spaceCount += 1
        elif (char.isdigit()):
            digitCount += 1
        elif (char in "!\"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~"):
            punctuationCount += 1

    print("The text contains,", characterCount, "characters:")
    print(upperCaseCount, "upper case letter")
    print(lowerCaseCount, "lower case letter")
    print(punctuationCount, "punctuation marks")
    print(spaceCount, "spaces")
    print(digitCount, "digits")


def main():
    """The main function of the program.
    It takes one argument from terminal and passes to analyze_text()
    If no argument is passed, it asks a user for input
    If more than one arguments are passed, It will print Error

    Args:
        None.

    Returns:
        None.
    """

    try:
        if (len(sys.argv) < 2):
            try:
                args = input("What is the text to count?\n")
                args += "\n"
            except EOFError:
                pass
        elif (len(sys.argv) == 2):
            args = sys.argv[1]
        else:
            raise AssertionError("more than one argument are provided")
    except AssertionError as e:
        print("Assertion error:", e)
        return
    analyze_text(args)


if (__name__ == "__main__"):
    main()
