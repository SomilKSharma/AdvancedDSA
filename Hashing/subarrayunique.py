#Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):

        #create a hashmap
        hashmap={}

        #iterate for the first B index
        for index in range(B):
            hashmap[A[index]]=hashmap.get(A[index],0)+1
        
        #get an answer array
        answer=[len(hashmap)]

        #iterate for the rest of the windows
        for index in range(len(A)-B):
            #remove the index element
            if hashmap[A[index]]==1:
                del hashmap[A[index]]
            else:
                hashmap[A[index]]=hashmap[A[index]]-1
            #add the index+B element
            hashmap[A[index+B]]=hashmap.get(A[index+B],0)+1
            #add to the answer array
            answer.append(len(hashmap))
        
        #return the answer
        return answer
        
