'''
You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.

You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.
'''
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        #get an answer string
        answer=''

        #for every letter in the string, toggle the case
        for letter in A:
            #check for case
            if letter.islower():
                answer=answer+letter.upper()
            else:
                answer=answer+letter.lower()
        
        #return the value
        return answer

