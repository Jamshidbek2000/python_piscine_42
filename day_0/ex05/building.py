import sys


def main():
    characterCount = 0
    upperCaseCount = 0
    lowerCaseCount = 0
    spaceCount = 0
    digitCount = 0
    punctuationCount = 0
    args = ""

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
            raise AssertionError("Too many arguments")
    except AssertionError as e:
        print("Assertion error:", e)
        return

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


if (__name__ == "__main__"):
    main()
