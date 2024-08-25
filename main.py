'''
Project:
Author: 
Course: 
Date: 

Description:

Lessons Learned:

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST
from bst import Node


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    pair_tree = BST()

    ignore = set(whitespace + punctuation)

    with open('around-the-world-in-80-days-3.txt', 'r') as file:
    #with open('test_file.txt', 'r') as file:
        for character in file.read():
            #print(character)
            #print("")

            if character in ignore:
                continue

            character = character.lower()

            try:
                found_char = pair_tree.find(Pair(character))
                found_char.count += 1
            except ValueError:
                pair_tree.add(Pair(character))

def main():

    #make_tree()

    my_test1 = BST()    #reg
    my_test1.add(2)
    my_test1.add(1)
    my_test1.add(3)

    my_test1.add(2)
    my_test1.add(1)
    my_test1.add(3)
    print(my_test1)

    '''
    my_test2 = BST()    #just root
    my_test2.add(1)
    print(my_test2)

    my_test3 = BST()    #nothing
    print(my_test3)

    my_test4 = BST()    #one childe
    my_test4.add(2)
    my_test4.add(1)
    print(my_test4)
    '''

    
if __name__ == "__main__":
    main()
