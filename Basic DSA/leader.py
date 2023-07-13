#An element is a leader if it is strictly greater than all the elements to its right side.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        #get the maximum upto an index
        maxi=float('-inf')

        #get an answer array
        array=[]

        #get the value of the leaders
        for value in reversed(A):
            #compare with maximum up untill now
            if value>maxi:
                array.append(value)
                maxi=value
        
        #return the value
        return array
