####################################
#Objective: Outline template for unit testing python scripts
#
#
#
####################################

# Needed Modules
import unittest

# Import the src file or functions we are testing
#import exSrcFile

# Create a UnitTest class instance
class TestMyModule(unittest.TestCase):
    #Passing Test
    def test_fctName1(self):
        #stuff
        self.assertEqual(1,1)

    #Failing Test
    def test_fctName2(self):
        #stuff
        self.assertEqual(2,1)

if __name__ == '__main__':
    unittest.main()