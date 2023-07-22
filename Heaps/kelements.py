'''
N people having different priorities are standing in a queue. The 
queue follows the property that each person is standing at most B 
places away from its position in the sorted queue.

Your task is to sort the queue in the increasing order of priorities.

NOTE:
No two persons can have the same priority.
Use the property of the queue to sort the queue with complexity 
O(NlogB).
'''

from heapq import heappop,heappush
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        #create a min heap
        min_heap=[]

        #iterate for the first B+1 elements
        for index in range(B+1):
            #insert the elements in the heap
            heappush(min_heap,A[index])
        
        #get an answer array to set the values
        answer=[]

        #iterate for the index in the array
        for index in range(B+1,len(A)):
            #put the value in answer
            answer.append(heappop(min_heap))
            #put the next value in min_heap
            heappush(min_heap,A[index])
        
        #put the remaining element in the answer array
        while min_heap:
            #put element in the answer array
            answer.append(heappop(min_heap))
        
        #return the answer array
        return answer
