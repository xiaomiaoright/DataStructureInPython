"""
# What is BST?
Data Structure
Keys in sorted order
each node at most 2 children: left and right

# Properties of BST
O(logN) for balanced BST
# Operations
bst.insert()
bst.delete()
bst.tranverse(): in order, pre-order, post-order
"""

# create a node class, each node has at most 2 children
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# define the BinarySearchTree class
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root: # root node is empty
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    # if tree balanced -- O(logN)
    def insertNode(self, data, node):
        if data < node.data: # should be insert on left of the node
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def getMinValue(self):
        if self.root: # when there are items
            return self.getMin(self.root)
    
    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        
        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node): # left - root - right
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print("%d" % node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self,data, node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild: # left node
                print('removing leaf node')
                del node
                return None
            if not node.leftChild:
                print('removing node with single right child')
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print('removing node with single left child')
                tempNode = node.leftChild
                del node
                return tempNode 
            
            print('removing node with two children')
            tempNode = self.getPredecesor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        
        return node
    
    def getPredecesor(self, node):
        if node.rightChild:
            return self.getPredecesor(node.rightChild)
        else:
            return node



bst = BinarySearchTree()
bst.insert(10)
bst.insert(13)
bst.insert(5)
bst.insert(1)

bst.getMaxValue()
bst.getMinValue()
bst.traverse()

bst.remove(10) # single left node

bst.traverse()



# bst = BinarySearchTree()
# bst.insert('A')
# bst.insert('B')
# bst.insert('F')
# bst.insert('O')

# bst.getMaxValue()
# bst.getMinValue()
# bst.traverse()