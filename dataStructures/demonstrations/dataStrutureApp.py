import argparse
import inspect
import cmd
from pathlib import Path
import os

# rich commandline modules
# documentation https://github.com/willmcgugan/rich
from rich import (
    pretty,
    text, # you can configure style and console like you would on CSS https://rich.readthedocs.io/en/stable/style.html
    traceback,
    print
    )
from rich.console import Console
from rich.markdown import Markdown

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
        # rich module elements
        pretty.install()
        traceback.install()
        self.console = Console()
        # Datastructure elements
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
            interactiveDataStructures.prompt = text.Text(f'({dataStructure}) ', style="bold magenta") # doesn't quite work
        else:
            raise ValueError(f'Please choose one of the following available data structure: {availableDataStrutuces.keys()}')


    def do_DSInfo(self,info=False):
        """
        print all non special method of the data structure that was selected
        """
        print(f'Info regarding the Class:{type(self.dataStructure).__name__}.__init__\n{self.dataStructure.__init__.__doc__}\n')
        print(f'Info regarding the Node used for the Class: {type(self.DSNode).__name__}.__init__\n{self.DSNode.__init__.__doc__}\n')
        print(f'The following methods for {type(self.dataStructure).__name__} are available:\n{vdir(self.dataStructure)}\n')
        if info:
            print(f'Detailled overview of each methods of {type(self.dataStructure).__name__}:\n{vdir(self.dataStructure,info=True)}')
        # print(f'If you want more info about what a specific {type(self.DSNode).__name__} method use')

    def do_manual(self,arg):
        """
        If you want to learn more about data structures
        """
        #taken from Django
        # BASE_DIR = Path(__file__).resolve().parent.parent
        # woah pathlib is amazing
        BASE_DIR = Path('../dataStructure.md')

        with open(BASE_DIR) as readme:
            markdown = Markdown(readme.read())
        self.console.print(markdown)

    def default(self, line): #! this is what I was looking for the exec() cmd
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        try:
            # https://stackoverflow.com/questions/7969949/whats-the-difference-between-globals-locals-and-vars
            # glo
            
            return exec(line, globals())

            # exec(print(str(line)))

        except:# Exception as e:
            self.console.print_exception()
            # print(f'{e.__class__}:{e}')


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