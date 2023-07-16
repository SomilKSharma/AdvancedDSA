#Insertion sort with recursion
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        #write a recrusive code to sort the array
        def insertion_sort(index):
            #base case
            if index==len(A):
                return
            #iterate in a reverse manner from index to 0
            point=index
            while point>0:
                if A[point]<A[point-1]:
                    A[point],A[point-1]=A[point-1],A[point]
                point=point-1
            #call recursion for next index
            insertion_sort(index+1)
        
        #call the recursive code
        insertion_sort(0)

        #return the array
        return A


