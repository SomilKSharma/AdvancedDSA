#Find the length of the longest subarray in the array which sums to zero.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #create the prefix sums
        for index in range(1,len(A)):
            A[index]=A[index-1]+A[index]

        #check for zero in the array
        maxi=0
        for index,value in enumerate(A):
            if not value:
                maxi=index+1

        #get a hashmap to store index
        hashmap={}
        for index,value in enumerate(A):
            #check if value in hashmap
            if value in hashmap:
                maxi=max(
                    maxi,
                    index-hashmap[value]
                )
            else:
                hashmap[value]=index
        
        #return
        return maxi
