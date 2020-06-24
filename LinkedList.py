"""
# What is LinkedList?

# Applications

# Advantages

# Disadvantages


"""

# Create a node object for linkedlist
class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None


# Create a LinkedList object
class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # insertAtStart O(1)
    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head  = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # Travese through LinkedList
    def traveseList(self):
        actualNode = self.head
        size = 0
        while actualNode is not None:
            # size +=1
            print('%d' % actualNode.data)
            actualNode = actualNode.nextNode

    # InsertAtEnd O(n)
    def insertEnd(self, data):
        self.size = self.size+1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None: # find the current end node
            actualNode = actualNode.nextNode
        
        actualNode.nextNode = newNode
        newNode.nextNode = None

    # Remove 
    def remove(self, data):
        if self.head == None: # empty linkedlist
            return 
        
        currentNode = self.head
        prevNode = None
        while currentNode.data != data:
            prevNode = currentNode
            currentNode = currentNode.nextNode

        if prevNode == None:
            # remove the headnode
            self.head = currentNode.nextNode
            self.size = self.size - 1
        else: 
            prevNode.nextNode = currentNode.nextNode
            self.size = self.size - 1






# create a linkedlist [1,2,3,4,5,6,7]

linkedlist = LinkedList()

linkedlist.insertStart(1)
linkedlist.insertEnd(2)
linkedlist.insertEnd(3)
linkedlist.insertEnd(4)
linkedlist.insertEnd(5)



linkedlist.traveseList()
linkedlist.size

linkedlist.remove(2)