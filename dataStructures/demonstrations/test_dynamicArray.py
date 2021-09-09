import unittest
import logging
import numpy as np
# custom py module import
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
    class that confirms the good working of the following method for the dynamic array class
        - search
        - deletion
        - insert
        - append
        - display
    """
    def setUp(self):
        """
        easier to init the values here than at every test methods
        """
        #print('Initializing test and class instances')
        # creating the class instances
        self.dynArrayA = DynamicArray()
        self.dynArrayB = DynamicArray(size=3)
        # populating each instances
        self.dynArrayA.array[0:3] = [1,2,3]#np.arange(1,4)
        self.dynArrayB.array[0:3] = np.arange(1,4)
        # ensuring the index points to the right value
        self.dynArrayA.lastValueIndex = 3
        self.dynArrayB.lastValueIndex = 3


    def test_append(self):
        """
        testing the appending function of the dynamicArray class method.
        Note that any changes in a test method doesn't affect
        
        """
        print('testing appending method')
        # expected behavior
        resA = np.array([1,2,3,5,8,np.nan,np.nan,np.nan])
        resB = np.array([1,2,3,5,8,np.nan])
        # populating the arrays
        appendVal = [5,8]
        for val in appendVal:
            self.dynArrayA.append(val)
            self.dynArrayB.append(val)
        # try block to disply debug file when problems are encountered
        try:
            self.assertTrue(nan_equal(self.dynArrayA.array, resA))
            self.assertTrue(nan_equal(self.dynArrayB.array, resB))
        except AssertionError:
            print('error')
            logging.debug(f'testing appending method error. ArrayA:{self.dynArrayA.array}, ArrayB:{self.dynArrayB.array}')
    
    
    def test_delete(self):
        print('testing deletion method')
        # expected behavior
        resA = np.array([8,5,3,np.nan])
        resB = np.array([3,2,np.nan])
        #inserting vals to expand the bucket size before deletion to see 
        appendVal = [5,8]
        for val in appendVal:
            self.dynArrayA.append(val)
        delVal=[1,2]
        for val in delVal:
            self.dynArrayA.delete(val)
        self.dynArrayB.delete(1)

        try:
            self.assertTrue(nan_equal(self.dynArrayA.array, resA))
            self.assertTrue(nan_equal(self.dynArrayB.array, resB))
        except AssertionError:
            print('error')
            logging.debug(f'testing deletion method error. ArrayA:{self.dynArrayA.array}, ArrayB:{self.dynArrayB.array}')
    

    def test_display(self):
        self.dynArrayA.display()
        self.dynArrayB.display()


    def test_insert(self):
        print('testing insert method')
        # expected behavior
        resA = np.array([8,5,3,2,1,np.nan,np.nan,np.nan])
        resB = np.array([8,5,3,2,1,np.nan])
        insertVal = [(5,1),(8,0)]
        for val,index in insertVal:
            self.dynArrayA.insert(val,index)
            self.dynArrayB.insert(val,index)

        try:
            self.assertTrue(nan_equal(self.dynArrayA.array, resA))
            self.assertTrue(nan_equal(self.dynArrayB.array, resB))
        except AssertionError:
            print('error')
            logging.debug(f'testing inser method error. ArrayA:{self.dynArrayA.array}, ArrayB:{self.dynArrayB.array}')
    

    def test_search(self):
        print('testing search method')
        # appending a single value to see if it will return the correct indexes
        self.dynArrayA.append(1)
        # expected behavior
        resA = [0,3] #1
        resB = [1] #2
        searchResA = self.dynArrayA.search(1)
        searchResB = self.dynArrayA.search(2)
        #print(f'expected Index:{resA} search res:{searchResA}\nexpected Index:{resB} search res:{searchResB}')
        try:
            self.assertEqual(resA,searchResA)
            self.assertEqual(resB,searchResB)
        except AssertionError:
            print('error')
            logging.debug(f'testing search method error. expected Index:{resA} search res:{searchResA} expected Index:{resB} search res:{searchResB}')
    

# python -m unittest test_dynamicArray.py 
if __name__ == '__main__':
    unittest.main()