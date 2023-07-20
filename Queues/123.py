'''
Given an integer, A. Find and Return first positive A integers 
in ascending order containing only digits 1, 2, and 3.
NOTE: All the A integers will fit in 32-bit integers.
'''
from collections import deque
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):

        #create a queue
        queue=deque()
        #add the first three digits
        queue.append('1')
        queue.append('2')
        queue.append('3')

        #get an value variable
        value=''
        #get an answer array
        answer=[]
        for _ in range(A):
            #get the value
            value=queue.popleft()
            answer.append(value)
            #add the values of value back into the queue
            queue.append(value+'1')
            queue.append(value+'2')
            queue.append(value+'3')
        
        #return answer
        return answer