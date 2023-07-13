'''Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #count the number of elements less than or equal to B
        count=0
        for value in A:
            #check for less and equal
            if value<=B:
                count+=1
        
        #get the first window of lenght count and get swap number
        swaps=0
        for index in range(count):
            #check for swap
            if A[index]>B:
                swaps+=1
            
        #take this swap count as the minimum
        mini=swaps

        #sliding window to get the other values
        for index in range(len(A)-count):
            #check for left most index to remove it
            if A[index]>B:
                swaps=swaps-1
            #check for new element
            if A[index+count]>B:
                swaps=swaps+1
            #get the minimum swaps
            mini=min(mini,swaps)

        return mini
