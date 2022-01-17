# Uses python3
import sys



# To build the binary search tree data structure, two classes are defined: BinaryTreeNode, specifying the properties of a binary tree
# and BinarySearchTree specifying the properties of a binary search tree in particular.
# An object of class BinaryTreeNode is a node consisting of a key, a left child and right child (simulating pointers since Python does not have pointers)
# and has basic OOP methods allowed to act on it outside the class, namely setters and getters for node elements
# As for the BinarySearchTree class, an object of it is the tree itself, consisting of a root (again simulating pointers)
# which is initially null and is assigned to an object of class BinaryTreeNode which by turn is connected to other objects/nodes of the class as the tree is filled up,
# and the root has a getter and setter as basic OOP methods.
# To be able to find the minimum key of a BST, an insertion method must be defined. To be able to insert a new node, its appropriate place (or parent in specific) must be found.

# A method FindParentOfNewNode is defined for this cause. This function takes the value of the key to be inserted to the new node,
# and current_node which is the root of the tree or subtree to find parent of new node in.
# The function compares the new key to the key of the current node, if it is less, it further checks if this node has a left child. If it does not, then the new node 
# can be its left child, then this node is returned as an expected parent of the new node. Otherwise, if it does have a child, then we further check down the tree by recursively
# calling the function but with the left child of the current node as the new current node of the next recursive step.
# The same happens if the new key is bigger than the key of the current node. If it does not have a right child, then the current node is returned as the expected parent
# of the new node. Otherwise, if it does, the function is recursively called with the right child of the current node as the new current node of the next recursive step,
# in order to further look down the tree for an appropriate parent of the new node, maintaining the properties of the BST.
# COMPLEXITY: O(h) where h is the height of the tree and ranges between O(log(n)), if the tree is balanced, and O(n), if the tree is extremely unbalaned.

# As for the insertion process itself, a method InsertOneNode is defined which takes the new key to be inserted. Firstly, an object of class BinaryTreeNode is instantiated as the new node.
# Then, the tree is checked if it is empty, if it is, this node is inserted as the root of the BST, otherwise, the method FindParentOfNewNode is called with the key and tree root as parameters
# to find the appropriate parent of the new node, then the new key is checked against the key of the parent, to find out whether to put the new node as its left or right child.
# COMPLEXITY: Same as complexity of FindParentOfNewNode method as the complexity of the rest of operations in the method is O(constant)

# To extend the generalization of the method to insert many nodes at once, not one by one, a method InsertManyNodes is defined, which takes a list of new keys to be added,
# and iteratively calls the InsertOneNode method on each key.
# COMPLEXITY: O(n*h), where n reperesnts the for loop of the number of new keys to be inserted, and in eaxh iteration, the method InsertOneNode
#             is called which is of complexity O(h), where O(log(n)) <= O(h) <= O(n)

# Finding minimum key in BST is implemented iteratively and recursively in FindMinimumIteratively and FindMinimumRecursively respectively. 
# The minimum key in general in a BST is key of the leftmost node of the tree. As long as the tree is not empty, the FindMinimumIteratively method sets the current_node, which is the node to begin 
# checking if it is the leftmost node from, as the root of the tree, and continues assigning the current node with its left child as long as it has one,
# until it reaches a node without a left child. Therefore, this is the leftmost node and its key is returned as the minimum of the BST.
# FindMinimumRecursively takes current node as a parameter and keeps recursively calling the function, assigning it with its left child as long as it has one,  
# until, a left-childless node is reached, and its key is returned as the minimum of the BST as it is the leftmost node.
# COMPLEXITY of both: O(h), where O(log(n)) <= O(h) <= O(n)
# Although both are of same complexity, each method has its pros and cons. Recursion is written in just a few lines of code but has a high space complexity due to stack consumption
# while iteration is sometimes less understandable and is written in relatively more lines of code, but has less space complexity than recursion. 



class BinaryTreeNode:

    def __init__(self, key):
        # Class Attributes: Node Elements: A Key, A Left Child and A Righ Child
        # Key is passed in the constructor and the children are initialized with none until assigned
        self.Key = key
        self.LeftChild = None
        self.RightChild = None

    # Setter for key of node
    def SetKey(self, new_key):
        self.Key = new_key

    # Setter for left child of node
    def SetLeftChild(self, new_left_child):
        self.LeftChild = new_left_child

    # Setter for right child of node
    def SetRightChild(self, new_right_child):
        self.RightChild = new_right_child

    # Getter for key of node
    def GetKey(self):
        return self.Key

    # Getter for left child of node
    def GetLeftChild(self):
        return self.LeftChild

    # Getter for right child of node
    def GetRightChild(self):
        return self.RightChild


class BinarySearchTree:

    def __init__(self):
        # Class Attributes: Root of BST, initialized as none until assigned (A tree can be empty)
        self.Root = None

    # Setter for Root of BST
    def SetRoot(self, new_root):
        self.Root = new_root

    # Getter for Root of BST
    def GetRoot(self):
        return self.Root

    def FindParentOfNewNode(self, key, current_node):

        # New key is compared against that of the current node,
        # If smaller and it has no left child, then new node can be its left child
        # Otherwise, if it has one, it is passed as the new current node in the recursive call of the function
        if current_node.GetKey() >= key:
            if current_node.GetLeftChild() != None:
                return self.FindParentOfNewNode(key, current_node.GetLeftChild())
            else: 
                return current_node

        # If new key is greater than that of the current node and it has no right child, then new node can be its right child
        # Otherwise, if it has one, it is passed as the new current node in the recursive call of the function
        if current_node.GetKey() < key:
            if current_node.GetRightChild() != None:
                return self.FindParentOfNewNode(key, current_node.GetRightChild())
            else:
                return current_node

    def InsertOneNode(self, key):

        # Instantiation of the new node of type BinaryTreeNode
        new_node = BinaryTreeNode(key)

        # If tree is already empty, the new node can be its root
        if self.Root == None:
            self.Root = new_node
        
        else:
            # Appropriate parent of new node is found
            parent = self.FindParentOfNewNode(key, self.Root)

            # Key of new node is compared against that of of the parent 
            # to assign it as its left or right child
            if key <= parent.GetKey():
                parent.SetLeftChild(new_node)
            else:
                parent.SetRightChild(new_node)

    # Generalization of the insertion process to insert a list of new nodes at once, instead of one-by-one
    def InsertManyNodes(self, new_keys_list):
        
        for i in range(len(new_keys_list)):
            self.InsertOneNode(new_keys_list[i])

    def FindMinimumIteratively(self):

        # If tree is already empty, the minimum does not exist, so None is returned
        if self.Root == None:
            return None

        # Beginning from the root, the leftmost node is checked for (it has not left child) until it is found 
        # by iteratively assigning current node with its child if it has one
        current_node = self.Root
        while current_node.GetLeftChild() != None:
            current_node = current_node.GetLeftChild()
        return current_node.GetKey()

    def FindMinimumRecursively(self, current_node):

        # If tree is already empty, the minimum does not exist, so None is returned
        if self.Root == None:
            return None

        # Beginning from the root, the leftmost node is checked for (it has not left child) until it is found 
        # by recursively replacing current node with its left child, if it has one, in the next recursive call
        if current_node.GetLeftChild() == None:
            return current_node.GetKey()
        else:
            return self.FindMinimumRecursively(current_node.GetLeftChild())
        
        

if __name__ == '__main__':

    input = sys.stdin.read()
    data = list(map(int, input.split()))

    tree = BinarySearchTree()
    tree.InsertManyNodes(data)

    print(tree.FindMinimumIteratively())
    print(tree.FindMinimumRecursively(tree.GetRoot()))
