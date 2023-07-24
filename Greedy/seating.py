'''
There is a row of seats represented by string A. Assume that it contains N seats adjacent to each other. 
There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.

An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')

Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.

In one jump a person can move to the adjacent seat (if available).
'''

class Solution:
	# @param A : string
	# @return an integer
	def seats(self, A):

        #get the position of all the crosses
        pos=[]
        for index in range(len(A)):
            #identify the value
            if A[index]=='x':
                pos.append(index)
        
        #get the length of pos array
        length=len(pos)

        #edge case of no length
        if not length:
            return 0

        #get the median of the pos array and use greedy for ideal pos
        if length&1:
            median=pos[length//2]
            #create the array
            greedy=list(
            range(median-length//2,median+length//2+1)
        ) 
        else:
            median=pos[length//2]
            #create the array
            greedy=list(
                range(median-length//2,median+length//2+1)
            )
        
        #get the seat hops required
        hops=0
        for index in range(length):
            #get the seat difference
            hops=hops+(
                abs(pos[index]-greedy[index])
            )
        
        #return the hops valuer
        return hops%10000003
              

