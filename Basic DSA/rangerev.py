#Reverse in a range
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):

        #get a while loop with two pointers and reverse the elements
        while B<C:
            #swap the value
            A[B],A[C]=A[C],A[B]
            B=B+1
            C=C-1
        
        #return A
        return A
