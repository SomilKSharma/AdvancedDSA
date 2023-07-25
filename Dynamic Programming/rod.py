'''
Given a rod of length N units and an array A of size N denotes prices that contains prices of all pieces of size 1 to N.
Find and return the maximum value that can be obtained by cutting up the rod and selling the pieces.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #create a dynamic array to get the answer
        dynamic=[
            -1
            for _ in range(len(A)+1)
        ]

        #write a recursive function to get the answer
        def max_cutting(length):
            #write the base case
            if not length:
                return 0
            #check if answer is in the dynamic array
            if dynamic[length]!=-1:
                return dynamic[length]
            #else we would calculate the answer
            else:
                #create a for loop to get the maximum
                maxi=A[length-1]
                for index in range(1,length):
                    #get the answer
                    maxi=max(
                        maxi,
                        max_cutting(index)+max_cutting(length-index)
                    )
                #put the value in the dynamic array
                dynamic[length]=maxi
            #return the answer
            return dynamic[length]
        
        #return the answer
        return max_cutting(len(A))
