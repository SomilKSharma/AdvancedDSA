'''
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit.
'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):

        #edge case
        if not A:
            return 0

        #get a variable for maximum profit and one to store lowest value
        max_profit=0
        buy_low=A[0]

        #iterate for each value in the array 
        for value in A[1:]:
            #check for price
            if value>buy_low:
                max_profit=max(
                    value-buy_low,
                    max_profit
                )
            else:
                buy_low=value
        
        #return the maximum profit
        return max_profit
