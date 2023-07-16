#quick sort
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        #quick sort function
        def quick_sort(start,end):
            #base case
            if start>=end:
                return
            #get the partition
            part=partition(start,end)
            #call the quick sort function agains
            quick_sort(start,part-1)
            quick_sort(part+1,end)
        
        #write the partition function
        def partition(start,end):
            #take variables for iteration
            lesser=start-1
            greater=start
            pivot=end
            #iterate till greater is less than pivot
            while greater<pivot:
                #check for lesser
                if A[greater]<A[pivot]:
                    #swap with lesser
                    lesser+=1
                    A[greater],A[lesser]=A[lesser],A[greater]
                greater+=1
            #swap with lesser
            lesser+=1
            A[pivot],A[lesser]=A[lesser],A[pivot]
            #return the pivot
            return lesser
        
        #call the function
        quick_sort(0,len(A)-1)

        #return the array
        return A
