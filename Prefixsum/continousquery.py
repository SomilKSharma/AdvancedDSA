#Continuous Sum Query

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):

        #beggar money
        beggar=[
            0
            for _ in range(A)
        ]

        #put values for prefix sum
        for start,end,donate in B:
            #reduce value by 1 for 0 indexing
            start,end=start-1,end-1
            #put values at the start
            beggar[start]=beggar[start]+donate
            #put values for the end
            if end+1!=A:
                beggar[end+1]=beggar[end+1]-donate
        
        #get the prefix sum to find the answer
        for index in range(1,A):
            beggar[index]=beggar[index-1]+beggar[index]
        
        #return the value of the index
        return beggar

