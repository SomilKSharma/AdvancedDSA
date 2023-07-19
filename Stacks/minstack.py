'''
Design a stack that supports push, pop, top, and retrieve the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
NOTE:
All the operations have to be constant time operations.
getMin() should return -1 if the stack is empty.
pop() should return nothing if the stack is empty.
top() should return -1 if the stack is empty.
'''
from collections import deque
class MinStack:
    
    # @param x, an integer
    # @return nothing
    def push(self, x):
        #push the value in the top of the stack
        self.stack.append(x)
        #check for mini
        if not self.mini or x<=self.mini[-1]:
            self.mini.append(x)

    # @return nothing
    def pop(self):
        #check if stack isn't empty
        if not self.stack:
            return -1
        #else we would pop the top element
        value=self.stack.pop()
        #check for mini element
        if self.mini[-1]==value:
            self.mini.pop()
        #return the value
        return value

    # @return an integer
    def top(self):
        #check for stack
        if not self.stack:
            return -1
        #return the top most value
        return self.stack[-1]
        
    # @return an integer
    def getMin(self):
        #check for mini
        if not self.mini:
            return -1
        #return the top most mini
        return self.mini[-1]
        
    #create the stack using constructor
    def __init__(self):
        #create the stack for value
        self.stack=deque()
        #create a stack for minimum value
        self.mini=deque()