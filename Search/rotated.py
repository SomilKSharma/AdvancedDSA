'''
Given a sorted array of integers A of size N and an integer B, 
where array A is rotated at some pivot unknown beforehand.

For example, the array [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

Your task is to search for the target value B in the array. If found, return its index; otherwise, return -1.

You can assume that no duplicates exist in the array.

NOTE: You are expected to solve this problem with a time complexity of O(log(N)).
'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):

        #check if B is less than the first element of the array or not
        if B<A[0]:
            #then search in the zone after the pivot
            start,end=0,len(A)-1
            while start<=end:
                #get the mid point in the array
                mid=(start+end)//2
                #check if less than A[0] or not
                if A[mid]>A[0]:
                    start=mid+1
                #else search in the designated space
                elif A[mid]==B:
                    return mid
                elif A[mid]<B:
                    start=mid+1
                else:
                    end=mid-1
        #else the element is on the left side of the pivot
        else:
            start,end=0,len(A)-1
            while start<=end:
                #get the mid point in the array
                mid=(start+end)//2
                #check if less than A[0] or not
                if A[mid]<A[0]:
                    end=mid-1
                #else search in the designated space
                elif A[mid]==B:
                    return mid
                elif A[mid]<B:
                    start=mid+1
                else:
                    end=mid-1
        
        #if not found anywhere
        return -1

        
