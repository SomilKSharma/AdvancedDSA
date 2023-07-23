'''
You are given an array A containing N numbers. This array is called special if it satisfies one of the following properties:

There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[0], A[1], ...., A[i-1]]
There exists an element A[i] in the array such that A[i] is equal to the median of elements [A[i+1], A[i+2], ...., A[N-1]]
The Median is the middle element in the sorted list of elements. If the number of elements is even then the median will be (sum of both middle elements) / 2.

Return 1 if the array is special else return 0.

NOTE:

Do not neglect decimal point while calculating the median
For A[0] consider only the median of elements [A[1], A[2], ..., A[N-1]] (as there are no elements to the left of it)
For A[N-1] consider only the median of elements [A[0], A[1], ...., A[N-2]]
'''

import heapq
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        if len(A)==1:
            return 0

        #write a function to get the median array
        def medians(array):
            #get heap data structures
            maxi=[]
            mini=[]
            heapq.heappush(maxi,-array[0])
            #get an answer array
            answer=[array[0]]
            #iterate to get the medians
            for value in array[1:]:
                #add the value to the heaps
                if value<-maxi[0]:
                    heapq.heappush(maxi,-value)
                else:
                    heapq.heappush(mini,value)
                #check for the length of the heaps
                if len(mini)>len(maxi):
                    heapq.heappush(maxi,-heapq.heappop(mini))
                elif len(maxi)-len(mini)>1:
                    heapq.heappush(mini,-heapq.heappop(maxi))
                #get the median
                if (len(mini)+len(maxi))&1==0:
                    answer.append((-maxi[0]+mini[0])/2)
                else:
                    answer.append(-maxi[0])
            #return the answer array
            return answer
        
        #get the left median
        left=medians(A)
        #get the right median
        right=medians(A[::-1])[::-1]

        #check for the edge cases
        if A[0]==right[1] or A[len(A)-1]==left[len(A)-2]:
            return 1
        #iterate through all the cases
        for index in range(1,len(A)-1):
            if A[index]==left[index-1] or right[index+1]==A[index]:
                return 1
      
        return 0
        
