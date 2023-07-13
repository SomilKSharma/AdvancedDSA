#Print all possible subarray.
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    length=int(input())
    array=list(map(int,input().split()))

    for index_1 in range(length):
        for index_2 in range(index_1,length):
            print(*array[index_1:index_2+1],end=' \n')

    return 0

if __name__ == '__main__':
    main()