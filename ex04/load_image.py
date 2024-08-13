from PIL import Image
import numpy as np


def ft_load() -> np.ndarray:
    """Load image to 3D array"""
    with Image.open("animal.jpeg") as img:
        pixels = img.load()
        width, height = img.size

        print(f"Image size: {width}x{height}")
        ret = []
        ret1 = []
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
    return (r)


def zoom():
    """Zoom image from 100->500, 450->850, 0->1, gray scale"""
    r = ft_load()
    shape = (list)(r.shape)
    if (r.ndim != 3 or shape[0] < 101 or shape[1] < 451 or shape[2] == 0):
        raise Exception("Image format bad, must be 3d,\
                         weight > 1000, height > 450")
    # print("The shape of image is:", r.shape)
    # print(r)
    r = r[100:500:, 450:850, 0:1]
    # print("New shape after slicing is:", r.shape)
    # print(r)
    return r


def main():
    return 1


if __name__ == "__main__":
    main()
