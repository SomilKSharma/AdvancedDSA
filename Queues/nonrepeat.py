'''
Given a string A denoting a stream of lowercase alphabets, 
you have to make a new string B. 
B is formed such that we have to find the first non-repeating 
character each time a character is inserted to the stream and 
append it at the end to B. If no non-repeating character is 
found, append '#' at the end of B.
'''
from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        #create a queue to store non repeating characters
        queue=deque()
        #use a hashmap to store the freq of a character
        hashmap={}
        #get an answer string to store the answer
        answer=''

        #iterate for each value in A
        for value in A:
            #check for value in hashmap
            if value in hashmap:
                #increase the value
                hashmap[value]+=1
            else:
                #else the value isn't in the hashmap
                queue.append(value)
                hashmap[value]=1
            #add value to the answer
            while queue and hashmap[queue[0]]>1:
                    queue.popleft()
            #check if queue has a value
            if not queue:
                answer=answer+'#'
            else:
                answer=answer+queue[0]
        
        #return the value
        return answer




