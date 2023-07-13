#number of subarrays in A with a sum less than B.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get the counter
        counter=0

        #iterate for all elements in the array
        for index_1 in range(len(A)):
            sums=0
            for index_2 in range(index_1,len(A)):
                #sum the value in the index
                sums=sums+A[index_2]
                #check for less than B array
                if (sums<B):
                    counter+=1
                else:
                    break
        
        return counter
