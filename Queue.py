"""
# What is Queue?
ADT
FIFO

# Applications of Queue
CPU scheduling

# Operations
enqueue()
dequeue()
peak()

"""

class Queue:
    def __init__(self):
        self.queue = [] # construct queue with array
    
    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data): # insert an item to the end of queue
        self.queue.append(data)

    def dequeue(self): # remove the first item in the queue
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peak(self): # return the value of first item without removing it
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

queue.sizeQueue()
queue.peak()
queue.dequeue()