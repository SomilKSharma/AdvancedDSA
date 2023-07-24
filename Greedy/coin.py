'''
The monetary system in DarkLand is really simple and systematic. The locals-only use coins. The coins come in different values. The values used are:

1, 5, 25, 125, 625, 3125, 15625, ...
Formally, for each K >= 0 there are coins worth 5K.
Given an integer A denoting the cost of an item, find and return the smallest number of coins necessary to pay exactly the cost of the item (assuming you have a sufficient supply of coins of each of the types you will need).
'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        #find the max value of 5 power to use greedy
        power=0
        while A>=5**power:
            power=power+1
        
        #get the max value for greedy
        power=power-1

        #get the counter value
        coins=0
        while A:
            #get coin for the value
            coins=coins+A//5**power
            #change power of A
            A=A%5**power
            #decrement power value
            power=power-1
        
        #return the value
        return coins
