#sum of all possible submatrices.
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        #get a sums variable
        sums=0

        #iterate for all elements
        for row in range(len(A)):
            for col in range(len(A[0])):
                sums=sums+(
                    A[row][col]*(row+1)*(col+1)*
                                (len(A)-row)*(len(A[0])-col)
                )
        
        #return the answer
        return sums
