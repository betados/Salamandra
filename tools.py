# -*- coding: utf-8 -*-

import math
from vector import Vector


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
    # FIXME esto debería ir dentro de vector y mejor hecho
    try:
        alpha = math.atan(a.get_comps()[1]/a.get_comps()[0])
        beta = math.atan(b.get_comps()[1]/b.get_comps()[0])
    except:
        return 0
    return abs(alpha - beta)


def vector(a, b):
    return (a[0] - b[0]), (a[1] - b[1])


def perpendiculars(u):
    return Vector(-u.get_comps()[1], u.get_comps()[0]), Vector(u.get_comps()[1], -u.get_comps()[0])


def forty_fivers(u, sep):
    f = [Vector(0, 0), Vector(0, 0)]
    ps = perpendiculars(u)
    for i, p in enumerate(ps):
        f[i] = (p - u * 1.5) * sep

    return f
