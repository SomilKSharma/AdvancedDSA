'''
Given a string A and a string B, find the window with minimum length in A, which will contain all the characters in B in linear time complexity.
Note that when the count of a character c in B is x, then the count of c in the minimum window in A should be at least x.

Note:

If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index and length )
'''
class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def minWindow(self, A, B):

        #create a hashmap of B
        hashmap={}
        for value in B:
            hashmap[value]=hashmap.get(value,0)+1
        
        #get a mini variable
        mini=float('inf')
        answer=''

        #variable to check if B is there
        b_counter=0
        length_b=len(B)

        #get two pointers to iterate
        start=end=0
        while end<len(A):
            #check if A[end] in hashmap
            if A[end] in hashmap:
                #decrement the value
                hashmap[A[end]]-=1
                #check if b_counter ought to be increased
                if hashmap[A[end]]>=0:
                    b_counter+=1
                #iterate for each start if string B is found
                while b_counter==length_b:
                    #get the minimum value
                    if mini>(end-start+1):
                        mini=end-start+1
                        answer=A[start:end+1]
                    #check if A[start] in hashmap
                    if A[start] in hashmap:
                        #increment the value
                        hashmap[A[start]]+=1
                        #check if b_counter ought to be increased
                        if hashmap[A[start]]>0:
                            b_counter-=1
                    #iterate start
                    start=start+1
            #iterate end
            end=end+1
        
        #return the mini
        return answer

