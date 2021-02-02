import argparse
import inspect
import cmd
# custom data structures
from dynamicArray import DynamicArray
from linkedList import (
    SinglyLinkedList,
    DoublyLinkedList,
    ListNode
    )
from stack import (
    StackNode,
    Stack
    )
from queues import (
    QueueNode,
    Queue,
    PQNode,
    PriorityQueue
    )

def is_relevant(obj):
    """Filter for the inspector to filter out non user defined functions/classes
    taken from:
    https://stackoverflow.com/questions/58089209/printing-python-docstrings-for-all-class-methods
    """
    if hasattr(obj, '__name__') and obj.__name__ == 'type':
        return False
    if inspect.isfunction(obj) or inspect.isclass(obj) or inspect.ismethod(obj):
        return True


def print_docs(module):
    default = 'No doc string provided' # Default if there is no docstring, can be removed if you want
    flag = True

    for child in inspect.getmembers(module, is_relevant):
        if not flag: print('\n\n\n')
        flag = False # To avoid the newlines at top of output
        doc = inspect.getdoc(child[1])
        if not doc:
            doc = default
        print(child[0], doc, sep = '\n')

        if inspect.isclass(child[1]):
            for grandchild in inspect.getmembers(child[1], is_relevant):
                doc = inspect.getdoc(grandchild[1])
                if doc:
                    doc = doc.replace('\n', '\n    ')
                else:
                    doc = default 
                print('\n    ' + grandchild[0], doc, sep = '\n    ')


def vdir(obj,info=False):
    """
    used to display to the user what non special method are available
    taken from stack overflow
    getattr is really cool to get access to a class object methods
    https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    callable allows us to filter the class variables (not callable()) and the class methods which are
    https://stackoverflow.com/questions/1398022/looping-over-all-member-variables-of-a-class-in-python
    """
    if info:
        return [print(f'Nethod name: {getattr(obj, str(x)).__name__}\nDocStrings:\n{getattr(obj, str(x)).__doc__}') for x in dir(obj) if callable(getattr(obj,x)) and not x.startswith('__')]
    return [x for x in dir(obj) if callable(getattr(obj,x)) and not x.startswith('__')]


    """
    Program that does the following:
    - runs entirely in the CLI
    - help the user with the choosen data structure associated method (dir of non-special methods
    and displays the docstrings
    #TODO: create better docstrings 
    - runs in a while loop and waits 
    """

# to be added for help
#print(ListNode.__init__.__doc__)
class interactiveDataStructures(cmd.Cmd):
    """
    documentation: https://docs.python.org/3/library/cmd.html
    """
    intro = 'Welcome to the command line interactive data Structure program.\nType help or ? to list commands.\n'
    prompt = None


    def __init__(self, dataStructure):
        super(interactiveDataStructures, self).__init__()

        availableDataStrutuces = {
            'DynamicArray': DynamicArray(),
            'SingleLinkedList': SinglyLinkedList(),
            'DoublyLinkedList': DoublyLinkedList(),
            'Stack': Stack(),
            'Queue': Queue(),
            'PriorityQueue': PriorityQueue()
            }

        correspondingNodes = {
            'DynamicArray': None,
            'SingleLinkedList': ListNode(None),
            'DoublyLinkedList': ListNode(None),
            'Stack': StackNode(None),
            'Queue': QueueNode(None),
            'PriorityQueue': PQNode(None)
            }

        if dataStructure in availableDataStrutuces:
            self.dataStructure = availableDataStrutuces[dataStructure]
            self.DSNode = correspondingNodes[dataStructure]
            self.DSname = dataStructure
            interactiveDataStructures.prompt = f'({dataStructure}) '
            print('yeah')
        else:
            raise ValueError(f'Please choose one of the following available data structure: {availableDataStrutuces.keys()}')


    def do_DSInfo(self,info=False):
        """
        print all non special method of the datastructure
        """
        print(f'Info regarding the Class:{type(self.dataStructure).__name__}.__init__\n{self.dataStructure.__init__.__doc__}\n')
        print(f'Info regarding the Node used for the Class: {type(self.DSNode).__name__}.__init__\n{self.DSNode.__init__.__doc__}\n')
        print(f'The following methods for {type(self.dataStructure).__name__} are available:\n{vdir(self.dataStructure)}\n')
        if info:
            print(f'Detailled overview of each methods of {type(self.dataStructure).__name__}:\n{vdir(self.dataStructure,info=True)}')
        # print(f'If you want more info about what a specific {type(self.DSNode).__name__} method use')


    def default(self, line): #! this is what I was looking for the exec() cmd
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        try:
            # https://stackoverflow.com/questions/7969949/whats-the-difference-between-globals-locals-and-vars
            # glo
            return exec(line, globals())
        except Exception as e:
            print(f'{e.__class__}:{e}')


    def do_exit(self,arg):
        """
        exits the command line
        """
        exit()
            

#python dataStrutureApp.py --dataStructure Queue # for testing

# the lines bellow won't run if imported
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    #TODO: add the list of available data structures in a way that I don't have to rewrite myself
    #parser.add_argument('--help',type=str,help='The following data Structures are available')
    parser.add_argument('--dataStructure', type=str, default=None,help='Enter the data')
    opt = parser.parse_args()
    #print(opt)
    # opt.dataStructure = 'Queue'
    interactiveDataStructures(opt.dataStructure).cmdloop()

# test
# nodes = [QueueNode(i) for i in range(5)]
# test = Queue()
# [test.enqueue(i) for i in nodes]
#! rewrite the docstrings (add search(self,nodeKey) to help people)