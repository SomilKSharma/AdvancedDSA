'''
Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.
Check whether A has redundant braces or not.
NOTE: A will be always a valid expression and will not contain any white spaces.
'''
from collections import deque
class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):

        #create a stack from the deque
        stack=deque()

        #iterate for each value in A
        for value in A:
            #check for alphabet
            if value in 'abcdefghijklmnopqrstuvwxyz':
                continue
            #else if the value is on operator
            elif value in '+-*/':
                stack.append(value)
            #check for braces
            elif value in '(':
                stack.append(value)
            #else check for redundant braces
            else:
                #check if an operator there
                if stack[-1] in '+-*/':
                    #remove the braces
                    while stack[-1]!='(':
                        stack.pop()
                    stack.pop()
                else:
                    return 1
            
        
        #return 1 if all is correct
        return 0
