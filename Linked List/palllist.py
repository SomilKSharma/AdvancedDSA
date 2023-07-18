'''
Given a singly linked list A, determine if it's a palindrome. 
Return 1 or 0, denoting if it's a palindrome or not, respectively.
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):

        #edge case
        if not A.next:
            return 1

        #get a slow and a fast pointer to get the middle pointer
        slow=fast=A
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        #function to reverse the array
        def reverse(node):
            #get three pointers and reverse the array
            prev,curr,later=None,node,node.next
            while curr:
                curr.next=prev
                prev=curr
                curr=later
                if later:
                    later=later.next
            #return the head of the new array
            return prev
        
        #get the new head post the slow pointer
        head=reverse(slow.next)
        slow.next=None

        #compare both the string to check if they are palindrome or not
        while head:
            #check for value
            if A.val!=head.val:
                return 0
            #else iterate both further
            A=A.next
            head=head.next
        
        #pallindrome otherwise
        return 1
