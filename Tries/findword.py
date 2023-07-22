'''
Given an array of words A (dictionary) and another array B 
(which contain some words).

You have to return the binary array (of length |B|) as the answer 
where 1 denotes that the word is present in the dictionary and 0 
denotes it is not present.

Formally, for each word in B, you need to return 1 if it is present 
in Dictionary and 0 if not.

Such problems can be seen in real life when we work on any online 
editor (like Google Documnet), if the word is not valid it is 
underlined by a red line.

NOTE: Try to do this in O(n) time complexity.
'''

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):

        #create a Tries data structure
        class Tries:
            #write the constructor for the class
            def __init__(self):
                self.hashmap={}
                self.is_end=False
        
        #create the root node for accessing the Tries
        root=Tries()

        #fill values in Tries for each item in the list A
        for word in A:
            #get reference to the original root
            node=root
            #iterate for each letter in the word
            for letter in word:
                #check if letter is in the hashmap
                if letter in node.hashmap:
                    pass
                else:
                    #create the new node
                    new=Tries()
                    node.hashmap[letter]=new
                #iterate to the new node
                node=node.hashmap[letter]
            #since the letter is the end of the word, change is end value
            node.is_end=True
        
        #get an answer array to store the value
        answer=[]

        #iterate for each word to get the value if present or not
        for word in B:
            #get reference to the original root
            node=root
            #an is found variable to identify found or not
            found=True
            #iterate for each letter in the word
            for letter in word:
                #check if letter is in the word
                if letter in node.hashmap:
                    #iterate to that letter
                    node=node.hashmap[letter]
                else:
                    found=False
                    break
            #check for found and is end variables
            if found and node.is_end:
                answer.append(1)
            else:
                answer.append(0)
        
        #return the answer arrray
        return answer


