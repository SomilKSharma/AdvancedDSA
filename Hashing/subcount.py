#Find the count of the subarrays in the array which sums to zero.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #create the prefix sum of A
        for index in range(1,len(A)):
            A[index]=A[index-1]+A[index]
        
        #get a counter
        counter=0

        #count sub array sum zero with base 0 index
        for value in A:
            if not value:
                counter+=1
        
        #create a hashmap
        hashmap={}

        #count other sums subarrays as zero
        for value in A:
            #check for value in hashmap
            if value in hashmap:
                counter=counter+hashmap[value]
            #add value to the hashmap
            hashmap[value]=hashmap.get(value,0)+1
        
        #return the counter
        return counter
