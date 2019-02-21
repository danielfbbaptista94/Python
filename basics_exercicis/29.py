from math import pi, pow


def sphere_volume(h, r=10):
    return ((4*pi*pow(r, 3)/3) - (pi*pow(h, 2)*(3*r-h)) / 3)


h = 2

print(sphere_volume(h))
