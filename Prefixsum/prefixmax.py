#Prefix maximum
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        #get a prefix maximum array
        prefix=[
            0
            for _ in range(len(A))
        ]
        maxi=float('-inf')

        #iterate for other values in the array
        for index,value in enumerate(A):
            #get the maximum value upto the index
            if value>maxi:
                maxi=value
            #add the value to prefix maximum
            prefix[index]=maxi
        
        return prefix
            
                

