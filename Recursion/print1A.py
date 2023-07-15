#You are given an integer A, print A to 1 using using recursion.
class Solution:
    # @param A : integer
    def solve(self, A):

        #write a recursive function to print these values
        def atoone(value):
            #base case
            if not value:
                print()
                return
            #else case
            else:
                print(value,end=' ')
                atoone(value-1)
        
        #call the function
        atoone(A)
            
