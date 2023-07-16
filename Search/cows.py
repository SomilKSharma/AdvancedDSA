'''
Farmer John has built a new long barn with N stalls. 
Given an array of integers A of size N where each element of the 
array represents the location of the stall and an integer B which 
represents the number of cows.

His cows don't like this barn layout and become aggressive 
towards each other once put into a stall. To prevent the cows from 
hurting each other, John wants to assign the cows to the stalls, 
such that the minimum distance between any two of them is as large 
as possible. What is the largest minimum distance?
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        #Sort the array
        A.sort()

        #write a function to check the distance
        def checker(distance):
            #get the counter
            counter=1
            #get a start variable
            start=A[0]
            #calcuate the distance
            for value in A[1:]:
                #find the distance
                d=value-start
                if d>=distance:
                    counter+=1
                    start=value
            #check the cow number is less or equal to given
            if counter>=B:
                return True
            else:
                return False
        
        #get the answer variable
        answer=0

        #write the binary search
        start,end=1,A[-1]-A[0]
        while start<=end:
            #get the middle value
            mid=(start+end)//2
            #run the checker function
            if checker(mid):
                answer=mid
                start=mid+1
            else:
                end=mid-1
        
        #return the answer
        return answer
        


