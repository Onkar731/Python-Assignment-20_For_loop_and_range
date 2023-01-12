"""
Write a python script to print first 10 multiples of N
"""

# taking input from the user
N = int(input("Enter a number : "))

# printing first 10 multiples of N using range in for loop
for e in range(N, N*10+1, N) :
    print(e)
    
# another logic
"""
    for e in range(1, 11) :
        print(e * N)
"""