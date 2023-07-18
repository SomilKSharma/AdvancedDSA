'''You are given a singly linked list having head node A. 
You have to reverse the linked list and return the head node of 
that reversed list.
NOTE: You have to do it in-place and in one-pass.
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def reverseList(self, A):

        #get three pointers for reversing a linked list
        prev=None
        curr=A
        later=curr.next

        #iterate till curr
        while curr:
            #point next of curr to prev
            curr.next=prev
            #iterate prev to curr
            prev=curr
            #move curr one forward
            curr=later
            #check if later is none or not
            if later:
                #iterate to the next
                later=later.next
        
        #return the head of the new ListNode
        return prev
