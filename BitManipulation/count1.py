#returns the number of 1 bits present in its binary representation.
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):

        #get a counter
        counter=0

        #iterate till A exists
        while A:
            #get if 0th element is 1 or not
            value=A&1
            #add to the counter
            counter=counter+value
            #right shift A
            A=A>>1
        
        #return the value
        return counter
