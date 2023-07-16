#activity selection
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        #create a modified complex array
        array=[
            [A[index],B[index]]
            for index in range(len(A))
        ]

        #modified sort function
        def sorting(tasks):
            return tasks[1]
        
        #sort the array
        array.sort(key=sorting)

        #get an ending time and a counter
        ending=counter=0

        #iterate for all values of the array
        for start,end in array:
            #check if the task canbe done
            if start>=ending:
                counter+=1
                ending=end
        
        #return the counter
        return counter