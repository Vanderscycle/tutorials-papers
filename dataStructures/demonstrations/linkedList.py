#
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
            SinglyLinkedList.listSize += 1 
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
    def __init__(self,val):
        self.value = val
        self.rightNode = None
        self.leftNode = None

# node1 = Node(31)
# node2 = Node(69)
# node3 = Node(420)
# node4 = Node(423)
# node5 = Node(426)
# node6 = Node(888)
# print(node1.value)

# singleList= SinglyLinkedList()
# singleList.append(node1)
# print('---node1---')
# print(singleList.head.value)
# print(singleList.head.rightNode)
# print(singleList.tail.value)
# print(singleList.tail.rightNode)

# singleList.append(node2)
# print('---node2---')
# print(singleList.head.value)
# print(singleList.head.rightNode)
# print(singleList.tail.value)
# print(singleList.tail.rightNode)
# print('---node3---')
# singleList.append(node3)
# print(singleList.head.value)
# print(singleList.head.rightNode)
# print(singleList.tail.value)
# print(singleList.tail.rightNode)
# print('---listsize---')
# print(singleList.listSize)

# value = singleList.head
# #while value!=None:
# for i in range(singleList.listSize):
#     print(f'value {value.value} node index: {value.nodeIndex}')
#     value = value.rightNode
# print('---display method---')
# singleList.display()
# print('---search method---')
# print(singleList.search(69))
# print(singleList.search(421))
# print(singleList.search(420))
# print('---insert method---')

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
# node1.insert(node2)
# node2.insert(node3)
# nextNode = node1
# while nextNode != None:
#     print(f'Node:{nextNode.nodeNumber} node value:{nextNode.value}')
#     nextNode = nextNode.rightNode
    


# print(node1.length)
# print(node3.nodeNumber)
