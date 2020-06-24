"""
# What is stack?
ADT
FILO

# What is Applications of Stack?

# Operations of Stack
push
pop
peak

# Stack and recursion
"""

# define a stack object with python
class Stack:
    def __init__(self):
        self.stack = []  # implement stack with array

    def isEmpty(self):
        return self.stack == []

    def push(self, data): # insert to the top of stack
        self.stack.append(data)


    def pop(self): # remove the last item inserted
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peak(self): # return the last item inserted without removing it
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)

stack = Stack()
stack.isEmpty()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.sizeStack()
stack.peak()
stack.pop()