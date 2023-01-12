"""
Write a python script to print table of user's choice
"""

# taking input from the user
table = int(input("Enter a number to print it's table : "))

# printing table of user's choice using range() in for loop
for e in range(table, table*10+1, table) :
    print(e)

# another logic
"""
    for e in range(1, 11) :
        print("%d * %d = %d" %(e, table, e*table))
"""