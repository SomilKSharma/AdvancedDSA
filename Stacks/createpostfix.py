'''
Given string A denoting an infix expression. Convert the infix expression into a postfix expression.

String A consists of ^, /, *, +, -, (, ) and lowercase English alphabets where lowercase English alphabets are operands and ^, /, *, +, - are operators.

Find and return the postfix expression of A.

NOTE:

^ has the highest precedence.
/ and * have equal precedence but greater than + and -.
+ and - have equal precedence and lowest precedence among given operators.
'''
from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):

        #create a precedence of the precedence
        precedence={
            '+':0,'-':0,'/':1,'*':1,'^':2
        }

        #create a stack
        stack=deque()

        #create a string for storing the answer
        answer=''

        #iterate for each value in A
        for value in A:
            #check the alphabets
            if value in 'abcdefghijklmnopqrstuvwxyz':
                answer=answer+value
            #check the braces
            elif value=='(':
                stack.append('(')
            elif value==')':
                #remove all the elements till ( comes
                while stack[-1]!='(':
                    answer=answer+stack.pop()
                stack.pop()
            #else value is an operators
            else:
                #iterate till the operator in stack has less precedence
                while stack and stack[-1]!='(' and precedence[stack[-1]]>=precedence[value]:
                    answer=answer+stack.pop()
                stack.append(value)
            

        #iterate for the remaining elements and add them to the answer
        while stack:
            answer=answer+stack.pop()

        #return the answer
        return answer