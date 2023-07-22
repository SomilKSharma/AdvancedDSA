'''
We want to make a custom contacts finder applications as part of 
our college project. The application must perform two types of 
operations:

Type 1: Add name B[i] ,denoted by 0 in vector A where B[i] is a 
string in vector B denoting a contact name. This must store B[i] 
as a new contact in the application.

Type 2: Find partial for B[i] ,denoted by 1 in vector A where B[i] 
is a string in vector B denoting a partial name to search the 
application for. It must count the number of contacts starting 
with B[i].

You have been given sequential add and find operations. You need 
to perform each operation in order.

And return as an array of integers, answers for each query of 
type 2(denoted by 1 in A) .
'''

class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):

        #create a Tries data structure
        class Tries:
            #create a constructor
            def __init__(self):
                self.hashmap={}
                self.freq=1
        
        #create a root node for the Solution
        root=Tries()

        #get an answer array
        answer=[]

        #iterate for each value in the array
        for check_value in range(len(A)):
            #check if the array wants value input or value checking
            if A[check_value]:
                #get the word to be input in the Tries
                word=B[check_value]
                #get node reference
                node=root
                #found variable
                found=True
                #iterate for each letter in the word
                for letter in word:
                    #check for letter
                    if letter in node.hashmap:
                        #iterate to the node
                        node=node.hashmap[letter]
                    else:
                        found=False
                        break
                #check for found
                if found:
                    answer.append(node.freq)
                else:
                    answer.append(0)
            #else input the value in Tries
            else:
                #get the word to be input in the Tries
                word=B[check_value]
                #get node reference
                node=root
                #iterate for each letter in the word
                for letter in word:
                    #check for letter
                    if letter in node.hashmap:
                        #iterate to the node
                        node=node.hashmap[letter]
                        #increment the freq
                        node.freq+=1
                    else:
                        #create a new node
                        new=Tries()
                        node.hashmap[letter]=new
                        node=node.hashmap[letter]
            
        #return the answer array
        return answer

