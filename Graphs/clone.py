'''
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

Note: The test cases are generated in the following format (use the following format to use See Expected Output option):
First integer N is the number of nodes.
Then, N intgers follow denoting the label (or hash) of the N nodes.
Then, N2 integers following denoting the adjacency matrix of a graph, where Adj[i][j] = 1 denotes presence of an undirected edge between the ith and jth node, O otherwise.
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        #create a dummy node
        dummy=UndirectedGraphNode(node.label)

        #get a visited hashmap
        hashmap={}
        hashmap[node]=dummy

        #create a queue for bfs
        queue=deque()
        queue.append(node)

        #iterate till the queue exists
        while queue:
            #pop the left most element
            element=queue.popleft()
            #iterate for each value in the neighbour
            for value in element.neighbors:
                #check if the element is in the hashmap or not
                if value in hashmap:
                    pass
                #else add it and create a clone node
                else:
                    dummy=UndirectedGraphNode(value.label)
                    hashmap[value]=dummy
                    queue.append(value)
                hashmap[element].neighbors.append(hashmap[value])
                
        
        #return the head of the clone graph
        return hashmap[node]
        
