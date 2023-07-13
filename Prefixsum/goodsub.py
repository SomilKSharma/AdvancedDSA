#Good Subarrays
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
            length=0
            for index_2 in range(index_1,len(A)):
                #sum the value in the index
                sums=sums+A[index_2]
                length=length+1
                #check for good array
                if (
                    (length&1 and sums>B)
                    or
                    (not length&1 and sums<B)
                ):
                    counter+=1
        
        return counter
