'''
Given an array of integers A. There is a sliding window of size B, 
moving from the very left of the array to the very right. You can 
only see the B numbers in the window. Each time the sliding window 
moves rightwards by one position. You have to find the maximum 
for each window.

Return an array C, where C[i] is the maximum value in the array 
from A[i] to A[i+B-1].
Refer to the given example for clarity.

NOTE: If B > length of the array, return 1 element with 
the max of the array.
'''
from collections import deque
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):

        #create a my_deque to solve the question
        my_deque=deque()

        #get an answer array
        answer=[]

        #iterate for the first window of length B
        for index in range(B):
            #add the value to the my_deque
            while my_deque and my_deque[-1]<A[index]:
                my_deque.pop()
            #add the value to the my_deque
            my_deque.append(A[index])
        
        #add the value to the answer
        answer.append(my_deque[0])

        #slide the window to get the answer
        for index in range(len(A)-B):
            #remove the left most from the my_deque
            if A[index]==my_deque[0]:
                #remove the left most element
                my_deque.popleft()
            #add the value to the my_deque
            while my_deque and my_deque[-1]<A[index+B]:
                my_deque.pop()
            #add the value to the my_deque
            my_deque.append(A[index+B])
            #add the value to the answer
            answer.append(my_deque[0])
        
        #return the answer array
        return answer
            