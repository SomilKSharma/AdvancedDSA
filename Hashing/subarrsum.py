#Find the total number of subarrays having sum equals to B.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #create the prefix sum out of the array
        for index in range(1,len(A)):
            A[index]=A[index-1]+A[index]
        
        #create a hashmap and a counter
        hashmap={}
        counter=0

        #coun occurence from base 0
        A=[0]+A

        #iterate for every value in A
        for value in A:
            #check if value in hashmap
            if value in hashmap:
                counter=counter+hashmap[value]
            #add present counter
            hashmap[B+value]=hashmap.get(B+value,0)+1
        
        #return the counter
        return counter
        


