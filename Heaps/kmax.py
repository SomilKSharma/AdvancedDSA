'''
Given an integer array B of size N. You need to find the Ath 
largest element in the subarray [1 to i], where i varies from 1 to N. 
In other words, find the Ath largest element in the sub-arrays 
[1 : 1], [1 : 2], [1 : 3], ...., [1 : N].

NOTE: If any subarray [1 : i] has less than A elements, then the output should be -1 at the ith index.
'''

from heapq import heappop,heappush
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):

        #create a min heap
        min_heap=[]

        #answer array
        answer=[]

        #iterate for the A elements
        for index in range(A):
            #push the element in the min heap
            heappush(min_heap,B[index])
            answer.append(-1)
        
        #add answer array
        answer.pop()
        answer.append(min_heap[0])

        #iterate for the other values in the index
        for index in range(A,len(B)):
            #get the value at the index
            value=B[index]
            #compare it withe value in min heap
            if value>min_heap[0]:
                #push the minimum element
                heappop(min_heap)
                #add the element
                heappush(min_heap,value)
            #add answer array
            answer.append(min_heap[0])
        
        #return the value
        return answer