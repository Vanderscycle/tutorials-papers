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
    - Enqueue (add to the front of the queue)
    - Dequeue (remove the last item of the queue)
    - peek (value of the last item)
    - search (contains)
    - removal (empty queue)
    - is Empty
    #TODO display method
    class a variable:
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
        Add a node to the front of the queue
        input
            - a node from Node Class
        output: 
            -
        """
        node.index = Queue.queueSize
        if self.isEmpty():
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
        Remove the node at the tail of the queue
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
        Traverse the queue looking for a specific node key
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
    

    def removal(self):
        """
        Completly empties the queue
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
        peek is an operation on certain abstract data types, 
        specifically sequential collections such as stacks and queues, which returns the value of the top 
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
        checks if the queue is empty
        input: 
            - 
        output: 
            - error message if the queue is empty
            - True (empty list) 
            - False (not empty)
        """
        if Queue.queueSize == 0:
            print('empty queue')
            return True
        return False

class PriorityQueue:
    """
    Implementation of the Priority Queue data structure
    - Insert
    - Poll
    - Remove
    """
    def __init__(self):
        pass

if __name__ == '__main__':

    
    simpleQ = Queue()
    node1 = Node(1)
    node1.data = {'key1':1,'key2':2}
    node2 = Node('test')
    node2.data = {'key1':3,'key2':4}
    node3 = Node(3)
    node3.data = {'key1':5,'key2':6}
    node4 = Node('4bro')
    node4.data = {'key1':7,'key2':8}
    simpleQ.enqueue(node1)
    simpleQ.enqueue(node2)
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
