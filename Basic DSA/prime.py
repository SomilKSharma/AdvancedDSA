#Return 1 if A is prime and return 0 if not. 
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #edge case
        if A<2:
            return 0

        #get the counter for factors
        count=0

        #a while loop to get the factors
        fact=1
        while fact*fact<=A:
            #check if A is divisible
            if A%fact==0:
                count=count+2
            fact=fact+1
        
        #check for prime
        if count>2:
            return 0
        return 1
