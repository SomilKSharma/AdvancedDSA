'''
Say you have an array, A, for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.

You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):

        #get the profit
        profit=0

        #iterate for each value in the array A
        for index in range(len(A)-1):
            #check the consectuive stock price
            if A[index]<A[index+1]:
                #add it to the total profit
                profit=profit+A[index+1]-A[index]
        
        #return the answer
        return profit

