'''
Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

NOTE: Rows are numbered from top to bottom, and columns are from left to right.
'''
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):

        #get the rows and columns
        rows=len(A)
        cols=len(A[0])

        #get a start and end in the binary search
        start,end=0,rows*cols-1
        while start<=end:
            #get the mid value
            mid=(start+end)//2
            #get the row and col
            row,col=mid//cols,mid%cols
            #compare the value
            if A[row][col]==B:
                return 1
            elif A[row][col]<B:
                start=mid+1
            else:
                end=mid-1
        
        #not found
        return 0
