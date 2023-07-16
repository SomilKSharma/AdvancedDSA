'''
    On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
    Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 0-indexed.).
'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #write a recursive function to get the answer
        def k_value(row,col):
            #base case
            if not row:
                return 0
            #get the length of the previous row
            length=2**(row-1)
            #assum we have a solution for previous row
            value=k_value(row-1,col%length)
            #link previous row with present
            if col>=length:
                return 1-value
            else:
                return value
        
        #return the answer
        return k_value(A-1,B)
