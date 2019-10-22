# CS3
# Angel Rodriguez II
# Lab 3 - Option B
# Diego Aguirre
# 10-21-2019
# Purpose: The purpose of this code is to utilize 2 different types of balanced search trees to store all of the
#              words in the english dictionary. This code contains a method that will create all the permutations of a
#               word and search them in the BST (either an AVL tree or Red-Black Tree).

import sys

def print_anagrams_avl(word, prefix=""):
   if len(word) <= 1:
       str = prefix + word

       if (avl_tree.search(root, str) == True):
          print(prefix + word)
   else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
              print_anagrams_avl(before + after, prefix + cur)

def count_anagrams_avl(word, prefix=""):
   count = 0
   if len(word) <= 1:
       str = prefix + word

       if (avl_tree.search(root, str) == True):
           return 1 # adds 1 to the recursive call
   else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
              count += count_anagrams_avl(before + after, prefix + cur) # recursive call that will add count
   return count

def print_anagrams_rb(word, prefix=""):
   if len(word) <= 1:
       str = prefix + word

       if (rb_tree.contains(str)):
           print(prefix + word)
   else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
               print_anagrams_rb(before + after, prefix + cur)

def count_anagrams_rb(word, prefix=""):
   count = 0
   if len(word) <= 1:
       str = prefix + word

       if (rb_tree.contains(str)):
           return 1
           # print(prefix + word)
   else:
       for i in range(len(word)):
           cur = word[i: i + 1]
           before = word[0: i] # letters before cur
           after = word[i + 1:] # letters after cur

           if cur not in before: # Check if permutations of cur have not been generated.
               count += count_anagrams_rb(before + after, prefix + cur)
   return count

def find_max_anagrams(list): # this method will find the word with the most amount of anagrams given a list
    max = 0
    word = ""
    for i in range(len(list)):
        num = count_anagrams_avl(list[i]) # sets the returned value of the method to num
        if num > max: # if num is greater than max, this if-statement will execute
            max = num
            word = list[i]
    print(word) #prints the word with the most amount of anagrams



# Python code to insert a node in AVL tree

# Generic tree node class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the
# Insert operation
class AVLTree(object):

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

            # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

            # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

            # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

            # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def search(self, root, key):
        if root is None:
            return False
        if root.val == key:
            return True
        if root.val > key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)


"""
A classic (not left-leaning) Red-Black Tree implementation, supporting addition
"""

# The possible Node colors
BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'


class Node:
    def __init__(self, value, color, parent, left=None, right=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree:
    # every node has null nodes as children initially, create one such object for easy management
    NIL_LEAF = Node(value=None, color=NIL, parent=None)

    def __init__(self):
        self.count = 0
        self.root = None
        self.ROTATIONS = {
            # Used for deletion and uses the sibling's relationship with his parent as a guide to the rotation
            'L': self._right_rotation,
            'R': self._left_rotation
        }

    def __iter__(self):
        if not self.root:
            return list()
        yield from self.root.__iter__()

    def add(self, value):
        if not self.root:
            self.root = Node(value, color=BLACK, parent=None, left=self.NIL_LEAF, right=self.NIL_LEAF)
            self.count += 1
            return
        parent, node_dir = self._find_parent(value)
        if node_dir is None:
            return  # value is in the tree
        new_node = Node(value=value, color=RED, parent=parent, left=self.NIL_LEAF, right=self.NIL_LEAF)
        if node_dir == 'L':
            parent.left = new_node
        else:
            parent.right = new_node

        self._try_rebalance(new_node)
        self.count += 1


    def contains(self, value) -> bool:
        """ Returns a boolean indicating if the given value is present in the tree """
        return bool(self.find_node(value))


    def _try_rebalance(self, node):
        """
        Given a red child node, determine if there is a need to rebalance (if the parent is red)
        If there is, rebalance it
        """
        parent = node.parent
        value = node.value
        if (parent is None  # what the fuck? (should not happen)
           or parent.parent is None  # parent is the root
           or (node.color != RED or parent.color != RED)):  # no need to rebalance
            return
        grandfather = parent.parent
        node_dir = 'L' if parent.value > value else 'R'
        parent_dir = 'L' if grandfather.value > parent.value else 'R'
        uncle = grandfather.right if parent_dir == 'L' else grandfather.left
        general_direction = node_dir + parent_dir

        if uncle == self.NIL_LEAF or uncle.color == BLACK:
            # rotate
            if general_direction == 'LL':
                self._right_rotation(node, parent, grandfather, to_recolor=True)
            elif general_direction == 'RR':
                self._left_rotation(node, parent, grandfather, to_recolor=True)
            elif general_direction == 'LR':
                self._right_rotation(node=None, parent=node, grandfather=parent)
                # due to the prev rotation, our node is now the parent
                self._left_rotation(node=parent, parent=node, grandfather=grandfather, to_recolor=True)
            elif general_direction == 'RL':
                self._left_rotation(node=None, parent=node, grandfather=parent)
                # due to the prev rotation, our node is now the parent
                self._right_rotation(node=parent, parent=node, grandfather=grandfather, to_recolor=True)
            else:
                raise Exception("{} is not a valid direction!".format(general_direction))
        else:  # uncle is RED
            self._recolor(grandfather)

    def __update_parent(self, node, parent_old_child, new_parent):
        """
        Our node 'switches' places with the old child
        Assigns a new parent to the node.
        If the new_parent is None, this means that our node becomes the root of the tree
        """
        node.parent = new_parent
        if new_parent:
            # Determine the old child's position in order to put node there
            if new_parent.value > parent_old_child.value:
                new_parent.left = node
            else:
                new_parent.right = node
        else:
            self.root = node

    def _right_rotation(self, node, parent, grandfather, to_recolor=False):
        grand_grandfather = grandfather.parent
        self.__update_parent(node=parent, parent_old_child=grandfather, new_parent=grand_grandfather)

        old_right = parent.right
        parent.right = grandfather
        grandfather.parent = parent

        grandfather.left = old_right  # save the old right values
        old_right.parent = grandfather

        if to_recolor:
            parent.color = BLACK
            node.color = RED
            grandfather.color = RED

    def _left_rotation(self, node, parent, grandfather, to_recolor=False):
        grand_grandfather = grandfather.parent
        self.__update_parent(node=parent, parent_old_child=grandfather, new_parent=grand_grandfather)

        old_left = parent.left
        parent.left = grandfather
        grandfather.parent = parent

        grandfather.right = old_left  # save the old left values
        old_left.parent = grandfather

        if to_recolor:
            parent.color = BLACK
            node.color = RED
            grandfather.color = RED

    def _recolor(self, grandfather):
        grandfather.right.color = BLACK
        grandfather.left.color = BLACK
        if grandfather != self.root:
            grandfather.color = RED
        self._try_rebalance(grandfather)

    def _find_parent(self, value):
        """ Finds a place for the value in our binary tree"""
        def inner_find(parent):
            """
            Return the appropriate parent node for our new node as well as the side it should be on
            """
            if value == parent.value:
                return None, None
            elif parent.value < value:
                if parent.right.color == NIL:  # no more to go
                    return parent, 'R'
                return inner_find(parent.right)
            elif value < parent.value:
                if parent.left.color == NIL:  # no more to go
                    return parent, 'L'
                return inner_find(parent.left)

        return inner_find(self.root)

    def find_node(self, value):
        def inner_find(root):
            if root is None or root == self.NIL_LEAF:
                return None
            if value > root.value:
                return inner_find(root.right)
            elif value < root.value:
                return inner_find(root.left)
            else:
                return root

        found_node = inner_find(self.root)
        return found_node

list = []
with open("words.txt", "r") as f: # opens the given file name in read mode and closed the file when the code is finished executing
    for line in f:
        # print(line, end="")
        current_line = line.split() # splits the lines in the text file where there is white space
        word = current_line[0]
        list.append(word)  # appends the passwords to a list

test_list = []
with open("test_words.txt", "r") as f: # opens the given file name in read mode and closed the file when the code is finished executing
    for line in f:
        # print(line, end="")
        current_line = line.split() # splits the lines in the text file where there is white space
        word = current_line[0]
        test_list.append(word)  # appends the passwords to a list

print("What word would you like to find the anagrams for?...")
word = input()
print("What type of binary tree would you like to use?")
print("Please enter 1 or 2.")
print("1. AVL Tree")
print("2. Red-Black Tree")
x = input()

if int(x) == 1:
    print("---computing---")
    avl_tree = AVLTree()
    root = None
    anagrams = []

    for i in range(len(list)):
        root = avl_tree.insert(root, list[i])

    print_anagrams_avl(word)

    print(count_anagrams_avl(word))

if int(x) == 2:
    print("---filling the tree & computing anagrams---")
    rb_tree = RedBlackTree()

    for i in range(len(list)):
        rb_tree.add(list[i])

    print(count_anagrams_rb(word))


print("Do you want to find the word with the most amount of anagrams in the test list?...")
print("Type '1' for yes or '2' for no")
user_input = input()
if int(user_input) == 1:
    print("---finding the max in the test list---")
    find_max_anagrams(test_list)
else:
    sys.exit()

