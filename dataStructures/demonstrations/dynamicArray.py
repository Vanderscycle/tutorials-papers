import numpy as np
import copy


#! to do
# testing bench class?
# create a counting sort

def countingSort():
    """
    Implementing the countingSort()
    """

    pass


def testBench(cls):
    """
    Would a testing bench class be more apporiate? 
    with class method testing each of the following component:
        - search
        - deletion
        - insert
    """
    pass


class DynamicArray:
    """
    Dynamic array data structure made from static arrays (buckets).
    This is an  unsorted dynamic array, and weirder since during inserts and delete values are swapped
    """
    def __init__(self, size=4):
        """
        create an empty static array bucket
        input:
            - size(optional) being the number of elements in the starting array 
        output: (nothing really)
            - empty one dimensional static numpy array of shape (1,size)
        """
        if size==0:
            raise ValueError(f'You created 1D static array of size(1,{size})\nPlease choose a size >= 1')
        self.size = size
        self.array = np.empty([1,size]) #reminder(y,x) limits: arr[0,size-1]
        self.DyArrSize = (size-1) # because computers are 0 indexed
        self.lastValueIndex = 0

    def appending(self, val):
        """
        Check if there is room in the static bucket. 
        Only insert one item at a time if more than one insertion is required just use a for loop
        Input:
            - value to be insert
        Output: (nothing really)
            - 
        """
        # checking for space in the static array 
        if self.lastValueIndex > (self.array.shape[1] - 1):
            self.expand() 
        # adding the value to the end of the array 
        self.array[0,self.lastValueIndex] = val
        # updating the array
        self.lastValueIndex += 1

    def expand(self):
        """
        class method to double the original size of the array. 
        Input:(internal changes)
            - 
        Output: (nothing really)
            - 
        """
        # creating a new empty bucket double the size of the original
        self.size = self.size * 2
        temp = copy.deepcopy(self.array) # copy will not do because we reinit the array instance
        self.array = np.empty([1,self.size])
        # repopulating the new array from old to new (using the old.shape for the range)
        for i in range(temp.shape[1]):
            self.array[0,i] = temp[0,i]
        # freeing memory
        temp = None

    def shrink(self):
        """
        class method to reduce the array size in half. Similar to expand with a small change to the for loop indexing
        Input:(internal changes)
            - 
        Output: (nothing really)
            - 
        """
        self.size = self.size // 2
        temp = copy.deepcopy(self.array)
        self.array = np.empty([1,self.size])
        # repopulating the new array from old to new (using the new.shape for the range)
        for i in range(self.array.shape[1]):
            self.array[0,i] = temp[0,i]

    def search(self, val):
        """
        Search the array and find the index where the value appears. 
        Note if more than one is found it will return them all
        Input:
            - value of the search
        Output: 
            - list of index where the value is present
        """
        return [i for i in range(self.lastValueIndex) if self.array[0,i]==val]

    def deletion(self,val,delAll='no'):
        """
        Search for the value to be deleted, and
        Input:
            - value to be deleted
            - delAll(y/n) gives the choice
        Output: 
            - 
        """
        searchIndexRes = self.search(val)
        if not searchIndexRes:
            print('Value not present in array')
        else:
            for backIndex, valueIndex in enumerate(searchIndexRes):
                """
                we use the index created from self.search to replace each value
                """
                self.array[0,valueIndex] = np.nan
                # switch the position of the value to be deleted with the 
                # if more than one item has to be delete the (self.lastValueIndex-backIndex) allows us to move from the back of the array toward the front
                self.array[0,(self.lastValueIndex-(backIndex+1))], self.array[0,valueIndex] =  self.array[0,valueIndex], self.array[0,(self.lastValueIndex-(backIndex+1))]        # since we know the 
                self.lastValueIndex -= 1
                if delAll=='no':
                    # default option is to delete a single value so we exit the for loop
                    break
            if self.lastValueIndex < (self.array.shape[1]//2):
                self.shrink()  

    def insert(self, val, index):
        """
        swap the value to be 
        Input:
            - value to be added
            - the index in which it is added
        Output: 
            - 
        """
        # check for improper user passed data
        if index > self.lastValueIndex:
            raise ValueError('out of range request')
        # check if we have enough room in the static array to insert value
        if self.lastValueIndex > (self.array.shape[1] - 1):
            self.expand() 
        # swap value     
        temp = self.array[0,index]
        self.array[0,index] = val
        self.array[0,self.lastValueIndex] = temp
        self.lastValueIndex+=1



# I should create a test bench for each data structures
# A QA wouldn't want to test all this crap manually

test = DynamicArray(size=4)
print(test.array.shape)
print(type(test.array))
print(test.array)
test.appending(2)
test.appending(2)
test.appending(3)
print(test.array)
test.appending(67)
print(test.array)
test.appending(69)
print(test.array)
print(test.search(2))
print(test.search(3))
test.deletion(3)
print(test.array)
test.deletion(2)
test.deletion(1001)
print(test.array)
print(test.array[0,1])
test.insert(900,2)
print(test.array)
test.insert(670,0)
print(test.array)