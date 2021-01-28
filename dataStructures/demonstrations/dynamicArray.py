import numpy as np
import copy



#TODO
# 2. create a counting sort
# 3. a bash shell script that would run in the terminal each data structure
# with a visible output in the terminal? would be really cool

def countingSort():
    """
    Implementing the countingSort()
    """

    pass


class DynamicArray:
    """
    Dynamic array data structure made from static arrays (buckets).
    This is an  unsorted dynamic array, and weirder since during inserts and deletes values are swapped with the end of the array
    """
    def __init__(self, size=4):
        """
        variables:
        __init__(self, size=4)
        - self.size (size of the array buckets)
        - self.array = np.empty(size) (the inital empty array)
        - self.lastValueIndex (keeps track of the number of items in the bucket)
        """
        if size==0:
            raise ValueError(f'You created 1D static array of size(1,{size})\nPlease choose a size >= 1')
        self.size = size
        self.array = np.empty(size) #reminder(y,x) limits: arr[0,size-1]
        # self.array = np.empty([1,self.size]) # old way
        # Because np empty array are initialised entries we replace them with np.nan (to make life easier)
        self.array[:] = np.nan
        self.lastValueIndex = 0


    def append(self, val):
        """
        Check if there is room in the static bucket and if so adds it to the bucket.
        If no room exist it will double the size of the bucket

        Input:
            - value to be insert
        Output: 
            - 
        """
        # checking for space in the static array 
        if self.lastValueIndex > (self.array.shape[0] - 1):
            self.expand() 
        # adding the value to the end of the array 
        self.array[self.lastValueIndex] = val
        # updating the array
        self.lastValueIndex += 1

    def display(self):
        """
        displays all elements in the dynamic list and bucket size

        Input:
            - value to be insert
        Output: 
            - 
        """
        print(f' Element in the array: {self.array}\nbucket size: {self.size}\nlast value pointer location: {self.lastValueIndex}')

    def expand(self):
        """
        class method to double the original size of the array. 

        Input:
            - 
        Output:
            - 
        """
        # creating a new empty bucket double the size of the original
        self.size = self.size * 2
        temp = copy.deepcopy(self.array) # copy will not do because we reinit the array instance
        # init the array with the new size
        self.array = np.empty(self.size)
        self.array[:] = np.nan
        # repopulating the new array from old to new (using the old.shape for the range)
        for i in range(temp.shape[0]):
            self.array[i] = temp[i]
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
        # init the array with the new size
        self.array = np.empty(self.size)
        self.array[:] = np.nan
        # repopulating the new array from old to new (using the new.shape for the range)
        for i in range(self.array.shape[0]):
            self.array[i] = temp[i]


    def search(self, val):
        """
        Search the array and find the index where the value appears. 
        Note if more than one is found it will return them all

        Input:
            - value of the search
        Output: 
            - list of index where the value is present
        """
        return [i for i in range(self.lastValueIndex) if self.array[i]==val]


    def delete(self,val,delAll='no'):
        """
        Search for the value to be deleted, and deletes it

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
                self.array[valueIndex] = np.nan
                # switch the position of the value to be deleted with the 
                # if more than one item has to be delete the (self.lastValueIndex-backIndex) allows us to move from the back of the array toward the front
                self.array[(self.lastValueIndex-(backIndex+1))], self.array[valueIndex] =  self.array[valueIndex], self.array[(self.lastValueIndex-(backIndex+1))]        # since we know the 
                self.lastValueIndex -= 1
                if delAll=='no':
                    # default option is to delete a single value so we exit the for loop
                    break
            if self.lastValueIndex < (self.array.shape[0]//2):
                self.shrink()  


    def insert(self, val, index):
        """
        navigates to the index of the value to be inserted. Move the current value to the last index and then inserts the new value to the index position

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
        if self.lastValueIndex > (self.array.shape[0] - 1):
            self.expand() 
        # swap value     
        temp = self.array[index]
        self.array[index] = val
        self.array[self.lastValueIndex] = temp
        self.lastValueIndex+=1

