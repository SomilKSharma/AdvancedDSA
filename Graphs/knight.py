'''
Given any source point, (C, D) and destination point, (E, F) on a chess board of size A x B, we need to find whether Knight can move to the destination or not.


The above figure details the movements for a knight ( 8 possibilities ).

If yes, then what would be the minimum number of steps for the knight to move to the said point. If knight can not move from the source point to the destination point, then return -1.

NOTE: A knight cannot go out of the board.
'''

from collections import deque
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):

        #create a matrix of zeroes
        matrix=[
            [0]*(B+1)
            for _ in range(A+1)
        ]

        #get a function to check validity of a node
        def valid(x,y):
            #check validity
            if x<=0 or x>A:
                return False
            if y<=0 or y>B:
                return False
            if matrix[x][y]:
                return False
            return True
        
        #add the start element and iterate
        queue=deque()
        queue.append((C,D,0))
        matrix[C][D]=1

        while queue:
            #pop the value
            x,y,d=queue.popleft()

            if (x,y)==(E,F):
                return d

            #check for all sides
            if valid(x-2,y-1):
                queue.append((x-2,y-1,d+1))
                matrix[x-2][y-1]=1
            if valid(x-1,y-2):
                queue.append((x-1,y-2,d+1))
                matrix[x-1][y-2]=1
            if valid(x+2,y-1):
                queue.append((x+2,y-1,d+1))
                matrix[x+2][y-1]=1
            if valid(x+1,y-2):
                queue.append((x+1,y-2,d+1))
                matrix[x+1][y-2]=1
            if valid(x+2,y+1):
                queue.append((x+2,y+1,d+1))
                matrix[x+2][y+1]=1
            if valid(x+1,y+2):
                queue.append((x+1,y+2,d+1))
                matrix[x+1][y+2]=1
            if valid(x-2,y+1):
                queue.append((x-2,y+1,d+1))
                matrix[x-2][y+1]=1
            if valid(x-1,y+2):
                queue.append((x-1,y+2,d+1))
                matrix[x-1][y+2]=1
        
        return -1
