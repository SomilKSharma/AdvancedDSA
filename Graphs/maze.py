'''
Given a matrix of integers A of size N x M describing a maze. The maze consists of empty locations and walls.

1 represents a wall in a matrix and 0 represents an empty location in a wall.

There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall (maze boundary is also considered as a wall). When the ball stops, it could choose the next direction.

Given two array of integers of size B and C of size 2 denoting the starting and destination position of the ball.
'''

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        
        #create a hashset
        hashset=set()

        #queue creation for bfs
        queue=deque()
        queue.append((B[0],B[1]))

        
        ###########################################
        #put values for first element
        x,y=queue.popleft()
        #check for left
        if y:
            #no walls
            if A[x][y-1]!=1:
                #check if hashset
                if (x,y-1,'fromright') not in hashset:
                    queue.append((x,y-1,1,'fromright'))
                    hashset.add((x,y-1,'fromright'))
        #check for right
        if y<len(A[0])-1:
            #no walls
            if A[x][y+1]!=1:
                #check if hashset
                if (x,y+1,'fromleft') not in hashset:
                    queue.append((x,y+1,1,'fromleft'))
                    hashset.add((x,y+1,'fromleft'))
        #check for up
        if x:
            #no walls
            if A[x-1][y]!=1:
                #check if hashset
                if (x-1,y,'frombottom') not in hashset:
                    queue.append((x-1,y,1,'frombottom'))
                    hashset.add((x-1,y,'frombottom'))
        #check for bottom
        if x<len(A)-1:
            #now walls
            if A[x+1][y]!=1:
                #check if hashset
                if (x+1,y,'fromtop') not in hashset:
                    queue.append((x+1,y,1,'fromtop'))
                    hashset.add((x+1,y,'fromtop'))

        
        ###########################################
        while queue:
            #pop the element and direction
            x,y,dist,direct=queue.popleft()
            #check if there is a wall ahead
            if (
                #check for left
                (direct=='fromright' and (not y or A[x][y-1]==1)) or
                #check for right
                (direct=='fromleft' and (y==len(A[0])-1 or A[x][y+1]==1)) or  
                #check for top
                (direct=='frombottom' and (not x or A[x-1][y]==1)) or  
                #check for bottom
                (direct=='fromtop' and (x==len(A)-1 or A[x+1][y]==1))
            ):
                #check if value is the answer
                if [x,y]==C:
                    return dist
                #else we can got to any of the four direction
                #check for left
                if y:
                    #no walls
                    if A[x][y-1]!=1:
                        #check if hashset
                        if (x,y-1,'fromright') not in hashset:
                            queue.append((x,y-1,dist+1,'fromright'))
                            hashset.add((x,y-1,'fromright'))
                #check for right
                if y<len(A[0])-1:
                    #no walls
                    if A[x][y+1]!=1:
                        #check if hashset
                        if (x,y+1,'fromleft') not in hashset:
                            queue.append((x,y+1,dist+1,'fromleft'))
                            hashset.add((x,y+1,'fromleft'))
                #check for up
                if x:
                    #no walls
                    if A[x-1][y]!=1:
                        #check if hashset
                        if (x-1,y,'frombottom') not in hashset:
                            queue.append((x-1,y,dist+1,'frombottom'))
                            hashset.add((x-1,y,'frombottom'))
                #check for bottom
                if x<len(A)-1:
                    #now walls
                    if A[x+1][y]!=1:
                        #check if hashset
                        if (x+1,y,'fromtop') not in hashset:
                            queue.append((x+1,y,dist+1,'fromtop'))
                            hashset.add((x+1,y,'fromtop'))
            #else keep moving in the same direction
            else:
                #if direction is fromright
                if direct=='fromright':
                    #check for left
                    if y:
                        #no walls
                        if A[x][y-1]!=1:
                            #check if hashset
                            if (x,y-1,'fromright') not in hashset:
                                queue.append((x,y-1,dist+1,'fromright'))
                                hashset.add((x,y-1,'fromright'))
                #if direction fromleft
                if direct=='fromleft':
                    #check for right
                    if y<len(A[0])-1:
                        #no walls
                        if A[x][y+1]!=1:
                            #check if hashset
                            if (x,y+1,'fromleft') not in hashset:
                                queue.append((x,y+1,dist+1,'fromleft'))
                                hashset.add((x,y+1,'fromleft'))
                #if direction frombottom
                if direct=='frombottom':
                    #check for up
                    if x:
                        #no walls
                        if A[x-1][y]!=1:
                            #check if hashset
                            if (x-1,y,'frombottom') not in hashset:
                                queue.append((x-1,y,dist+1,'frombottom'))
                                hashset.add((x-1,y,'frombottom'))
                #if direction fromtop
                if direct=='fromtop':
                    #check for bottom
                    if x<len(A)-1:
                        #now walls
                        if A[x+1][y]!=1:
                            #check if hashset
                            if (x+1,y,'fromtop') not in hashset:
                                queue.append((x+1,y,dist+1,'fromtop'))
                                hashset.add((x+1,y,'fromtop'))
        
        #not able to reach
        return -1
                


                




