# find a special pair such that the distance between that pair is minimum.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #get the dummy minimum
        mini=float('inf')

        #store value in a hashmap
        hashmap={}

        #Iterate through the array
        for index,value in enumerate(A):
            #check if value in hashmap
            if value in hashmap:
                mini=min(
                    index-hashmap[value],
                    mini
                )
            #add to teh hashmap
            hashmap[value]=index
        
        #return the minimum
        return mini if mini!=float('inf') else -1
