import math


def distance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


def modulo(v):
    return distance((0, 0), v)


def unit_vector(a, b):
    d = distance(a, b)
    if d == 0:
        return 0, 0
    x, y = vector(a, b)
    return x / d, y / d


def cosTh(a, b, c):
    try:
        return math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    except Exception as e:
        print(e)
        return 1


def angle(a, b):
    alpha = math.atan(a[1]/a[0])
    beta = math.atan(b[1]/b[0])
    return abs(alpha - beta)


def vector(a, b):
    return (a[0] - b[0]), (a[1] - b[1])


def perpendiculars(u):
    return (-u[1], u[0]), (u[1], -u[0])


def forty_fivers(u, sep):
    f = [[0, 0], [0, 0]]
    ps = perpendiculars(u)
    for i, p in enumerate(ps):
        for j in range(2):
            f[i][j] = (p[j] - u[j] * 1.5) * sep

    return f
