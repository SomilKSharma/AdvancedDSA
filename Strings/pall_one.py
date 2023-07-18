'''
Given a string A consisting of lowercase characters.

Check if characters of the given string can be rearranged to form a palindrome.

Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.
'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self,A):

        #create a hashmap out of the words of string A
        hashmap={}
        for value in A:
            hashmap[value]=hashmap.get(value,0)+1
        
        #get an odd freq counter
        odd=0

        #count letters with odd freq
        for value in hashmap.values():
            #count
            if value&1:
                odd+=1
        
        #return the answer
        if odd<=1:
            return 1
        else:
            return 0

