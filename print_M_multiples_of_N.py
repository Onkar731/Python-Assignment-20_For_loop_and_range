"""
Write a python script to print first M multiples of N
"""

# taking input from the user
M, N = int(input("Enter 'M' multiples of 'N' : ")), int(input())

# printing M multiples of N using range in for loop
for e in range(N, N*M+1, N) :
    print(e)
    
# another logic
"""
    for e in range(1, M+1) :
        print(e * N)
"""