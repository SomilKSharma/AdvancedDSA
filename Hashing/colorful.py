#If number A is a COLORFUL number return 1 else, return 0.
class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):

        #create a hashset
        hashset=set()

        #convert the number to a list of digits
        number=list(map(int,str(A)))

        #iterate in a nested loop,createing all the subsets
        for index_1 in range(len(number)):
            prod=1
            for index_2 in range(index_1,len(number)):
                #create the consecutive product
                prod=prod*number[index_2]
                #check if in hashset
                if prod in hashset:
                    return 0
                #add to the hashset
                hashset.add(prod)
        
        #return the answer
        return 1
                


