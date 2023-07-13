'''Given an array A. You have some integers given in the array B.
For the i-th number, find the frequency of B[i] in the array A and return a list containing all the frequencies.'''
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):

        #create a hashmap
        hashmap={}
        for value in A:
            hashmap[value]=hashmap.get(value,0)+1
        
        #get an answer array
        answer=[]

        #iterate for each value in array B
        for value in B:
            answer.append(hashmap.get(value,0))
        
        #return the answer
        return answer

