class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):

        #get a minimum and a max profit variable
        mini_buy=float('inf')
        max_profit=0

        #iterate for each value of A
        for stock_price in A:
            #check if less than mini_buy
            if stock_price<mini_buy:
                mini_buy=stock_price
                continue
            else:
                max_profit=max(
                    max_profit,
                    stock_price-mini_buy
                )
        
        #return the value
        return max_profit
