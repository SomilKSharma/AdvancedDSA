'''
You are given a function to_upper() consisting of a character array A.

Convert each character of A into Uppercase character if it exists. If the Uppercase of a character does not exist, it remains unmodified.
The lowercase letters from a to z is converted to uppercase letters from A to Z respectively.

Return the uppercase version of the given character array.
'''
class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):

        #get an answer array
        answer=[]

        #iterate for each value in A
        for value in A:
            answer.append(value.upper())
        
        #return the answer array
        return answer
