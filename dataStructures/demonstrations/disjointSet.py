from rich import (
    print,
    traceback
    )
# really usefull when you have a weird sort to do (a list of lists where you want to sort by first index, then on second index, etc)
#https://docs.python.org/3/library/operator.html#operator.itemgetter
from operator import itemgetter

class KruskalNode:
    """
    Node class used for the Kruskal class which can have a number of pointers

    """
    def __init__(self,key,data=None):
        """
        __init__(self,key,data=None):
        variables:
            - key (the key used to access the node)
            - data (the data json,dict,list,etc that the node will hold)
            - index (auto assigned)
            - pointers (a list for all the edges)
        """
        self.key = key
        self.data = data
        self.index = None
        # unlike the binary tree or linked list where the pointers were defined. We create a list to store a tupple (nodeClassInstancePointerTo, weightOfLink)
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
        #checks if the key is unique
        if self.isPresent(node,mode='check'):
            raise ValueError("The key is already present please choose a different and unique key")
        node.index = GraphKruskal.graphSize
        self.position.append(node)
        GraphKruskal.graphSize += 1
        if mode=='append':
            return node


    def isPresent(self,nodeKeys,mode='search',info=False): # 
        """
        isPresent(self,nodeKeys,mode='search',info=False) (HelperMethod)
        description:
            - check is a given node key is present in the graph
            - double hatted class method
            - O(n)* can be really expensive depending on how many arguments are passed
        input: 
            - The node class instance keys 
            - optional mode=['check','search']
                - check: if the node key is the present return True or False 
                - search: if the node(s) class instance(s) are present we want to return a list of class instances or False if not present
            - optional info=[True,False] if more info in the check mode is required it will do in a print form
        output: 
            - returns the node class instance
            - message if not present
        """   
        # In this mode we want a simple True/False about the presence of a single item #TODO(could be changed for multiple items)
        if mode=='check':
            result = next((i for i in self.position if nodeKeys == i.key),False)
            if result:
                if info:
                    print(f'node: {result.key}, data: {result.data}, pointers: {[(n.key,w) for n,w in result.pointers]} ')
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
        createEdge(self,nodeFromKey,nodeToKey,weight=0):
        description:
            - create edges between two nodes. If one or both node do not  
            If the node already exists we want to link to it
            ELIF the node doesn't exists we wnat to add it and create
            pointers have to be made both ways (doubly linked)
                - check is a given node key is present in the graph
        input: 
            - The node class instance keys 
        output: 
            - create and append the node(internal)
            -
        """
        nodeList = [nodeFromKey,nodeToKey]
        status = self.isPresent(nodeList,mode='search')
        # if an element isn't present we will create it, but with empty data
        # the list comprehension look complex because of the if else statement. if not present create else pass the node class instance
        # https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension
        nodeAvail = [self.append(KruskalNode(nodeKey),mode='append') if i == False else i for i,nodeKey in zip(status,nodeList)]
        # creating the edges for both nodes
        #! Need to check if they were present before
        [f.pointers.append((t,weight)) for f,t in zip(nodeAvail,nodeAvail[::-1])] # tupple (nodeClassInstancePointerTo, weightOfLink)


    def display(self):
        """
        display(self): (helper method)
        description:
            - allow the user to see the 
        input: 
            -  
        output: 
            - message about each node class instance information
        """
        print(f'edge with other nodes (nodeTo, Weight)')
        [print(f'Node key:{i.key}, node index:{i.index}, data: {i.data}, edge with other nodes:{[(j[0].key,j[1]) for j in i.pointers]}') for i in self.position]
    
    
    def minimumSpanningTree(self):
        """
        display(self): 
        description:
            - sorts all the edges from lowest to highest
        input: 
            -  
        output: 
            - message about each node class instance information
        """
        #! My god the spaghetti I laid down bellow
        # double_comprehension = [word for words in text for word in words]
        ListToSort = [(node.key,edge[0].key,edge[1]) for node in self.position for edge in node.pointers]
        # https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list/4174955
        ListSorted = sorted(ListToSort, key=itemgetter(2,0))
        print('(NodeKeyFrom,NodeKeyTo,weight)')
        # because each nodes contain a pointer to each other (A->B and B->A) there's essentially twice as many pointers 
        ListSorted = [n for i,n in enumerate(ListSorted) if i%2 ==0 ]
        # [print(i) for i in ListSorted]
        #(NodeKey,nodeClassInstance,NodePointsToKey,NodeClassInstance ) by default they all point to themselves until they are full unionised
        self.optimizedMST = [list([i.key,i,i.key,i]) for i in self.position]
        # [print(i) for i in resultsMST]
        for nodeKeyPair in ListSorted: # we do not care about the weight since the list is sorted
            print(nodeKeyPair)
            print(self.optimizedMST)
            self.union(nodeKeyPair[0],nodeKeyPair[1])


    def union(self,NodeKeyFrom,NodeKeyTo):
        """
        display(self,NodeKeyFrom,NodeKeyTo): (helper method)
        description:
            - combine nodes into a tree
        input: 
            - (NodeKeyFrom,NodeKeyTo) the two nodes that will be combine
        output: 
            - 
        """
        # print(itemgetter(NodeKeyFrom)(self.optimizedMST)[:2])
        # print(itemgetter(NodeKeyTo)(self.optimizedMST)[:2],'\n')
        # They are pointing to the same thing hence they belong to the same tree
        if itemgetter(NodeKeyTo)(self.optimizedMST)[3] == itemgetter(NodeKeyFrom)(self.optimizedMST)[3]:
            return

        result = self.find(itemgetter(NodeKeyTo)(self.optimizedMST)[3],itemgetter(NodeKeyFrom)(self.optimizedMST)[2])

        if result == itemgetter(NodeKeyFrom)(self.optimizedMST)[2]:
            return
        else:
            itemgetter(NodeKeyTo)(self.optimizedMST)[2:] = itemgetter(NodeKeyFrom)(self.optimizedMST)[:2]


    def find(self,node, i):
        """
        display(self): (helper method)
        description:
            - see if a node share the same common ancestor
        input: 
            -  
        output: 
            - message about each node class instance information
        """
        #! Really cool how you can do recursion
        print(node.key,i)
        if node.key == i:
            return i
        return self.find(itemgetter(node.key)(self.optimizedMST)[3],itemgetter(node.key)(self.optimizedMST)[2])


if __name__ == '__main__':
    val = [0,1,2,3,4] # all the way right
    data = ['a30','b20','c0','d10','e5']
    nodeLists = [ KruskalNode(k,d) for k,d in zip(val,data)]  
    gK = GraphKruskal()
    [gK.append(i) for i in nodeLists]
    gK.createEdge(0,1,8)
    gK.createEdge(0,2,5)
    gK.createEdge(1,2,9)
    gK.createEdge(1,3,11)
    gK.createEdge(2,3,15)
    gK.createEdge(2,4,10)
    gK.createEdge(3,4,7)
    
    
    print(gK.isPresent(['1231',0,769]))
    # print(gK.isPresent([4]))
    gK.display()
    gK.minimumSpanningTree()
