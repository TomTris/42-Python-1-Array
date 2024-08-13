import matplotlib.pyplot as plt
from load_image import zoom


def rotate():
    """Rotate animal.jpeg"""
    try:
        img_arr = zoom()
        ret = []
        width = img_arr.shape[0]
        print(width)
        for i in range(width):
            ret.append(img_arr[::, i])

        plt.imshow(ret, cmap='gray')
        plt.show()
    except Exception as e:
        print(f"Error occurs {e}")
    return 1


def main():
    return 1


if __name__ == "__main__":
    main()
