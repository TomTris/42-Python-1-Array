import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
	for xD in family:
		if xD.__class__ != list:
			print("Error")
			return []
		for nbr in xD:
			if nbr.__class__ != int:
				print("Error")
				return []
	family = np.array(family)
	print("My shape is :", family.shape)
	family = family[start:end]
	print("My new shape is :", family.shape)
	return family.tolist()
