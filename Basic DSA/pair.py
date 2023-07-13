#You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j.
class Solution:
    # @param A : string
     # @return an long
    def solve(self, A):

        #get an a counter
        a=0

        #get pair counter
        pair=0

        #iterate for all values in the array A
        for value in A:
            #check if equal to A
            if value=='A':
                a=a+1
            elif value=='G':
                pair=pair+a
        
        #return the pair counter
        return pair
