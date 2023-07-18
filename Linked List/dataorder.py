'''You are given the head of a linked list A. 
Check if the data inside it exists in non-decreasing order.
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):

        #get a prev
        prev=float('-inf')

        #get node reference
        node=A

        #iterate for each value of the node
        while node:
            #check if non-decreasing or not
            if node.val<prev:
                return 0
            prev=node.val
            #iterate to the next node
            node=node.next
        
        #return 1 since the ll is in a non decreasing order
        return 1