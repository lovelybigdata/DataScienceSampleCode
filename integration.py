import math


def horizontal_line(x):
    return 0*x + 5


def integrate(fun, start, end):
    step = 0.1
    new_x = start
    area = 0
    while new_x < end:
        new_x += step
        new_y = fun(new_x)
        area = area + new_y*step
    return area


print integrate(horizontal_line, 0, 10)
