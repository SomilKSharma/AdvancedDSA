#inversion count in an array
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #get an inversion count variable
        global inversion
        inversion=0

        #a merge sort recursive code
        def merge_sort(start,end):
            #base case
            if start>=end:
                return
            #mid point in the array
            mid=(start+end)//2
            #call the merge sort function for left half
            merge_sort(start,mid)
            #call the merge sort function for right half
            merge_sort(mid+1,end)
            #call the merging function
            merging(start,mid,end)
        
        #merging function
        def merging(start,mid,end):
            #get the ivnersion count
            global inversion
            #get a merged array
            merged=[]
            #create a left and a right index
            left=start
            right=mid+1
            #iterate in the array till left<mid+1 and right<end+1
            while left<=mid and right<=end:
                #compare the two indices
                if A[left]<=A[right]:
                    merged.append(A[left])
                    left=left+1
                else:
                    #count the inversion
                    inversion=inversion+mid-left+1
                    merged.append(A[right])
                    right=right+1
            
            #iterate for remaining left
            while left<=mid:
                merged.append(A[left])
                left=left+1
            
            #iterate for remaining right
            while right<=end:
                merged.append(A[right])
                right=right+1
            
            #amend original array
            A[start:end+1]=merged
        
        #call the function
        merge_sort(0,len(A)-1)

        #return the answer
        return inversion%1000000007



