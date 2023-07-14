#Count the number of pairs (i,j) such that A[i] - A[j] = B and i ≠ j. 
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get a counter
        counter=0

        #get a hashmap
        hashmap={}

        #iterate for each element in the array
        for value in A:
            #check if the value in hashmap
            if value in hashmap:
                counter=counter+hashmap[value]
            hashmap[B+value]=hashmap.get(B+value,0)+1
            hashmap[value-B]=hashmap.get(value-B,0)+1
        
        #return the counter values
        return counter%1000000007
        
        
