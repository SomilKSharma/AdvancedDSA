'''
You are given a function to_lower() which takes a character array A as an argument.

Convert each character of A into lowercase characters if it exists. If the lowercase of a character does not exist, it remains unmodified.
The uppercase letters from A to Z are converted to lowercase letters from a to z respectively.

Return the lowercase version of the given character array.
'''
class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):

        #get an answer array
        answer=[]

        #iterate for each value in A
        for value in A:
            answer.append(value.lower())
        
        #return the answer array
        return answer
