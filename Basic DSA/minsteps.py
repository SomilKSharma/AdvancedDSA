#You have to make all elements unique. To do so, in one step you can increase any number by one.
#Find the minimum number of steps.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #sort the array
        A.sort()

        #get a counter
        counter=0

        #iterate for all values of A
        for index in range(1,len(A)):
            #check for left element
            if A[index-1]>=A[index]:
                counter=counter+(A[index-1]-A[index]+1)
                A[index]=A[index-1]+1
        
        #return the values
        return counter
