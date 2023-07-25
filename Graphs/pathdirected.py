'''
Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2such that there is a edge directed from node

B[i][0] to node B[i][1].

Find whether a path exists from node 1 to node A.

Return 1 if path exists else return 0.

NOTE:

There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
'''

from collections import deque
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        #create a queue for breadth first search
        queue=deque()

        #create an adjacency list to store the directed relations
        adj=[
            []
            for _ in range(A+1)
        ]    

        #iterate for each value in the array B
        for start,end in B:
            #create the adj list
            adj[start].append(end)

        #created a visited array
        visited=[
            False
            for _ in range(A+1)
        ]
        
        #put the node 1 in the queue and the iterate
        queue.append(1)
        while queue:
            #pop the element
            node=queue.popleft()
            #update the value in the visited array
            visited[node]=True
            #iterate over the connections of the node
            for value in adj[node]:
                #if not visited add to the queue
                if not visited[value]:
                    queue.append(value)

        #check if A was visited or not
        if visited[A]:
            return 1
        else:
            return 0
