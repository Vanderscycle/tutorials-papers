class Node:
    """
    The class node can be used for both singly and doubly linked list. All that matters is the implementation
    """
    def __init__(self,val):
        self.value = val # or any data you want store (pass a json)
        # we could add a data 
        self.nodeIndex = None # the nodeIndex will be assigned when assigned to a linked list
        self.rightNode = None
        self.leftNode = None


class SinglyLinkedList:
    """
    Insertion(3) − Adds an element at the beginning of the list/middle to end
    Deletion(3) − Deletes an element at the beginning of the list/middle to end
    Display − Displays the complete list.
    Search − Searches an element using the given key.
    Delete − Deletes an element using the given key.
    """
    listSize = 0    


    def __init__(self):
        self.head = None
        self.tail = None


    def append(self,nextNode):
        """
        insert nodes FIFO
        jesus daisy chaining these bad boys is something
        input:
            - node class instance to be inserted
        output: (nothing really)
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
        inserts a node to a specific index. 
        Will check if user wants the node to be inserted at the end
        input:
            - node class instance to be inserted
            - index value to be insersted 
        output: (nothing really)
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
        # we also have to update the node index of each value
            temp = cursor.rightNode
            cursor.rightNode = node
            node.rightNode = temp
        SinglyLinkedList.listSize += 1
            # cleaning the memory
            # (although because the way python organize the stack memory along with the heap. It will be deleted)
        temp = None
        self.resetIndex()


    def delete(self,value):
        """
        look for a value in the linked list using the search method
        and unlink the item when found.
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
        navigate the entire linked list to reset its index.
        The index information is not necessary and increases the complexity to O(n) even in O(1) operations
        Can be removed in the future (scalability depending)
        """
        cursor = self.head
        for i in range(SinglyLinkedList.listSize):
            cursor.nodeIndex = i
            cursor = cursor.rightNode
        

    def display(self):
        """
        iterates throught the entire linked list (head to tail)
        print each nodes with its index and value
        """
        cursor = self.head
        print(cursor)
        print('\n(nodeIndex,nodeValue)')
        while cursor != None:
            print(f'({cursor.nodeIndex},{cursor.value})')
            cursor = cursor.rightNode


    def search(self,value):
        """
        class method defining the search function
        input:
            - value the user is looking for
        output: 
            - tupple (index,value)
        iterates throught the entire linked list (head to tail)
        returns the first value match
        possibly could make a change where it returns all occurances
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
    Insertion(3) − Adds an element at the beginning of the list/middle to end
    Deletion(3) − Deletes an element at the beginning of the list/middle to end
    Display − Displays the complete list.
    Search − Searches an element using the given key.
    Delete − Deletes an element using the given key.
    """
    listSize = 0 


    def __init__(self):
        self.head = None
        self.tail = None


    def append(self,nextNode):
        """
        Append a given node to the end of the doubly linked list
        Checks whether that is the first node
        input:
            - node class instance to be inserted
        output: (nothing really)
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
        inserts a node to a specific index. 
        Will check if user wants the node to be inserted at the end
        input:
            - node class instance to be inserted
            - index value to be insersted 
        output: (nothing really)
            - 
        """
        cursor = self.head
        # the user specify a value corresponding to the end of the list
        if index == DoublyLinkedList.listSize:
            return self.append(node)
        # user specify to enter a value at the beginning of the list

        elif index == 0:
            # biggest challenge was to realise that the change needed to happen at self.head
            Node.nodeIndex = 0
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

            # temp = cursor.rightNode
            # cursor.rightNode = node
            # node.rightNode = temp
            # SinglyLinkedList.listSize += 1            

        DoublyLinkedList.listSize += 1
        print(DoublyLinkedList.listSize)
        # cleaning the memory
        # (although because the way python organize the stack memory along with the heap. It will be deleted)
        temp = None
        self.resetIndex()


    def resetIndex(self):
        """
        navigate the entire linked list to reset its index.
        The index information is not necessary and increases the complexity to O(n) even in O(1) operations
        Can be removed in the future (scalability depending)
        """
        cursor = self.head
        for i in range(DoublyLinkedList.listSize):
            cursor.nodeIndex = i
            cursor = cursor.rightNode


    def display(self):
        """
        iterates throught the entire linked list (head to tail)
        print each nodes with its index and value. 
        """
        cursor = self.head
        print(cursor)
        print('\n(nodeIndex,nodeValue)')
        while cursor != None:
            print(f'({cursor.nodeIndex},{cursor.value})')
            cursor = cursor.rightNode


    def search(self,value):
        """
        class method defining the search function
        iterates throught the entire linked list (head to tail)
        returns the first value match
        possibly could make a change where it returns all occurances or a single one
        input:
            - value the user is looking for
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
        look for a value in the linked list using the search method
        and unlink the item when found.
        #! should add the ability to navigate both way in search
        input:
            - node value to be removed. If the value/data is a json we could use the index instead
            or change the value from a number to a PKI or str identifier. Or add a data field to the Node class 
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

#! main improvement would be to either use the node index or class len because they are used interchangeably
#! which could spell disaster
node1 = Node(31)
node2 = Node(69)
node3 = Node(420)
node4 = Node(423)
node5 = Node(426)
node6 = Node(888)

nodes = [Node(i) for i in range(10,20,2)]
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


