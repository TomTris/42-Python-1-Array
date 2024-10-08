from PIL import Image
import numpy as np
# import matplotlib.pyplot as plt


def ft_load(path: str) -> np.ndarray:
    """Load """
    if (path.__class__ != str):
        raise Exception("Argument not a string")
    try:
        with Image.open(path) as img:
            pixels = img.load()
            width, height = img.size

            print(f"Image size: {width}x{height}")
            ret = []
            a = 0
            for i in range(height):
                if a == 0:
                    a = 1
                else:
                    ret.append(ret1)
                ret1 = []
                for j in range(width):
                    ret1.append(pixels[j, i])
        ret.append(ret1)
        r = np.array(ret)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    print(r)
    return r


def main():
    ft_load("tester.py")


if __name__ == "__main__":
    main()
