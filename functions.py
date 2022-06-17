import random as rdm


def random_color():
    r = rdm.randint(0,255)
    g = rdm.randint(0, 255)
    b = rdm.randint(0, 255)
    rgb = (r, g, b)
    return rgb
