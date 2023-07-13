#Reverse the bits of an 32 bit unsigned integer A. 
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):

        #get an answer variable
        answer=0

        #while loop to iterate for each position
        pos=0
        while pos<32:
            #get the value at the index
            value=(A>>pos)&1
            #add the value at the 31-index position in the answer
            answer=answer|(value<<(31-pos))
            #increment the pos variable
            pos=pos+1
        
        #return the answer
        return answer
