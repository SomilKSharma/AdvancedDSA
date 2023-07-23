'''
Given a sorted matrix of integers A of size N x M and an integer B.
Each of the rows and columns of matrix A is sorted in ascending order, find the Bth smallest element in the matrix.

NOTE: Return The Bth smallest element in the sorted order, not the Bth distinct element.
'''

from heapq import heappop,heappush
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #create a max heap
        max_heap=[]

        #iterate for each row in the matrix
        for row in range(len(A)):
            #iterate for each column
            for col in range(len(A[0])):
                #get the value at the location
                value=A[row][col]
                #check the length of max_heap
                length=len(max_heap)
                #see if value has to be added or the be replaced
                if length<B:
                    #add the element to the max_heap
                    heappush(max_heap,-value)
                else:
                    #compare the present value with the max value in the stack
                    if value<-max_heap[0]:
                        #remove the max element
                        heappop(max_heap)
                        #add the minimum
                        heappush(max_heap,-value)
        
        #return the answer
        return -max_heap[0]


            

