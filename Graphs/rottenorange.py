'''
Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:

The value 0 representing an empty cell.

The value 1 representing a fresh orange.

The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.
'''

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        #create a queue out of the deque
        queue=deque()

        #iterate for all values in the array A and put the rotten in queue
        for row in range(len(A)):
            for col in range(len(A[0])):
                #check for rotten and add them to the queue
                if A[row][col]==2:
                    queue.append((row,col,0))
        
        #iterate in the queue till it is not empty
        while queue:
            #pop the leftmost element
            row,col,time=queue.popleft()
            #check for possible oranges to rott
            if row-1>=0:
                #check
                if A[row-1][col]==1:
                    #add it tot the queue
                    queue.append((row-1,col,time+1))
                    A[row-1][col]=2
            if col-1>=0:
                #check
                if A[row][col-1]==1:
                    #add
                    queue.append((row,col-1,time+1))
                    A[row][col-1]=2
            if row+1<len(A):
                #check
                if A[row+1][col]==1:
                    #add
                    queue.append((row+1,col,time+1))
                    A[row+1][col]=2
            if col+1<len(A[0]):
                #check
                if A[row][col+1]==1:
                    #add
                    queue.append((row,col+1,time+1))
                    A[row][col+1]=2
        
        #check if any orange is left untouched
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col]==1:
                    return -1
        
        #else return the last time
        return time