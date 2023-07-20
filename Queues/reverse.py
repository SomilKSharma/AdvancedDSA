'''
Given an array of integers A and an integer B, we need to reverse the order of the first B elements of the array, 
leaving the other elements in the same relative order. 
NOTE: You are required to the first insert elements into an auxiliary queue then perform Reversal of first B elements.
'''
from collections import deque
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        #create a queue
        queue=deque()

        #put the values in a queue
        for value in A:
            queue.append(value)

        #create a stack
        stack=deque()

        #iterate for the first B elements
        for _ in range(B):
            #remove value from the queue and add to the stack
            stack.append(queue.popleft())
        
        #put the stack values back in the queue
        while stack:
            #add value tot he queue
            queue.append(stack.pop())
        
        #take our remaining elements and put them back in the queue
        for _ in range(len(queue)-B):
            queue.append(queue.popleft())
        
        #return the answer
        return queue
