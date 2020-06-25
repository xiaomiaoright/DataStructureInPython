"""
# What is heap
BST one type
Two main types: min heap and max heap
new elements inserted to next available place
implement with array
parent > children max heap
parent < children min heap
parent: i -> children: 2i+1, i+2

# properties of heap
search min or max: O(1)
insert new elemetns: O(logN)
remove: O(logN)

# applications of heap
Dijjkstra algorithm
Prims algorithm

# Operations
"""

# Define maximum # of elements stored in a heap, similiar to array
CAPACITY = 10

class Heap(object):
    def __init__(self):
        # initiate heap with capacity
        self.heap = [0] * CAPACITY
        self.heap_size = 0


    def insert(self, item):
        if self.heap_size == CAPACITY:
            return
        
        self.heap[self.heap_size] = item
        self.heap_size = self.heap_size+1

        self.fix_up(self.heap_size - 1)
    
    def fix_up(self, index):
        parent_index = (index-1) //2
        if index>0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def get_max(self):
        return self.heap[0]

    def poll(self): # remove max item and remove from heap
        max = self.get_max()
        self.swap(0, self.heap_size-1)
        self.heap_size = self.heap_size -1
        self.fix_down(0)
        return max

    def fix_down(self, index):
        index_left = 2*index+1
        index_right = 2*index+2
        index_largest = index

        if index_left < self.heap_size and self.heap[index_left] > self.heap[index]:
            index_largest = index_left
        if index_right < self.heap_size and self.heap[index_right] > self.heap[index]:
            index_largest = index_right
        
        if index != index_largest:
            self.swap(index, index_largest)
            self.fix_down(index_largest)

    def heap_sort(self):
        size = self.heap_size
        for i in range(size):
            max = self.poll()
            print(max)
        
if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(8)
    heap.insert(12)
    heap.insert(20)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(1)
    heap.insert(321)
    heap.heap


    heap.heap_size

    heap.get_max()


    heap.poll()
    heap.heap_sort()


# create heap data structure in python
from heapq import heappop, heappush, heapify
heap = []
nums = [12,3,-2,6,4,8,9]

for num in nums:
    heappush(heap, num)

while heap:
    print(heappop(heap))

heap

heapify(nums)
nums