from PIL import Image
from load_image import open_img
import numpy as np
import matplotlib.pyplot as plt


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


def crop_to_square(img):
    """
    Crops an image to a square.

    Args:
        img: The image to crop.

    Returns:
        The cropped image.
    """

    width, height = img.size

    left = width // 2 - 200 + 125
    right = width // 2 + 200 + 125
    top = height // 2 - 200 - 75
    bottom = height // 2 + 200 - 75

    return img.crop((left, top, right, bottom))


def transpose_image(img, degrees):
    """
    Transposes an image.

    Args:
        img: The image to transpose.

    Returns:
        The transposed image.
    """

    img_array = np.array(img)
    height, width = img_array.shape[:2]

    transposed_array = np.empty((width, height, img_array.shape[2]),
                                dtype=np.uint8)
    if degrees == 90:
        for i in range(width):
            for j in range(height):
                transposed_array[i, j] = img_array[j, width - i - 1]
    elif degrees == -90:
        for i in range(width):
            for j in range(height):
                transposed_array[i, j] = img_array[height - j - 1, i]

    transposed_img = Image.fromarray(transposed_array)
    return transposed_img


def mirror_image(img):
    """
    Mirrors an image.

    Args:
        img: The image to mirror.

    Returns:
        The mirrored image.
    """

    width, height = img.size

    mirrored_img = Image.new("RGB", (width, height))
    pixels = list(img.getdata())

    for y in range(height):
        row_pixels = pixels[y * width: (y + 1) * width]
        mirrored_row = row_pixels[::-1]
        for x, pixel in enumerate(mirrored_row):
            mirrored_img.putpixel((x, y), pixel)

    return mirrored_img

def print_rows(arr, int):
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
                print("[[[", row[0], "]", sep="")
            else:
                print("[[", row[0], sep="")
        if count > 0 and count < 3 or count > length - 4:
            if int == 1:
                if count == length - 1:
                    print("  [", row[0], "]]]", sep="")
                elif count < length - 1:
                    print("  [", row[0], "]", sep="")
            else:
                if count == length - 1:
                    print("  ", row[0], "]]", sep="")
                else:
                    print("  ", row[0], sep="")
        if count == 2:
            print("  ...")
        count += 1

def main():
    """
    The main function of the image processing script.

    Function performs several image processing operations on an input image:
    - Crops the input image to a square.
    - Transposes the cropped image by -90 degrees.
    - Mirrors the transposed image horizontally.
    - Converts the mirrored image to grayscale.
    - Saves the processed images as separate files:
    "square_animal.jpg", "rotated_animal.jpg", and "mirrored_animal.jpg".
    - Displays the final mirrored grayscale image using Matplotlib.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: If any error occurs during image processing or saving.
    """

    try:
        img = open_img("animal.jpeg")

        cropped_img = crop_to_square(img)

        width, height = cropped_img.size

        transposed_img = transpose_image(cropped_img, -90)
        transposed_img = transposed_img.convert("L")

        mirrored_img = mirror_image(transposed_img)
        mirrored_img = mirrored_img.convert("L")

        cropped_img.save("square_animal.jpg")
        transposed_img.save("rotated_animal.jpg")
        mirrored_img.save("mirrored_animal.jpg")

        # new_layers_size = len(mirrored_img.split())
        # print(f"New shape of image is", end=" ")
        # print(f"{mirrored_img.size} or ({width, height, new_layers_size})")
        print_rows_firstelem(np.asarray(cropped_img.convert("L")), 1)

        print(np.asarray(transposed_img))

        plt.imshow(mirrored_img)
        plt.title("Mirrored Image")
        plt.axis('on')
        plt.gray()
        # plt.show()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
