# -*- coding: utf-8 -*-

import math
from vector_2D.vector import Vector
from vector_2D.vectorPolar import VectorPolar


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
        alpha = math.atan(a(1) / a(0))
        beta = math.atan(b(1) / b(0))
    except ZeroDivisionError:
        return math.pi * 0.25
    return abs(alpha - beta)


def vector(a, b):
    return (a[0] - b[0]), (a[1] - b[1])


def perpendiculars(u):

    p = Vector(-u(1), u(0)), Vector(u(1), -u(0))
    print u, -u(1), u(0), p
    return p


def forty_fivers(u, sep):
    # print u, perpendiculars(u)
    return [(p - u*2) * sep for p in perpendiculars(u)]
