from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
	"""Load """
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
	return (r)


def main():
	print(ft_load("landscape.jpg"))


if __name__ == "__main__":
	main()
