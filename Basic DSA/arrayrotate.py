#you have to return the same array after rotating it B times towards the right.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        #get the rotation value of B
        B=B%len(A)

        #last B elements
        rev=[]

        #remove and rotate
        for _ in range(B):
            rev.append(A.pop())

        #return the value
        return rev[::-1]+A