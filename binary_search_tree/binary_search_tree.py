import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, num):
        # base case:
        # if there is no node at root:
        if (self.value == None):
            # insert this node at root
            self = BinarySearchTree(num)
            return

        else:
            # compare value to the root
            if num < self.value:
            # if value < root:
                # look left,
                if self.left is not None:
                    #if node: repeat steps
                    return self.left.insert(num)
                else:
                    # else: no node, make new one w this value 
                    self.left = BinarySearchTree(num)
            # if value >= root:
            if num >= self.value:
                # look right
                if self.right is not None:
                    #if node: repeat steps
                    return self.right.insert(num)
                    # else, no node, make new one w this value
                else:
                    self.right = BinarySearchTree(num)
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        # if value < root, go left
        elif self.left and target < self.value:
            return self.left.contains(target)
        elif self.right and target >= self.value:
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if no right child, return
        if not self.right:
            return self.value
        else:
             # else, go right
            return self.right.get_max()
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        else:
            return

        
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)

        while q.len() is not 0:
            temp = q.dequeue()
            print(temp.value)

            if temp.right:
                q.enqueue(temp.right)
            if temp.left:
                q.enqueue(temp.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)

        while s.len() is not 0:
            temp = s.pop()
            print(temp.value)

            if temp.right:
                s.push(temp.right)
            if temp.left:
                s.push(temp.left)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # data, complete entire left tree, complete entire right tree
        print(node.value)
        # continue going left
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # left, right, data
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)
