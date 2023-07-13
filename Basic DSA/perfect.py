#Perfect number is a positive integer which is equal to the sum of its proper positive divisors.
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #get the sum variable
        sums=0

        #iterate to get the sum of the proper divisors
        for value in range(1,A):
            #check for divisiblity
            if not A%value:
                sums=sums+value
        
        return int(sums==A)
