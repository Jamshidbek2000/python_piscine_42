import sys


def main():
    """
    Converts a text string to Morse code.

    Args:
        text (str): The input text to be converted.

    Returns:
        str: The input text converted to Morse code.

    Raises:
        AssertionError:
        If the input contains characters not supported by Morse code.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are not bad")
    except AssertionError as e:
        print("Assertion error:", e)
        return

    morse_alpha = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', ' ': '/',

        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    input = sys.argv[1]
    sentenceInMorse = ""

    try:
        for ch in input:
            if ch in morse_alpha.keys():
                sentenceInMorse += morse_alpha[ch] + " "
            else:
                raise AssertionError("the arguments are not bad")
    except AssertionError as e:
        print("Assertion error:", e)
        return

    print(sentenceInMorse)


if __name__ == "__main__":
    main()
