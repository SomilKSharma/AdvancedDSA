'''
Given an integer array A of size N. You have to find the product of 
the three largest integers in array A from range 1 to i, where i goes 
from 1 to N.

Return an array B where B[i] is the product of the largest 3 integers in range 1 to i in array A. If i < 3, then the integer at index i in B should be -1.
'''

from heapq import heappop, heappush
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        #create a min heap
        min_heap=[]

        #get an answer array with -1 as first two values
        answer=[-1,-1]

        #get a product variable
        product=1

        #iterate for the first three values
        for index in range(3):
            #append the values
            heappush(min_heap,A[index])
            product=product*A[index]
        
        #append the product in the answer array
        answer.append(product)

        #iterate for all other values in the array using sliding window
        for value in A[3:]:
            #check for value being among the three greatest
            if value>min_heap[0]:
                #remove the minimum element in the heap
                mini=heappop(min_heap)
                #remove it from the product
                product=product//mini
                #add the value to the min heap and to the product
                heappush(min_heap,value)
                product=product*value
            #add value to the answer array
            answer.append(product)
        
        #return the answer array
        return answer
