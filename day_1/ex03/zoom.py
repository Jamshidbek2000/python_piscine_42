from load_image import ft_load
from load_image import open_img
import matplotlib.pyplot as plt
import numpy as np


def print_rows_firstelem(arr, int):
    """
    Print a formatted display of the first elements
    in each row of a given array.

    Parameters:
    arr (array-like): The input array containing elements to be displayed.
    int (int): An integer specifying the display format: 0 for single brackets,
               1 for triple brackets.

    Iterates through the rows of the input array and displays the first
    elements of each row in a formatted manner. The display format is
    determined by the 'int' parameter. For 'int' equal to 0, single
    brackets are used to enclose the elements, while for 'int' equal
    to 1, triple brackets are used.
    """
    count = 0
    for row in arr:
        count += 1
    length = count
    count = 0
    for row in arr:
        if count == 0:
            if int == 1:
                print("[[", row[0], sep="")
            else:
                print("[[[", row[0], "]", sep="")
        if count > 0 and count < 3 or count > length - 4:
            if int == 1:
                if count == length - 1:
                    print("  ", row[0], "]]", sep="")
                elif count < length - 1:
                    print("  ", row[0], sep="")
            else:
                if count == length - 1:
                    print("  [", row[0], "]]]", sep="")
                else:
                    print("  [", row[0], "]", sep="")
        if count == 2:
            print("  ...")
        count += 1


def main():
    """
    Load an image, crop it, convert it to grayscale, and show the results.

    Args:
        None.

    Returns:
        None.

    Description:
        This function is the entry point for the program.
        It loads the image from the file `animal.jpeg`,
        crops it to a smaller size, converts it to grayscale,
        and shows the results.

    Raises:
        AssertionError: If the image file is not found or
        is not in a supported format.
        Exception: If an error occurs during image processing.
    """
    try:
        path = "animal.jpeg"
        image = open_img(path)
        ft_load(path)
        print_rows_firstelem(np.array(image), 1)
        image.show()

        zoomed_image = image.crop((400, 100, 800, 600))
        zoomed_image.save("zoomed_image.jpg")

        grayscale_image = zoomed_image.convert("L")
        grayscale_image.save("greyscale_image.jpg")
        grayscale_image.show()

        new_width, new_height = grayscale_image.size
        new_layers_size = len(grayscale_image.split())
        print(f"New shape after slicing {grayscale_image.size}\
              or ({new_width, new_height, new_layers_size})")
        print_rows_firstelem(np.array(grayscale_image), 0)

        plt.imshow(zoomed_image)
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
