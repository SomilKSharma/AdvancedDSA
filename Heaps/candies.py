'''
Misha loves eating candies. She has been given N boxes of Candies.
She decides that every time she will choose a box having the minimum number of candies, eat half of the candies and put the remaining candies in the other box that has the minimum number of candies.
Misha does not like a box if it has the number of candies greater than B so she won't eat from that box. Can you find how many candies she will eat?

NOTE 1: If a box has an odd number of candies then Misha will eat the floor(odd / 2).

NOTE 2: The same box will not be chosen again.
'''

from heapq import heappush,heappop
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        #create the eat variable to store the answer
        eat=0

        #store all the values in a heap
        min_heap=[]
        for value in A:
            heappush(min_heap,value)
        
        #iterate till heap exists
        while min_heap:
            #get the value from the heap
            min_candy=heappop(min_heap)
            #check for the size of B
            if min_candy>B:
                break
            else:
                #add the candies that she will
                eat=eat+min_candy//2
                #check if value in heap
                if not min_heap:
                    break
                else:
                    #add the new value after putting half values in it
                    heappush(min_heap,heappop(min_heap)+min_candy-min_candy//2)
        
        #return the eat variable
        return eat


