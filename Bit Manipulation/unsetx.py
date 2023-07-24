#Unset x bits from right
class Solution:
    # @param A : long
    # @param B : integer
     # @return an long
    def solve(self, A, B):

        #get a position
        pos=0

        #run a loop
        while pos<B:
            #change A
            if (A>>pos)&1:
                A=A^(1<<pos)
            pos=pos+1

        #return the value
        return A
