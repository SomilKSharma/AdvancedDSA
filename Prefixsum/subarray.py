#Print array of numbers in which each element is sum of a subarray.
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    #get the input of the array
    length=int(input())
    array=list(map(int,input().split()))

    #get an answer array
    answer=[]

    for index_1 in range(length):
        sums=0
        for index_2 in range(index_1,length):
            sums=sums+array[index_2]
            answer.append(sums)
    
    print(*answer,end=' ')

    return 0

if __name__ == '__main__':
    main()