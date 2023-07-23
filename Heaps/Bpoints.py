'''
We have a list A of points (x, y) on the plane. Find the B closest points to the origin (0, 0).
Here, the distance between two points on a plane is the Euclidean distance.
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.)

NOTE: Euclidean distance between two points P1(x1, y1) and P2(x2, y2) is sqrt( (x1-x2)2 + (y1-y2)2 ).
'''

from heapq import heappop, heappush
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):

        #create a min heap
        min_heap=[]

        #iterate for all the values and put them in the heap
        for x,y in A:
            #add each value to the array
            heappush(min_heap,(x**2+y**2,x,y))
        
        #create an answer array
        answer=[]

        #iterate for the first B value
        for _ in range(B):
            #points for the array
            _,x,y=heappop(min_heap)
            answer.append((x,y))

        #return the B values
        return answer
