import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        img = Image.open(path)
        print(
            f"The shape of Image is: {img.size[1]},{img.size[0]}, {img.layers}"
            )
        print("Image format: ", img.format)
        return np.array(img)
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
        return ""

def main():
    ft_load("animal.jpeg")
    ft_load("landscape.jpeg")



if __name__ == "__main__":
    main()
