#Count the number of elements that have at least 1 elements greater than itself.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #get the maximum
        maxi=max(A)

        #get a counter
        counter=0

        #iterate over the array
        for value in A:
            #check
            if value<maxi:
                counter+=1

        #return the value
        return counter
