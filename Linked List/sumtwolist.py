'''
You are given two linked lists, A and B, representing two non-negative numbers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return it as a linked list.
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def addTwoNumbers(self, A, B):

        #get another linked list head node
        head=node=ListNode(None)

        #take a carry variable
        carry=0

        #iterate till both the linked list don't end
        while A or B or carry:
            #check for value
            value_a=A.val if A else 0
            value_b=B.val if B else 0
            #sum all the value
            sums=value_a+value_b+carry
            #if sums>9
            node.next=ListNode(sums%10)
            carry=sums//10
            #iterate to the next node
            A=A.next if A else None
            B=B.next if B else None
            node=node.next

        
        #return the value
        return head.next
