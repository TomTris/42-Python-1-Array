import array
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> array:
    """Create inverted image"""
    arr1 = array.copy()
    arr1 = 255 - arr1
    plt.imshow(arr1)
    plt.show()
    return arr1


def ft_red(array) -> array:
    """Create an image filtered by red"""
    arr1 = array.copy()
    arr1[:, :, 1] = 0
    arr1[:, :, 2] = 0
    plt.imshow(arr1)
    plt.show()
    return arr1


def ft_green(array) -> array:
    """Create an image filtered by green"""
    arr1 = array.copy()
    arr1[:, :, 0] = 0
    arr1[:, :, 2] = 0
    plt.imshow(arr1)
    plt.show()
    return arr1


def ft_blue(array) -> array:
    """Create an image filtered by blue"""
    arr1 = array.copy()
    arr1[:, :, 0] = 0
    arr1[:, :, 1] = 0
    plt.imshow(arr1)
    plt.show()
    return arr1


def ft_grey(array) -> array:
    """Create an black-white image"""
    arr1 = array.copy()

    ar1 = arr1[:, :, 0] / 3.3456005353
    ar2 = arr1[:, :, 1] / 1.70357751278
    ar3 = arr1[:, :, 2] / 8.77192982456

    arr = np.sum([ar1, ar2, ar3], axis=0)
    arr1[:, :, 0] = arr
    arr1[:, :, 1] = arr
    arr1[:, :, 2] = arr
    plt.imshow(arr1)
    plt.show()
    return arr1


def main():
    return 1


if __name__ == "__main__":
    main()
