'''
You are given a linked list A
Each node in the linked list contains two pointers: a next pointer and a random pointer
The next pointer points to the next node in the list
The random pointer can point to any node in the list, or it can be NULL
Your task is to create a deep copy of the linked list A
The copied list should be a completely separate linked list from the original list, but with the same node values and random pointer connections as the original list
You should create a new linked list B, where each node in B has the same value as the corresponding node in A
The next and random pointers of each node in B should point to the corresponding nodes in B (rather than A)
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):

        #create a new linked list head
        B=answer=RandomListNode(None)

        #get reference of head
        node=head

        #create a hashmap to store old and the new nodes
        hashmap={}

        #iterate over each value of head
        while node:
            #create a new node
            answer.next=RandomListNode(node.label)
            answer.next.random=node.random
            #store the created node to a hashmap
            hashmap[node]=answer.next
            #iterate to the next node
            node=node.next
            answer=answer.next
        
        #iterate through the answer linked list and replace random data
        answer=B.next
        while answer:
            answer.random=hashmap.get(answer.random,None)
            answer=answer.next
        
        #return the created linked list
        return B.next
        
