import numpy as np
from PIL import Image
import os
import sys


def open_img(path: str) -> Image.Image:
    """
    Open an image file and return it as a PIL Image object.

    Args:
        path (str): The path to the image file.

    Returns:
        Image.Image: The opened image as a PIL Image object.

    Raises:
        AssertionError: If the image file is not found or is not readable.
    """
    if len(path) == 0:
        raise AssertionError("Empty path passed to open_img")
    if not os.path.exists(path):
        raise AssertionError(f"File not found: {path}")
    if not path.lower().endswith(("jpg", "jpeg")):
        raise AssertionError("Only JPG and JPEG formats are supported.")
    if not os.access(path, os.R_OK):
        raise AssertionError(f"No permissions for reading {path}")
    img = Image.open(path)
    return img


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from a file and return it as a NumPy array.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray: The image data as a NumPy array.

    Raises:
        AssertionError: If the image file is not found,
        is not readable, or is not in a supported format.
    """
    img = open_img(path)
    print(
        f"The shape of Image is: {img.size[1]},{img.size[0]}, {img.layers}"
        )
    print("Image format: ", img.format)
    print(np.array(img))
    return np.array(img)


def main():
    try:
        if len(sys.argv) == 1:
            raise AssertionError("Program accepts image as an input")
        if len(sys.argv) > 2:
            raise AssertionError("Program accepts image as an input")

        path = sys.argv[1]
        img_data = ft_load(path)
        print(img_data)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
