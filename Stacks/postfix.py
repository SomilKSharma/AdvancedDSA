from collections import deque
class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):

        #get a stack to solve
        stack=deque()

        #iterate for each value of A
        for value in A:
            #check if value an operator
            if value in '+-*/':
                #get the two values
                second=stack.pop()
                first=stack.pop()
                #get the answer for this operation
                if value=='+':
                    answer=first+second
                elif value=='-':
                    answer=first-second
                elif value=='*':
                    answer=first*second
                else:
                    answer=first//second
                #add the answer back to the stack
                stack.append(answer)
            else:
                stack.append(int(value))
        
        #return the answer stored in the stack
        return stack.pop()
