from load_image import ft_load
import matplotlib.pyplot as plt


def zoom(path: str):
    """Zoom image from 100->500, 450->850, 0->1, gray scale"""
    try:
        r = ft_load(path)
        shape = (list)(r.shape)
        if (r.ndim != 3 or shape[0] < 101 or shape[1] < 451 or shape[2] == 0):
            raise Exception("Image format bad, must be 3d,\
                            weight > 1000, height > 450")
        print("The shape of image is:", r.shape)
        print(r)
        r = r[100:500:, 450:850, 0:1]
        print("New shape after slicing is:", r.shape)
        print(r)
        plt.imshow(r, cmap="grey")
        plt.show()
    except Exception as e:
        print(f"An Error occurs: {e}")


def main():
    return 1


if __name__ == "__main__":
    main()
