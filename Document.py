import math


def circle(r: float) -> float:
    """
    Circle area
    :param r:radius (รัศมี)
    :return: float [พื้นที่วงกลม]
    """
    return math.pi * r * r


if __name__ == '__main__':
    c1 = circle(7)  # ctrl + q
    print(c1)
