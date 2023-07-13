# Return the count of elements with frequncy 1 in the given array.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #create a hashmap out of A
        hashmap={}
        for value in A:
            hashmap[value]=hashmap.get(value,0)+1
        
        #get a counter
        counter=0

        #iterate over the hashmap and get the count
        for value in hashmap.values():
            if value==1:
                counter+=1
        
        #return teh value
        return counter
