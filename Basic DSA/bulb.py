#find the minimum number of switches you have to press to turn on all the bulbs.
class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):

        #get the switch count
        switch=0

        #get an odd even state
        state='even'

        #iterate for all values
        for bulb in A:
            #check for on or off
            if (
                (bulb and state=='odd')
                or
                (not bulb and state=='even')
            ):
                switch=switch+1
                state='odd' if state=='even' else 'even'
        
        #return the switch values
        return switch
                
            
