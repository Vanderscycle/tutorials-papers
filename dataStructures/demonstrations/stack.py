class Node:


    def __init__(self,key):
        # 
        self.key = key
        self.index = None # index = 0 means its a the bottom of the stack
        self.data = None
        # pointer
        self.nodeBellow = None


class Stack:
    """
    Implementation of the stack data structure
    - push (add to the top)
    - pop (remove top)
    - search (navigate the stack)
    - peek (see what is the value of the top node)
    - size (length of stack)
    #TODO display method
    """
    stackSize = 0


    def __init__(self):
        self.top = None


    def push(self,node):
        """
        Add the node class to the top of the stack
        input:
            - node class instance to be inserted on the top
        output: 
            - 
        """
        if Stack.stackSize == 0:
            node.index = 0
            self.top = node
        else:
            node.index = Stack.stackSize
            node.nodeBellow = self.top
            self.top = node
            temp = None
        Stack.stackSize+=1


    def pop(self):
        """
        Removes the node on the top of the stack
        input: 
            - 
        output: 
            - the top node of the stack
        """
        if Stack.stackSize == 0:
            self.top = None
        else:
            temp = self.top
            self.top = self.top.nodeBellow
            return temp
        Stack.stackSize -=1


    def search(self,nodeKey):
        """
        returns information about the location of a node in the stack.
        input
            - the node's key
        output: 
            - tupple (index, data)
            - error message if not found
        """
        cursor = self.top
        while (cursor != None) and (cursor.key!=nodeKey):
            cursor = cursor.nodeBellow
        if cursor:
            return (cursor.index,cursor.data)
        else:
            print('key not found in stack')


    def peek(self):
        """
        Returns, but doesn't remove, the value of the top node of the stack
        peek is an operation on certain abstract data types, 
        specifically sequential collections such as stacks and queues, which returns the value of the top 
        input: 
            - 
        output: 
            - tupple (key,index,value)
        """
        print('Tupple: (key,index,value)')
        return (self.top.key,self.top.index,self.top.data)
    
    
    def size(self,info=False):
        """
        return the size of the stack
        print the info is the info flag is up
        input
            - optional info flag (default=False)
        output: 
            - class instance stack size
            - print message if the info flag is selected
        """
        if info:
            print(f'stack size: {Stack.stackSize}')
        return(Stack.stackSize)

if __name__ == '__main__':

    
    fullStackMemory = Stack()
    node1 = Node(1)
    node1.data = {'key1':1,'key2':2}
    print(node1.data)
    node2 = Node('test')
    node2.data = {'key1':3,'key2':4}
    node3 = Node(3)
    node3.data = {'key1':5,'key2':6}
    node4 = Node('4bro')
    node4.data = {'key1':7,'key2':8}
    print(node2.data)
    print(node2.key)
    print('--stack operations')
    fullStackMemory.push(node1)
    print(fullStackMemory.top.nodeBellow)
    print(fullStackMemory.top.index)
    fullStackMemory.push(node2)
    print(fullStackMemory.top.nodeBellow.data)
    print(fullStackMemory.top.index)
    fullStackMemory.push(node3)
    fullStackMemory.push(node4)
    fullStackMemory.pop()
    print('--peek operations')
    print(fullStackMemory.peek())
    print('--size operations')
    print(fullStackMemory.size())
    print('--test operations')
    print(fullStackMemory.search('test'))