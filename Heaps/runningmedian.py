'''
Given an array of integers, A denoting a stream of integers. 
New arrays of integer B and C are formed. 
Each time an integer is encountered in a stream, append it at the 
end of B and append the median of array B at the C.

Find and return the array C.

NOTE:
If the number of elements is N in B and N is odd, then consider the median as B[N/2] ( B must be in sorted order).
If the number of elements is N in B and N is even, then consider the median as B[N/2-1]. ( B must be in sorted order).
'''

from heapq import heappop,heappush
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        #get a median array to store the answer
        median=[]

        #create two heaps
        max_heap=[]
        min_heap=[]

        #put the first value in max_heap and median array
        median.append(A[0])
        heappush(max_heap,-A[0])

        #iterate for each value in the array
        for value in A[1:]:
            #check if value in less than max in max_heap
            if value<=-max_heap[0]:
                #put value in max_heap
                heappush(max_heap,-value)
            else:
                #put value in min_heap
                heappush(min_heap,value)
            #check for the length difference
            if len(min_heap)>len(max_heap):
                heappush(max_heap,-heappop(min_heap))
            elif len(max_heap)-len(min_heap)>1:
                heappush(min_heap,-heappop(max_heap))
            #store the value in the median array
            median.append(-max_heap[0])
        
        #return the median array
        return median
