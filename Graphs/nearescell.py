'''
Given a matrix of integers A of size N x M consisting of 0 or 1.

For each cell of the matrix find the distance of nearest 1 in the matrix.

Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.

Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.

NOTE: There is atleast one 1 is present in the matrix.
'''

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):

        #create a queue
        queue=deque()

        #iterate for each value in A and put 1 in the queue
        for row in range(len(A)):
            for col in range(len(A[0])):
                #check
                if A[row][col]:
                    queue.append((row,col,0))
                    A[row][col]=float('inf')
        
        #iterate for each value in the queue
        while queue:
            #get the point and the distance
            x,y,d=queue.popleft()
            #iterate for all the nearby elements
            if x:
                #check for empty
                if not A[x-1][y]:
                    queue.append((x-1,y,d+1))
                    A[x-1][y]=d+1
            if y:
                #check
                if not A[x][y-1]:
                    queue.append((x,y-1,d+1))
                    A[x][y-1]=d+1
            if x<len(A)-1:
                #check
                if not A[x+1][y]:
                    queue.append((x+1,y,d+1))
                    A[x+1][y]=d+1
            if y<len(A[0])-1:
                #check
                if not A[x][y+1]:
                    queue.append((x,y+1,d+1))
                    A[x][y+1]=d+1
        
        #iterate for each value in the array A and make inf to 0
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col]==float('inf'):
                    A[row][col]=0
        return A

