'''
Given a Tree of A nodes having A-1 edges. Each node is numbered from 1 to A where 1 is the root of the tree.

You are given Q queries. In each query, you will be given two integers L and X. Find the value of such node which lies at level L mod (MaxDepth + 1) and has value greater than or equal to X.

Answer to the query is the smallest possible value or -1, if all the values at the required level are smaller than X.

NOTE:

Level and Depth of the root is considered as 0.
It is guaranteed that each edge will be connecting exactly two different nodes of the tree.
Please read the input format for more clarification.
'''

from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F):

        #create an adjacency matrix
        adj=[
            []
            for _ in range(A+1)
        ]
        for index in range(len(B)):
            adj[B[index]].append(C[index])
            adj[C[index]].append(B[index])
        
        #create a visited array
        visited=[
            False
            for _ in range(A+1)
        ]

        #create a level array
        levels=[
            []
            for _ in range(A)
        ]

        #do a breadth first search using queue
        queue=deque()
        queue.append((1,0))
        while queue:
            #pop the value from the queue
            node,level=queue.popleft()
            #add value to the level array
            levels[level].append(D[node-1])
            levels[level].sort()
            #add to the visited array
            visited[node]=True

            #iterate for the adjacency list
            for value in adj[node]:
                #check if already visited
                if not visited[value]:
                    queue.append((value,level+1))
        
        array=[]
        for index in range(len(E)):
            find=E[index]%(level+1)
            number=F[index]
            answer=float('inf')
            
            left = 0
            right = len(levels[find]) - 1
            while left <= right:
                mid = (left + right) // 2
                if levels[find][mid] >= number:
                    answer = min(answer, levels[find][mid])
                    right = mid - 1
                else:
                    left = mid + 1

            if answer != float('inf'):
                array.append(answer)
            else:
                array.append(-1)
        
        return array
