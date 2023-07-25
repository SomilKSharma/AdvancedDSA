'''
Given an directed acyclic graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

Return the topological ordering of the graph and if it doesn't exist then return an empty array.

If there is a solution return the correct ordering. If there are multiple solutions print the lexographically smallest one.

Ordering (a, b, c) is said to be lexographically smaller than ordering (e, f, g) if a < e or if(a==e) then b < f and so on.

NOTE:

There are no self-loops in the graph.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
'''

from heapq import heappush,heappop
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
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
        
        #create a min heap and put values in it
        min_heap=[]
        for node in range(1,len(degree)):
            if not degree[node]:
                heappush(min_heap,(0,node))

        #get the topological sort array
        topo=[]
        while min_heap:
            #get the 0 degree element
            _,node=heappop(min_heap)
            #add it to the asnwer
            topo.append(node)
            #iterate throught the adjacency list
            for value in adj[node]:
                #reduce the degree of the value
                degree[value]-=1
                #check if value should be put in the min_heap
                if not degree[value]:
                    heappush(min_heap,(0,value))
        
        #return the topological sorted graph
        return topo
