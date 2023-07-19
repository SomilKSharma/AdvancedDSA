'''
Given an expression string A, examine whether the pairs and 
the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.
Refer to the examples for more clarity.
'''
from collections import deque
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        #create a stack out of the data
        stack=deque()

        #get a hashmap for comparison
        hashmap={
            ')':'(','}':'{',']':'['
        }

        #iterate for each value of the string
        for brace in A:
            #check if the brace is opening
            if brace in '{([':
                stack.append(brace)
            else:
                #check if the braces match
                if stack and stack[-1]==hashmap[brace]:
                    stack.pop()
                else:
                    return 0
        
        #return 1 if the stack is empty
        if not len(stack):
            return 1
        else:
            return 0
        


