'''
You are given N towns (1 to N). All towns are connected via unique directed path as mentioned in the input.

Given 2 towns find whether you can reach the first town from the second without repeating any edge.

B C : query to find whether B is reachable from C.

Input contains an integer array A of size N and 2 integers B and C ( 1 <= B, C <= N ).

There exist a directed edge from A[i] to i+1 for every 1 <= i < N. Also, it's guaranteed that A[i] <= i for every 1 <= i < N.

NOTE: Array A is 0-indexed. A[0] = 1 which you can ignore as it doesn't represent any edge.
'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def solve(self, A, B, C):

        #create the adjacency list
        adj=[
            []
            for _ in range(len(A)+1)
        ]

        #iterate for each element in the array A
        for index in range(1,len(A)):
            adj[A[index]].append(index+1)
        
        #create a visited list
        visited=[
            False
            for _ in range(len(A)+1)
        ]

        #create the depth first search recursive function
        def dfs(element):
            #check if already visited or NOTE
            if visited[element]:
                return
            #else iterate to its next edge
            visited[element]=True
            #iterate for each element in the adjacency list
            for value in adj[element]:
                #call the function
                dfs(value)
        
        #call the function
        dfs(C)
        
        #check if C was reached
        return int(visited[B])
