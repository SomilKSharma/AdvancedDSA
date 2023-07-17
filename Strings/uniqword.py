'''
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.

The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".
'''
class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):

        #get the word with minimum length
        mini=float('inf')
        base=''
        for value in A:
            #check the length
            if len(value)<mini:
                mini=len(value)
                base=value

        #get an answer strings
        answer=''
        for index,letter in enumerate(base):
            #check for letter in all words of A
            for word in A:
                #if letter not found return answer
                if word[index]!=letter:
                    return answer
            #add to answer
            answer=answer+letter

        #return the answer
        return answer