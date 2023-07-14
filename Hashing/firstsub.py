#Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        #array copy
        array=A.copy()

        #create a prefix sum
        for index in range(1,len(A)):
            A[index]=A[index-1]+A[index]
        
        #hashset
        hashmap={}

        #edge case
        if B in A:
            return array[:A.index(B)+1]

        #answer variable
        answer=[-1]
        mini=len(A)

        #iterate through all the values of A
        for index,value in enumerate(A):
            #check
            if value in hashmap:
                #check for mini
                if hashmap[value]<mini:
                    mini=hashmap[value]
                    answer=array[hashmap[value]:index+1]
            #check for the new value
            if B+value in hashmap:
                pass
            else:
                hashmap[B+value]=index+1
        
        #return the answer
        return answer
