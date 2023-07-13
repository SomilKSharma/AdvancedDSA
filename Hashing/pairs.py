'''Check if there exists a pair (i,j) such that Bi + Bj = A and i!=j.'''
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        #create a hashset
        hashset=set()

        #for every element add B-value to the hashset
        for value in B:
            #check if pair found
            if value in hashset:
                return 1
            #else add the value to the hashset
            hashset.add(A-value)
        
        #return 0 if none found
        return 0