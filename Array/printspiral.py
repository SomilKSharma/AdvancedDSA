#Print the matrix in spiral form starting from A[0][0] in the first row.
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    #get the array input
    length=int(input())
    A=[]
    for _ in range(length):
        A.append(
            list(map(int,input().split()))
        )
    
    #edge case
    if length==1:
        print(array[0][0])
    
    #iterate inside the while loop
    row=col=0
    while length>1:

        #iterate in the for loop
        for _ in range(length-1):
            print(A[row][col],end=' ')
            col=col+1
        #iterate in the for loop
        for _ in range(length-1):
            print(A[row][col],end=' ')
            row=row+1
        #iterate in the for loop
        for _ in range(length-1):
            print(A[row][col],end=' ')
            col=col-1
        #iterate in the for loop
        for _ in range(length-1):
            print(A[row][col],end=' ')
            row=row-1
        
        row=row+1
        col=col+1

        length=length-2
        if length==1:
            print(A[row][col],end=' ')


        

    return 0

if __name__ == '__main__':
    main()