'''
Given an array of integers A.
A represents a histogram i.e A[i] denotes the height of the ith 
histogram's bar. Width of each bar is 1.
Find the area of the largest rectangle formed by the histogram.
'''
from collections import deque
class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):

        #create a stack
        stack=deque()

        #get left min index array
        left=[]
        #iterate for each value
        for index,value in enumerate(A):
            #check for value
            while stack and A[stack[-1]]>=value:
                stack.pop()
            #add the answer
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1])
            #add the following value to the stack
            stack.append(index)
        
        #declare a stack again
        stack=deque()

        #get right min index array
        right=[]
        #iterate for each value
        for index in reversed(range(len(A))):
            #check for value
            while stack and A[stack[-1]]>=A[index]:
                stack.pop()
            #add the answer
            if not stack:
                right.append(len(A))
            else:
                right.append(stack[-1])
            #add the following value to the stack
            stack.append(index)
        
        #reverse right
        right=right[::-1]
        
        #get the maximum index
        maxi=float('-inf')

        #iterate for each index,value and get the answer
        for index,value in enumerate(A):
            #get the maximum
            maxi=max(
                maxi,
                (right[index]-left[index]-1)*value
            )
        
        #return the maximum
        return maxi
        
