'''
Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.

Elements which are appearing twice are adjacent to each other.

NOTE: Users are expected to solve this in O(log(N)) time.

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #check for the edge cases that is start and end
        if len(A)==1:
            return A[0]
        elif A[0]!=A[1]:
            return A[0]
        elif A[-1]!=A[-2]:
            return A[-1]
        
        #binary search to get the answer
        start=1
        end=len(A)-2
        while start<=end:
            #get the middle value
            mid=(start+end)//2
            #check for unique
            if A[mid-1]<A[mid]<A[mid+1]:
                return A[mid]
            #check if unique in the left or right
            elif A[mid-1]==A[mid]:
                #check if unique on the right
                if mid&1:
                    start=mid+1
                #check if unique on th left
                else:
                    end=mid-1
            #check if unique in the left or right
            else:
                #check if unique on the left
                if mid&1:
                    end=mid-1
                #check if unique on th right
                else:
                    start=mid+1
        




        


