#!/usr/bin/python3
import math

def polysum(n, s):
    area = (0.25*n*s**2)/math.tan(math.pi/n)
    permiter = n*s
    return round(area + permiter**2, 4)
