#Pylint Score: 10/10

"""
Module DocString
"""

def add(number1, number2):
    """
    :param number1:
    :param number2:
    :return:
    """
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print("The sum of {} and {} is {}".format(NUM1, NUM2, TOTAL))
