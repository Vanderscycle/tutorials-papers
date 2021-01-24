import unittest
import logging
# custom py module import
from linkedList import (
    Node,
    SinglyLinkedList,
    DoublyLinkedList
)

class TestLinkedList(unittest.TestCase):
    """
    class that confirms the good working of the following method for the dynamic array class
        - insert
        - search
        - append        
        - delete
        - display (is it really a test tho?)
    """
    def setUp(self):
        # node creation
        # [10, 12, 14, 16, 18]
        self.nodes = [Node(i) for i in range(10,20,2)]
        # linked list creation
        self.singleList = SinglyLinkedList()
    

    def test_append(self):
        print('testing append method')
        print('singly linked lists')

        self.singleList.append(self.nodes[0])#10
        self.singleList.append(self.nodes[1])#12
        self.assertEqual(self.singleList.tail.value, 12)
        self.singleList.append(self.nodes[4])#12
        self.assertEqual(self.singleList.tail.value, 18)
        self.singleList.append(self.nodes[2])#12

    def test_search(self):
        print('testing search method')
        print('singly linked lists')

        self.setUp()
        print('list size:',self.singleList.listSize)#?? like the listsize is not reset between instances what?
        self.singleList.listSize = 0
        print('list size:',self.singleList.listSize)
        self.singleList.display()

        for i in range(len(self.nodes)):
            print('list size:',self.singleList.listSize)
            self.singleList.append(self.nodes[i])
        self.assertEqual(self.singleList.search(16), (3,16))
        self.assertEqual(self.singleList.search(14), (2,14))        


    def test_insert(self):
        print('testing insert method')
        print('singly linked lists')
        print('list size:',self.singleList.listSize)
        self.singleList.insert(self.nodes[3],0)
        self.singleList.insert(self.nodes[4],1)
        self.singleList.insert(self.nodes[5],1)
        


    # def test_delete(self):
    #     pass

# if __name__ == '__main__':
#     unittest.main()