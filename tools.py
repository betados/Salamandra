import math


def distance(a, b):
    return math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))


def modulo(v):
    return distance((0, 0), v)


def unit_v(a, b):
    d = distance(a, b)
    if d == 0:
        return 0, 0
    return (a[0]-b[0])/d, (a[1]-b[1])/d


def perpendiculars(u):
    return (-u[1], u[0]), (u[1], -u[0])


def forty_fivers(u):
    f = [[0, 0], [0, 0]]
    ps = perpendiculars(u)
    for i, p in enumerate(ps):
        for j in range(2):
            f[i][j] = (p[j] - u[j]) * 10

    return f
