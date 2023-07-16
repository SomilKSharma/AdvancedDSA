#check and return whether the array elements are consecutive or not.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #sort the array
        A.sort()

        #iterate for each consecutive value comparison
        for index in range(1,len(A)):
            if A[index]!=A[index-1]+1:
                return 0
        
        #else return 1
        return 1
