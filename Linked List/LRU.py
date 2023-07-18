'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
The LRUCache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number of unique keys it can hold at a time.

Definition of "least recently used" : An access to an item is defined as a get or a set operation of the item. "Least recently used" item is the one with the oldest access time.
'''

class LRUCache:


    #create a class for using doubly linked list
    class Node:
        def __init__(self,value=None,key=None):
            self.key=key
            self.value=value
            self.left=None
            self.right=None

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity=capacity
        self.cache={}
        self.head=self.Node(-1)
        self.tail=self.Node(-1)
        self.head.right=self.tail
        self.tail.left=self.head

    # @return an integer
    def get(self, key):
        #check for key in hashmap
        if key in self.cache:
            #get node adress of the key
            node=self.cache[key]
            #remove the node from the doubly linked list
            node.left.right=node.right
            node.right.left=node.left
            #add the node at the end as latest node
            node.left=self.tail.left
            node.right=self.tail
            self.tail.left.right=node
            self.tail.left=node
            #return the value of the node
            return node.value
        #if not found in the hashmap
        else:
            return -1
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        #check for key in hashmap
        if key in self.cache:
            #get node adress of the key
            node=self.cache[key]
            #remove the node from the doubly linked list
            node.left.right=node.right
            node.right.left=node.left
            node.left=node.right=None
            #add the node at the end as latest node
            node.value=value
            node.left=self.tail.left
            node.right=self.tail
            self.tail.left.right=node
            self.tail.left=node
        #if key not found
        else:
            if len(self.cache)==self.capacity:
                #delete the element closest to head
                deleted_key=self.head.right.key
                node=self.head.right
                node.left=None
                node.right.left=self.head
                self.head.right=node.right
                node.right=None
                del self.cache[deleted_key]
            #add the new element close to the tail
            node=self.Node(key,value)
            node.left=self.tail.left
            node.left.right=node
            self.tail.left=node
            node.right=self.tail
            self.cache[key]=node

        
