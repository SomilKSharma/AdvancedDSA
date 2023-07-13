#Find that integer that occurs once.
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):

        #get a product variable
        product=0

        #do xor of all variables
        for value in A:
            product=product^value
        
        #return the product variable
        return product
