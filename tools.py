import math


def distance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


def modulo(v):
    return distance((0, 0), v)


def unit_v(a, b):
    d = distance(a, b)
    return (a[0]-b[0])/d, (a[1]-b[1])/d