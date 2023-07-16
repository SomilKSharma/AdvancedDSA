#Implement pow(A, B) % C.
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):

        #edge case
        if not A:
            return 0
        
        #write a recursive code to get the answer
        def power_function(power):
            #check for base case
            if not power:
                return 1
            #assume the power function works for lower values
            sol=power_function(power//2)
            #link lower values with present value
            if power&1:
                return ((sol*sol)%C*A)%C
            else:
                return (sol*sol)%C
        
        #return the answer
        return power_function(B)
        