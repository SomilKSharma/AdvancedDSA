'''
Given an array A, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.
More formally,

G[i] for an element A[i] = an element A[j] such that
j is maximum possible AND
j < i AND
A[j] < A[i]
Elements for which no smaller element exist, consider the next smaller element as -1.
'''
from collections import deque
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):

        #get a stack to get the near minimum
        stack=deque()

        #get an answer array to store the answer
        answer=[]

        #iterate for each value in A
        for value in A:
            #check for values in the stack
            while stack and stack[-1]>=value:
                stack.pop()
            #add value to the answer array
            if not stack:
                answer.append(-1)
            else:
                answer.append(stack[-1])
            #add value to the stack
            stack.append(value)
        
        #return the answer
        return answer
