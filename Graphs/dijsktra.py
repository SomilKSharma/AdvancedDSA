'''
Given a weighted undirected graph having A nodes and M weighted edges, and a source node C.

You have to find an integer array D of size A such that:

D[i]: Shortest distance from the C node to node i.
If node i is not reachable from C then -1.
Note:

There are no self-loops in the graph.
There are no multiple edges between two pairs of vertices.
The graph may or may not be connected.
Nodes are numbered from 0 to A-1.
Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.
'''

from heapq import heappush,heappop
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):

        #create an adjacency list
        adj=[
            []
            for _ in range(A)
        ]
        for start,end,weight in B:
            adj[start].append((end,weight))
            adj[end].append((start,weight))
        
        #create a distance array
        distance=[
            float('inf')
            for _ in range(A)
        ]
        distance[C]=0

        #get a min heap
        min_heap=[]
        heappush(min_heap,(0,C))

        #iterate till the min heap exists
        while min_heap:
            #get the distance and the node
            d,node=heappop(min_heap)
            #iterate for the present and put the values in the queue
            for value,dist in adj[node]:
                #get the total distance to the value
                total=d+dist
                #check
                if total<distance[value]:
                    #update the value
                    distance[value]=total
                    #add to the heap
                    heappush(min_heap,(total,value))
        
        #return the min value to the node
        for index in range(len(distance)):
            #check for infinity
            if distance[index]==float('inf'):
                distance[index]=-1
        
        #return the distance array
        return distance


