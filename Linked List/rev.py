'''
You are given a singly linked list having head node A. You need to print the linked list in reverse order.
Note :- The node values must be space separated. You must give a newline after printing all the nodes.
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def solve(self, A):

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
        
        #present head of the reversed list is at prev
        while prev:
            #print the element
            print(prev.val,end=' ')
            prev=prev.next
        
        #add a new line
        print()
