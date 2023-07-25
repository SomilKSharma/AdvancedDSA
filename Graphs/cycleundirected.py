'''
Given an undirected graph having A nodes labelled from 1 to A with M edges given in a form of matrix B of size M x 2 where (B[i][0], B[i][1]) represents two nodes B[i][0] and B[i][1] connected by an edge.

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast three nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
'''

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        #create an adjacency list
        adj=[
            []
            for _ in range(A+1)
        ]
        for start,end in B:
            adj[start].append(end)
            adj[end].append(start)

        #created a visited array
        visited=[
            False
            for _ in range(A+1)
        ]

        #write the depth fisrt search code
        def dfs(node):
            #check if already visited
            if visited[node]:
                return
            #else iterate for the adj list
            visited[node]=True
            #iterate for the adj list
            for value in adj[node]:
                dfs(value)
        
        #create a component counter
        component=0

        #iterate for all the values in the visited array
        for index in range(1,len(visited)):
            #check if not visited
            if not visited[index]:
                dfs(index)
                component+=1
        
        #check for a cycle
        if len(B)>A-component:
            return 1
        else:
            return 0