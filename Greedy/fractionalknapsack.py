'''
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.
Also given an integer C which represents knapsack capacity.
Find out the maximum total value that we can fit in the knapsack. If the maximum total value is ans, then return ⌊ans × 100⌋ , i.e., floor of (ans × 100).

NOTE:
You can break an item for maximizing the total value of the knapsack
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        #create a novel array that combines both A and B
        array=[
            (A[index]/B[index],A[index],B[index])
            for index in range(len(A))
        ]
        
        #sort the array in terms of value per weight
        def sorting(value):
            #return the value per weights
            return value[0]
        
        #sort the array
        array.sort(key=sorting,reverse=True)
        
        #get a variable to note the value of the array
        answer=0
        
        #iterate for each value in the array
        for per,value,weight in array:
            #check for C
            if C<weight:
                #add the value
                answer=answer+per*C
                break
            else:
                #add the value
                answer=answer+value
                C=C-weight
        
        #return the answer
        return int(answer*100)

