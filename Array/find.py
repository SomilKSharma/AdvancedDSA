'''Given an matrix A of size NxN, which is row-wise and column-wise sorted. Find if the number B exists in the matrix.'''
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get the starting point in the bottom left corner
        row=len(A)-1
        col=0

        #iterate in the for loop
        while row>0 and col<len(A[0]):
            #get value at the index
            value=A[row][col]
            #check for value
            if value==B:
                return 1
            elif value<B:
                col=col+1
            else:
                row=row-1
        
        return 0

