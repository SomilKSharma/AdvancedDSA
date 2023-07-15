#Write a program to find the factorial of the given number A using recursion.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #write a recursive code for factorial
        def factorial(value):
            #base case
            if not value:
                return 1
            #assume code works for n-1
            fact=factorial(value-1)
            #link n-1 with n
            return fact*value
        
        #return the answer
        return factorial(A)
