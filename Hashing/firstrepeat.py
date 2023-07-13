#Given an integer array A of size N, find the first repeating element in it.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #create a hashset
        hashset=set()

        #get an answer variable
        answer=-1

        #iterate in the array in a reverse manner
        for value in reversed(A):
            if value in hashset:
                answer=value
            hashset.add(value)
        
        #return the first repeating character
        return answer
