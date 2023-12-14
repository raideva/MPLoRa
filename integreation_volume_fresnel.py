import math
import numpy


def area_occupied(x, d, hr, ht):
    h = (hr * x + ht * (d - x)) / d
    r = math.sqrt(2) * 17.3 * numpy.sqrt((x * (d - x)) / (868 * d))
    if h >= r:
        return 0, numpy.pi * r * r
    val = (r * r * numpy.arccos(h / r)) - (h * r * numpy.sqrt(1 - (h / r) ** 2))
    return val, numpy.pi * r * r


def integrate(hr, ht, d, steps=1000):
    s = 0
    t = 0
    for i in range(1, steps):
        a, b = area_occupied(d * i / steps, d, hr, ht)
        s += a
        t += b
    return s / t

