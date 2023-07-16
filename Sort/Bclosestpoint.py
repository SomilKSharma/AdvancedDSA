#We have a list A of points (x, y) on the plane. Find the B closest points to the origin (0, 0).
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):

        #modified sort function
        def sorting(point):
            #return the distance
            return point[0]**2+point[1]**2
        
        #sort using the modified function
        A.sort(key=sorting)

        #return the first B
        return A[:B]
