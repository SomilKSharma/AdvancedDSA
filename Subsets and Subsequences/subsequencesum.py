#You have to find that there is any subsequence exists or not whose sum is equal to B.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #run a while loop for each possibility of subsequence
        number=0
        while number<(2**len(A)):
            #use bit manipulation to get the answer for each subsequence
            sums=0
            for index in range(len(A)):
                #check if present number has 1 or 0 at this index
                if (number>>index)&1:
                    sums=sums+A[index]
            #check if sums is equal to B
            if sums==B:
                return 1
            #increment the number
            number=number+1
        
        #else no answer found
        return 0
