'''
There are a total of A courses you have to take, labeled from 1 to A.

Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].

So you are given two integer array B and C of same size where for each i (B[i], C[i]) denotes a pair.

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.
'''

class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):

        #create a degree array
        degree=[0]*(A+1)
        degree[0]=-1

        matrix=[
            []
            for _ in range(A+1)
        ]
        
        for index in range(len(B)):
            matrix[B[index]].append(C[index])
            degree[C[index]]+=1
        
        zero=[]
        #create the 0_degree heap
        for index in range(len(degree)):
            if not degree[index]:
                zero.append(index)
                
        
        #get the answer array and do the soring
        answer=[]
        while zero:
            #get the least value node
            node=zero.pop()
            answer.append(node)

            #decrease the degree of adjacent connected nodes
            for value in matrix[node]:
                degree[value]-=1
                if not degree[value]:
                    zero.append(value)
        
        #check for cycles
        if len(answer)!=A:
            return 0
        else:
            return 1


        
        
        



        
        