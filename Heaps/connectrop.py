'''
You are given an array A of integers that represent the lengths of 
ropes. You need to connect these ropes into one rope. The cost of 
joining two ropes equals the sum of their lengths.

Find and return the minimum cost to connect these ropes into one rope.
'''

from heapq import heappop, heappush
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #create a min heap
        min_heap=[]

        #add all the elements to the min heap
        for value in A:
            #add the elements to the heap
            heappush(min_heap,value)
        
        #get the minimum cost
        cost=0
        while min_heap:
            #get the two ropes length
            first=heappop(min_heap)
            #check if heap empty
            if not min_heap:
                break
            second=heappop(min_heap)
            #add the two
            add=first+second
            #add the cost to the total cost
            cost=cost+add
            #return added rope to the min heap
            heappush(min_heap,add)
        
        #return the cost
        return cost
