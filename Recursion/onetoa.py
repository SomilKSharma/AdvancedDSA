#printonetoa
class Solution:
    # @param A : integer
    def solve(self, A):

        #write a recursive code
        def onetoa(number):
            #base case
            if number>A:
                print()
                return
            #print values
            print(number,end=' ')
            #assum code works for n+1
            onetoa(number+1)
        
        onetoa(1)

