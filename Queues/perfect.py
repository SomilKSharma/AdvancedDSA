'''
Given an integer A, you have to find the Ath Perfect Number.
A Perfect Number has the following properties:
It comprises only 1 and 2.
The number of digits in a Perfect number is even.
It is a palindrome number.
For example, 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.
'''
from collections import deque
class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):

        #create a queue and add initial value
        queue=deque()
        queue.append('11')
        queue.append('22')

        #get the answer variable that will store the Ath number
        answer=''
        #iterate for Ath values
        for _ in range(A):
            #get the value
            answer=queue.popleft()
            #get the length of answer
            length=len(answer)
            #put the answer into the queue with modified value
            queue.append(answer[:length//2]+'11'+answer[length//2:])
            queue.append(answer[:length//2]+'22'+answer[length//2:])
        
        #return the answer
        return answer






