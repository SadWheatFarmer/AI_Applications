########################################################################
# Objective: Example of unit testing
#               Test File
#
# To Run Test: 'Run' this file - Test file.
########################################################################

import unittest
from myModule import square, double, add


class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3.0), 9)
        self.assertEqual(square(-3), 9)


class TestDouble(unittest.TestCase):
    def test1(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(-3.1), -6.2)
        self.assertEqual(double(0), 0)


class TestAdd(unittest.TestCase):
    def test1(self):
        self.assertEqual(add(2,4), 6)
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(2.3,3.6), 5.9)
        self.assertEqual(add('hello','world'), 'helloworld')
        self.assertEqual(add(2.3,4.3), 6.6)
        self.assertNotEqual(add(-2,-2), 0)

if __name__ == '__main__':
    unittest.main()
