"""
# What is AVL Trees
A Binary Search Tree Balanced

# what is balanced?
Height of left and right difference <=1

# what is height
distance of longest path for a node to its leaf node
height of leaf node is 0
height of parent node = max(child height) + 1
child of leaf node is null, with height -1
height can be calculated use recursion 
# properties
search O(logN)
sort: O(NlogN) 
# Applications
database
hashtables operations
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 0


class AVL(object):
    def __init__(self):
        self.root = None

    def calcHeight(self, node):
        if not node: 
            return -1
        return node.height

    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)
        # > 1 : left heavy tree -> right rotation
        # < -1: right heavy tree _> left rotation

    def rotateRight(self, node):
        print('Rotating to the right on the node ', node.data)
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild
        tempLeftChild.rightChild = node
        node.leftChild = t
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) +1
        return tempLeftChild
    
    def rotateLeft(self, node):
        print('Rotating to the left on the node ', node.data)
        tempRightChild = node.rightChild
        t = tempRightChild.leftChild
        tempRightChild.leftChild = node
        node.rightChild = t
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) +1
        return tempRightChild

    def insert(self,data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        # when the AVL tree is empty no root, add the node with data
        if not node:
            return Node(data)

        # when the AVL tree is not empty, check the value of node to data
        if data < node.data: # insert to the left
            node.leftChild = self.insertNode(data, node.leftChild)
        else: 
            node.rightChild = self.insertNode(data, node.rightChild)
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolation(data, node) 

    def settleViolation(self, data, node):
        balance = self.calcBalance(node)

        if balance > 1 and data < node.leftChild.data:
            print("Left heavy situation")
            return self.rotateRight(node)

        if balance < -1 and data > node.rightChild.data:
            print("Right heavy situation")
            return self.rotateLeft(node)
        if balance > 1 and data > node.rightChild.data:
            print("Left right heavy situation")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and data < node.leftChild.data:
            print("Right left heavy situation")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        return node

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            # remove the node
            if not node.leftChild and not node.rightChild: # node is leaf node
                print("removing a leaf node")
                del node
                return None
            if not node.leftChild: # node with right child
                print("removing node with single right child")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild: # node with left child
                print("removing node with signle left child")
                tempNode = node.leftChild
                del node
                return tempNode
            
            print("removing node with two children")
            tempNode = self.getPredecesor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolation(data, node) 

    def getPredecesor(self, node):
        if node.rightChild:
            return self.getPredecesor(node.rightChild)
        return node

    def traverse(self):
        if self.root:
            self.tranverseInOrder(self.root)

    def tranverseInOrder(self, node):
        if node.leftChild:
            self.tranverseInOrder(node.leftChild)
        print("%d" % node.data)

        if node.rightChild:
            self.tranverseInOrder(node.rightChild)



avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(30)

# avl.traverse()

# avl = AVL()
avl.insert(40)
avl.insert(50)
avl.insert(60)

avl.traverse()

avl.remove(20)