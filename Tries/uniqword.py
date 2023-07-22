'''
Given a list of N words, find the shortest unique prefix to represent each word in the list.
NOTE: Assume that no word is the prefix of another. In other words, the representation is always possible
'''

class Solution:
	# @param A : list of strings
	# @return a list of strings
	def prefix(self, A):

        #create a Tries dta structure class
        class Tries:
            #create the constructor
            def __init__(self):
                self.hashmap={}
                self.is_unique=True
        
        #create the root of the Tries
        root=Tries()
        root.is_unique=False

        #iterate for each word in the array A
        for word in A:
            #get the reference for the root node
            node=root
            #iterate for each letter in the word
            for letter in word:
                #check if letter is in the hashmap
                if letter in node.hashmap:
                    #the letter is no more unique
                    node=node.hashmap[letter]
                    node.is_unique=False
                else:
                    new=Tries()
                    node.hashmap[letter]=new
                    node=node.hashmap[letter]
        
        #get an answer array
        answer=[]

        #iterate for each word to find the unique words
        for word in A:
            #get the reference for the root node
            node=root
            #get a string variable to store answer for this string
            string=''
            #iterate for each letter in the word
            for letter in word:
                #check for uniqueness
                node=node.hashmap[letter]
                #add letter to the string
                string=string+letter
                #check if unique
                if node.is_unique:
                    break
            #add the string to the answer
            answer.append(string)
        
        #return the answer
        return answer
