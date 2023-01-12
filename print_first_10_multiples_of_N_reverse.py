"""
Write a python script to print the first 10 multiples of N in reverse order
"""

# taking N input from the user
N = int(input("Enter a number : "))

# printing first 10 multiples of N in reverse order using range in for loop
for e in range(N*10, N-1, -N) :
    print(e)
    
# another logic
"""
    for e in range(10, 0, -1) :
        print(e * N)
"""