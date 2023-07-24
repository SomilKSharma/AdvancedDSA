'''
Given a positive integer A, write a program to find the Ath Fibonacci number.
In a Fibonacci series, each term is the sum of the previous two terms and the first two terms of the series are 0 and 1. i.e. f(0) = 0 and f(1) = 1. Hence, f(2) = 1, f(3) = 2, f(4) = 3 and so on.

NOTE: 0th term is 0. 1th term is 1 and so on.
'''

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    #get the A number for Fibonacci number
    A=int(input())

    #create a dynamic array and initialise the first two values
    dynamic=[
        0
        for _ in range(A+1)
    ]
    dynamic[0],dynamic[1]=0,1

    #iterate for further values to get the answer
    for index in range(2,A+1):
        dynamic[index]=dynamic[index-1]+dynamic[index-2]
    
    #return the A+1 term
    print(dynamic[A])

if __name__ == '__main__':
    main()