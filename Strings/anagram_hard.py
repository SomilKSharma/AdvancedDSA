'''
Given an array A of N strings, return all groups of strings that are anagrams.

Represent a group by a list of integers representing the index(1-based) in the original list. Look at the sample case for clarification.

NOTE: Anagram is a word, phrase, or name formed by rearranging the letters, such as 'spar', formed from 'rasp'.


'''
class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):

        #change tuple A to an array
        A=list(A)

        #alphabeteically sort all words in the list
        for index,value in enumerate(A):
            A[index]=''.join(sorted(value))
        
        #get a hashmap
        hashmap={}
        for index,value in enumerate(A):
            #hcek if value in hashmap
            if value in hashmap:
                hashmap[value].append(index+1)
            else:
                hashmap[value]=[index+1]
        
        #get the answer
        answer=[]
        for array in hashmap.values():
            answer.append(array)
        
        #return the answer
        return answer

