from copy import deepcopy
class QueueNode:
    """
    Node used for the simple queue class
    """
    def __init__(self,key):
        """
        Variables:
        - __init__(self,key)
        - self.key
        - self.data (the data you want the node to contain. can be a JSON, dict, list, a single variable, etc.)
        - self.Index (the node automatically given by the queue class)
        - self.nodeBefore = None used by the queue class (not its PQ )
        """
        self.key = key
        self.data = None
        self.index = None
        self.nodeBefore = None # pointer


class Queue:
    """
    Implementation of the Queue data structure
    class methods:
        - Enqueue (add to the front of the queue)
        - Dequeue (remove the last item of the queue)
        - peek (value of the last item)
        - search (contains)
        - removal (empty queue)
        - is Empty
        - display method
    class variable:
        - Queue.queueSize (the amount of nodes in the class instance)
    """
    queueSize = 0


    def __init__(self):
        """
        Variables:
        - __init__(self,key)
        - self.key
        """
        self.head = None
        self.tail = None


    def enqueue(self,node):
        """
        enqueue(self,node)
        Description:
            - Add a node to the front of the queue

        input
            - a node from Node Class
        output: 
            -
        """
        node.index = Queue.queueSize
        if Queue.queueSize == 0:
            self.head = node
            self.tail = node
        else:
            temp = self.tail
            self.tail = node
            self.tail.nodeBefore = temp
            temp = None
        
        Queue.queueSize +=1


    def dequeue(self):
        """
        dequeue(self):
        description:
           - Remove the node at the tail of the queue

        input 
            -
        output:  
            - message if queue is empty
        """ 

        if self.isEmpty():
            return
        else:
            temp = self.tail
            self.tail = self.tail.nodeBefore
            temp = None

        Queue.queueSize -=1


    def search(self,nodeKey):
        """
        search(self,nodeKey)
        description:
            - Traverse the queue looking for a specific node key

        input:
            - the desired Key associated with the node
        output:  
            - message if queue is empty or value not found
            - node value and index if found
        """         
        if self.isEmpty():
            return
        cursor = self.tail
        while (cursor != None) and (cursor.key!=nodeKey):
            cursor = cursor.nodeBefore
        if cursor:
            return (cursor.index,cursor.data)
        else:
            print('key not found in stack')


    def display(self):
        """
        display(self)
        description:
            - Traverse the queue and display its content

        input:
            - 
        output:  
            - message if queue is empty
            - print statements 
        """         
        if self.isEmpty():
            return
        cursor = self.tail
        while (cursor != None):
            print(f'node index: {cursor.index} key: {cursor.key} data: {cursor.data}')
            cursor = cursor.nodeBefore


    def removal(self):
        """
        removal(self)
        description:
            - Completly empties the queue

        input: 
            - 
        output:  
            - message if queue is empty
        """
        if self.isEmpty():
            return  
        cursor = self.tail
        for i in range(Queue.queueSize):
            self.dequeue()
        self.head = cursor


    def peek(self):
        """
        peek(self)
        description:
            - peek is an operation on certain abstract data types, 
            - specifically sequential collections such as stacks and queues, which returns the value of the top 
        
        input: 
            - 
        output: 
            - tupple (key,index,value)
            - message if queue is empty 
        """
        if self.isEmpty():
            return 
        else:
            print('Tupple: (key,index,value)')
            return (self.tail.key,self.tail.index,self.tail.data)


    def isEmpty(self):
        """
        isEmpty(self) (helper method)
        description:
            - checks if the queue is empty

        input: 
            - 
        output: 
            - message if the queue is empty
            - True (empty list) 
            - False (not empty)
        """
        if Queue.queueSize == 0:
            print('empty queue')
            return True
        return False

class PQNode:
    """
    Node used for the priority queue class
    """
    def __init__(self,key):
        self.key = key
        self.data = None # same principle as a dictionary make the key independent of the data value
        self.left = None
        self.right = None
        self.parentIndex = None


class PriorityQueue:
    """
    Implementation of the Priority Queue data structure using a MIN binary heap and python lists. Optimization could be found using 
    class methods:
    - Insert
        - bubble down (helper)
        - bubble up (helper)
        - #TODO add some data to to the PQNODES and see if more modifications are required
        - Poll
        - delete ( remove naive)
        - search (naive)
        - Peek
        - Display 
    class variables:
        - PriorityQueue.heapsize

    """
    heapSize = 0
    def __init__(self):
        self.position = list()
        pass


    def append(self,node):
        """
        append(self,node)
        description:
            - Appends a PQNode class instance in the binary tree at the first available leaf node. 
            - #! Doesn't actually sort it so depending of the order it may violates the heap invariant rule.
            - finds the index of the parent node (i) using the 
                - nodeIndex (left) = 2i + 1 where nodeIndex element of Z
                - nodeIndex (right) = 2i + 2 where nodeIndex element of Z

        input: 
            - the PQNode node class instance
        output: 
            - 
        """
        if self.is_empty():
            node.parentIndex = 0
            self.position.append(node)

        else:
            node.parentIndex = PriorityQueue.heapSize 
            # assign to the left node 
            if ((PriorityQueue.heapSize - 1)/2).is_integer():
                parentNodeIndex = int((PriorityQueue.heapSize - 1)/2)
                # fetch and updates the parent's node pointer
                parentNode = self.position[parentNodeIndex]
                parentNode.left = node
                self.position[parentNodeIndex] = parentNode

            # assign to the right node
            elif ((PriorityQueue.heapSize - 2)/2).is_integer():
                parentNodeIndex = int((PriorityQueue.heapSize - 2)/2)
                # fetch and updates the parent's node pointer
                parentNode = self.position[parentNodeIndex]
                parentNode.right = node
                self.position[parentNodeIndex] = parentNode

            else:
                #isinstance will not work because of PEP 328 https://www.python.org/dev/peps/pep-0238/
                # solution: https://stackoverflow.com/questions/21583758/how-to-check-if-a-float-value-is-a-whole-number
                print(f'check 1 {(PriorityQueue.heapSize - 1)/2} check 2 {(PriorityQueue.heapSize - 2)/2}')
                print('error debug please')
            self.position.append(node)
        PriorityQueue.heapSize += 1


    def delete(self,nodeToDeleteKey):
        """
        delete(self,nodeToDeleteKey):
        description:
            - search for a node key in the tree, if found swaps it with the last node in the tree (have to figure out hte pointers)

        input: 
            - the node class instance 
        output:
            - message if not found
        """
        nodeDeleteIndex, nodeInstanceDelete = self.search(nodeToDeleteKey) # (index,node class instance)

        # the node to delete is last so we just remove it
        if nodeDeleteIndex == PriorityQueue.heapSize:
            self.position[nodeDeleteIndex] = None
            PriorityQueue.heapSize -= 1
            return
        # the node to delete is last so we just remove it
        elif nodeDeleteIndex == 0:
            poll()
            return
        
        # making copy otherwise its a headache
        temp = deepcopy(nodeInstanceDelete)
        lastNodeTemp = deepcopy(self.position[-1])

        # adjusting the parent pointers of the node to be deleted
        if ((nodeDeleteIndex - 1)/2).is_integer():
            print("updating topnode's parent left reference ")
            self.position[int((nodeDeleteIndex - 1)/2)].left = lastNodeTemp #! THE REASON WHY IT WASN'T UPDATING

        elif ((nodeDeleteIndex - 2)/2).is_integer():
            print("updating topnode's parent right reference ")
            self.position[int((nodeDeleteIndex - 2)/2)].right = lastNodeTemp

        # it is possible that the node to be delete actually points to the last node. In which case we want to remove the pointer to it.
        if (nodeInstanceDelete.left.key == lastNodeTemp.key):
            nodeInstanceDelete.left = None

        elif (nodeInstanceDelete.right.key == lastNodeTemp.key):
            nodeInstanceDelete.right = None

        # SWAPPING THE NODE TO DELETE POINTERS WITH LAST NODE 
        (
            # nodeInstanceDelete.left,
            # nodeInstanceDelete.right,
            # nodeInstanceDelete.parentIndex,
            nodeInstanceDelete.key
            ) = ( 
                # lastNodeTemp.left,
                # lastNodeTemp.right,
                # lastNodeTemp.parentIndex,
                lastNodeTemp.key
            )        
        # SWAPPING THE LAST NODE WITH THE NODE TP DELETE
        (
            self.position[-1].left,
            self.position[-1].right,
            self.position[-1].parentIndex,
            self.position[-1].key
            ) = ( 
                temp.left,
                temp.right,
                temp.parentIndex,
                temp.key
            )

        # the node to be deleted (now in the last position) can be removed
        self.position.pop()
        PriorityQueue.heapSize -= 1
        self.position[nodeDeleteIndex] = nodeInstanceDelete

        # self.display() # debugging
        # clearing memory (although that isn't necessary I think)
        temp = None
        tempTopNode = None
        self.bubbleDown(self.position[nodeDeleteIndex])  
        # bubble down after


    def insert(self,node):
        """
        insert(self,node)
        description:
            - Inserts a node to the bottom of the tree and then bubbles it up depending on the key value 

        input: 
            - the node class instance 
        output:
            - 
        """
        # we append the node at the end of the tree
        self.append(node)
        # then we bubble up the node
        self.bubbleUp(self.position[-1])
        self.display() # debugging


    def bubbleUp(self,bottomNode):
        """
        bubbleUp(self,bottomNode) (helper method)
            description:
                - Bubble up a node by comparing with its parent key

        input: 
            - a parent PQNode class instance 
        output: 
            - 
        """
        # assuming the heap invariability isn't respected at the start
        heapRule = False
        parentNode = bottomNode
        while heapRule == False:

            # no need to bubble anything if this is the only node
            if (bottomNode.parentIndex==0):
                return
            # FINDING WHO THE PARENT OF THE BOTTOMNODE IS (LEFT OR RIGHT PARENT)
            elif (bottomNode.parentIndex>=1):
                if ((bottomNode.parentIndex - 1)/2).is_integer():
                    print("The parent of bottomNode is pointing to it using a left pointer\n")
                    parentNode = self.position[int((bottomNode.parentIndex - 1)/2)]
                    pointerPositon = 'left'
  
                elif ((bottomNode.parentIndex - 2)/2).is_integer():
                    print("The parent of bottomNode is pointing to it using a right pointer\n")
                    parentNode = self.position[int((bottomNode.parentIndex - 2)/2)]    
                    pointerPositon = 'right'

            # the parent respects the min heap variant so it is at the right position
            if parentNode.key <= bottomNode.key:
                heapRule = True

            # the bottom node needs to be swapped
            elif (parentNode.key > bottomNode.key) and (pointerPositon == 'left') :
                print('done')
                # we reuse both previously created methods but in this case the parentNode is the topNode
                bottomNode = self.swapDownLeft(bottomNode,parentNode.right,parentNode)

            # the bottom node needs to be swapped
            elif (parentNode.key > bottomNode.key) and (pointerPositon == 'right') :
                # we reuse both previously created methods but in this case the parentNode is the topNode
                bottomNode = self.swapDownRight(parentNode.left,bottomNode,parentNode)
                  

    def search(self,nodeKey,info=False):
        """
        search(self,nodeKey,info=False)
        description:
            - Returns the top PQNode class instance 

        input: 
            - the node class instance from which we will get the key from
        output:
            - tuple(index,the PQNode node class instance)   (if found)
            - print statement about the tupple (info=True)
            - message if node not found
        """
        if self.is_empty():
            return
        for node in self.position:
            if node.key == nodeKey:
                return (node.parentIndex,node)


    def is_empty(self):
        """
        is_empty(self)
        description:
            - Checks if the heap is empty

        input: 
            - 
        output: 
            - message if the heap is empty
            - True (empty list) 
            - False (not empty)
        """
        if PriorityQueue.heapSize == 0:
            print('Empty tree')
            return True
        return False


    def poll(self):
        """
        poll(self):
        description:
            - Returns the top PQNode class instance 

        input: 
            - 
        output: 
            - the PQNode node class instance at root
        """
        if self.is_empty():
            return
        # creating a pointer
        temp = self.position[0]

        # removing the parent node pointer to the last node
        if self.position[-1].parentIndex % 2 != 0:
            # the last node is the left children node of its parent
            parentLastNodeIndex = int((self.position[-1].parentIndex - 1)/2)
            self.position[parentLastNodeIndex].left = None
        else: 
            print('right')
            # the last node is the right children node of its parent
            parentLastNodeIndex = int((self.position[-1].parentIndex - 2)/2)
            self.position[parentLastNodeIndex].right = None

        # swaps root with the last leaf node
        self.position[-1],  self.position[0] = self.position[0],  self.position[-1]
        # changing index and pointers for the new root
        self.position[0].parentIndex = 0
        self.position[0].left = temp.left
        self.position[0].right = temp.right
        temp = self.position.pop()
        PriorityQueue.heapSize -= 1
        self.bubbleDown(self.position[0])       
        return temp


    def bubbleDown(self,topNode):
        """
        bubbleDown(self,topNode) (helper method)
        description:
            - Bubble down a node by comparing its subsequent left and right node keys

        input: 
            - a parent PQNode class instance 
        output: 
            - 
        """
        # assuming the heap invariability isn't respected at the start
        heapRule = False
        while heapRule == False:
            leftNode = topNode.left
            rightNode = topNode.right
            try: # debugg
                print(f'traveling variable key: {topNode.key}, list position: {topNode.parentIndex} leftchild {topNode.left.key} rightchild {topNode.right.key}\n')
                print(f'left travelling key: {leftNode.key}, list position: {leftNode.parentIndex} leftchild {leftNode.left.key} rightchild {leftNode.right.key}')
                print(f'left travelling key: {rightNode.key}, list position: {rightNode.parentIndex} leftchild {rightNode.left.key} rightchild {rightNode.right.key}\n')
            except:
                pass
            #! add a check to see whether there is a left or right node to begin. If 
            # the parent node respects the heap invariability rule since it is the smallest
            if (topNode.left!=None) and (topNode.right==None):
                if (topNode.key > topNode.left.key):
                    print('swap left, right node is empty')
                    topNode = self.swapDownLeft(leftNode,rightNode,topNode)
                else:
                    print('done')
                    heapRule = True      

            elif (topNode.left==None) and (topNode.right!=None):
                if (topNode.key > topNode.right.key):
                    print('swap right, left node is empty')
                    topNode = self.swapDownRight(leftNode,rightNode,topNode)       
                else:
                    print('done')
                    heapRule = True 

            elif (topNode.left==None) and (topNode.right==None):
                print('done')
                heapRule = True                                  

            elif (topNode.key <= topNode.left.key) and (topNode.key <= topNode.right.key):
                print('topNode respect the invariability relue')
                print('done')
                heapRule = True  

            # the left node is smaller that its parent so we swap
            elif (topNode.key > topNode.left.key) and (topNode.key <= topNode.right.key):
                print('swap left')
                # remembering position
                temp = topNode.left.parentIndex

                # swapping the pointers
                topNode, topNode.left = topNode.left, topNode
                topNode, topNode.right = topNode.right, topNode
                
                #swapping positions
                self.position[topNode.parentIndex],self.position[topNode.left.parentIndex] = self.position[topNode.left.parentIndex], self.position[topNode.parentIndex]
                topNode = self.position[temp]
                print(topNode)

            # the right node is smaller that its parent so we swap
            elif (topNode.key <= topNode.left.key) and (topNode.key > topNode.right.key):
                print('swap right')
                topNode, topNode.right = topNode.right, topNode

            # both children nodes are smaller but
            elif (topNode.key > topNode.left.key) and (topNode.key > topNode.right.key):

                if (topNode.left.key <= topNode.right.key):
                    print('swap left 2')
                    topNode = self.swapDownLeft(leftNode,rightNode,topNode)

                else:

                    print('swap right 2') 
                    topNode = self.swapDownRight(leftNode,rightNode,topNode)


    def swapDownLeft(self,leftNode,rightNode,topNode):
        """
        swapDownLeft(self,leftNode,rightNode,topNode) (helper method)
        description:
            - Swaps the parent node with its left child node. (only adjacent node) 

        input: 
            - parent node (topNode)
            - left child node
        output: 
            - the new travellingNode (the swapped topNode with its child)
        """

        # remembering position because that's a massive source of headache
        temp = deepcopy(leftNode)
        tempTopNode = deepcopy(topNode)

        # SWAPPING THE PARENT'S TOPNODE LEFT POINTER WITH  LEFTNODE (TOPNODE.LEFT)
        if (topNode.parentIndex!=0):
            if ((topNode.parentIndex - 1)/2).is_integer() and (leftNode!=None):
                print("updating topnode's parent left reference ")
                self.position[int((topNode.parentIndex - 1)/2)].left = temp 

            elif ((topNode.parentIndex - 2)/2).is_integer() and (rightNode!=None):
                print("updating topnode's parent right reference ")
                self.position[int((topNode.parentIndex - 2)/2)].right = tempTopNode.right
        
        # SWAPPING CHILD POINTERS LEFT NODE WITH PARENT NODE

        (
            leftNode.left,
            leftNode.right,
            leftNode.parentIndex,
            leftNode.key
            ) = ( 
                temp.left,
                temp.right,
                temp.parentIndex,
                tempTopNode.key
            )

        #SWAPPING POINTERS PARENT NODE W/ DEEPCOPY OF PARENT LEFT NODE (CHILD)
        (
            topNode.left,
            topNode.right,
            topNode.parentIndex,
            topNode.key
            ) = (
                tempTopNode,
                tempTopNode.right,
                tempTopNode.parentIndex,
                temp.key
            )
        #swapping positions 
        self.position[leftNode.parentIndex] = leftNode
        self.position[topNode.parentIndex] = topNode
        topNode = self.position[leftNode.parentIndex] 
        # self.display() # debugging
        # clearing memory (although that isn't necessary I think)
        temp = None
        tempTopNode = None
        return topNode


    def swapDownRight(self,leftNode,rightNode,topNode):
        """
        swapDownRight(self,leftNode,rightNode,topNode) (helper method)
        description:
            - Swaps the parent node with its right child node 

        input: 
            - parent node (topNode)
            - right child node
        output: 
            - the new travellingNode (the swapped topNode with its child)
        """
        temp = deepcopy(rightNode)
        tempTopNode = deepcopy(topNode)

        # SWAPPING THE PARENT'S TOPNODE LEFT POINTER WITH  LEFTNODE (TOPNODE.LEFT)
        if (topNode.parentIndex!=0):
            if ((topNode.parentIndex - 1)/2).is_integer() and (leftNode!=None):
                print("updating topnode's parent left reference ")
                self.position[int((topNode.parentIndex - 1)/2)].left = temp 

            elif ((topNode.parentIndex - 2)/2).is_integer() and (rightNode!=None):
                print("updating topnode's parent right reference ")
                self.position[int((topNode.parentIndex - 2)/2)].right = tempTopNode.right
        
        # SWAPPING CHILD POINTERS RIGHT NODE WITH PARENT NODE

        (
            rightNode.left,
            rightNode.right,
            rightNode.parentIndex,
            rightNode.key
            ) = ( 
                temp.left,
                temp.right,
                temp.parentIndex,
                tempTopNode.key
            )

        #SWAPPING POINTERS PARENT NODE W/ DEEPCOPY OF PARENT RIGHT NODE (CHILD)
        (
            topNode.left,
            topNode.right,
            topNode.parentIndex,
            topNode.key
            ) = (
                tempTopNode.left,
                tempTopNode,
                tempTopNode.parentIndex,
                temp.key
            )
        #swapping positions 
        self.position[rightNode.parentIndex] = rightNode
        self.position[topNode.parentIndex] = topNode
        topNode = self.position[rightNode.parentIndex] 
        # self.display() # debugging
        # clearing memory (although that isn't necessary I think because of stacks)
        temp = None
        tempTopNode = None
        return topNode

    def peek(self):
        """
        peek(self)
        description:
            - Returns the top PQNode class instance 

        input: 
            - 
        output: 
            - the PQNode node class instance at root
        """
        return self.position[0]


    def display(self):
        """
        display(self)
        description:
            - Not a beautiful or graphical print, but text will have to do for now

        input: 
            - 
        output: 
            - print statements of the structure of the binary heap
        """
        for i in self.position:
            if (i.left!= None) and (i.right!= None):
                print(f'node parent index {i.parentIndex}, key {i.key}, left node key {i.left.key}, right node key {i.right.key}')

            elif (i.left == None) and (i.right!= None):
                print(f'node parent index {i.parentIndex}, key {i.key}, left node key {i.left}, right node key {i.right.key}')

            elif (i.left != None) and (i.right == None):
                print(f'node parent index {i.parentIndex}, key {i.key}, left node key {i.left.key}, right node key {i.right}')

            else:
                 print(f'node parent index {i.parentIndex}, key {i.key} is is leaf node')


if __name__ == '__main__':

    # heapo = PriorityQueue()
    # vals = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,1299] # all the way left
    # vals = [0,20,10,60,50,40,30,140,130,120,110,100,90,80,70,150,1299] # all the way right
    # nodeLists = [ PQNode(i) for i in vals ]

    # [heapo.append(i)for i in nodeLists ]    
    # heapo.display()

    # print(heapo.poll().key)
    # print(heapo.heapSize)
    # heapo.display()
    # print(heapo.search(410))

    print('--insert tests--')
    heapo2 = PriorityQueue()
    vals = [30,20,0,10,5] # all the way right
    nodeLists = [ PQNode(i) for i in vals ]    
    [heapo2.insert(i)for i in nodeLists ] 
    print('--delete--')
    heapo2.delete(5)
    heapo2.display()













    print('--Simple Queue print test --')    
    simpleQ = Queue()
    node1 = QueueNode(1)
    node1.data = {'key1':1,'key2':2}
    node2 = QueueNode('test')
    node2.data = {'key1':3,'key2':4}
    node3 = QueueNode(3)
    node3.data = {'key1':5,'key2':6}
    node4 = QueueNode('4bro')
    node4.data = {'key1':7,'key2':8}
    simpleQ.enqueue(node1)
    simpleQ.enqueue(node2)
    print('--display test')
    simpleQ.display()
    print('--test search')
    print(simpleQ.search('test'))
    print(simpleQ.search(3))
    print(simpleQ.head.key)
    print(simpleQ.peek())
    simpleQ.dequeue()
    print(simpleQ.peek())
    simpleQ.dequeue()
    simpleQ.dequeue()
    simpleQ.search('4bro')
    simpleQ.enqueue(node1)
    simpleQ.enqueue(node2)
    simpleQ.enqueue(node3)
    simpleQ.enqueue(node4)
    print(simpleQ.peek())
    print('--removal test')
    simpleQ.removal()
    simpleQ.display()