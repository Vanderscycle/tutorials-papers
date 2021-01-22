import unittest
import logging
import numpy as np
# cust
from dynamicArray import DynamicArray

def nan_equal(arrA,arrB):
    """
    np.testing.assert_equal throw an error when both arrays are not of the same size.
    https://stackoverflow.com/questions/10710328/comparing-numpy-arrays-containing-nan 
    """
    try:
        np.testing.assert_equal(arrA,arrB)
    except AssertionError:
        return False
    return True

logging.basicConfig(filename='test.log',filemode='w',datefmt='%H:%M:%S',level=logging.DEBUG)
class TestDynamicArray(unittest.TestCase):
    """
    class that confirms the good working 
        - search
        - deletion
        - insert
        - appending
    """
    def setUp(self):
        print('Initializing test')
        # creating the class instances
        self.dynArrayA = DynamicArray()
        self.dynArrayB = DynamicArray(size=3)
        # populating each instances
        self.dynArrayA.array[0:3] = [1,2,3]#np.arange(1,4)
        self.dynArrayB.array[0:3] = np.arange(1,4)
        # ensuring the index points to the right value
        self.dynArrayA.lastValueIndex = 3
        self.dynArrayB.lastValueIndex = 3


    def test_appending(self):
        """
        testing the appending function of the dynamicArray class method
        """
        print('testing appending method')
        
        resA = np.array([1,2,3,5,8,np.nan,np.nan,np.nan])
        resB = np.array([1,2,3,5,8,np.nan])

        insertVal = [5,8]
        for val in insertVal:
            self.dynArrayA.appending(val)
            self.dynArrayB.appending(val)
        # try block to disply debug 
        try:
            self.assertTrue(nan_equal(self.dynArrayA.array, resA))
            self.assertTrue(nan_equal(self.dynArrayB.array, resB))
        except AssertionError:
            logging.debug('test bench problems',self.dynArrayA.array,self.dynArrayB.array)
    def test_deletion(self):
        ""
        print((self.dynArrayA.array,self.dynArrayB.array))

# python -m unittest 
if __name__ == '__main__':
    unittest.main()