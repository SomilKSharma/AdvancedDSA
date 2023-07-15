#Find and return the number of unique points in the array.
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        #create an array of tuple of points
        A=list(map(tuple,A))

        #create a set of tuple of points
        A=set(A)

        #return the len of the set
        return len(A)
