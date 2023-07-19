'''
Given an array A, find the next greater element G[i] for every element A[i] in the array. 
The next greater element for an element A[i] is the first greater element on the right side of A[i] in the array, A.
More formally:
G[i] for an element A[i] = an element A[j] such that 
    j is minimum possible AND 
    j > i AND
    A[j] > A[i]
Elements for which no greater element exists, consider the next greater element as -1.
'''
from collections import deque
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):

        #create a function to find the closest greater element on left
        def greater_left(array):
            #create a stack
            stack=deque()
            #create an answer array
            answer=[]
            #iterate for each value of the array get the answer
            for value in array:
                #check for elements greater to the left
                while stack and stack[-1]<=value:
                    stack.pop()
                #check if stack is empty or not
                if not stack:
                    answer.append(-1)
                else:
                    answer.append(stack[-1])
                #add value to the stack
                stack.append(value)
            #return the answer array
            return answer
        
        #call the greater_left function in reverse
        answer=greater_left(A[::-1])

        #reverse the answer array to get the answer
        return answer[::-1]


