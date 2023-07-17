'''
You are given a function isalpha() consisting of a character array A.

Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.
'''
class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):

        #create a string out of the array
        string=''.join(A)
        #check if alpha and numeric only
        if string.isalnum():
            return 1
        else:
            return 0
            
        
