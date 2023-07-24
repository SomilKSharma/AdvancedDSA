'''
The local ship renting service has a special rate plan:

It is up to a passenger to choose a ship.
If the chosen ship has X (X > 0) vacant places at the given moment, then the ticket for such a ship costs X.
The passengers buy tickets in turn, the first person in the queue goes first, then the second one, and so on up to A-th person.

You need to tell the maximum and the minimum money that the ship company can earn if all A passengers buy tickets.
'''

from heapq import heappop,heappush
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):

        #create a max heap from array C
        maxi=[]
        for value in C:
            #push the negative of value
            heappush(maxi,-value)
        #get the maximum profit
        max_money=0
        #iterate for each passenger
        for _ in range(A):
            #seat costs
            seat=-heappop(maxi)
            #add it to the maximum money
            max_money=max_money+seat
            #put the value back in the heap
            if seat-1:
                heappush(maxi,-(seat-1))
        
        #create a min heap from array C
        mini=[]
        for value in C:
            #push the value
            heappush(mini,value)
        #get the minimum profit
        min_money=0
        #iterate for each passenger
        for _ in range(A):
            #seat costs
            seat=heappop(mini)
            #add it to the minimum money
            min_money=min_money+seat
            #put the value back in the heap
            if seat-1:
                heappush(mini,(seat-1))
        
        #return the answer
        return max_money,min_money
        

        

