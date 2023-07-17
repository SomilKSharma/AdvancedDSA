'''
You are given a string A of size N.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
'''
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        #convert the string to an array
        array=list(A)

        #reverse the array
        array=array[::-1]

        #add the array to a string and return
        return ' '.join(array)
    
