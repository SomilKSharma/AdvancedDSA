'''
Reverse a linked list A from position B to C.
NOTE: Do it in-place and in one-pass.
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @param C : integer
	# @return the head node in the linked list
	def reverseBetween(self, A, B, C):

        #make the pos 0 based
        B,C=B-1,C-1

        #write a function to reverse the linked list
        def reverse(node):
            #get a previous,curr and later pointer
            prev,curr,later=None,node,node.next
            #iterate till current node is not null
            while curr:
                curr.next=prev
                prev=curr
                curr=later
                if later:
                    later=later.next
        
        #get the left and the right bridge, along with left and right
        left_bridge=right_bridge=None
        left=right=None
        #get node reference
        node=A
        #iterate till node to get all the value
        pos=0
        while node:
            #check for position
            if pos==B-1:
                left_bridge=node
            if pos==B:
                left=node
            if pos==C+1:
                right_bridge=node
            if pos==C:
                right=node
            #iterate for the next node
            node=node.next
            pos=pos+1
        
        #call the reverse function
        right.next=None
        reverse(left)

        #combine the reversed list
        if left_bridge:
            left_bridge.next=right
            left.next=right_bridge
            #return the head
            return A
        elif not left_bridge:
            left.next=right_bridge
            return right
            








