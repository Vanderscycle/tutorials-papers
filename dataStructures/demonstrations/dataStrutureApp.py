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


def vdir(obj):
    """
    used to display to the user what non special method are available
    taken from stack overflow
    """
    return [x for x in dir(obj) if not x.startswith('__')]


def interactiveDataStructuresTest():
    """
    Program that does the following:
    - runs entirely in the CLI
    - help the user with the choosen data structure associated method (dir of non-special methods
    and displays the docstrings
    #TODO: create better docstrings 
    - runs in a while loop and waits 
    """

    dataStructure = opt.dataStructure
    while True:
        try:
            # f'{dataStructure}:'
            #! instead of input I may want to use cmd module 
            # https://docs.python.org/3/library/cmd.html
            userCommand = input(f'{dataStructure}:')
            if userCommand == ('exit' or 'quit'):
                print('Exiting program')
                break
        except Exception as e:
            print(e)

    pass


class interactiveDataStructures(cmd.Cmd):
    """
    documentation: https://docs.python.org/3/library/cmd.html
    """
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = None
    file = None
    def __init__(self, dataStructure):
        self.dataS
        interactiveDataStructures.prompt = f'{dataStructure}'



# the lines bellow won't run if imported
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #TODO: add the list of available data structures in a way that I don't have to rewrite myself
    parser.add_argument('--help',type=str,help='The following data Structures are available')
    parser.add_argument('--dataStructure', type=str, default=None,help='Enter the data')
    opt = parser.parse_args()
    print(opt)
    interactiveDataStructuresTest()

