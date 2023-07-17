'''
Given an one-dimensional integer array A of size N and an integer B.

Count all distinct pairs with difference equal to B.

Here a pair is defined as an integer pair (x, y), where x and y are both numbers in the array and their absolute difference is B.
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #sort the array
        A.sort()

        #get the start and end index
        start,end=0,1

        #get a counter set
        hashset=set()

        #iterate till start<=end
        while end<len(A):
            #check if equal
            if A[end]-A[start]==B:
                hashset.add((A[end],A[start]))
                end=end+1
            #if the difference is less
            elif A[end]-A[start]>B:
                start=start+1
                if start==end:
                    end=end+1
            #the difference is more than required
            else:
                end=end+1
        
        #return the length of hashset
        return len(hashset)
            