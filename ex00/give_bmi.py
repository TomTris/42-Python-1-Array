import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Give a list of heights and weight, with help of numpy,\
    it will give a list of bmi. Error when something is wrong,\
    maybe because of 'variable'"""
    if (height.__class__ != list or weight.__class__ != list):
        print("Error")
        ret = np.array([])
        return ret
    for index in height:
        if ((index.__class__ != int and index.__class__ != float)
            or index <= 0):
            print("Error")
            ret = np.array([])
            return ret
    for index in weight:
        if ((index.__class__ != int and index.__class__ != float)
            or index <= 0):
            print("Error")
            ret = np.array([])
            return ret

    try:
        np.seterr(divide='ignore', invalid='ignore')
        height_arr = np.array(height)
        weight_arr = np.array(weight)
        ret = weight_arr / (height_arr ** 2)
        ret = np.where(np.isnan(ret), 0.0, ret)
    except Exception:
        print("Error")
        ret = np.array([])
    return ret.tolist()


def apply_limit(bmi: list[int: float], limit: int) -> list[bool]:
    """Give a list of int/float numbers (bmi),\
        returns value bigger than limit"""
    try:
        bmi_arr = np.array(bmi)
        ret = bmi_arr > limit
        return ret.tolist()
    except Exception:
        print("Error")
        return []


def main():
    print("use tester.py")


if __name__ == "__main__":
    main()
