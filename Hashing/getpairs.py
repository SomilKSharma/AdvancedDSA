#find if there exists a pair of elements in the array whose difference is B.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get a hashset to find the pair
        hashset=set()

        #iterate over all the elements of the array A
        for value in A:
            #check if element in hashset:
            if value in hashset:
                return 1
            #add the differences in the hashset
            hashset.add(B+value)
            hashset.add(value-B)
        
        #if not found
        return 0

        
