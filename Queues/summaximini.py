'''
Given an array A of both positive and negative integers.
Your task is to compute the sum of minimum and maximum elements 
of all sub-array of size B.

NOTE: Since the answer can be very large, you are required to return the sum modulo 109 + 7.
'''
from collections import deque
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #deques for maximum and minimum
        maxi=deque()
        mini=deque()

        #iterate through the first window
        for index in range(B):
            #get the value
            value=A[index]
            #iterate for each value
            while maxi and maxi[-1]<value:
                maxi.pop()
            while mini and mini[-1]>value:
                mini.pop()
            #add the value
            maxi.append(value)
            mini.append(value)
        
        #get a sums variable
        sums=0
        sums=sums+maxi[0]+mini[0]

        #slide the window to get the answer
        for index in range(len(A)-B):
            #check for left most value
            value=A[index]
            #compare with the first element of the deque
            if value==maxi[0]:
                maxi.popleft()
            if value==mini[0]:
                mini.popleft()
            #get the right most element
            value=A[index+B]
            #iterate for each value
            while maxi and maxi[-1]<value:
                maxi.pop()
            while mini and mini[-1]>value:
                mini.pop()
            #add the value
            maxi.append(value)
            mini.append(value)
            #sum the value
            sums=sums+maxi[0]+mini[0]
        
        #return the value
        return sums%1000000007



