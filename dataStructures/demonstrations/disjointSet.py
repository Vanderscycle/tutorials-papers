from rich import (
    print,
    traceback
    )

class KruskalNode:
    """
    Node class used for the Kruskal class which can have a number of pointers
    """
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.index = None
        # unlike the binary tree or linked list where the pointers were defined. We create a list to store a tupple (nodeClassInstancePointer, weightOfLink)
        self.pointers = list()

class GraphKruskal:
    """
    regular union
    find (find if two nodes belong to the same group)
    path compression union (all nodes points to the parent node)
    a node can be present in the graph but not joined to anything
    """
    graphSize = 0


    def __init__(self):
        self.position = list()


    def append(self,node,mode=''):
        """
        append(self,node)
        description:
            - check is a given node key is present in the graph
            - O(1)
        input: 
            - the node class instance
            - optional mode ['append'] for when I I'd like the node to be returned 
        output: 
            - 
        """
        node.index = GraphKruskal.graphSize
        self.position.append(node)
        GraphKruskal.graphSize += 1
        if mode=='append':
            return node


    def isPresent(self,nodeKeys,mode='search',info=False): # 
        """
        isPrsent(self,nodeKey) (HelperMethod)
        description:
            - check is a given node key is present in the graph
            - double hatted class method
            - O(n)* can be really expensive depending on how many arguments are passed
        input: 
            - The node class instance keys 
            - #! see you a list can be passed so that we don't have to search the list twice
            - optional mode=['check','search']
                - check we want to check for the present
                - search we want the node
            - optional info=[True,False] if more info in the check mode is required in a print form
        output: 
            - returns the node class instance
            - message if not present
        """   
        # In this mode we want a simple 
        if mode=='check':
            result = next(i for i in self.position if any(nodeKeys == i.key))
            if result:
                if info:
                    print(f'node: {result.key}, data: {result.data}, pointers: {[(n.key,w) for n,w in result.pointers ]} ')
                return True
                
            print(f'node: {nodeKeys} not found')
            return False

        # in this mode we want to return
        elif mode=='search':
            result = list()
            for nodeKey in nodeKeys:
                #? there has to be a more efficient way to do it than traversing the entire list each time
                #? also there can be alot of issue with similar keys
                # https://stackoverflow.com/questions/2361426/get-the-first-item-from-an-iterable-that-matches-a-condition
                result.append(next((i for i in self.position if nodeKey == i.key), False))
            return result

        else:
            raise ValueError("mode can only be ['check','search']")


    def createEdge(self,nodeFromKey,nodeToKey,weight=0):
        """
        description:
        If the node already exists we want to link to it
        ELIF the node doesn't exists we wnat to add it and create
        pointers have to be made both ways (doubly linked)
            - check is a given node key is present in the graph
        input: 
            - The node class instance keys 

        output: 
            - r
            -
        """
        status = self.isPresent([nodeFromKey,nodeToKey],mode='search')
        # if an element isn't present we will create it, but with empty data
        # https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension
        nodeAvail = [self.append(KruskalNode(nodeKey,None),mode='append') if i == False else i for i,nodeKey in zip(status,[nodeFromKey,nodeToKey]) ]
        print(nodeAvail)



if __name__ == '__main__':
    val = [30,20,0,10,5] # all the way right
    data = ['a30','b20','c0','d10','e5']
    nodeLists = [ KruskalNode(k,d) for k,d in zip(val,data)]  

    gK = GraphKruskal()
    [gK.append(i) for i in nodeLists]
    print(gK.isPresent(['1231',30,769]))
    gK.createEdge(30,4)
    print(gK.isPresent([4]))