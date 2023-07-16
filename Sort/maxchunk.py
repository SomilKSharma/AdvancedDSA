'''
    Given an array of integers A of size N that is a permutation of [0, 1, 2, ..., (N-1)], if we split the array into some number of "chunks" (partitions), and individually sort each chunk. After concatenating them in order of splitting, the result equals the sorted array.
    What is the most number of chunks we could have made?
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #chunks counter
        chunk=0

        #take a maximum counter
        maxi=float('-inf')

        #iterate for each index and get the maximum to check for chunk
        for index,value in enumerate(A):
            #get the maxi
            maxi=max(maxi,value)
            #check for chunks
            if maxi==index:
                chunk+=1
        
        #return the answer
        return chunk
