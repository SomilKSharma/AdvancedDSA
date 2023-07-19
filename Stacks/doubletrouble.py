'''You have a string, denoted as A.

To transform the string, you should perform the following operation repeatedly:
Identify the first occurrence of consecutive identical pairs of characters within the string.
Remove this pair of identical characters from the string.
Repeat steps 1 and 2 until there are no more consecutive identical pairs of characters.
The final result will be the transformed string.
'''
from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        #create a stack for the answer
        stack=deque()

        #iterate for each value in the string
        for letter in A:
            #check if value is similar to the last stack value
            if stack and letter==stack[-1]:
                stack.pop()
            #append the value to the stack
            else:
                stack.append(letter)
        
        #return the left string
        return ''.join(stack)
