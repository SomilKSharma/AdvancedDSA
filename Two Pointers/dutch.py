#Dutch flag
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):

        #get the three pointers
        red,white,blue=0,0,len(A)-1

        #iterate for the values of white less than blue
        while white<=blue:
            #check if it's red, and then swap
            if A[white]==0:
                A[white],A[red]=A[red],A[white]
                red=red+1
                white=white+1
            #swap for blue
            elif A[white]==2:
                A[white],A[blue]=A[blue],A[white]
                blue=blue-1
            else:
                white=white+1
        
        #return the array
        return A
