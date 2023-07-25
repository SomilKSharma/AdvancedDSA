'''
Given an directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast two nodes.
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

        #create an adjacency list
        adj=[
            []
            for _ in range(A+1)
        ]

        #get a degree array
        degree=[
            0
            for _ in range(A+1)
        ]

        #iterate for the directed values B
        for start,end in B:
            adj[start].append(end)
            degree[end]+=1
        
        #create a queue and put values in it
        queue=deque()
        for node in range(1,len(degree)):
            if not degree[node]:
                queue.append(node)

        #get the topological sort array
        topo=[]
        while queue:
            #get the 0 degree element
            node=queue.popleft()
            #add it to the asnwer
            topo.append(node)
            #iterate throught the adjacency list
            for value in adj[node]:
                #reduce the degree of the value
                degree[value]-=1
                #check if value should be put in the min_heap
                if not degree[value]:
                    queue.append(value)
        
        #return the answer
        return int(len(topo)!=A)
