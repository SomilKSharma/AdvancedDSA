'''
Given a sorted array of distinct integers A and an integer B, find and return how many rectangles with distinct configurations can be created using elements of this array as length and breadth whose area is lesser than B.

(Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view)
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #get the start and the end pointer
        start,end=0,len(A)-1

        #get a counter variable
        counter=0

        #iterate for start and end
        while start<=end:
            #get the area
            area=A[start]*A[end]
            #check if lesser
            if area<B:
                counter=counter+(
                    end-start
                )*2+1
                #iterate further
                start=start+1
            else:
                end=end-1
        
        #return the value
        return counter%(1000000007)
