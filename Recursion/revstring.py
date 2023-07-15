#Print reverse string
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    
    #set recursion limit
    import sys
    sys.setrecursionlimit(10**8)
    #string input
    string=input()

    #recursive function to print in the reverse order
    def print_reverse(string):
        #base case
        if not string:
            print()
            return
        #print last
        print(string[-1],end='')
        #call the function for remaining
        print_reverse(string[:-1])
    
    #call the function
    print_reverse(string)

    return 0

if __name__ == '__main__':
    main()