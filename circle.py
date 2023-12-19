import math
import unittest

def area_circle(r):
    '''Принимает число r-радиус окружности, возвращает её площадь'''
    return math.pi * r * r


def perimeter_circle(r):
    '''Принимает число r-радиус окружности, возвращает её длину'''
    return 2 * math.pi * r