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
            'dynamicArray': DynamicArray(),
            'singleLinkedList': SinglyLinkedList(),
            'DoublyLinkedList': DoublyLinkedList(),
            }
        if dataStructure in availableDataStrutuces:
            self.dataStructure = availableDataStrutuces[dataStructure]
            self.DSname = dataStructure
            interactiveDataStructures.prompt = f'({dataStructure}) '
            print('yeah')
        else:
            raise ValueError(f'Please choose one of the following available data structure: {availableDataStrutuces.keys()}')
    

    def do_DSInfo(self,arg):
        """
        print all non special method of the datastructure
        """
        print(f'info regarding the {self.DSname}.__init__\n{self.dataStructure.__init__.__doc__}')
        print(f'the following methods for {self.DSname} are available:\n{vdir(self.dataStructure)}')
        print(f'If you want more info about what a specific {self.DSname} method use')


    def do_DSMetInfo(self,line):
        """
        I want to print the docstrings of the in usage datastructure when the user type it in the search cmd line
        """
        # methodList = [s for s in line.split()]
        # [print_docs(m) for m in vdir(self.dataStructure)]

                #print_docs(self.dataStructure.__str__(method) )
        # else:
        #     print(f'To learn more about methods available in {self.DSname} select one of the following method {methods}\n You entered: {method}')


    def do_exit(self,arg):
        """
        exits the command line
        """
        exit()
            

#python dataStrutureApp.py --dataStructure dynamicArray # for testing

# the lines bellow won't run if imported
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #TODO: add the list of available data structures in a way that I don't have to rewrite myself
    #parser.add_argument('--help',type=str,help='The following data Structures are available')
    parser.add_argument('--dataStructure', type=str, default=None,help='Enter the data')
    opt = parser.parse_args()
    #print(opt)
    interactiveDataStructures(opt.dataStructure).cmdloop()

