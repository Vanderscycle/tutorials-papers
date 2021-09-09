from rich import (
    print
    )
class ListNode:
    """
    The class node can be used for both singly and doubly linked list. 
    """
    def __init__(self,val):
        """
        Variables:
        - __init__(self,val)
        - self.value (or the key used in search to access the node)
        - self.data (the data you want the node to contain. can be a JSON, dict, list, a single variable, etc.)
        - self.nodeIndex (the node automatically given by the linked list class)
        - self.rightNode = None (pointers for the class)
        - self.leftNode = None (pointers for the class)
        """
        self.value = val # More like the key of the Node
        self.data = None # whatever data the user wants
        self.nodeIndex = None # the nodeIndex will be assigned when assigned to a linked list
        self.rightNode = None
        self.leftNode = None


class SinglyLinkedList:
    """
    class methods:
        - append = Add an element at the end of the list
        - Insert(3) − Adds an element at the beginning of the list/middle to end
        - Delete(3) − Deletes an element at the beginning of the list/middle to end
        - Display − Displays the complete list.
        - Search − Searches an element using the given key.
        - Delete − Deletes an element using the given key.
    class variable:
        - SinglyLinkedList.listSize (the amount of nodes in the class instance)
    """
    listSize = 0    


    def __init__(self):
        """
        variables
        __init__(self):
        - self.head = None (class pointers)
        - self.tail = None (class pointers)
        """
        self.head = None 
        self.tail = None


    def append(self,nextNode):
        """
        append(self,nextNode)
        description:
            - Appends a node to the end SinglyLinkedList

        input:
            - ListNode class instance to be inserted
        output: 
            - 
        """
        nextNode.nodeIndex = SinglyLinkedList.listSize
        if SinglyLinkedList.listSize == 0:
            
            self.head = nextNode
            self.tail = nextNode
        else:
            self.tail.rightNode = nextNode
            self.tail = nextNode
        SinglyLinkedList.listSize += 1


    def insert(self,node,index):
        """
        insert(self,node,index)
        description:
            - Inserts a node to a specific index of the singly linked list. 
            - Check whether the index is specified to be at the beginning, middle or end of the list
        
        input:
            - LinkedNode class instance to be inserted
            - index value to be insersted 
        output: 
            - 
        """
        cursor = self.head
        # the user specify a value corresponding to the end of the list
        if index == SinglyLinkedList.listSize:
            return self.append(node)
        # user specify to enter a value at the beginning of the list
        elif index == 0:
            # biggest challenge was to realise that the change needed to happen at self.head
            temp = self.head
            self.head = node
            node.rightNode = temp
            Node.nodeIndex = 0
        else:  
            while (cursor!=None) and (cursor.nodeIndex != (index-1)):
                cursor = cursor.rightNode
        
            temp = cursor.rightNode
            cursor.rightNode = node
            node.rightNode = temp
        SinglyLinkedList.listSize += 1
        temp = None
        # we also have to update the node index of each value
        self.resetIndex()


    def delete(self,value):
        """
        delete(self,value)
        description:
            - look for a value in the linked list using the search method
            - unlink, and delete the item found.

        input:
            - node value to be removed. If the value/data is a json we could use the index instead
            or change the value from a number to a PKI or str identifier 
        output: 
            - error message if value doesn't exist
        """
        undesiredNode = self.search(value) # (index,val)
        if not undesiredNode:
            print('about to exit')
            return
        #beginning of the list
        elif undesiredNode[0]==0:
            self.head = self.head.rightNode
        else:
            cursor = self.head 
            # to remove any item at the middle or end you need to traverse the entire list
            while (cursor!=None) and (cursor.nodeIndex != (undesiredNode[0]-1)):
                cursor = cursor.rightNode
            temp = cursor
            cursor = cursor.rightNode
            
            temp.rightNode = cursor.rightNode
        SinglyLinkedList.listSize -=1
        self.resetIndex()

    
    def resetIndex(self):
        """
        resetIndex(self)
        description:
            - navigate the entire linked list to reset its index. (used mostly internally)
            - The index information is not necessary and increases the complexity to O(n) even in O(1) operations
            - Can be removed in the future (scalability depending)

        input:
            - 
        output: 
            - 
        """
        cursor = self.head
        for i in range(SinglyLinkedList.listSize):
            cursor.nodeIndex = i
            cursor = cursor.rightNode
        

    def display(self):
        """
        display(self)
        Iterates throught the entire linked list (head to tail)
        print each nodes with its index and value/ley

        input:
            - 
        output: 
            - 
        """
        cursor = self.head
        print(cursor)
        print('\n(nodeIndex,nodeValue)')
        while cursor != None:
            print(f'({cursor.nodeIndex},{cursor.value})')
            cursor = cursor.rightNode


    def search(self,value):
        """
        search(self,value)
        description:
            - Iterates throught the entire linked list (head to tail) and returns the first occurance
            - class method defining the search function

        input:
            - value/key the user is looking for
        output: 
            - tupple (index,value)
        """
        cursor = self.head
        while (cursor != None) and (cursor.value != value):
            cursor = cursor.rightNode
        if cursor:
            return (cursor.nodeIndex,cursor.value)
        else:
            print(f'Value: {value} not present in linked list')


class DoublyLinkedList: 
    """
    class methods
        - append = Add an element at the end of the list
        - Insert(3) − Adds an element at the beginning of the list/middle to end
        - Delete(3) − Deletes an element at the beginning of the list/middle to end
        - Display − Displays the complete list.
        - Search − Searches an element using the given key.
        - Delete − Deletes an element using the given key.
    class variable:
        - DoublyLinkedList.listSize (the amount of nodes in the class instance)
    """
    listSize = 0 


    def __init__(self):
        """
        variables
        __init__(self):
        - self.head = None (class pointers)
        - self.tail = None (class pointers)
        """
        self.head = None
        self.tail = None


    def append(self,nextNode):
        """
        append(self,nextNode)
        description:
            - Appends a node to the end DoublyLinkedList

        input:
            - ListNode class instance to be inserted
        output: 
            - 
        """
        nextNode.nodeIndex = DoublyLinkedList.listSize
        if DoublyLinkedList.listSize == 0:
            self.head = nextNode
            self.tail = nextNode
            
        else:
            self.tail.rightNode = nextNode
            temp = self.tail
            # moving to the next node
            self.tail = nextNode
            self.tail.leftNode = temp
            temp = None
        DoublyLinkedList.listSize += 1
        print(DoublyLinkedList.listSize)

    def insert(self,node,index):
        """
        insert(self,node,index)
        description:
            - Inserts a node to a specific index of the DoublyLinked list. 
            - Check whether the index is specified to be at the beginning, middle or end of the list

        input:
            - LinkedNode class instance to be inserted
            - index value to be insersted 
        output: 
            - 
        """
        cursor = self.head
        # the user specify a value corresponding to the end of the list
        if index == DoublyLinkedList.listSize:
            return self.append(node)
        # user specify to enter a value at the beginning of the list

        elif index == 0:
            Node.nodeIndex = 0
            # biggest challenge was to realise that the change needed to happen at self.head
            temp = self.head
            temp.leftNode = node
            self.head = node
            self.head.rightNode = temp


        else:  
            while (cursor!=None) and (cursor.nodeIndex != (index-1)):
                cursor = cursor.rightNode
            # we also have to update the node index of each value
            temp = cursor.rightNode

            cursor.rightNode = node
            node.leftNode = cursor

            temp.leftNode = node
            node.rightNode = temp

        DoublyLinkedList.listSize += 1
        temp = None
        self.resetIndex()


    def resetIndex(self):
        """
        resetIndex(self)
        description:
            - navigate the entire linked list to reset its index. (used mostly internally)
            - The index information is not necessary and increases the complexity to O(n) even in O(1) operations
            - Can be removed in the future (scalability depending)

        input:
            - 
        output: 
            - 
        """
        cursor = self.head
        for i in range(DoublyLinkedList.listSize):
            cursor.nodeIndex = i
            cursor = cursor.rightNode


    def display(self):
        """
        display(self)
        description:
            - Iterates throught the entire linked list (head to tail)
            - print each nodes with its index and value/key

        input:
            - 
        output: 
            - 
        """
        cursor = self.head
        print(cursor)
        print('\n(nodeIndex,nodeValue)')
        while cursor != None:
            print(f'({cursor.nodeIndex},{cursor.value})')
            cursor = cursor.rightNode


    def search(self,value):
        """
        search(self,value)
        description
            - Iterates throught the entire linked list (head to tail) and returns the first occurance
            - class method defining the search function

        input:
            - value/key the user is looking for
        output: 
            - tupple (index,value)
        """
        print(DoublyLinkedList.listSize)
        cursor = self.head
        while (cursor != None) and (cursor.value != value):
            cursor = cursor.rightNode
        if cursor:
            return (cursor.nodeIndex,cursor.value)
        else:
            print(f'Value: {value} not present in linked list')


    def delete(self,value):
        """
        delete(self,value)
        description:
            - look for a value in the linked list using the search method
            - unlink, and delete the item found.
            #! only navigates from head to tail and not vice-versa can be implemented (in the future)

        input:
            - node value to be removed. If the value/data is a json we could use the index instead
            or change the value from a number to a PKI or str identifier 
        output: 
            - error message if value doesn't exist
        """
        undesiredNode = self.search(value) # (index,val)
        if not undesiredNode:
            return
        # beginning of the linked list
        elif undesiredNode[0]==0:
            self.head = self.head.rightNode
            self.head.leftNode = None
            
        # end of the linked list
        elif (undesiredNode[0]+1)==(DoublyLinkedList.listSize):
            self.tail = self.tail.leftNode
            self.tail.rightNode = None

        else:
            cursor = self.head 
            # to remove any item at the middle or end you need to traverse the entire list
            while (cursor!=None) and (cursor.nodeIndex != (undesiredNode[0]-1)):
                cursor = cursor.rightNode
            before = cursor
            # we may occur a memory leak issue this way

            cursor = cursor.rightNode
            after = cursor.rightNode


            before.rightNode = after
            after.leftNode = before
            cursor = None

        DoublyLinkedList.listSize -=1
        print(DoublyLinkedList.listSize)
        self.resetIndex()


#won't show if this is ran as the main file       
if __name__ == '__main__':

    
    #! main improvement would be to either use the node index or class len because they are used interchangeably
    #! which could spell disaster
    node1 = ListNode(31)
    node2 = ListNode(69)
    node3 = ListNode(420)
    node4 = ListNode(423)
    node5 = ListNode(426)
    node6 = ListNode(888)

    nodes = [ListNode(i) for i in range(10,20,2)]
    singleList = SinglyLinkedList()
    for i in range(len(nodes)):
        print('list size:',singleList.listSize)
        singleList.append(nodes[i])
    singleList.display()
    #! IDK why it works here but crashes in unittest as if the instance is not reset between test.



    singleList2 = SinglyLinkedList()
    singleList2.listSize = 69
    print(singleList2.listSize)
    print(singleList.listSize)
    print([x for x in dir(SinglyLinkedList) if not x.startswith('__')])
    print(SinglyLinkedList.__dict__)
    print(ListNode.__init__.__doc__)
    # print(help(SinglyLinkedList.append))
    # print(help(SinglyLinkedList.display))
    # doubleList = DoublyLinkedList()
    # doubleList.append(node1)
    # doubleList.append(node2)
    # doubleList.display()
    # doubleList.insert(node4,0)
    # doubleList.display()
    # doubleList.insert(node6,1)
    # doubleList.display()
    # print('--search method--')
    # print(doubleList.search(31))
    # print('--delete method--')
    # print('--delete first--')
    # doubleList.delete(423)
    # doubleList.display()
    # doubleList.insert(node5,1)
    # print('--delete middle--')
    # doubleList.delete(31)
    # doubleList.display()
    # print('--delete last--')
    # doubleList.delete(69)
    # doubleList.display()

    # print('*-*- single list *-*-')
    # singleList= SinglyLinkedList()
    # print('---node1---')
    # singleList.append(node1)
    # print('---node2---')
    # singleList.append(node2)
    # print('---node3---')
    # singleList.append(node3)
    # print('---display method---')
    # singleList.display()
    # print('---search method---')
    # print(singleList.search(69))
    # print(singleList.search(421))
    # print(singleList.search(420))
    # print('---insert method---') #! error here

    # singleList.insert(node4,3)
    # singleList.insert(node5,1)
    # singleList.display()

    # singleList.insert(node6,0)
    # singleList.display()
    # print('---delete method---')
    # singleList.delete(67)
    # singleList.delete(69)
    # singleList.display()
    # singleList.delete(888)
    # singleList.display()


