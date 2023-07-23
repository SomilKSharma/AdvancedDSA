'''
Given N jobs where every job is represented by following three elements of it. 
1.Start Time
2.Finish Time
3.Profit Associated
Find and return the maximum profit subset of jobs such that no 
two jobs in the subset overlap.
'''

from heapq import heappop,heappush
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        #sort the array by default based on the start time
        A.sort()

        #make a variable to store the last profit
        last_max_profit=0
        present_profit=0

        #create the heap to store the value
        min_heap=[]

        #make a loop to iterate for each value in the array A
        for start,end,profit in A:
            #iterate on the min heap for an answer
            while min_heap and start>=min_heap[0][0]:
                #pop the minimum level
                _,present_profit=heappop(min_heap)
                #store the last maximum profit
                last_max_profit=max(present_profit,last_max_profit)
            #add the value to the min heap
            heappush(min_heap,(end,profit+last_max_profit))
        
        #get a maximum variable to get the max answer
        maximum=0
        while min_heap:
            #pop the elements and get the maximum
            _,profit=heappop(min_heap)
            maximum=max(maximum,profit)
        
        #return the answer
        return maximum

