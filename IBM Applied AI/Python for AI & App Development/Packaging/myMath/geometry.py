import cmath

def area_of_rectangle(length,width):
    """
    :param length: Length of desired rectangle
    :param width: Width of desired rectangle
    :return: Resulting area of inputs
    """
    return length * width

def area_of_circle(radius):
    """
    :param radius: The radius of the desired circle
    :return: Resulting area of circle with inputted radius
    """
    return cmath.pi * (radius ** 2)